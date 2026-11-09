# Noise smoothing sharpens a quantitative Aaronson-Ambainis influence bound

**Daniel Fredriksen · Quantyra Inc. · [ORCID 0009-0002-9123-7435](https://orcid.org/0009-0002-9123-7435)**

[Read the manuscript PDF](manuscript/main.pdf) · [LaTeX source](manuscript/main.tex) · [Review and scope](REVIEW.md) · [Zenodo setup](publication/README.md)

Version **0.1.0 manuscript draft**. No GitHub release, Zenodo record or DOI has been created for this package. Repository availability is not peer review or formal certification.

For every real multilinear polynomial `f : {-1,1}^n -> [-1,1]` of degree at most `d >= 1` and uniform variance `V > 0`, the note proves the corollary

```text
max_i Inf_i(f) >= sqrt(45) / (16000 pi^4) * V^(5/2) / d^(11/2),
Inf_i(f) = E[((f(X) - f(X with sign i reversed))/2)^2].
```

The argument combines Turturean's row/influence theorem with classical interior Bernstein smoothing. It improves the degree exponent of his displayed general bound from 6 to 11/2, with the same variance exponent. The note attributes the row bound to Agarwal and Ben-David and the smoothing method to Filmus, Hatami, Keller and Lifshitz. Constants are conservative; the new bound need not dominate other bounds at each parameter pair. This is a quantitative corollary, not an independent AA proof or a result about BPP versus BQP.

An explicitly proved decision-tree consequence gives a sufficient `O(T^(13/2) epsilon^(-5) delta^(-7/2))` query bound on most uniform inputs. Query selection and leaf computation can be exponentially expensive.

## Build and verify

Use Python 3.10+, Tectonic 0.17.0, PyMuPDF 1.28.2 and PyYAML 6.0.3. The optional rendering dependency is for document inspection, not a mathematical experiment.

```sh
python -m pip install -r requirements.txt
python tools/build.py --tectonic /path/to/tectonic --render
python tools/check_package.py
```

The build uses Tectonic's standard TeX bundle; an uncached environment may need network access to fetch typesetting packages. Build products and page renders go in `.build/`; the PDF and a compact build receipt are retained in `manuscript/` and `verification/`. No Lean build, remote compute or research job is part of this package. The package check validates file identities and metadata; it does not prove the theorem. See [REVIEW.md](REVIEW.md) for the analytic checks and remaining limits.

## Cite and archive

Until a DOI exists, cite Daniel Fredriksen, *Noise smoothing sharpens a quantitative Aaronson-Ambainis influence bound*, manuscript draft, 2026, and identify the repository commit. [CITATION.cff](CITATION.cff) provides the manuscript as the preferred citation. There is no invented DOI or publication date in the metadata.

The root [.zenodo.json](.zenodo.json) describes a **publication/preprint**, including the PDF and its source. It takes precedence over CITATION.cff for Zenodo's GitHub ingestion. Enable this repository on [Zenodo's GitHub settings](https://zenodo.org/account/settings/github/), then use the documented release checklist. Connecting the repository does not itself create the first archive; a subsequent published GitHub release triggers it. No workflow here publishes automatically.

All original package material is available under [CC BY 4.0](LICENSE). External papers are linked and cited, not redistributed. OpenAI Codex assisted with derivation, source comparison, drafting and package preparation; no independent peer review or formal verification of this corollary is claimed.
