# AGENTS.md — grammar-first Erdős solver instructions

This repository is a mathematical experiment. The objective is not to produce mathematical-sounding text. The objective is to obtain correct, preferably novel, progress on currently open Erdős problems and to preserve enough provenance that another system can reproduce or reject it.

These instructions govern agents working anywhere in this repository.

## 0. Read before acting

**Let** the repository be the persistent state of the experiment.

**Before** selecting or revisiting a problem, read:

1. `AGENTS.md`;
2. `TESTING_METHODOLOGY.md`;
3. `index.md`;
4. `RUN_LOG.md` when the work is autonomous or scheduled;
5. the relevant `problems/<n>.md` file when revisiting a processed problem.

**If** a problem appears in `index.md`, **then** treat it as processed.

**If** you deliberately revisit a processed problem, **then** say `REOPENED FOR SECOND PASS` in the working record rather than silently treating it as new.

**If** the maintained public status or a current claim audit says the problem is no longer open, **then** do not spend a discovery attempt on it as an open problem.

## 1. Primary objective

**Let** the target be the complete mathematical statement, including its quantifiers.

**If** you find a reformulation, identity, reduction, computation, construction family, obstruction, or lemma, **then** treat it as a newly available premise — not as the endpoint.

**Then ask:**

> Given this, what follows next that moves the unresolved quantifier?

**Continue** until one of these is true:

- the complete statement is proved;
- the complete statement is disproved by a valid counterexample or construction;
- the allotted attempt is genuinely exhausted.

**Do not** stop merely because something is interesting.

## 2. Discovery representation: make the relation legible

During discovery, mathematical notation may be treated as compressed representation.

For each important expression:

**Let** the symbols be named.

**Then** recover what relation the symbols represent in ordinary language.

Examples:

- `a | b` → `b is made from an integer number of copies of a`, or `a is a whole-factor of b`;
- `x ≡ y (mod m)` → `x and y occupy the same position in repeating blocks of size m`;
- `A ⊆ B` → `every object admitted by A is also admitted by B`;
- `∀` → `for every`; `∃` → `there is at least one`;
- equality → two representations are required to denote the same mathematical object or quantity;
- inequality → one side is bounded by the other, with direction preserved.

Mere transliteration is not enough. `one plus two equals three` is still compressed if no useful relation has been exposed.

## 3. Use explicit logical grammar as control flow

Prefer reasoning whose dependency structure is audible in the prose.

Use words such as:

`Let` · `Suppose` · `Given` · `If` · `Then` · `Because` · `Only if` · `Unless` · `For every` · `There exists` · `Therefore` · `But` · `Contradiction` · `Hence`.

Treat these words as operators, not decoration.

For each inference:

**Given** the currently established facts,

**ask** what new fact becomes available.

**If** the new fact requires an unstated premise,

**then** state and justify that premise before continuing.

**If** an implication `A -> B` is useful,

**then** reverse it and ask whether `B -> A` also holds.

**If not**, locate the asymmetry. The failed converse often contains the useful constraint.

## 4. Search operators

When progress stalls, inspect the current relation through these local operations:

- reverse;
- complement;
- opposite;
- inverse;
- boundary case;
- extremal case;
- part versus whole;
- local versus global;
- equality case;
- preserved quantity / invariant;
- representation change;
- factorization or decomposition;
- recombination.

**Do not assume** that every object possesses a useful global symmetry.

**If** an opposition or symmetry is invoked, **then** specify exactly which relation is being reversed or preserved.

## 5. Prefer the shortest forced dependency path

**Let** every `therefore` be typechecked.

Seek a decisive invariant or relation that makes the next step forced.

Prefer:

> premise → relation → constraint → contradiction/construction

over
> theorem name → theorem name → theorem name → conclusion

when the first path is available.

Deep machinery is allowed when necessary. Simplicity is a search preference, not a restriction on valid mathematics.

## 6. Do not confuse representations with truth

A useful sentence can represent a mathematical relation without establishing it.

**If** you write `X is Y`, **then** ask whether you have proved identity, proved only a relation, or merely chosen a representation.

**If** a language-level insight and exact mathematics disagree, **then** the language-level inference loses. Locate the translation or inference error.

Intensity, elegance, repetition, and apparent inevitability are not proof.

## 7. Quantifier discipline

At every promising endpoint, restate the original target in plain language.

Then ask:

- Did I prove `for every`, or did I test many examples?
- Did I prove `there exists`, or did I only derive a necessary condition?
- Did I prove an asymptotic statement uniformly, or only on a subsequence?
- Did I prove the converse I am now using?
- Did I replace a global claim with a local lemma without noticing?

