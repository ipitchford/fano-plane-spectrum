# The homogeneous adjacency spectrum of the Fano plane

Anonymous · v0.1.0-candidate · 19 September 2026.

**Unrefereed, AI-assisted computational theorem candidate.** Exact degree-448
resultant factorization with nineteen distinct eigenvalues, explicit witnesses,
H-spectrum `{0,1,3,theta}`, and a characteristic-zero degree-eight genus-three
eigencurve certificate. Not an incidence-matrix or E/Z-spectrum computation.
Priority, unaffiliated validation, formal verification and impact are unestablished.

Read [the paper](report/fano_spectrum.pdf), [accessible source](report/fano_spectrum.md),
[assurance](ASSURANCE.md), [review response](REVIEW_RESPONSE.md), and
[novelty audit](NOVELTY_REPORT.md).

## Reproduce

Install Python 3.12 or later, Singular 4.4.1, and the pinned Python packages:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python package.py check
python verify.py
python -O verify.py
python test_negative.py
```

Expected status is PASS; failed obligations return nonzero even under `-O`.
Default replay checks every saved final coefficient/residue and CRT bounds,
freshly substitutes vectors, recomputes saturation/smoothness/resolution and
rational chart lengths in characteristic zero, re-expands the real obstruction,
and makes four fresh Macaulay evaluations. It does not freshly repeat all thirty
modular polynomials or every number-field decomposition. The quicker saved-data
subset is `python verify.py --artifacts-only`.

Full original-resultant recomputation into a new directory:
`python code/poisson.py fresh-resultant 30 2`. This can take hours. The historical
twelve-prime H7 output is retained as diagnostic data; the hardened generator
now rejects products below the a-priori bound. The historical
`code/macaulay_full.py` shares interpolation helpers with Poisson; inspect its
interface before running and do not overwrite preserved original results.

## Layout

- `report/`: revised source and PDF.
- `code/`: supplied discovery programs, with explicit verifier failures added.
- `out/`, `out30/`, `out_rowling/`, `logs/`: historical computation artifacts.
- `verification/`: characteristic-zero certificates and current replay receipts.
- `verify.py`, `test_negative.py`, `package.py`: release entry points.
- `MANIFEST.sha256`: payload inventory, excluding itself, Git and caches.

Empty historical output slots now contain replacement pointers, not invented
certificates. Original prose/data are CC0; code is MIT. Third-party articles and
the supplied review are not redistributed. Build the PDF with
`pandoc report/fano_spectrum.md --pdf-engine=tectonic -o report/fano_spectrum.pdf`.
