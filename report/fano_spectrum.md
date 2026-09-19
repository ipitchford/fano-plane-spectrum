---
title: "The homogeneous adjacency spectrum of the Fano plane"
subtitle: "Exact resultant computation and eigenvector geometry — unrefereed candidate"
author: "Anonymous"
date: "19 September 2026 · v0.1.0-candidate"
geometry: margin=2.4cm
fontsize: 11pt
header-includes:
  - \usepackage{amsmath,amssymb,booktabs,longtable}
  - \usepackage{microtype}
  - \usepackage{xurl}
  - \emergencystretch=3em
---

# Summary

We compute the homogeneous adjacency spectrum of the Fano plane, the seven-point, seven-line projective plane of order two. Under the Cooper–Dutle adjacency normalization, its characteristic polynomial is the resultant of seven quadratic eigen-equations and has degree $448$. We give its complete factorization, explicit eigenvectors for all nineteen distinct roots, an exact obstruction to real eigenvectors at the real eigenvalue $2$, and a characteristic-zero certificate for a smooth geometrically irreducible degree-eight, genus-three eigenvector curve. Modular Poisson recursion, a deterministic coefficient bound and recorded residues support the integer resultant; a different Macaulay determinant construction supplies additional producer-side checks. The problem appears in Cooper's October 2020 list and UnsolvedMath as AMR-030-0030. This is an anonymous, AI-assisted, unrefereed computational theorem candidate: historical priority, unaffiliated reproduction and formal verification are not established.

The full answer is the following.

