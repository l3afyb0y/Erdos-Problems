# Experiment ledger

This file is also the autonomous processed-problem state. A problem listed here is not selected again by routine solver runs unless it is deliberately reopened for verification.

Fresh same-model reproduction audit: [`REPRODUCTION_AUDIT_2026-08-30.md`](REPRODUCTION_AUDIT_2026-08-30.md). That audit caught and repaired a logical overstatement in #324, a collision-statistic overstatement in #971, and a boundary qualification in #850.

| Erdős problem | Database status at attempt | Experiment result | Public note |
|---|---|---|---|
| [#137](problems/137.md) | OPEN | useful reformulation / proof audit | Exposed a non-monotone multiplication error in a tempting reduction to three consecutive factors; no complete solution. |
| [#242](problems/242.md) | OPEN | useful reformulation / exact finite evidence | Language-derived residue identities reduce the Erdős–Straus search to primes `1 mod 24`; a fresh reproduction reran all 9,732 hard-class primes below one million and exactly matched the original `k<=15` witness distribution. No universal proof. |
| [#307](problems/307.md) | OPEN | known reduction independently rediscovered | Lowest-terms and disjointness lemmas plus the exact reciprocal-prime-sum barrier rederive the known requirement of at least 59 distinct primes total; exact rational threshold reproduced. |
| [#863](problems/863.md) | OPEN | known reduction independently rediscovered | Algebraic comparison of the quoted published bounds reproduces conditionally and gives `c'_r < c_r`; prior 2026 observation already exists. Underlying external bounds were not re-proved in the reproduction audit. |
| [#663](problems/663.md) | OPEN | useful reformulation | Exact partition of primes into unique consecutive-position buckets; exposes bounded-difference constraints lost by the primorial product bound. Fresh derivation reproduced the iff reduction. |
| [#130](problems/130.md) | OPEN | useful reformulation / elementary structural lemma | No-four-concyclic condition gives at most three neighbors per integer-radius shell, hence quantitative long-edge forcing for high chromatic critical subgraphs. Reproduced. |
| [#132](problems/132.md) | OPEN | useful reformulation / exact counting lemma | `L >= (D(n+1)-C(n,2))/n`; in particular, more than `n/2` distinct distances forces at least two distance classes of multiplicity at most `n`. Reproduced. |
| [#1056](problems/1056.md) | OPEN | known reduction independently rediscovered | Consecutive product-one intervals are exactly repeated factorial residues modulo a prime; fresh modular computation reproduced every listed example through 9 intervals. |
| [#971](problems/971.md) | OPEN | useful reformulation / corrected in audit | Exact empty-class identity and all finite tuples reproduce. Pair-collision count is not equivalent to first-order redundancy; the original overstatement was repaired. |
| [#749](problems/749.md) | OPEN | useful reformulation | Any solution must have counting function on the Sidon scale `Theta(sqrt N)`; periodic positive-density constructions are impossible. Reproduced. |
| [#312](problems/312.md) | OPEN | no-progress | Maximal under-approximation gives an elementary `epsilon(A)<1/(R(A)-1)` cutoff lemma, weaker than Erdős--Graham's known quadratic-gap bound. Lemma reproduced. |
| [#324](problems/324.md) | OPEN | no-progress / corrected in audit | Fifth-power search through inputs 1500 reproduced exactly with no collision. Original claim equating distinct-index sum uniqueness with uniqueness of all positive differences was false and has been repaired. |
| [#850](problems/850.md) | OPEN | candidate-partial-lemma / boundary-qualified | For nondegenerate `x`, any repeated three-term prime-support pattern has `rad(x(x+1)(x+2)) | (y-x)`; two exponent-preserving construction families are ruled out. Fresh derivation reproduced them; `x=0,1` are now handled separately. No complete solution. |
| [#25](problems/25.md) | OPEN | useful reduction / elementary partial lemma | If the densities `delta_k` of all finite truncations tend to zero, then the full survivor set has natural density zero; only the positive-limit case can remain difficult. Reproduced. |
| [#28](problems/28.md) | OPEN | known reduction independently rediscovered | Eventual ordered representation bound `<=2` contradicts the generating-function identity at a negative real argument; fresh derivation reproduced the contradiction. |
| [#17](problems/17.md) | OPEN | known reduction independently rediscovered | Cluster property forces `>> log T` primes in every terminal interval `[p-T,p]`; fresh counting derivation reproduces the known consequence. |
| [#18](problems/18.md) | OPEN | no-progress / computation reproduced | Fresh dynamic programming exactly reproduced `h(60)=4`, `h(420)=5`, `h(840)=5`, `h(2520)=5`, `h(27720)=6`; no polylogarithmic bound was obtained. |
| [#30](problems/30.md) | OPEN | no-progress | Difference packing and shift-incidence routes return to the known `N^{1/4}`-scale error; no subpolynomial improvement. No positive new claim to promote. |

No entry in this ledger is represented as a new solution unless separately labeled `verified-complete-proof` after completeness, correctness, reproduction, and prior-art auditing.
