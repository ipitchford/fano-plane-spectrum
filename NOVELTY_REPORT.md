# Novelty gate: homogeneous adjacency spectrum of the Fano plane

Search date: 19 September 2026. Scope: bounded primary-source and code search, not priority certification. Frozen target: `target.yaml`.

## Claim and normalization

The proposed contribution is the complete degree-448 resultant factorization for the symmetric order-three adjacency tensor with entries 1/2 on permutations of Fano lines, plus its eigenvector geometry. The eigen-equation is A x² = lambda x^[2]. It is not the incidence matrix, Heawood graph, matroid characteristic polynomial, or E/Z-spectrum. Those were excluded rather than treated as collisions.

Fingerprints searched included degree448; exponents35,28,52; the factor lambda²+lambda+2; codegree14 coefficient120204; and the exceptional degree-eight eigenvector curve. Small exact objects were fixed as H1: lambda; H2: lambda^4; H4: lambda^14(lambda³−1)^6; and the H5 bowtie polynomial. The coefficient sequence starts 1,0,0,−336,0,0,55524,−696. Aliases included hypermatrix/tensor resultant, homogeneous adjacency spectrum, STS(7), PG(2,2), and eigenvariety. Graph and matroid spectra use different equations and degrees, so they cannot settle this claim.

## Searches actually made

Web queries included:

- `"Fano plane" "spectrum" characteristic polynomial`
- `"Fano" "52" "35" spectrum`
- `"Fano" "120204"`
- `"Fano plane" eigenvariety curve degree eight`
- `"Fano plane" "characteristic polynomial" spectrum -site:unsolvedmath.com`
- `"Fano" "lambda" "52" characteristic polynomial`
- `site:github.com "Fano" "spectrum" tensor`
- `"Fano plane" "homogeneous" spectrum eigenvalues`
- `"Fano plane" "characteristic polynomial" "448"`
- `"Fano" "lambda^2+lambda+2" spectrum`
- `"Fano plane" "eigenvariety"`
- `"Fano plane" "tensor" eigenvalues spectrum Cooper Clark`
- `"Fano plane" "120204" characteristic`
- `"Fano plane" "448" eigenvalues`
- `"Fano" "degree eight" eigenvectors`
- `"Fano plane" spectrum "Klein" tensor`
- `"Fano plane" "eigenvalues" "2" Cooper Dutle`
- `site:github.com "Fano" "charpoly"`
- `Hu Ye Multiplicities tensor eigenvalues reduced eigenvariety conjecture 2016`
- `"Fano plane" "spectrum" "35"`
- `"Fano plane" "spectrum" "52"`

Direct GitHub CLI code searches `"Fano" "spectrum"` (limit15) and `"Fano" "characteristic"` (limit20) both returned empty arrays. This is negative search evidence, not evidence that no implementation exists. Indexed GitHub search also produced no relevant tensor-resultant implementation; octonion code hits were different objects.

## Primary-source adjudication

1. [Cooper's problem list](https://people.math.sc.edu/cooper/combprob.html) still asks the homogeneous adjacency spectrum question. The page explicitly dates itself October2020. This confirms provenance, **not current open status**.
2. [Clark–Cooper, Applications of the Harary–Sachs theorem](https://arxiv.org/html/2107.10781v1), Section4/Figure2, distinguishes the sixteen leading coefficients for the full Fano plane from a complete polynomial for the Rowling hypergraph (two lines removed). The printed Fano c14 is −122004. No complete Fano factorization was located in this inspected source. The Oxford published-paper search extract supports the same distinction; its direct download failed during this audit, so the fully accessible inspected version was the arXiv text/PDF.
3. [Clark–Cooper, leading coefficients and multiplicity manuscript](https://people.math.sc.edu/cooper/coeffandmult.pdf), pp10–11, supplies the complete Rowling polynomial, not the full Fano polynomial. This is established prior work, not a new contribution of the supplied bundle.
4. [Lin–Bu, September2026](https://arxiv.org/html/2609.05897v1), introduction, says the Fano characteristic polynomial was obtained in2022 and cites Clark–Cooper. The cited accessible paper does not support that stronger wording. This is a **citation ambiguity requiring cautious priority language**, not a verified collision with the submitted factorization.
5. [ILAS IMAGE62, spring2019](https://ilasic.org/wp-content/uploads/IMAGE/image62.pdf), p18, asks for the totally nonzero Fano eigenvalues and their use in computing the characteristic polynomial. This is an earlier provenance lead, not a present-day novelty certificate.
6. [Hu–Ye, Conjecture1.1](https://arxiv.org/abs/1412.2831) states the component-dimension multiplicity lower bound. The manuscript's added equality-if-and-only-if-reduced qualification is not part of that conjecture.
7. **New relevant literature:** [Doğan–Tsigaridas–Zafeirakopoulos, September1,2026](https://arxiv.org/html/2609.01268v1), Theorem1.7, claims a proof of a stronger degree-refined bound, implying Hu–Ye. No Fano mention was found in that text. For a reduced degree-eight curve, the stated bound gives 8·2·2=32, not merely4; the candidate multiplicity52 is compatible with it. This audit checked the theorem statement/application, not the whole general proof. Cite it as a recent preprint and update the literature discussion.

The new smooth genus-three curve calculation suggests a relation to the Klein quartic. Searches found standard Fano/Klein symmetry connections, including [Baez's exposition](https://math.ucr.edu/home/baez/klein.html), but did not establish the identity of this particular eigencurve with a classical model. No new cross-identification is claimed. If that bridge is pursued, its own formula-level novelty gate must be run.

## Outcome by contribution

| Unit | Outcome | Defensible wording |
|---|---|---|
| Complete Fano polynomial | BOUNDED UNCERTAINTY; no exact collision found | A complete exact computation; no earlier full formula located in this search |
| Poisson/Macaulay method | Established method | An application and reproducible implementation, not a new resultant algorithm |
| Explicit eigenvectors and eigencurve | Promising; priority unconfirmed | Explicit constructions and checked geometry for this tensor |
| Rowling polynomial | COLLISION / validation fixture | Reproduction of Clark–Cooper's known result |
| Hu–Ye inequality | Established conjecture with recent claimed general resolution | Context, not a conjecture resolved by this example |
| New audit certificates | Newly generated audit artifacts | Reproducible checks, not independent external peer review |

## Missingness and decision

No author inquiries were made. This audit did not exhaust MathSciNet, zbMATH, theses, non-English sources, unindexed code, or unpublished computations. It did not independently repeat every search claimed in the submitted manuscript. Search engines produced many irrelevant Fano-variety and graph-spectrum hits, limiting recall. No result is promoted to historical priority merely because formula searches were negative.

Decision: **BOUNDED UNCERTAINTY, with a credible publication candidate.** The exact formula has plausible novelty; publish only with bounded language unless a specialist/author check establishes stronger priority. A new explicit classical-curve identification, discovery of source code, or a response from Clark/Cooper should trigger a renewed gate.