**Theorem.** Let $\phi_F(\lambda)$ be the characteristic polynomial of the adjacency hypermatrix of the Fano plane $F$, normalised as in Cooper and Dutle (2012). Then
$$
\begin{aligned}
\phi_F(\lambda)={}&\lambda^{35}(\lambda-1)^{35}(\lambda-2)^{28}(\lambda-3)\,(\lambda^{2}-\lambda+1)^{7}(\lambda^{2}+2\lambda+6)^{7}(\lambda^{2}+\lambda+1)^{21}\\
&\times(\lambda^{2}+\lambda+2)^{52}(\lambda^{3}+2\lambda^{2}+2\lambda-2)^{21}(\lambda^{4}-\lambda^{3}-\lambda^{2}+\lambda+1)^{28}.
\end{aligned}
$$
Consequently the Fano plane has exactly nineteen distinct eigenvalues. The spectral radius $3$ is a simple root; $0$ has multiplicity $35$; the real eigenvalues are $0,1,2,3$ and the real root $\theta=0.5747430738\ldots$ of $\lambda^{3}+2\lambda^{2}+2\lambda-2$; of these, $0,1,3$ and $\theta$ possess real eigenvectors (they are H-eigenvalues in Qi's terminology) while $2$, although a real eigenvalue of multiplicity $28$, has no real eigenvector at all. The spectrum is not invariant under multiplication by a primitive cube root of unity.

Every displayed root has an explicit, hand-checkable eigenvector (Section 3). These substitutions prove existence, not completeness: exclusion of further eigenvalues and all resultant multiplicities depend on Section 4's exact computation. Section 5 distinguishes correlated internal identities, a published-object regression, a different determinant algorithm, and newly replayed checks. None is labelled unaffiliated independent reproduction. Except at the roots of $\lambda^{2}+\lambda+2$, finite eigenvectors are organized by points, lines, flags and anti-flags; those two roots instead have a curve of eigenvectors (Section 3.1).

# 1. The problem and its status

## 1.1 Definitions

Label the points of the Fano plane $1,\dots,7$ and take the lines to be the translates of the difference set $\{1,2,4\}$ modulo $7$:
$$
124,\;235,\;346,\;457,\;561,\;672,\;713 .
$$
Each point lies on three lines, any two points lie on exactly one line, and any two lines meet in exactly one point. The automorphism group is $\mathrm{PSL}(2,7)$, of order $168$, and it is transitive on points, on lines, on flags (incident point–line pairs) and on anti-flags.

Following Cooper and Dutle (2012, Definition 3.1), the adjacency hypermatrix of a $k$-uniform hypergraph $H$ on $n$ vertices is the symmetric order-$k$ array $\mathcal A$ with $a_{i_1\cdots i_k}=1/(k-1)!$ when $\{i_1,\dots,i_k\}$ is an edge and $0$ otherwise. The normalisation makes the $i$-th coordinate of $\mathcal A x^{k-1}$ equal to the sum, over the edges $e$ containing $i$, of the product of the $x_j$ for $j\in e\mathbin{\backslash}\{i\}$. For the Fano plane ($k=3$, $n=7$) this reads
$$
(\mathcal A x^{2})_i=\sum_{\{i,j,l\}\ \text{a line}} x_j x_l ,\qquad i=1,\dots,7 .
$$
A number $\lambda\in\mathbb C$ is an eigenvalue if $\mathcal A x^{2}=\lambda x^{[2]}$ for some non-zero $x\in\mathbb C^{7}$, where $x^{[2]}=(x_1^{2},\dots,x_7^{2})$; this is the "homogeneous" eigenvalue problem of Qi (2005) and Lim (2005), as distinct from the E- or Z-eigenvalue problem. The characteristic polynomial is the resultant
$$
\phi_F(\lambda)=\operatorname{Res}\bigl(\lambda x_1^{2}-(\mathcal Ax^{2})_1,\ \dots,\ \lambda x_7^{2}-(\mathcal Ax^{2})_7\bigr),
$$
a monic polynomial of degree $n(k-1)^{n-1}=7\cdot 2^{6}=448$ whose roots are exactly the eigenvalues; the spectrum is the multiset of its roots, the multiplicity of a root being its algebraic multiplicity. An eigenvalue is an H-eigenvalue when it has a real eigenvector (so it is itself real).

## 1.2 What was known

Cooper's October 2020 snapshot poses the question and marks it open; that historical label is not a current priority certificate. Clark and Cooper (2021) proved a Harary–Sachs theorem for hypergraphs, expressing characteristic coefficients through Veblen multi-hypergraphs. The inspected author version of their sequel (2022, arXiv:2107.10781v1, Fig. 2) gives the coefficients $c_0,\dots,c_{15}$ for the Fano plane and its one- and two-line deletions. For the latter, the "Rowling hypergraph" $R$, it gives the complete polynomial,
$$
\begin{aligned}
\phi_R(x)={}&x^{133}(x^{3}-1)^{27}(x^{15}-13x^{12}+65x^{9}-147x^{6}+157x^{3}-64)^{12}\\
&\times(x^{6}-x^{3}+2)^{6}(x^{6}-17x^{3}+64)^{3},
\end{aligned}
$$
and reports difficulty with direct resultant computation. For the full Fano plane the inspected version stops at $c_{15}$. Lin and Bu (2026, Introduction) refer to a Fano characteristic polynomial obtained in 2022, citing this work. That statement is a relevant priority lead, but the inspected source supports only the leading-coefficient computation. We have not authenticated the final publisher PDF in this revision. The database's unsupported closed-form annotation likewise does not resolve priority. Section 6 states the bounded search conclusion.

# 2. The result

Table 1 lists the ten irreducible factors. A factor's exponent is the multiplicity of **each** of its roots, not a count of eigenvectors. The degree-weighted exponents sum to $448$.

| Minimal polynomial | Degree | Multiplicity per root |
|:---|---:|---:|
| $\lambda$ | 1 | 35 |
| $\lambda-1$ | 1 | 35 |
| $\lambda-2$ | 1 | 28 |
| $\lambda-3$ | 1 | 1 |
| $\lambda^2-\lambda+1$ | 2 | 7 |
| $\lambda^2+2\lambda+6$ | 2 | 7 |
| $\lambda^2+\lambda+1$ | 2 | 21 |
| $\lambda^2+\lambda+2$ | 2 | 52 |
| $\lambda^3+2\lambda^2+2\lambda-2$ | 3 | 21 |
| $\lambda^4-\lambda^3-\lambda^2+\lambda+1$ | 4 | 28 |

Table 1. Exact factor data. Decimal approximations are auxiliary data in the accompanying JSON summary. The cubic has exactly one real root because its derivative $3\lambda^2+4\lambda+2$ is positive. The quartic equals $(\lambda^2-\lambda/2-1)^2+3\lambda^2/4$ and is strictly positive on $\mathbb R$. Each quadratic has negative discriminant. Thus the five real eigenvalues listed in the theorem are exhaustive.

Several features deserve comment. First, the largest coefficient of $\phi_F$ in absolute value is that of $\lambda^{173}$, about $-1.05\times10^{62}$ (207 bits), and yet the polynomial splits over $\mathbb Q$ into factors of degree at most four. Second, the spectral radius $3$ — the common degree of the vertices — is a simple root, so its algebraic multiplicity equals the number of its projective eigenvectors (one, the all-ones vector), the case of equality in the inequality $\operatorname{am}(\lambda)\ge|\mathbb V_\lambda|$ proved by Fan (2024) for eigenvalues of modulus $\rho$ of weakly irreducible non-negative tensors. Third, the spectrum is not invariant under multiplication by $\omega=e^{2\pi i/3}$: the coefficient $c_7=-696$ of $\lambda^{441}$ is non-zero, whereas invariance would force every non-zero coefficient to sit at a codegree divisible by three (Cooper and Dutle, 2012, proof of Theorem 4.2). This is as it should be: Cooper and Dutle prove such invariance for $k$-partite $k$-graphs, and the Fano plane is famously not tripartite (no 3-colouring of its points makes every line rainbow). Fourth, $2$ is a real eigenvalue with twenty-eight-fold multiplicity whose eigenvectors are all non-real; its eigenvectors are built from cube roots of unity (Section 3).

As by-products the same computation gives the characteristic polynomials of the induced sub-hypergraphs along the chain used in the recursion: the "bowtie" of two lines through a common point on five vertices,
$$
\phi(\lambda)=\lambda^{35}(\lambda-1)^{6}(\lambda^{2}+\lambda+1)^{6}(\lambda^{3}-2)^{9}\qquad(\deg 80),
$$
and the Pasch configuration (the Fano plane with a point and the three lines through it deleted; four lines on six points),
$$
\begin{aligned}
\phi(\lambda)={}&\lambda^{75}(\lambda-1)^{12}(\lambda-2)^{3}(\lambda^{2}+2\lambda+4)^{3}(\lambda^{2}+\lambda+1)^{12}\\
&\times(\lambda^{2}+\lambda+2)^{12}(\lambda^{4}-\lambda^{3}-\lambda^{2}-2\lambda+4)^{12}\qquad(\deg 192).
\end{aligned}
$$
Eigenvalues of an induced sub-hypergraph need not be eigenvalues of the whole; the same warning applies to ordinary graphs. Here the roots of $\lambda^{2}+2\lambda+4$ and $\lambda^{4}-\lambda^{3}-\lambda^{2}-2\lambda+4$ occur for the Pasch configuration but not the Fano plane. Extending a Pasch eigenvector by zero at the deleted point $p$ imposes the additional equation $\sum_{L\ni p}x_ux_v=0$. The disjoint-union multiplicity theorem of Cooper and Dutle does not remove this condition.

# 3. Explicit eigenvectors: existence by hand

The automorphism group supplies natural ansätze: look for eigenvectors constant on the orbits of a subgroup. The point stabiliser, the line stabiliser, the flag stabiliser and the anti-flag stabiliser each give a small polynomial system, and between them they account for all nineteen eigenvalues except $2$ and the roots of $\lambda^{2}+\lambda+2$, which need cube roots of unity. In what follows $p$ is a point, $L$ a line, and I write $x_v$ for the coordinate at vertex $v$; each verification uses only the incidence facts stated in Section 1.1. All ten identities were also checked symbolically (script `verify_eigenvectors.py`, reducing $(\mathcal Ax^{2})_i-\lambda x_i^{2}$ modulo the minimal polynomial of $\lambda$).

**Point ansatz.** Put $x_p=a$ and $x_v=1$ for $v\neq p$. At $p$ each of the three lines contributes $1$, so $3=\lambda a^{2}$; at $v\neq p$ exactly one line through $v$ contains $p$, so $a+2=\lambda$. Hence $(a+2)a^{2}=3$, i.e. $(a-1)(a^{2}+3a+3)=0$: $a=1$ gives $\lambda=3$ with the all-ones eigenvector, and $a^{2}+3a+3=0$ gives $\lambda=a+2$ with $\lambda^{2}-\lambda+1=0$, eigenvector $\mathbf 1+(\lambda-3)e_p$.

**Line ansatz.** Put $x_v=a$ on $L$ and $x_v=1$ off $L$. At a point of $L$: $a^{2}+2=\lambda a^{2}$; off $L$ every line through $v$ meets $L$ once: $3a=\lambda$. So $3a^{3}-a^{2}-2=(a-1)(3a^{2}+2a+2)=0$: $a=1$ is again $\lambda=3$, and $3a^{2}+2a+2=0$ gives $\lambda=3a$ with $\lambda^{2}+2\lambda+6=0$, eigenvector equal to $\lambda/3$ on $L$ and $1$ elsewhere.

**A single line.** The indicator vector of $L$ satisfies $(\mathcal Ax^{2})_v=1=x_v^{2}$ on $L$ and $0=x_v^{2}$ off $L$, so $\lambda=1$. Twisting by a cube root of unity, $x=(1,\omega,1)$ on $L$ (in any order) and $0$ off $L$ gives $\lambda=\omega$: at the vertex carrying $\omega$ the product of the other two is $1=\omega\cdot\omega^{2}$, at the others it is $\omega=\omega\cdot1$. The conjugate gives $\bar\omega$; these are the roots of $\lambda^{2}+\lambda+1$.

For $\lambda=1$, the two further projective classes on each ordered line are $(1,\omega,\omega^2)$ and $(1,\omega^2,\omega)$, extended by zero. Products of the other two entries equal the square of the remaining entry. Permutation and projective scaling give exactly these two classes besides the indicator. Thus there are three classes per line, not three real classes.

**Point–line ansatz with cube roots of unity.** Fix $p$ and a line $M$ not through $p$. The three lines through $p$ are $\{p,u_i,v_i\}$ with $M=\{v_1,v_2,v_3\}$. The remaining three lines are $\{v_i,u_j,u_k\}$, one for each $i$, where $\{i,j,k\}=\{1,2,3\}$; two of these lines pass through each $u_i$. Let $\zeta_1,\zeta_2,\zeta_3$ be the three cube roots of unity in some order and put $x_p=0$, $x_{v_i}=\zeta_i$, $x_{u_i}=\mu\zeta_i$. Using $\zeta_j\zeta_k=\zeta_i^{-1}=\zeta_i^2$, the equation at $p$ is $\mu(\zeta_1^2+\zeta_2^2+\zeta_3^2)=0$, at $v_i$ it is $(1+\mu^2)\zeta_i^2=\lambda\zeta_i^2$, and at $u_i$ it is $2\mu\zeta_i^2=\lambda\mu^2\zeta_i^2$. Hence $\lambda=1+\mu^2$ and $\lambda\mu=2$, so $\lambda^3-\lambda^2-4=(\lambda-2)(\lambda^2+\lambda+2)=0$. The choice $\mu=1$ gives $\lambda=2$, with zero at $p$ and a distinct cube root on each opposite pair. The choice $\mu=2/\lambda=\bar\lambda$ gives the two quadratic roots. No real vector arises in these constructions; Section 5(e) excludes every real eigenvector at $2$.

**Flag ansatz.** Fix $p\in L$ and put $x_p=a$, $x=b$ on $L\mathbin{\backslash}\{p\}$, $x=1$ on the four points off $L$. The equations are $b^{2}+2=\lambda a^{2}$ at $p$, $ab+2=\lambda b^{2}$ on $L\mathbin{\backslash}\{p\}$, and $a+2b=\lambda$ off $L$. Eliminating $a$ and $b$ gives $(\lambda-3)(\lambda^{2}-\lambda+1)(\lambda^{2}+2\lambda+6)(\lambda^{3}+2\lambda^{2}+2\lambda-2)=0$, and for a root of the cubic the eigenvector is
$$
x_p=\frac{\lambda^{2}+2\lambda+4}{\lambda+2},\qquad x_v=-\frac{2}{\lambda+2}\ (v\in L\mathbin{\backslash}\{p\}),\qquad x_v=1\ (v\notin L).
$$
For the real root $\theta$ this vector is real, so $\theta$ is an H-eigenvalue.

**Anti-flag ansatz.** Fix $p\notin M$ and put $x_p=a$, $x=b$ on $M$, $x=1$ on the other three points $R$. Every line through $p$ has one point in $M$ and one in $R$; through $m\in M$ pass $M$, the line $\{m,p,r\}$ and a line $\{m,r',r''\}$; through $r\in R$ pass $\{r,p,m\}$ and two lines of type $\{r,m',r'\}$. The equations are $3b=\lambda a^{2}$, $b^{2}+a+1=\lambda b^{2}$, $ab+2b=\lambda$, whose eliminant is $\lambda(\lambda-3)(\lambda^{2}-\lambda+1)(\lambda^{2}+2\lambda+6)(\lambda^{4}-\lambda^{3}-\lambda^{2}+\lambda+1)$; for a root of the quartic,
$$
x_p=-(\lambda+1)(\lambda^{2}-2\lambda+2),\qquad x_v=\lambda^{2}-1\ (v\in M),\qquad x_v=1\ (v\in R).
$$

**Zero.** Each $e_p$ is an eigenvector. There are also four projective sign classes supported on each quadrangle $Q$ (the complement of a line): set coordinates off $Q$ to zero and put signs $s_v\in\{1,-1\}$ on $Q$ with $\prod_{v\in Q}s_v=-1$. At a point of $Q$ every product vanishes; at a point outside $Q$ the two nonzero products cancel. Of the eight odd-parity sign assignments, global negation pairs them into four projective classes. This gives $7+7\cdot4=35$ explicit zero-eigenvectors.

This establishes that all nineteen numbers in Table 1 are eigenvalues. A stronger statement also holds: the involution of the Fano plane fixing the line $124$ pointwise and swapping $3\leftrightarrow5$, $6\leftrightarrow7$ has five orbits, and eliminating the five orbit-variables from the eigen-equations (Singular, `eliminate`) yields exactly the product of the ten irreducible factors of Table 1 and nothing else; so every eigenvalue of the Fano plane admits an eigenvector invariant under a reflection. That the list is *complete*, and the multiplicities, require the resultant.

## 3.1 Eigenvarieties and the meaning of the multiplicities

For each eigenvalue one can also ask for *all* eigenvectors. Table 2 records the finite projective classifications from exact chart computations and the curve result proved below. Work in $x_7=1$ over $\mathbb Q$ or $\mathbb Q(\lambda)$. The automorphism group is point-transitive, so the translates of this chart cover every nonzero eigenvector. Distinct classes, local scheme lengths and resultant exponents must be counted separately. In particular, a primary component need not be prime, and its residue field need not be the coefficient field. The finite classifications use the supplied primary-decomposition computations; the release verifier checks their rational chart lengths and explicit vector families but does not claim to rerun every number-field decomposition.

| eigenvalue | projective eigenvectors | length of the eigen-scheme | algebraic multiplicity |
|------------------|-------------------------|----------------------------------|------------|
| $3$ | $1$ | $1$ | $1$ |
| $e^{\pm i\pi/3}$ | $7$ (one per point) | $7$ | $7$ |
| $-1\pm i\sqrt5$ | $7$ (one per line) | $7$ | $7$ |
| roots of the cubic | $21$ (one per flag) | $21$ | $21$ |
| roots of the quartic | $28$ (one per anti-flag) | $28$ | $28$ |
| $\omega,\bar\omega$ | $21$ (three per line) | $21$ | $21$ |
| $0$ | $35$ | $35$ | $35$ |
| $1$ | $21$ (three per line) | $35$ | $35$ |
| $2$ | $14$ (two per point) | $28$ (every point double) | $28$ |
| $(-1\pm i\sqrt7)/2$ | a curve of degree $8$ | — | $52$ |

Table 2. Eigenvectors, eigen-scheme lengths and resultant multiplicities. Length is summed globally over geometric projective points, using chart computations and the group action, not by multiplying a single chart length by seven. At $1$, seven line indicators are simple and fourteen twisted vectors are double; at $2$, all fourteen points are double. The rational chart lengths at $0,1,2,3$ are respectively $17,15,24,1$.

The historical `eig_run.py` output prints the associated primes, entry two of each `primdecGTZ` pair, not its primary ideal. A new labelled check, `verification/primary_lengths.sing`, prints both. At $1$ the six rational chart components have (primary quotient length, prime residue degree) equal to $(1,1)$ three times and $(4,2)$ three times: nine geometric points of total length fifteen. At $2$ the pair is $(4,2)$ six times: twelve geometric double points of total length twenty-four. The old prime output is preserved without relabelling it as a primary certificate.

The last two columns agree in the finite cases here. This agreement is an observation, not a general theorem identifying fibre length with the order of vanishing of a resultant pencil. Hu and Ye (2016) conjecture the lower bound $\operatorname{am}(\lambda)\ge\sum_i\dim(V_i)2^{\dim(V_i)-1}$ for the irreducible affine eigenvariety components. No assertion that equality is equivalent to reducedness is made. The degree-sensitive inequality in the recent preprint of Doğan, Tsigaridas and Zafeirakopoulos (2026, Theorem 1.7) yields $8\cdot2\cdot2=32$ for the degree-eight curve cone, compared with the resultant exponent $52$. We cite that preprint as related work, not as a premise needed for the computation.

### Characteristic-zero proof of the curve assertion

Let $K=\mathbb Q(t)$ with $t^2+t+2=0$, let $R=K[x_1,\ldots,x_7]$, and let $I$ be the ideal of the seven homogeneous eigen-equations at $t$. Set $J=I:(x_1,\ldots,x_7)^\infty$. The script `verification/geometry_audit.sing` constructs these equations directly and computes saturation, a Gröbner basis, the Jacobian ideal and a minimal free resolution over this characteristic-zero field. Its exact outputs are
$$
\dim R/J=2,\qquad H_{R/J}(z)=\frac{1+4z+3z^2}{(1-z)^2},\qquad
\dim R/(J+I_5(\operatorname{Jac}J))=0.
$$
Here $I_5$ denotes all $5\times5$ minors. The saturated ideal contains $x_1+\cdots+x_7$; this statement is about $J$, not the original unsaturated cone ideal $I$. The Cohen–Macaulay calculation below implies that the cone is pure of dimension two. The last displayed dimension therefore says that its singular locus is supported only at the origin: the minors give tangent-space dimension at most two at each nonzero geometric closed point, equal to its local dimension. The projective curve is smooth, also after extension to an algebraic closure in characteristic zero.

The computed minimal resolution has nonzero homological columns $0$ through $5$ and none later. Thus $\operatorname{pd}_R(R/J)=5$ and Auslander–Buchsbaum gives depth $2$, equal to the dimension: the coordinate ring is Cohen–Macaulay. Its depth-two local-cohomology vanishing identifies $H^0(\operatorname{Proj}R/J,\mathcal O)$ with $(R/J)_0=K$. These properties persist under field extension; hence the curve is geometrically connected. A smooth connected curve over an algebraically closed field is irreducible, since distinct irreducible components of a smooth curve are disjoint. This proves geometric irreducibility, without inference from a single finite-field prime.

Finally the Hilbert polynomial from the displayed series is $8n-2$, giving degree $8$ and genus $3$. For fixed $p$, the cube-root point–line construction gives eight distinct projective points in $x_p=0$ (four choices of the disjoint line, two root assignments modulo common scaling). Because the irreducible degree-eight curve is not contained in that hyperplane, these exhaust its hyperplane section and are simple intersections. Conjugating $t$ proves the same assertions for the other quadratic root. This is a computer-assisted proof relative to the stated exact CAS operations, not a proof-assistant formalization.

# 4. Computing the resultant

## 4.1 The Poisson product formula as a recursion on vertices

We avoid direct symbolic expansion of the resultant (the Macaulay matrix has $\binom{14}{6}=3003$ rows and entries linear in $\lambda$). The Poisson product formula (Cox, Little and O'Shea, 2005, Ch. 3, §3, Theorem 3.4) turns the problem into a recursion over induced sub-hypergraphs, in the spirit of Cooper and Dutle (2015). For homogeneous $F_1,\dots,F_n$ of degrees $d_1,\dots,d_n$ in $x_1,\dots,x_n$, writing $\bar F_i=F_i(x_1,\dots,x_{n-1},0)$ and $f_i=F_i(x_1,\dots,x_{n-1},1)$,
$$
\operatorname{Res}(F_1,\dots,F_n)=\operatorname{Res}(\bar F_1,\dots,\bar F_{n-1})^{d_n}\cdot\det\bigl(m_{f_n}\bigr)
$$
whenever $\operatorname{Res}(\bar F_1,\dots,\bar F_{n-1})\neq0$, where $m_{f_n}$ is multiplication by $f_n$ on the $d_1\cdots d_{n-1}$-dimensional algebra $\mathbb K[x_1,\dots,x_{n-1}]/\langle f_1,\dots,f_{n-1}\rangle$.

Apply this to $F_i=\lambda_0x_i^{2}-(\mathcal Ax^{2})_i$ for a fixed number $\lambda_0$, with the vertices ordered $1,\dots,7$ and $H_m$ the sub-hypergraph induced on $\{1,\dots,m\}$. The restricted forms $\bar F_i$ ($i<m$) are exactly the eigen-forms of $H_{m-1}$, so
$$
\phi_{H_m}(\lambda_0)=\phi_{H_{m-1}}(\lambda_0)^{2}\cdot\det\bigl(m_{f_m}\bigr),\qquad f_m=\lambda_0-(\mathcal A^{(m)}x^{2})_m\big|_{x_m=1},
$$
valid whenever $\phi_{H_{m-1}}(\lambda_0)\neq0$; the algebra has dimension $2^{m-1}$ (at most $64$). Note that $\det(m_{f_m})$ is a rational function of $\lambda_0$ in general — for $H_4$, a line plus an isolated vertex, it equals $(\lambda^{3}-1)^{6}/\lambda^{10}$ — so one interpolates $\phi_{H_m}$, not the quotient. Along the chain used, $H_1,H_2,H_3$ are edgeless, $H_4$ is a single line, $H_5$ the bowtie, $H_6$ the Pasch configuration and $H_7$ the Fano plane.

## 4.2 Modular evaluation, interpolation and lifting

For each of the primes $p$ used (all just below $2^{31}$, the largest characteristic Singular accepts), and for each integer $\lambda_0=1,\dots,\deg\phi_{H_m}+4$, the script computes in $\mathbb F_p[x_1,\dots,x_{m-1}]$ a reduced Gröbner basis of $\langle f_1,\dots,f_{m-1}\rangle$, checks that the quotient has dimension $2^{m-1}$, builds the $2^{m-1}\times2^{m-1}$ multiplication matrix of $f_m$ on the monomial basis, and takes its determinant; points at which $\phi_{H_{m-1}}(\lambda_0)\equiv0\pmod p$ are discarded. Newton interpolation through $\deg\phi_{H_m}+1$ points gives $\phi_{H_m}\bmod p$, and the surplus points are used as a consistency check (every one of them agreed, for every prime and every $m$). The Chinese remainder theorem then lifts the coefficients to symmetric residues modulo the product of the primes.

Two recorded runs were made for $H_7$: twelve primes (about $372$ product bits), and thirty primes with $2^{929}<M<2^{930}$. The latter reuses $H_6$ and recomputes the final Poisson step. Every eigenvalue has modulus at most the maximum vertex degree: choose a largest-modulus nonzero coordinate in the eigen-equation and apply the triangle inequality (Cooper and Dutle, 2012; Yang and Yang, 2010). Thus every coefficient is bounded by $\binom{448}{k}3^k\le4^{448}=2^{896}$. The inequality $M>2\cdot2^{896}$ makes the symmetric CRT lift unique **provided the modular computations are correct**. The observed 207-bit coefficients, agreement between runs and stability under dropping primes are checks, not substitutes for this a-priori bound. Twelve primes alone do not certify the final lift by that bound.

The reused polynomials are certified inductively by the same argument: $H_m$ has degree $m2^{m-1}$ and maximum degree $\Delta_m$, so $2(1+\Delta_m)^{m2^{m-1}}$ suffices. All six lower-stage products exceed their bounds; for $H_6$, $\Delta_6=2$ and the required bound has $306$ bits, below the available $372$. The verifier checks these inequalities, prime distinctness/primality, all thirty stored residue polynomials and coefficientwise CRT. Reading residue artifacts is distinguished from freshly recomputing their resultants.

The original logs report approximately five minutes per prime at the final Poisson step; this is a historical observation, not a portable benchmark or comparison with another workflow. Current replay receipts record their own wall times. Exact factor multiplication reproduces every coefficient of the degree-$448$ polynomial.

# 5. Verification

(a) *Prior leading coefficients.* The inspected arXiv author version of Clark and Cooper (2022, Fig. 2) gives $c_0,\ldots,c_{15}$. Our polynomial reproduces fifteen entries: $c_3=-336$, $c_6=55524$, $c_7=-696$, $c_9=-6017746$, $c_{10}=220038$, $c_{12}=481293561$, $c_{13}=-34237560$, $c_{15}=-30303162330$, the leading coefficient $1$, and zeros at $1,2,4,5,8,11$. Our $c_{14}=120204$ differs from that version's $-122004$. The exact resultant routes below support the computed value; we do not claim to have verified a correction to the final publisher PDF. The same inspected table's Rowling $c_{15}$ sign also differs from its displayed complete formula. Neither discrepancy is a premise of our computation.

(b) *A complete published polynomial.* The historical run of the same pipeline on the Rowling hypergraph $R=([7],\{123,145,167,256,357\})$ reproduced Clark and Cooper's closed form exactly, all $449$ coefficients (ten primes; lift stable under dropping two). This is a complete published-object regression, not a fresh independent validation or an a-priori certified full lift from ten primes.

(c) *Different determinant construction.* Macaulay's quotient of a $3003\times3003$ degree-eight matrix determinant by a $2555\times2555$ extraneous-minor determinant supplies a different resultant algorithm (Cox, Little and O'Shea, 2005). The supplied nine spot checks agree, as does the saved complete interpolation modulo $2147483647$ through 449 admissible values with one surplus check. This is producer-side algorithmic diversity, not organizational independence. In particular, `macaulay_full.py` imports interpolation and evaluation helpers from `poisson.py`; no claim of zero shared code is warranted. A root-count bound $448/p$ would be about $4.48\times10^{-7}$ at $p=10^9+7$, but is not a probability that the whole program is correct, and we use no such probabilistic assurance claim. The saved complete Macaulay polynomial confirms the coefficient discrepancy modulo this prime; newly evaluated spot checks are identified separately in the release replay report.

(d) *Internal identities.* The power sums $\operatorname{Tr}_d=\sum\lambda_i^{d}$ computed from the factorisation vanish for $d=1,2,4,5,8,11$ and equal $1008,5544,4872,54306,138180,786996,3064152,1708056,15053598$ for $d=3,6,7,9,10,12,13,14,15$. The vanishing of $\operatorname{Tr}_1,\operatorname{Tr}_2$ and the value $\operatorname{Tr}_3=1008=7\cdot144$ are what the Harary–Sachs theorem demands ($c_3=-2^{7}\cdot\tfrac38\cdot|E|=-336$; Clark and Cooper, 2022, §3), and $c_7=-696=-2^{7}\cdot\tfrac{87}{16}$ is the contribution of the Fano plane as a Veblen 3-graph with its own coefficient $87/16$ (their Remark 5). The multiplicities also respect the degree count $35+35+28+1+2\cdot7+2\cdot7+2\cdot21+2\cdot52+3\cdot21+4\cdot28=448$.

(e) *Eigenvectors and their reality.* Symbolic substitution checks existence of the displayed families. At $\lambda=2$ in $x_7=1$, the six components over $\mathbb Q$ are **primary, not prime**. Each has quotient dimension four and radical residue degree two: geometrically they give twelve double points, hence chart length twenty-four, not twenty-four distinct points. A more direct real obstruction avoids primary-decomposition terminology entirely. With $I_2$ the seven chart equations, `verification/reality_audit.sing` computes exact rational multipliers $c_i$ satisfying
$$1+x_1^2+\cdots+x_6^2=\sum_{i=1}^7c_i F_i.$$
The script re-expands the identity and obtains zero residual. No real chart solution can satisfy it; point-transitivity excludes every nonzero real eigenvector. Real witnesses at $0,1,3,\theta$ were given in Section 3. Thus the H-spectrum is exactly $\{0,1,3,\theta\}$.

The original runs used Singular 4.3.2; the present characteristic-zero replay uses Singular 4.4.1, SymPy 1.14.0 and python-flint 0.9.0. Correctness of these systems and the source-to-equations translation remains a trust boundary. Cross-algorithm agreement and internal model-assisted review reduce some risks but do not establish external specialist acceptance, unaffiliated reproduction or formal verification.

# 6. Literature status

The supplied draft reported a 14 September search. The subsequent local audit searched accessible literature for the homogeneous Fano spectrum, exact characteristic-polynomial and multiplicity expressions, aliases, and the discrepant coefficient; GitHub code searches for Fano with spectrum or characteristic returned no matching implementation in those searches. It inspected the cited author/arXiv versions, Cooper's historical list, Lin–Bu and the recent multiplicity preprint. No matching full factorization was located in this bounded search. This is a publishable novelty lead, not exhaustive novelty or priority clearance: MathSciNet, zbMATH, unindexed computation and unpublished work were not exhaustively checked; no authors were contacted. The release's `NOVELTY_REPORT.md` preserves the search scope. We do not advertise a proven first solution of a problem known to remain open in 2026.

# 7. Files in the bundle

The root README gives current commands and coverage. Programs are in `code/`, historical results in `out/`, `out30/`, `out_rowling/` and `logs/`, and characteristic-zero certificates and fresh receipts in `verification/`. The current entry point is `python verify.py`; repeat with `python -O verify.py`, then run `python test_negative.py`. These explicit failures remain active when Python assertions are disabled. The manifest and deterministic archive tool bind the source, data and PDF. The complete thirty-prime resultant generator is available separately and is more expensive than routine replay. Macaulay uses a different determinant construction but shares interpolation helpers. Empty historical output slots have explicit replacement pointers and are not used as evidence.

# Declarations and limitations

The release is anonymous and AI-assisted. The user supplied the candidate and review and authorized revision and publication; AI tools performed manuscript revision, symbolic coding, producer-side replay and internal editorial assessment. No named human authorship or unaffiliated reviewer endorsement is inferred. No human-participant or animal research is involved. No external funding or conflict-of-interest information was supplied; these are not declarations by an identified researcher. Original release prose and data are dedicated under CC0; code is MIT-licensed. Third-party source articles and the supplied review are not relicensed or redistributed. The code, coefficients, exact certificates, environment requirements and replay instructions accompany this manuscript. Discovery resource use predates prospective publication measurement and is not reconstructed.

Limitations include dependence on exact CAS implementations, incomplete fresh replay of the original thirty-prime computation and all finite number-field decompositions, bounded novelty screening, and absence of proof-assistant verification or authenticated external peer review. The curve is not identified with the Klein quartic here, and no conceptual formula for the exponent $52$ is claimed.

# References

**The problem and prior work on it**

Clark, G. J., & Cooper, J. N. (2021). A Harary–Sachs theorem for hypergraphs. *Journal of Combinatorial Theory, Series B, 149*, 1–15. <https://doi.org/10.1016/j.jctb.2021.01.002> (arXiv version: <https://arxiv.org/abs/1812.00468>)

Clark, G. J., & Cooper, J. N. (2022). Applications of the Harary–Sachs theorem for hypergraphs. *Linear Algebra and its Applications, 649*, 354–374. <https://doi.org/10.1016/j.laa.2022.05.012> (open-access copy: <https://ora.ox.ac.uk/objects/uuid:09d8629c-5501-4864-aa0e-225a9ddb8f3a;> arXiv: <https://arxiv.org/abs/2107.10781>)

Cooper, J. (2020, October). *Combinatorial problems I like*. University of South Carolina. <https://people.math.sc.edu/cooper/combprob.html>

Lin, G., & Bu, C. (2026). Spectral moments and characteristic polynomials of vertex expansion hypergraphs of graphs. *arXiv*. <https://arxiv.org/abs/2609.05897>

ulamai. (2026). *UnsolvedMath* (Version 1.6.0) [Data set]. Hugging Face. <https://huggingface.co/datasets/ulamai/UnsolvedMath> (problem record AMR-030-0030; browsable at <https://www.unsolvedmath.com/>)

**Spectral theory of hypergraphs and tensors**

Cooper, J., & Dutle, A. (2012). Spectra of uniform hypergraphs. *Linear Algebra and its Applications, 436*(9), 3268–3292. <https://doi.org/10.1016/j.laa.2011.11.018>

Cooper, J., & Dutle, A. (2015). Computing hypermatrix spectra with the Poisson product formula. *Linear and Multilinear Algebra, 63*(5), 956–970. <https://doi.org/10.1080/03081087.2014.910207>

Fan, Y.-Z. (2024). The multiplicity of eigenvalues of nonnegative tensors and hypergraphs. *arXiv*. <https://arxiv.org/abs/2410.20830>

Hu, S., & Ye, K. (2016). Multiplicities of tensor eigenvalues. *Communications in Mathematical Sciences, 14*(4), 1049–1071. <https://doi.org/10.4310/CMS.2016.v14.n4.a9>

Doğan, M. L., Tsigaridas, E., & Zafeirakopoulos, Z. (2026). *Resultant multiplicity via projective degrees and applications to tensor eigenvalues*. Preprint, version 1. <https://doi.org/10.48550/arXiv.2609.01268>

Lim, L.-H. (2005). Singular values and eigenvalues of tensors: A variational approach. In *1st IEEE International Workshop on Computational Advances in Multi-Sensor Adaptive Processing (CAMSAP 2005)* (pp. 129–132). <https://doi.org/10.1109/CAMAP.2005.1574201>

Qi, L. (2005). Eigenvalues of a real supersymmetric tensor. *Journal of Symbolic Computation, 40*(6), 1302–1324. <https://doi.org/10.1016/j.jsc.2005.05.007>

Yang, Y., & Yang, Q. (2010). Further results for Perron–Frobenius theorem for nonnegative tensors. *SIAM Journal on Matrix Analysis and Applications, 31*(5), 2517–2530. <https://doi.org/10.1137/090778766>

**Resultants and software**

Cox, D. A., Little, J., & O'Shea, D. (2005). *Using algebraic geometry* (2nd ed.). Springer. <https://doi.org/10.1007/b138611>

Decker, W., Greuel, G.-M., Pfister, G., & Schönemann, H. (2024). *Singular 4-3-2 — A computer algebra system for polynomial computations*. <https://www.singular.uni-kl.de>

The FLINT team. (2023). *FLINT: Fast Library for Number Theory* (Version 3.0). <https://flintlib.org> (Python bindings: <https://github.com/flintlib/python-flint>)
