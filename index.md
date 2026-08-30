# Experiment ledger

This file is also the autonomous processed-problem state. A problem listed here is not selected again by routine solver runs unless it is deliberately reopened for verification.

| Erdős problem | Database status at attempt | Experiment result | Public note |
|---|---|---|---|
| [#137](problems/137.md) | OPEN | useful reformulation / proof audit | Exposed a non-monotone multiplication error in a tempting reduction to three consecutive factors; no complete solution. |
| [#242](problems/242.md) | OPEN | useful reformulation / exact finite evidence | Language-derived residue identities reduce the Erdős–Straus search to primes `1 mod 24`; an exact sweep below one million found witnesses with small search depth, but no universal proof. |
| [#307](problems/307.md) | OPEN | known reduction independently rediscovered | Lowest-terms and disjointness lemmas plus the exact reciprocal-prime-sum barrier rederive the known requirement of at least 59 distinct primes total. |
| [#863](problems/863.md) | OPEN | known reduction independently rediscovered | Published bounds imply `c'_r < c_r` by one-line strict inequality; prior 2026 observation already exists. |
| [#663](problems/663.md) | OPEN | useful reformulation | Exact partition of primes into unique consecutive-position buckets; exposes bounded-difference constraints lost by the primorial product bound. |
| [#130](problems/130.md) | OPEN | useful reformulation / elementary structural lemma | No-four-concyclic condition gives at most three neighbors per integer-radius shell, hence quantitative long-edge forcing for high chromatic critical subgraphs. |
| [#132](problems/132.md) | OPEN | useful reformulation / exact counting lemma | `L >= (D(n+1)-C(n,2))/n`; in particular, more than `n/2` distinct distances forces at least two distance classes of multiplicity at most `n`. |
| [#1056](problems/1056.md) | OPEN | known reduction independently rediscovered | Consecutive product-one intervals are exactly repeated factorial residues modulo a prime; exact search reproduces known OEIS examples through 9 intervals. |
| [#971](problems/971.md) | OPEN | useful reformulation | Recast least-prime delays as empty residue boxes produced by redundancy/collisions among early primes; missing step is a uniform prime-correlation bound. |
| [#749](problems/749.md) | OPEN | useful reformulation | Any solution must have counting function on the Sidon scale `Theta(sqrt N)`; periodic positive-density constructions are impossible. |
| [#312](problems/312.md) | OPEN | no-progress | Maximal under-approximation gives an elementary `epsilon(A)<1/(R(A)-1)` cutoff lemma, weaker than Erdős--Graham's known quadratic-gap bound. |
| [#324](problems/324.md) | OPEN | no-progress | Difference-family/convexity reformulation plus exact fifth-power collision search through inputs 1500; no new obstruction or construction. |
| [#850](problems/850.md) | OPEN | candidate-partial-lemma | Any repeated three-term prime-support pattern has `rad(x(x+1)(x+2)) | (y-x)`; two broad exponent-preserving construction families are ruled out. No complete solution. |
| [#25](problems/25.md) | OPEN | useful reduction / elementary partial lemma | If the densities `delta_k` of all finite truncations tend to zero, then the full survivor set has natural density zero; only the positive-limit case can remain difficult. |
| [#28](problems/28.md) | OPEN | known reduction independently rediscovered | Eventual ordered representation bound `<=2` contradicts the generating-function identity at a negative real argument; classical work already gives stronger finite lower bounds. |
| [#17](problems/17.md) | OPEN | known reduction independently rediscovered | Cluster property forces `>> log T` primes in every terminal interval `[p-T,p]`; this is a known consequence/exercise. |
| [#18](problems/18.md) | OPEN | no-progress | Exact small computations make `lcm(1,...,k)` look attractive, but no polylogarithmic bound for `h` was obtained. |
| [#30](problems/30.md) | OPEN | no-progress | Difference packing and shift-incidence routes return to the known `N^{1/4}`-scale error; no subpolynomial improvement. |

No entry in this ledger is represented as a new solution unless separately labeled `verified-complete-proof` after completeness, correctness, reproduction, and prior-art auditing.