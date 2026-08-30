# Fresh reproduction audit — 2026-08-30

This audit is a fresh pass by the same model family over the mathematical records already present in this repository. It is useful for catching derivational mistakes and checking exact computations, but it is **not** treated as fully independent external verification: correlated model errors remain possible. A different system/formal checker/mathematician should be used before promoting any future complete solution.

The audit deliberately separates three questions:

1. **Does the stated local argument reproduce?**
2. **Do exact numerical/computational claims reproduce?**
3. **Does any record actually solve the full open problem?**

At audit time, no processed entry in the repository is a complete solution.

## Results

| Problem | Fresh reproduction result | Audit note |
|---|---|---|
| #17 | REPRODUCED | From the cluster condition, each odd `t<=T` is represented as an admissible offset plus a prime; one terminal offset covers at most `pi(T)` such `t`, forcing `>> T/pi(T) >> log T` terminal primes. This remains a known consequence, not a solution. |
| #18 | REPRODUCED COMPUTATION | Fresh subset-sum dynamic programming gives exactly `h(60)=4`, `h(420)=5`, `h(840)=5`, `h(2520)=5`, `h(27720)=6`. No asymptotic proof is present. |
| #25 | REPRODUCED | Each finite truncation is eventually periodic. Since the full survivor set lies inside every truncation, `upper_density(A)<=delta_k`; if `delta_k -> 0`, the full set has natural density zero. |
| #28 | REPRODUCED | Assuming eventual ordered representation bound `<=2`, parity forces the stated eventual coefficient pattern. The resulting generating-function identity at `z=-r` has a nonnegative left side and a right side tending to `-infinity`, contradiction. This only excludes the bound two. |
| #30 | NO POSITIVE CLAIM TO REPRODUCE | The entry records unsuccessful standard routes. The standard Sidon difference-packing facts are consistent, but no new theorem is asserted. |
| #130 | REPRODUCED | A fixed integer radius is one circle through the center vertex; no four concyclic points permits at most three neighbors per shell. Hence a finite diameter-`D` piece has degree at most `3 floor(D)`, and a `t`-critical core forces an incident integer edge of length at least `ceil((t-1)/3)` at every vertex. |
| #132 | REPRODUCED | Pair counting gives `C(n,2) >= L + (D-L)(n+1)`, hence `L >= (D(n+1)-C(n,2))/n`. In particular `D>n/2` forces `L>=2`. |
| #137 | REPRODUCED | The monotonicity shortcut is invalid. The safe lemma is correct: a prime larger than the interval span cannot divide two terms, so a first-power occurrence in its unique term stays exponent one in the full product. |
| #242 | REPRODUCED EXACTLY | All displayed elementary identities and the divisor-factor equation reproduce. A fresh exact sweep over all `9,732` primes `p<1,000,000` with `p≡1 mod 24` again found a witness with `k<=15`. The first-witness distribution reproduced exactly: `{1:5192, 2:3551, 3:594, 4:129, 5:132, 6:81, 7:13, 8:28, 9:1, 10:3, 11:2, 12:2, 13:1, 14:1, 15:2}`. This remains finite evidence, not a universal proof. |
| #307 | REPRODUCED EXACTLY | Lowest-terms, mirror, and disjointness lemmas reproduce. Fresh exact rational arithmetic gives the stated first-58-prime reciprocal sum `1.998740043147044... < 2`, while adding `1/277` gives `2.002350151450293... > 2`; the 59-prime barrier follows. |
| #312 | REPRODUCED | Maximality forces every omitted reciprocal to exceed the deficit `delta`; multiplicity of denominator `q` is at most `q-1`; summing gives `R(A)<1+1/delta` and therefore `delta<1/(R(A)-1)`. The bound remains weaker than known work. |
| #324 | CORRECTED | The exact fifth-power search through `0<=a<b<=1500` was independently rerun: all `1,125,750` sums are distinct. However, the original text incorrectly called uniqueness of all positive differences *equivalent* to uniqueness of sums of two distinct values. It is only a stronger sufficient condition in the stated `a<b` formulation. The problem file has been corrected. |
| #663 | REPRODUCED | For `p>k`, a prime cannot divide two positions in a block of length `k`; therefore primes in `(k,y]` partition uniquely among offsets. Their bucket products are pairwise coprime, squarefree divisors of the corresponding consecutive integers, and the converse works because every prime `<=k` divides some member of any `k`-term block. |
| #749 | REPRODUCED | Bounded ordered representation gives `A(N)^2 <= 2gN`; a sumset of lower density at least `1-epsilon` gives `A(N)^2 >= (1-epsilon-o(1))N`. Thus any construction lives on the `sqrt(N)` scale. Positive-density periodic sets cannot have uniformly bounded representation. |
| #850 | REPRODUCED WITH BOUNDARY QUALIFICATION | For nondegenerate `x`, support equality forces every prime in `x(x+1)(x+2)` to divide `y-x`, giving the radical divisor condition. Both displayed exponent-preserving families again lead to contradiction. The natural-number boundary `x=0,1` should be disposed of separately before using the ordinary radical; the problem file has been corrected accordingly. |
| #863 | REPRODUCED CONDITIONALLY | The inequality comparison is exact: with `m=floor(r/2)>0`, `((r+m)^2)/(r+2m)-r = m^2/(r+2m)>0`. Therefore the desired strict inequality follows **if the quoted published lower and upper bounds apply to exactly the constants defined in the problem**. This audit did not independently re-prove those external bounds. |
| #971 | REPRODUCED, THEN CORRECTED | The occupancy identity `L=phi(d)-P+(P-O)` is exact, and all five numerical tuples in the file were independently recomputed exactly. But the original wording overstated the pair-collision statistic `C=sum binom(r_a,2)` as equivalent to the needed redundancy `P-O`. In fact `P-O<=C`, and large `C` may be concentrated. The problem file has been corrected. |
| #1056 | REPRODUCED EXACTLY | Consecutive product-one intervals are equivalent to repeated factorial residues when endpoints lie below `p`. Fresh modular computation reproduced every listed collision: `p=23`, `71`, `599`, and `3011`, with the exact residues and indices stated in the file. |

