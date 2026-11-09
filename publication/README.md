# Zenodo setup and first release

Candidate version: 0.1.0. Status: repository manuscript draft; no tagged release or DOI. This file is a preparation guide, not a publication receipt or release instruction.

## Enable the repository

1. Sign in to Zenodo and open [GitHub settings](https://zenodo.org/account/settings/github/).
2. Connect the GitHub account if necessary. Refresh the repository list and enable **Quantyra/aa-noise-influence**. If the organization is not accessible, review the GitHub organization's authorization for the Zenodo integration.
3. Confirm that the repository is enabled. Merely enabling it does not publish the first archive. A subsequent published GitHub release is the trigger.

Official instructions: [enable a repository](https://help.zenodo.org/docs/github/enable-repository/), [metadata precedence](https://help.zenodo.org/docs/github/describe-software/), [archive a release](https://help.zenodo.org/docs/github/archive-software/).

## Package behavior

The repository is a manuscript archive, including the checked PDF and LaTeX source. Root `.zenodo.json` explicitly requests `upload_type: publication` and `publication_type: preprint`, using the confirmed author/ORCID and CC BY 4.0. Zenodo reads that file in preference to CITATION.cff. Metadata has no guessed DOI, existing related DOI or publication date. Do not describe a repository archive as a second independently published paper or create a duplicate record without a deliberate relationship/version plan.

Zenodo's GitHub integration archives the repository release. A PDF is included in the repository itself; the package does not rely on GitHub release attachments being imported. There is no release workflow, publishing token or automatic DOI step in this repository.

## Before a later first release

- Finish the exact-candidate manuscript/claims decision and inspect the current PDF. Keep the note's dependence on imported results and its unestablished priority explicit.
- If the working-draft wording is revised for release, update the PDF, README, metadata, checks and review record together. Verify author, title, version, licenses and AI disclosure.
- Run `python tools/check_package.py` and record the exact commit and PDF hash. Rebuild only when source changes require it.
- After the user's connection is confirmed and release is authorized, create the intended GitHub tag/release from that exact commit. Creating a published release can cause automatic public archiving and DOI registration.
- Verify the actual Zenodo record, metadata, files and version/concept DOI before recording publication success. Reuse an existing DOI where appropriate; do not invent or pre-fill one.
- Add the verified DOI to citation/repository metadata in a follow-up commit. If putting a DOI inside the first PDF is essential, choose Zenodo's separate draft-reservation workflow deliberately before release; GitHub integration does not by itself supply a pre-reserved manuscript DOI.

The first-release checklist remains pending. A DOI is a persistent identifier, not peer review or formal certification. Material file corrections after publication should be handled as explicit version updates under [Zenodo's versioning guidance](https://help.zenodo.org/docs/deposit/manage-versions/).
