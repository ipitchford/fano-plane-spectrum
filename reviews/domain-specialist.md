# Domain-specialist internal editorial review

Recommendation: **Minor Revision**. No fatal mathematical defect was identified in the reviewed geometry or reality arguments. This is a producer-coordinated, model-assisted internal review, not external specialist validation or historical-priority clearance.

## Scope and identity

Read-only review of `baseline-extract-final/fano-plane-spectrum`, identified by the supplied frozen ZIP SHA256 `0d3282ca0b3e123981f40c7f09c1adfcf591c194c0cf2120ef66bab023041ba5`, manuscript PDF SHA256 `4818810c1c914948e52bf0f4d24fe2017a459d4a3f3f780cc421a30802fbc8a5`, and manifest SHA256 `2b98d6996e98df092b9616e9dee0dbc56e3910d43db9bd0181a38cecc171aad2`. These identities were provided by the coordinator; I did not independently recompute the hashes. No submission files were edited, and no other new review reports were consulted.

I read the manuscript Markdown, characteristic-zero geometry and reality scripts, geometry output, chart-length script, finite eigenvector decomposition generator and selected outputs, subgroup-elimination generator, novelty report, and source map. The coordinator reports normal/optimized replay, negative controls and clean extraction passing; this review does not claim another execution of those tests. Confidence is high in the logical geometry implication given the reported exact CAS outputs, moderate in the complete finite classification and its artifact exposition, and limited concerning priority. I did not rerun the thirty-prime resultants, independently audit every decomposition, authenticate the publisher version of the prior paper, or conduct a new literature search.

## Strengths and substantive assessment

1. **Saturation and geometric irreducibility.** The manuscript correctly works with the saturation J rather than silently identifying the original cone ideal with its projective coordinate ring. The displayed Betti array has its last nonzero homological column at 5. With seven polynomial variables, the stated Auslander–Buchsbaum calculation gives depth 2. For this standard graded quotient, Cohen–Macaulayness yields the required purity and vanishing of the degree-zero local-cohomology obstruction, so global regular functions on Proj are K. After field extension the same resolution and Hilbert-series computation apply. The Jacobian-minor ideal having dimension zero excludes singular projective points. Thus the resulting geometric curve is smooth and connected, and consequently irreducible. This avoids the invalid shortcut from arithmetic irreducibility over a finite field to geometric irreducibility in characteristic zero.

2. **Degree and genus.** The numerator 1+4z+3z² gives Hilbert polynomial 8n−2, hence degree eight and arithmetic genus three. Smooth geometric irreducibility makes this the geometric genus. Saturation does not change Proj, so this is indeed the eigenvector curve. The eight exhibited distinct points on a coordinate hyperplane exhaust a degree-eight proper hyperplane section, once distinctness and properness are understood as in the construction.

3. **Reality.** The direct identity 1+Σx_i² in the rational chart ideal is an especially useful certificate. Its recorded construction uses a lift against the original seven equations and re-expands the residual. Together with point-transitivity, this rules out every nonzero real eigenvector at 2, including any outside the selected chart. It is stronger and clearer for this purpose than reliance on descriptions of primary components.

4. **Multiplicity interpretation.** The manuscript separates algebraic resultant exponent, geometric point count, and fibre scheme length. The 1 and 2 rows explicitly preserve nonreduced structure; the equality of finite scheme length and resultant exponent is presented as an observation for this example. The exponent 52 is not misidentified with the degree or a number of eigenvectors. The recent degree-sensitive bound is contextual and not a premise for the computation.

5. **Priority scope.** The normalization and mathematical object are explicit, excluding incidence/graph/E-spectrum collisions. The Rowling polynomial is credited as a regression fixture. The unresolved Lin–Bu wording and unauthenticated final publisher version are disclosed. A negative search is not promoted to a first-solution claim. These are appropriate boundaries for releasing an unrefereed computational candidate.

## Required minor revisions

### D1 — Clarify which decomposition objects are printed

Severity: minor, evidence-traceability issue. Required.

Section 5(e) states that the six components at 2 are primary, not prime, with quotient dimension four and radical residue degree two. However, `code/eig_run.py` explicitly sets `P = std(L[i][2])` for `primdecGTZ(I)`: these are the associated prime ideals, not the primary ideals in `L[i][1]`. Correspondingly, `out/eigenvectors/t-2.txt` prints six components of vector-space dimension two and total chart length 24. The mathematical distinction in the revised prose is right, but a reader following the cited historical decomposition output sees a different object and dimension.

Remedy: either add a small audit that prints both primary quotient dimension and associated-prime residue degree, clearly labelled, or explain that the historical files print associated primes and derive the double-point lengths from total length plus the transitive automorphism action (with conjugation if needed). Do the analogous clarification at 1, whose output lists associated-prime dimensions 1,2,1,1,2,2 but total chart length 15. Do not relabel the existing prime outputs as primary outputs. A full new number-field decomposition campaign is not required for this documentary correction.

### D2 — Remove ambiguity in the point–line incidence description

Severity: minor exposition. Required.

The point–line construction says the remaining lines are `{v_i,u_j,u_l}` **and** `{u_i,u_j,v_l}` over permutations of `{1,2,3}`. These are two indexings of the same three lines, not two disjoint families. The calculation itself uses the correct incidence pattern, but the wording suggests too many lines.

Remedy: list the remaining three lines once as `{v_i,u_j,u_k}` with `{i,j,k}={1,2,3}`, and explain that two such lines pass through each `u_i`.

## Optional improvements

- Supply a concise finite-classification receipt recording coefficient field, chart length, associated-prime residue degrees, primary lengths, and global orbit count. This would make Table 2 substantially easier to audit without suggesting every decomposition has been freshly replayed.
- Cite a standard algebraic-geometry reference for the depth/local-cohomology-to-connectedness step. The argument is valid as stated, but the audience may not routinely use it.
- Explain in one sentence why the eight coordinate-hyperplane points are distinct: for fixed quadratic root, the two coordinate triples have ratio μ, with μ²≠1, so different disjoint lines cannot identify their projective vectors; the two cube-root assignments remain distinct modulo common scaling.
- Authenticate the final Clark–Cooper publisher version or obtain an author response before strengthening priority or coefficient-correction language. Under the present bounded wording, this is not required to release the candidate as such.

## Editorial disposition

Acceptable as a carefully labelled computational theorem candidate after the two small clarifications above. This recommendation does not certify the original modular generation, every finite number-field decomposition, novelty, named human authorship, or external mathematical acceptance. It specifically endorses the internal logic of the characteristic-zero geometric argument and the sum-of-squares real obstruction, subject to the disclosed exact-CAS trust boundary.
