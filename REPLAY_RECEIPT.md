# Producer replay receipt — 19 September 2026

`verification/replay-normal.json` and `replay-optimized.json` record current
default checks; `negative-controls.txt` records rejection of five corruption
classes in both modes. Saved-artifact checking includes all 449 coefficients,
all thirty residue polynomials, independent coefficientwise CRT, prime validity,
inductive bounds, source edge encoding and the stored Macaulay polynomial.
Fresh checks include all 168 automorphisms, 28 quadrangle sign classes, 21 line
classes at one, ten symbolic witness families, characteristic-zero saturation,
Hilbert series, Jacobian ideal and minimal resolution, the rational no-real-point
identity, chart lengths 17/15/24/1 and four Macaulay evaluations.

The complete original thirty-prime computation and full single-prime Macaulay
interpolation are preserved, not freshly repeated by this command. Earlier
local reconstruction additionally ran a fresh full H7 Poisson polynomial at
prime 1000000007; that earlier observation is not part of this default receipt.
No result here is unaffiliated reproduction or a formal proof.

The eleven-page rebuilt PDF passed raw-TeX preflight. All pages were visually
inspected; missing set-difference glyphs and overflowing reference links were
repaired. The final build emitted no overflow or missing-glyph warnings.
The baseline clean-extraction gate and exact frozen hashes are retained in the
publication workflow receipts, outside the self-hashed payload.
