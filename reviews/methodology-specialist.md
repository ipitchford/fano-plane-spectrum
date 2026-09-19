# Methodology specialist review — frozen submission r1-final

Recommendation: **Accept for publication as the explicitly unrefereed computational theorem candidate described in this package.** No required methodological correction identified in the inspected scope. This is an internal model-assisted editorial assessment, not external validation or journal acceptance.

## Scope, identity, confidence and conflicts

Reviewed the read-only extracted package `baseline-extract-final/fano-plane-spectrum`, specifically the mathematical/computational dependency chain in `report/fano_spectrum.md`, `verify.py`, `code/poisson.py`, `code/run_h7_30.py`, `code/macaulay.py`, the characteristic-zero geometry and reality scripts, chart-length script, source of the number-field ideal, README, ASSURANCE, STATUS and current replay receipt. The paper and manifest hashes were freshly read and match the assigned frozen identity:

- Paper SHA256: `4818810c1c914948e52bf0f4d24fe2017a459d4a3f3f780cc421a30802fbc8a5`.
- Manifest SHA256: `2b98d6996e98df092b9616e9dee0dbc56e3910d43db9bd0181a38cecc171aad2`.
- Assigned ZIP SHA256: `0d3282ca0b3e123981f40c7f09c1adfcf591c194c0cf2120ef66bab023041ba5` (not independently rehashed in this role).

Confidence is high in the code-to-equation correspondence and stated logical dependencies examined here, moderate in the overall computational claim because the complete modular runs and all finite decompositions were not rerun by this role. Baseline normal/optimized, negative-control and extraction gates were supplied as already passing; I inspected the current receipt and underlying code rather than claiming another execution. No other new reviewer reports were read. No submission files were edited and no subagents were used. This reviewer is part of the same AI-assisted production/editorial process, with no organizational independence; no other conflicts are known to this role. Bibliographic priority, authenticated authorship, CAS implementation correctness and proof-assistant verification are outside this review.

## Substantive strengths

1. **Resultant recovery has a valid deterministic uniqueness argument.** Section 4 correctly applies the largest-coordinate argument to bound every eigenvalue by maximum degree and then bounds coefficients by `(1+Delta)^degree`. Its thirty-prime final modulus clears twice the bound; the six reused stages have their own bounds. The twelve-prime final run and drop-prime stability are explicitly demoted to checks. In `poisson.py`, restriction at the last coordinate zero gives the induced previous hypergraph, the quotient determinant multiplies the square of the previous resultant, and interpolation is applied to that product, not to the generally rational determinant alone. Usable points exclude previous-resultant zeros and quotient dimensions are checked. Monicity, surplus interpolation points, CRT stability and the deterministic modulus requirement have explicit failures.

2. **The two determinant constructions really differ, with shared dependencies acknowledged.** `macaulay.py` constructs the degree `n+1` Macaulay matrix by assigning each monomial to its first square divisor and takes the extraneous minor on monomials with at least two square divisors. The verifier demands a nonzero denominator. The paper correctly calls this algorithmic diversity and discloses shared interpolation helpers. Neither fixed spot checks nor the stored full single-prime interpolation is promoted to a probability of program correctness.

3. **The curve argument supplies the missing geometric logic after CAS output.** Section 3.1 uses a characteristic-zero quadratic field, saturation, dimension/Hilbert series, Jacobian minors and the length of a minimal resolution. The script equations match the seven stated edges. Codimension five explains the selected minors. Cohen–Macaulay depth two supplies purity and the global-functions/connectedness argument; geometric smoothness plus geometric connectedness then gives geometric irreducibility. The Hilbert numerator yields degree eight and polynomial `8n-2`, hence genus three. This is materially stronger than inferring irreducibility or smoothness from a single finite-field computation.

4. **The real obstruction is a directly checkable algebraic identity.** `reality_audit.sing` lifts `1 + sum(x_i^2)` into the rational chart ideal and explicitly re-expands the identity. The equations agree with the lambda-two specialization. Positivity excludes real chart points, and the freshly computed point-transitive automorphisms justify covering every nonzero real eigenvector. This avoids mistaking rational primary components for geometric points or prime ideals.

5. **Assurance statements track actual verifier coverage.** `verify.py` compares all final coefficients/residues, independently reconstructs CRT coefficients, and separately performs fresh symbolic, geometry, reality, chart-length and Macaulay checks. Explicit `require` failures survive optimization. The paper distinguishes existence witnesses from resultant completeness and fibre lengths from resultant multiplicities. README/ASSURANCE/receipt disclose the historical computations that default replay does not rerun.

## Issues and improvements

All items below are **optional**, low severity, and do not invalidate the frozen candidate or require a new publication revision.

- **Preserve modular residues in the advertised full generator.** Location: `code/poisson.py:180–199`, README full recomputation command. The all-stage generator accumulates `per_prime` but serializes only the lifted stage polynomials, whereas the historical final-stage driver preserves `h7_per_prime.json`. A fresh run reproduces the integer result but does not leave the same granular audit trail as the frozen final-stage artifacts. Remedy: in a future release, serialize each stage's per-prime polynomials and prime/evaluation metadata to the new output directory. Existing final-stage residues are present and their checking is correctly described.

- **Make finite classification coverage easier to audit.** Location: paper Section 3.1/Table 2, `code/eig_nf.sing`, `verify.py:fresh_checks`. Rational chart lengths do not, by themselves, establish each nonrational classification, and the paper correctly says so. A compact table mapping each Table 2 row to its exact producer script, output and geometric point/length calculation would reduce effort for reproduction. An optional extended replay command could regenerate these decompositions. This is a traceability improvement, not a request to present the current receipt as more comprehensive.

- **Reduce duplicated equation encodings in future verification infrastructure.** Location: the edge lists in Poisson/Macaulay/verifier and the explicit Singular audit equations. I checked the inspected encodings against the same seven lines and found correspondence. A future machine-generated equation comparison or canonical edge-to-polynomial export would make this trust boundary easier to recheck after edits. Retaining differently implemented determinant constructions remains valuable; the proposal concerns input correspondence, not collapsing both algorithms into one.

- **Output matching is deliberately version-sensitive.** Location: `verify.py:fresh_checks`, literal Singular Hilbert/Betti/generator strings. These checks fail closed and are adequate for the pinned environment, but harmless formatting or Gröbner-basis presentation changes may cause failure on another release. Structured algebraic assertions inside Singular would improve portability. This is a reproducibility inconvenience, not an observed false pass.

## Decision boundary

Accept the bounded publication claim and its disclosed exact-CAS dependencies. Do not relabel this review, baseline replay, hashes or preserved computations as unaffiliated reproduction, formal proof, priority clearance or journal peer review. A fresh full resultant run and expanded finite-classification replay would strengthen later validation, but the submission already states their present coverage accurately.
