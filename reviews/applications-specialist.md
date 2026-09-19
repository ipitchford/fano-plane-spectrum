# Applications and cross-disciplinary specialist review

Recommendation: **Accept**, within the release's stated anonymous, AI-assisted, unrefereed computational-candidate status. No required revision arises from this role. This is an internal model review, not external validation, authenticated peer review, or novelty clearance.

## Scope, identity, and limitations

Reviewed the frozen package at `baseline-extract-final/fano-plane-spectrum`, specifically the complete manuscript Markdown, `ASSURANCE.md`, `SOURCES.md`, `NOVELTY_REPORT.md`, and `CLAIMS.json`. The parent supplied passing baseline checks and the following binding identifiers: submission ZIP SHA256 `0d3282ca0b3e123981f40c7f09c1adfcf591c194c0cf2120ef66bab023041ba5`; manuscript PDF SHA256 `4818810c1c914948e52bf0f4d24fe2017a459d4a3f3f780cc421a30802fbc8a5`; manifest SHA256 `2b98d6996e98df092b9616e9dee0dbc56e3910d43db9bd0181a38cecc171aad2`. I have not independently regenerated those hashes or computation receipts.

My remit was the semantic bridge from the tensor calculation to mathematical interpretation and possible reuse, omitted constraints, and overstatement or misuse risks. I did not repeat literature searches, independently authenticate source articles, inspect other new role reports, rerun the resultant, or certify the algebraic geometry proof. Confidence is high in the assessment of the manuscript's stated boundaries and moderate in the prospective benchmark value, which has not been demonstrated by third-party use.

## Strengths and implications

1. **The mathematical object is sufficiently specified for responsible reuse.** Manuscript lines 36–50 provide the seven lines, tensor normalization, complex eigen-equation, resultant, and algebraic-multiplicity definition. They explicitly distinguish homogeneous eigenvalues from E/Z eigenvalues. `ASSURANCE.md:3–4` and `NOVELTY_REPORT.md:7–9` additionally exclude incidence-matrix, graph, and matroid spectra. Consequently, the formula can be compared with another implementation only after matching this object and normalization; the package supplies the needed matching information.

2. **The difficult semantic distinctions are unusually well exposed.** Manuscript lines 65–80 and 126–145 distinguish root multiplicity, projective vector counts, finite scheme lengths, and positive-dimensional eigenvector sets. Lines 28–30 and 196–200 distinguish real eigenvalues from eigenvalues admitting real eigenvectors, and distinguish explicit existence witnesses from completeness. These prevent the main likely cross-disciplinary errors: interpreting multiplicity 52 as 52 vectors, treating all five real eigenvalues as H-eigenvalues, or regarding symmetry ansätze alone as a full spectral computation.

3. **The result has credible bounded mathematical benchmark value.** Conditional on the claimed computation being correct, the same small incidence structure offers a degree-448 exact target, low-degree factors, a real root without real eigenvectors, finite nonreduced eigenvector schemes, and a positive-dimensional eigencurve. Those features make it a useful prospective test case for resultant implementations and tensor-eigenvalue or eigenscheme computations. Its explicit vector families and separate real-obstruction certificate also permit narrower tests without replaying the entire resultant. This is a defensible pure-mathematical contribution; practical deployment, broad field impact, or a new numerical algorithm need not be established for this release.

4. **Generalization and verification claims are appropriately restricted.** Manuscript line 95 warns against carrying induced-subhypergraph eigenvalues into the whole object. Line 145 explicitly avoids generalizing observed equality of finite scheme length and resultant multiplicity. Lines 190–200 and `ASSURANCE.md:10–22` distinguish producer replay, saved outputs, different determinant constructions with shared helpers, and unaffiliated reproduction. `CLAIMS.json:14` excludes research acceleration and impact claims. No unsupported bridge to physical systems, network applications, or general tensor-performance gains is offered.

5. **The novelty record supports cautious release language.** Manuscript lines 54–61 and 202–204 keep the historical problem statement separate from present open status, disclose the unauthenticated final publisher version, and avoid a proven-first-solution claim. `NOVELTY_REPORT.md:49,55–66` also avoids identifying the eigencurve with the Klein quartic or elevating negative searches into priority certification. I assessed consistency of these boundaries, not the underlying external searches.

## Optional improvements

### A1 — Put the matrix-spectrum exclusion in the standalone summary

- **Severity:** Low; optional, not an acceptance condition.
- **Location:** `report/fano_spectrum.md:17`, compared with definitions at lines 42–50 and `ASSURANCE.md:3–4`.
- **Issue:** A reader encountering only the summary could still associate “Fano spectrum” with an incidence matrix or its associated graph. The summary already says homogeneous adjacency and resultant, so the risk is limited and the full manuscript resolves it.
- **Remedy:** Optionally add a short sentence that the result concerns the specified order-three tensor, not the incidence-matrix or associated-graph spectrum. This would make excerpted summaries as clear as the assurance document.

### A2 — Label historical timing as a run observation

- **Severity:** Low; optional, not an acceptance condition.
- **Location:** Section 4.2, paragraph beginning “The whole computation takes about five minutes of Singular time per prime”.
- **Issue:** The timings describe useful practical scale, but without hardware and timing-method details they should not be reused as a portable performance benchmark or comparative speed claim. The paper currently makes no comparative speed claim, so this is a presentation refinement.
- **Remedy:** Optionally say “In the recorded runs” and identify hardware/timing conditions if recoverable; otherwise explicitly label the numbers as approximate historical observations. Do not reconstruct unavailable measurements.

## Decision

Accept for this internal editorial role. The submission specifies a narrow mathematical object, makes its unusual spectral and geometric behavior interpretable, and preserves the distinction between computation, proof dependencies, reproduction, priority, and impact. Required corrections: **none from this review**. Optional changes A1–A2 would improve reuse by readers encountering only excerpts. Publication must retain the existing candidate and assurance language; this recommendation does not promote the result to externally validated theorem status.