## Exact computational reproductions

### Erdős–Straus hard-class sweep (#242)

Fresh code independently regenerated the primes below one million, selected the `9,732` primes congruent to `1 mod 24`, factored the relevant `Q^2`, searched the divisor congruence condition, reconstructed `x<y<z`, and checked the unit-fraction identity using exact rational arithmetic. There were zero failures at search depth `k<=15`, and the full depth histogram matched the repository exactly.

### Reciprocal-prime threshold (#307)

Fresh exact rational arithmetic reproduced the numerator and denominator printed in the problem file for the sum of reciprocals of the first 58 primes. The 58th prime is `271`; the next is `277`. The inequality changes from below two to above two exactly where stated.

### Fifth powers (#324)

Fresh hashing of every unordered distinct pair `0<=a<b<=1500` checked `1,125,750` exact integer sums `a^5+b^5` and found no collision.

### Residue occupancy (#971)

For `c=0.1`, fresh prime enumeration reproduced exactly:

- `(120, 32, 168, 36, 5)`
- `(300, 80, 501, 92, 14)`
- `(840, 192, 1422, 219, 32)`
- `(1000, 400, 3039, 433, 76)`
- `(3000, 800, 7045, 903, 169)`

### Factorial residues (#1056)

Fresh modular factorial iteration confirmed every listed index has the stated common residue:

- modulo `23`: indices `1,4,8,11,21` -> `1`;
- modulo `71`: indices `7,9,19,51,61,63,70` -> `-1`;
- modulo `599`: indices `28,50,122,183,250,289,500,539,555` -> `175`;
- modulo `3011`: indices `1,611,723,749,805,2205,2261,2287,2399,3009` -> `1`.

## Audit conclusion

The fresh pass found **one definite logical error** (#324), **one meaningful overstatement of equivalence** (#971), and **one boundary qualification worth making explicit** (#850). Those records were repaired immediately.

The remaining local lemmas checked in this pass reproduce. That does **not** upgrade any open problem to solved status. The strongest exact computations also reproduce, but finite reproduction does not bridge universal quantifiers.

For a future `candidate-complete-proof`, the next verification layer should intentionally use a different reasoning system or formal proof environment so that agreement is less correlated than repeated runs of the same model family.