A finite computation cannot by itself discharge an infinite universal quantifier.

A reduction is not a solution unless the reduced target is itself closed.

## 8. Candidate complete solution protocol

**If** a complete proof, disproof, or construction appears, **then stop discovery and freeze it before detailed literature comparison.**

Preserve the first derivation.

Then perform fresh reproductions.

### Reproduction A

Start again from the problem statement.

Do not consult the frozen dependency chain.

Try to derive the result again using explicit language-first reasoning.

### Reproduction B

Start again from the problem statement.

Change representation deliberately: conventional mathematics, exact computation, structural combinatorics, formal proof, or another materially different route.

### Compare only afterward

**If** the independent derivations disagree, **then** find the first divergent implication and treat the candidate as unverified.

**If** they converge, **then** this is supporting evidence, not automatic certification. Correlated model errors remain possible.

Proceed to adversarial verification as specified in `TESTING_METHODOLOGY.md`.

## 9. Attack your own proof

For every candidate proof, deliberately search for failure.

Check:

- boundary values;
- degenerate cases;
- hidden positivity assumptions;
- hidden coprimality assumptions;
- quantifier reversal;
- converse use;
- monotonicity claims;
- division by a possible zero;
- counting overlaps;
- ordered versus unordered objects;
- distinct versus repeated objects;
- exact versus asymptotic statements;
- dependence of constants;
- finite evidence being promoted to universality.

**If** exact code can falsify a claim cheaply, **then** write and run the code.

**If** a formal checker can verify the decisive finite or symbolic step, **then** prefer it over confidence.

## 10. Novelty control

Before discovery, use only enough public searching to establish that the target is currently open and not obviously superseded by a fresh complete claim.

Do not unnecessarily read detailed solution attempts before discovery when novelty is part of the experiment.

After a candidate result exists, reverse the policy:

**Search aggressively** for prior art on the decisive lemma, invariant, construction, proof shape, constants, and conclusion.

**If** equivalent prior work exists, **then** label the result rediscovered.

**If** no equivalent work is found, **then** say `novelty unresolved` until stronger independent review is complete.

Search failure is not proof of novelty.

## 11. Status vocabulary

Use conservative labels.

- `no progress`
- `useful reformulation`
- `known reduction independently rediscovered`
- `candidate/new partial lemma — novelty unresolved`
- `candidate complete proof — verification pending`
- `candidate complete proof — novelty unresolved`
- `verified complete proof`

Use `verified complete proof` only after completeness, adversarial checking, reproduction, and current prior-art review all survive.

## 12. Repository organization

`index.md` is the compact processed-problem ledger.

`problems/<n>.md` is the authoritative mathematical record for a problem.

`verification/` contains exact checkers where useful.

`TESTING_METHODOLOGY.md` records the public experimental and verification controls.

`RUN_LOG.md` records autonomous execution provenance and scheduler/tool anomalies.

**If** you change a mathematical claim, **then** update the relevant problem record.

**If** the problem's classification changes, **then** update `index.md`.

**If** an autonomous run occurs, **then** update `RUN_LOG.md` truthfully.

Never reconstruct a run that did not happen.

## 13. Public/private boundary

This repository may document the operational mathematical reasoning instructions needed for reproducibility, including this file.

Do not add private biographical material, private philosophical archives, or unrelated personal context.

Do not turn the repository into a general theory-of-language manuscript. Keep the object here mathematical: what the agent was instructed to do, what mathematics resulted, and how that result was checked.

## 14. Default loop

The default agent loop is deliberately simple.

**Let** `P` be a candidate Erdős problem.

**If** `P` is already processed and this is not an explicit revisit, **then** choose another problem.

**If** `P` is not currently open, **then** choose another problem.

**Otherwise, attempt P.**

**If** a partial result appears, **then** use it as a premise and continue toward the full target.

**If** the attempt exhausts without a complete result, **then** preserve the strongest valid result, classify it conservatively, and move on.

**If** a complete result appears, **then** freeze it.

**Then** reproduce it independently.

**Then** attack it.

**Then** verify exact steps.

**Then** audit prior art.

**If** it survives all gates, **then** promote its status.

**Then** record the result.

**Then** choose the next open problem.

## 15. Final checksum

Before claiming completion, ask in this order:

1. **What exactly was required?**
2. **What exactly did I establish?**
3. **Which sentence connects those two?**
4. **Does that sentence actually follow?**
5. **Can I derive it again without copying myself?**
6. **Can I make the claim fail by computation or a boundary case?**
7. **Has somebody already done it?**

If any answer is unresolved, the mathematical status is unresolved.

**Let the prose expose the dependency. Let the mathematics decide whether the dependency is true.**
