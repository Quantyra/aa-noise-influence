"""Check the actual manuscript package and citation metadata; never publishes."""
import hashlib
import json
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    citation = yaml.safe_load((ROOT / 'CITATION.cff').read_text(encoding='utf-8'))
    zenodo = json.loads((ROOT / '.zenodo.json').read_text(encoding='utf-8'))
    build = json.loads((ROOT / 'verification' / 'build.json').read_text(encoding='utf-8'))
    visual = json.loads((ROOT / 'verification' / 'visual.json').read_text(encoding='utf-8'))
    preferred = citation['preferred-citation']
    assert preferred['title'] == zenodo['title']
    assert citation['version'] == zenodo['version'] == '0.1.0'
    assert citation['license'] == zenodo['license'] == 'CC-BY-4.0'
    assert preferred['authors'] == citation['authors']
    author = citation['authors'][0]
    creator = zenodo['creators'][0]
    assert creator['name'] == f"{author['family-names']}, {author['given-names']}"
    assert creator['affiliation'] == author['affiliation']
    assert author['orcid'] == 'https://orcid.org/' + creator['orcid']
    assert zenodo['upload_type'] == 'publication' and zenodo['publication_type'] == 'preprint'
    assert 'doi' not in zenodo
    publication_path = ROOT / 'verification' / 'publication-v0.1.0.json'
    publication = json.loads(publication_path.read_text(encoding='utf-8')) if publication_path.exists() else None
    if publication:
        assert publication['status'] == 'PUBLISHED_AND_VERIFIED'
        assert preferred['doi'] == publication['version_doi']
        assert str(citation['date-released']) == '2026-11-09'
        assert publication['pdf_sha256'] == sha(ROOT / 'manuscript' / 'main.pdf')
    else:
        assert 'doi' not in preferred and 'date-released' not in citation
    assert 'publication_date' not in zenodo
    assert build['source_sha256'] == sha(ROOT / 'manuscript' / 'main.tex')
    assert build['pdf_sha256'] == sha(ROOT / 'manuscript' / 'main.pdf')
    assert build['final_log_diagnostics'] == [] and build['pages'] > 0
    assert visual['pdf_sha256'] == build['pdf_sha256']
    assert visual['pages_inspected'] == list(range(1, build['pages'] + 1))
    assert visual['verdict'] == 'PASS_DOCUMENT_LAYOUT'
    text = (ROOT / 'manuscript' / 'main.tex').read_text(encoding='utf-8')
    assert r'\frac{\sqrt{45}}{16000\pi^4}' in text
    assert 'OpenAI Codex' in text and 'No independent peer review' in text
    required = ['README.md', 'AGENTS.md', 'REVIEW.md', 'publication/README.md',
                'LICENSE', 'LICENSES/CC-BY-4.0.txt', 'CITATION.cff', '.zenodo.json',
                '.gitattributes', '.gitignore', 'requirements.txt',
                'manuscript/main.tex', 'manuscript/main.pdf',
                'tools/build.py', 'tools/check_package.py', 'verification/build.json',
                'verification/visual.json', 'publication/RELEASE-NOTES-v0.1.0.md']
    if publication:
        required.append('verification/publication-v0.1.0.json')
    for filename in required:
        path = ROOT / filename
        assert path.is_file() and path.stat().st_size > 0, filename
        if path.suffix in ('.md', '.tex', '.json', '.cff', '.py'):
            data = path.read_text(encoding='utf-8')
            assert not re.search(r'[A-Za-z]:[/\\]Users[/\\]', data), filename
        if path.suffix == '.md':
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                target = target.strip('<>').split('#')[0]
                if target and '://' not in target:
                    assert (path.parent / target).exists(), (filename, target)
    receipt = {
        'status': 'PASS',
        'scope': 'Local files, hashes, links, author/title/version/license and Zenodo field consistency',
        'not_performed': ([] if publication else ['Zenodo ingestion']) + ['formal proof verification', 'independent peer review'],
        'files': {name: sha(ROOT / name) for name in sorted(required)},
        'publication_record_created': bool(publication),
        'scope_note': 'Current working package integrity; publication receipt separately pins the immutable archive',
    }
    (ROOT / 'verification' / 'package.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps({'package': 'PASS', 'checked_files': len(required), 'pages': build['pages']}))


if __name__ == '__main__':
    main()
