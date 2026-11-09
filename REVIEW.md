# Scope, source comparison and internal checks

Assessment date: 2026-11-09. Candidate: manuscript version 0.1.0. This record is an internal AI-assisted analytic and document assessment, not independent peer review.

## Exact claim and proof interface

Theorem 1 concerns every exactly bounded real multilinear polynomial on the uniform sign cube, degree at most d >= 1 and positive variance, with squared HALF-edge differences as influence. The full edge L1 sum is a separate quantity. No homogeneity or variance floor is used.

The composition has been checked term by term:

1. Multilinear interpolation is an expectation over independent signs, so cube boundedness extends to the continuous cube. Noise smoothing preserves range and does not increase degree.
2. Parseval gives `Var(T_rho f) >= rho^(2d) Var(f)` and `Inf_i(T_rho f) <= rho^2 Inf_i(f)`. No coordinate is replaced by an auxiliary encoding.
3. Classical interior Bernstein gives `L(T_rho f) <= 2 rho d / sqrt(1-rho^2)`. The manuscript supplies the trigonometric-curve derivation and attributes the antecedent.
4. The imported theorem has denominator `L K^2`, not `L^2 K`; with `K = pi^2 d^2`, the powers are exactly `rho^(5d-3) sqrt(1-rho^2) V^(5/2) / d^5` and coefficient `sqrt(15)/(250 pi^4)`.
5. At `rho = 1-1/(2d)`, variance retention is at least 1/4 and `L <= (4/sqrt(3))d^(3/2)`. The displayed conservative constant is `sqrt(45)/(16000 pi^4)`. The d=1 endpoint is admitted.
6. The decision-tree potential is TOTAL squared influence. Its expected one-query drift is the selected coordinate's influence; variance alone would have only the singleton Fourier square as drift. Finite telescoping, the query cap and the two error allocations are explicit. Runtime is unrestricted.

No separate proof of the imported AA theorem is claimed. The paper does not identify the classical smoothing estimate as a new theorem. It retains the unrounded rho bound and limits the exponent comparison to the specified polynomial branch; it does not claim to dominate small-variance or constant-refined alternatives.

## Focused priority question

Question: is this exact general `V^(5/2)/d^(11/2)` composition already stated or subsumed by the closest primary sources?

- David Turturean, *A proof of the Aaronson-Ambainis conjecture*, pinned [commit 2a6ceaef872ae993708950f951989134084b851a](https://github.com/physical-superintelligence/aaronson-ambainis/blob/2a6ceaef872ae993708950f951989134084b851a/paper/aaronson_ambainis_paper.tex). Inspected the main bound, row statement, influence statement and discussion of exponents. It states the general d^(-6) bound. Its row theorem is attributed to Agarwal and Ben-David, with constant refinements also acknowledged.
- Filmus, Hatami, Keller and Lifshitz, [arXiv:1404.3396v3](https://arxiv.org/abs/1404.3396v3), Proposition 3.2 and Section 5.1. It contains the interior Bernstein/smoothing technique and the inverse-noise obstacle for unsmoothing total L1 influence. Our use applies the imported influence theorem before transferring squared influences back, so the unsmoothing ratio is not assumed.
- Agarwal and Ben-David, [arXiv:2410.19062v2](https://arxiv.org/abs/2410.19062v2), is cited as the row-bound antecedent through the explicitly identified source above. This packaging pass is not an independent audit of its entire oracle-separation proof.
- Aaronson and Ambainis, [arXiv:0911.0996v3](https://arxiv.org/abs/0911.0996v3), supplies the influence-to-query framework. The manuscript includes a full derivation of its particular sufficient exponents instead of attributing those exponents to the earlier paper.

Exact-name searches combining Aaronson-Ambainis with `11/2`, smoothing and Turturean did not locate the same combined corollary in this bounded check. This is not an exhaustive novelty search or evidence of priority. Public descriptions therefore call this a short quantitative corollary and do not claim a first proof or independently established publication significance. Finding an earlier subsuming result requires correcting that positioning, not hiding it.

## Artifact and release posture

The current build identity and automated document checks are recorded in `verification/build.json`; metadata/file checks are in `verification/package.json`. These establish artifact consistency only. Visual PDF inspection is recorded below after the build.

Publication posture: the user instructed publication on 2026-11-09 conditional on multi-lens review. The existing review covers four internal lenses: mathematical composition/normalization, sources/attribution, claim boundaries, and artifact integrity/readability. It is not a record of independent reviewers, multiple model providers or human peer review. No blocking finding was recorded for the scoped preprint. Exact candidate `e0804d18567ef36e7b90bf45d62db543f5298929` was published as v0.1.0; [DOI 10.5281/zenodo.24088381](https://doi.org/10.5281/zenodo.24088381) and all 19 archived files were verified. The [post-publication receipt](verification/publication-v0.1.0.json) is outside the immutable release. Mathematical statements and proofs remain unchanged. Full Lean certification is not asserted or silently imposed as a prerequisite by this note.

Visual inspection: all five rendered pages inspected on 2026-11-09. After the preprint wording change, pages 1 and 5 were reinspected; page renders 2-4 are hash-identical to the previously inspected pages. Equations, theorem/proof continuations, bibliography, page numbers and author/ORCID text are readable; no clipping, overlap or missing glyph was observed. The final TeX log has no overfull/underfull boxes or unresolved-reference diagnostics. All 19 PDF fonts remain embedded. The local compiler emitted a nonfatal Fontconfig configuration message, retained in `verification/build.json`; the rendered output and embedded-font inspection show no resulting document defect. Exact PDF identity and scope are recorded in `verification/visual.json`.

## Provenance

This note develops the November 8, 2026 S227 derivation and its corrected baseline comparison. The original technical source commit is `45added15b5d631cf719058722c8f76d1ba5c192`, file `proofs/e005-s227-noise-influence-2026-11-08.md`, Git blob `89da71a9e4edbd1e8155aeb5fddd2a21090941fc`. The original research records stay in their source repository. This distribution contains the full argument needed to read the corollary, plus links to its public mathematical dependencies; private logs and adjacent failed investigations are not bundled.
