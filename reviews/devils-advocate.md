# Devil's Advocate internal editorial review

Recommendation: **Accept as an explicitly unrefereed computational theorem candidate.** No Critical or Major defect was established in this review. Acceptance here is an internal editorial recommendation, not external validation, proof-assistant verification, or novelty clearance.

## Strongest counterargument

The full degree-448 resultant remains the most consequential dependency that routine replay does not freshly reconstruct. A coherent wrong factorization and residue set could pass the artifact checks: `verify.py:25–47` starts with the displayed factors, compares stored coefficients and residues with their expansion, and verifies CRT reconstruction. Those operations establish agreement and uniqueness *conditional on correct resultant residues*, not that those residues came from the stated seven equations. Four fresh determinant evaluations (`verify.py:114–120`), including only two for H7, do not deterministically exclude another degree-448 polynomial. The full saved single-prime Macaulay polynomial adds substantial algorithmic evidence, but it still does not by itself uniquely determine an integer polynomial within the stated coefficient bound.

This is a serious limitation of what a default PASS means, but it is **not an undisclosed defect** in this submission. The paper explicitly states the residue-correctness condition at `report/fano_spectrum.md:180–182`, identifies saved versus fresh Macaulay checks at line 192, and discloses incomplete full replay at line 214. `ASSURANCE.md` and `README.md:29–42` repeat the boundary and supply a separate full generator command. Requiring external validation or a complete new run merely because this review is adversarial would change the declared publication standard.

## Scope, identity, confidence and limits

I read the frozen package's complete paper Markdown and verifier, assurance statement, novelty report, claim ledger, README, Poisson recursion and H7 lifting code, curve and real-obstruction scripts, and selected finite-eigenvector output and its driver. I did not read any other new review report, edit the submission, or delegate. I inspected mathematical dependence and source-to-equation correspondence rather than treating packaging success as mathematical proof.

Fresh SHA-256 checks matched the assigned identity:

- ZIP: `0d3282ca0b3e123981f40c7f09c1adfcf591c194c0cf2120ef66bab023041ba5`.
- Manuscript PDF: `4818810c1c914948e52bf0f4d24fe2017a459d4a3f3f780cc421a30802fbc8a5`.
- Manifest: `2b98d6996e98df092b9616e9dee0dbc56e3910d43db9bd0181a38cecc171aad2`.

The assigned normal, optimized, negative-control and clean-extraction passes are baseline information supplied by the coordinating reviewer; I did not repeat those runs. I did not rerun the full resultant or every number-field decomposition, visually audit the PDF, authenticate publisher versions, or independently repeat the literature searches. Confidence is high in the assessment of the stated assurance boundaries, and moderate in the mathematical editorial assessment. This is an internal model review.

## Mathematical challenges adjudicated

1. **Existence versus completeness.** Explicit vectors only establish roots. The paper correctly places completeness and multiplicities on the resultant computation (`report/fano_spectrum.md:30,124,180`). The eigen-equations in the characteristic-zero scripts match the seven normalized Fano lines. The Poisson code uses the induced lower-stage forms, quotient multiplication determinant and squared lower resultant; it rejects an unexpected quotient dimension on admissible evaluation points. I found no demonstrated normalization or recursion error.

2. **CRT versus observed coefficient size.** The maximum-coordinate triangle argument gives root modulus at most three. Vieta bounds each coefficient by `binomial(448,k) * 3^k`, hence by `4^448`. A modulus greater than twice that bound suffices for unique symmetric lifting. The thirty-prime condition is therefore substantively different from empirical twelve-prime stability. The lower-stage bound with each induced graph's maximum degree is the appropriate inductive argument. The manuscript makes this distinction rather than using observed 207-bit coefficients as its proof.

3. **Complex points versus real points.** A real eigenvalue or a number-field component count does not establish real eigenvectors. The submitted rational identity `1 + sum(x_i^2) in I_2` supplies a direct real obstruction. All its terms and the chart equations use real rational coefficients; point transitivity permits normalization of any purported nonzero real vector into this chart. Thus the stated logic excludes real eigenvectors at two without confusing primary components, residue degrees or geometric points (`report/fano_spectrum.md:196–198`; `verification/reality_audit.sing:1–15`).

4. **Smoothness versus geometric irreducibility.** Smoothness alone would allow disjoint components. Here the argument also uses the computed resolution to obtain depth two, then the degree-zero global-function calculation to establish geometric connectedness. The Hilbert series gives degree eight and arithmetic genus three; smoothness and connectedness permit the irreducibility conclusion. Saturation is essential and is actually performed. I found no missing logical step in this implication chain relative to the CAS outputs (`report/fano_spectrum.md:149–158`; `verification/geometry_audit.sing`).

5. **Eigen-scheme lengths versus resultant exponents.** Their equality for finite fibers is explicitly an observation, not a universal multiplicity theorem (`report/fano_spectrum.md:143–145`). The curve's exponent 52 is not explained by its degree or genus, and the paper does not claim otherwise. Finite number-field classifications retain a weaker replay status, disclosed at line 128 and in the limitations.

6. **Priority versus a historical problem listing.** The manuscript does not turn the 2020 open label into a claim of openness in 2026. It acknowledges the Lin–Bu priority lead, the unavailable authenticated publisher PDF, and bounded search recall (`report/fano_spectrum.md:54–61,204`). An earlier computation remains a live alternative explanation for apparent novelty. That possibility limits priority language; it does not invalidate an exact computation presented without a first-solution claim.

## Findings and remedies

**Critical:** None established.

**Major:** None established.

**Minor M1 — optional reproducibility enhancement.** At `verify.py:51–61`, the lower-stage checks verify edge encoding, degrees, prime products and agreement of copies; they do not reconstruct those lower resultants from saved per-prime residues. The source generator and historical logs carry that part of the computational provenance. This is compatible with the current assurance description, but a compact per-stage residue ledger or a separate full-replay receipt would make the inductive chain easier to audit. Optional remedy: preserve those residues on a future full run and bind its receipt to the package identity. Do not relabel the present artifact check as fresh full resultant verification.

**Minor M2 — optional precision improvement.** `report/fano_spectrum.md:190` calls the Rowling regression the strongest available end-to-end test. This can reasonably mean a complete known-answer test on a different object, but it is not the strongest evidence for every individual Fano claim, and that historical ten-prime run is not presented with a deterministic full coefficient-bound certification. Optional remedy: describe it as a complete published-object regression and leave comparative strength unstated. No mathematical claim in the paper depends on this ranking.

**Required changes before publication:** None identified for the declared unrefereed-candidate scope. Preserve the existing limits in any abstract, landing page or promotional summary. A claim of authenticated external validation, exhaustive novelty, current open-problem resolution, or full fresh resultant reproduction would require additional evidence absent here.
