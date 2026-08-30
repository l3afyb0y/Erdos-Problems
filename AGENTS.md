# AGENTS.md — grammar-first instructions for mathematical agents

This file is the repository-level instruction layer for Codex and other agents working in this repository.

Its primary practical purpose is to let an agent enter a local clone and immediately understand **how to work here** without requiring the user to reconstruct the experiment from chat history. Scheduled or remote agents may read the same file so that different systems share one portable method.

The method is shared. The task is not. The run log is not shared either.

**If the user gives a specific task, then that task is the target.**

Do not silently replace a request to solve one problem, verify one proof, inspect one file, write one checker, or revise one argument with a broader autonomous batch.

**Only enter autonomous next-problem mode when the user, scheduler, or higher-level task explicitly requests it.**

These instructions govern agents working anywhere in this repository unless a more specific instruction file exists below the current path.

---

## 0. Resolve the task before acting

**Let** `T` be the task actually requested.

**First ask:** what exact output would count as completing `T`?

Then identify the operating mode.

### Mode A — specific solve / second pass

Use when the user names a problem or asks to take another crack at one already attempted.

Read:

1. `AGENTS.md`;
2. `TESTING_METHODOLOGY.md`;
3. the relevant `problems/<n>.md`;
4. directly relevant verifier/source files;
5. `index.md` only as needed for state and status.

If the problem is already processed, treat the work as **REOPENED FOR SECOND PASS**. Do not pretend it is a fresh first attempt.

### Mode B — reproduction / verification

Use when the user asks whether an existing claim, proof, computation, or candidate result is correct.

Read the claim to be checked, then reconstruct it independently where possible.

**Do not begin by trying to make the existing proof sound better. Begin by trying to make it fail.**

Use `TESTING_METHODOLOGY.md` as the governing protocol.

### Mode C — autonomous solving

Use only when explicitly requested.

Read:

1. `AGENTS.md`;
2. `TESTING_METHODOLOGY.md`;
3. `index.md`;
4. the run log appropriate to the executing agent.

Then choose **one** currently open target and work it deeply. The default autonomous unit is one problem, not a five-problem spray.

### Mode D — repository / tooling work

Use when the user asks to organize files, improve instructions, write verification code, prepare Codex context, repair the ledger, or otherwise maintain the research environment.

Do the repository task. Do not start solving unrelated mathematics merely because this is a solver repository.

---

## 1. Depth before breadth

The experiment does not need a farm of shallow or wrong Erdős attempts.

**One correct new lemma, improved bound, closure principle, obstruction, or complete proof is more valuable than many reformulations.**

Therefore:

- default to one target per autonomous run;
- stay with the strongest branch while it is still producing new constraints;
- do not abandon a problem merely because a useful lemma has been found;
- do not move on merely to increase the processed-problem count;
- if a second pass can preserve more state or compose an earlier lemma, prefer that depth when the task permits it;
- record `no progress` only after the strongest plausible branch has actually been attacked, not after the first failed idea.

A partial result is useful primarily as **newly available machinery**.

After obtaining one, ask:

> **What can I now do that I could not do before?**

Then do that.

---

## 2. Keep the unresolved quantifier visible

**Let** the target be the complete mathematical statement, including its quantifiers.

Rewrite the unresolved part in plain language before serious discovery begins.

Examples:

- `for every n` means no finite sweep can finish the task;
- `there exists` means necessary conditions are not enough;
- `o(N)` means a fixed constant-factor improvement is not yet the target;
- `infinitely many` means one construction family must genuinely be unbounded;
- `unique` means both existence and exclusion of alternatives matter.

After every substantial lemma, restate the unresolved clause.

Then ask:

> **Given this lemma, what part of the original quantifier has actually moved?**

If the answer is “none,” the lemma may still be true, but it is not yet the route to completion.

A reduction is not a solution unless the reduced target is itself closed.

---

## 3. Decompile notation into relations, not merely words

During discovery, treat mathematical notation as compressed representation when expansion makes the next inference easier to see.

For each important expression:

**Let** the symbols be named.

**Then** recover the relation represented by those symbols in ordinary language.

Examples:

- `a | b` → `b contains a as an integer factor`;
- `x ≡ y (mod m)` → `x and y occupy the same position in repeating blocks of size m`;
- `A ⊆ B` → `every object admitted by A is also admitted by B`;
- `∀` → `for every`;
- `∃` → `there is at least one`;
- equality → `two representations are constrained to denote the same mathematical object or quantity`;
- inequality → `one side is constrained above or below by the other, with direction preserved`.

Mere transliteration is not enough. `one plus two equals three` is still compressed if no useful relation has been exposed.

### Symbol budget during discovery

Prefer ordinary language for multiplication, division, quantifiers, and scope when symbolic density hides the relation.

Simple symbols such as `+`, `-`, and `=` are often useful because their relational roles remain visually obvious.

ASCII `*` and `/` are acceptable when exact manipulation is clearer that way. Do not force prose where notation is genuinely easier to inspect.

The rule is not “ban symbols.” The rule is:

> **Use the representation that makes the dependency easiest to inspect.**

---

## 4. Use explicit logical grammar as control flow

Prefer reasoning whose dependency structure is audible in the prose.

Use operators such as:

`Let` · `Suppose` · `Given` · `If` · `Then` · `Because` · `Only if` · `Unless` · `For every` · `There exists` · `Therefore` · `But` · `Contradiction` · `Hence`.

Treat these words as control operators, not decoration.

A useful default form is:

> **Let** the object be defined.  
> **Given** what is already true, identify the available relation.  
> **If** that relation holds, state exactly what follows.  
> **Because** the implication needs a reason, expose that reason.  
> **Then** carry the new fact forward.  
> **If not**, inspect the failed condition.  
> **Therefore**, advance only what has actually been established.

For every important inference:

**If** the new fact requires an unstated premise,

**then** state and justify that premise before continuing.

Do not let `therefore` hide a theorem-sized gap.

---

## 5. Type the objects and relations

Before manipulating a dense statement, identify what each important term is doing.

Useful roles include:

- object;
- quantity;
- operation;
- relation;
- condition;
- quantifier;
- scope marker;
- boundary;
- invariant;
- state;
- transformation;
- residual object.

This prevents category mistakes such as treating a necessary condition as a construction, a representation as an identity, or a finite statistic as an asymptotic statement.

If two phrases look similar but occupy different logical roles, keep them separate.

---

## 6. Ask what becomes available next

At each serious step ask:

> **Given everything presently established, what operation, relation, or fact has become newly available?**

Examples:

- divisibility may make a quotient integral;
- a gcd may exclude a shared prime;
- an extremal choice may make a local modification impossible;
- equality may force every inequality in a chain to be equality;
- a missing object may itself define a smaller instance;
- a partition may expose mutually exclusive cases;
- a bound may turn an infinite search into a finite one;
- a surviving state may support another application of the same argument;
- a necessary condition may become a falsifiable local obligation.

The goal is to follow a shortest valid dependency path, not to maximize theorem names.

---

## 7. Preserve state; do not aggregate too early

Several of the strongest improvements in this repository appeared only after an earlier proof stopped throwing away case information.

When a proof produces:

- selected versus omitted objects;
- equality versus strict inequality;
- a residue class;
- a deficit;
- a surviving subset;
- a missing origin;
- a boundary state;
- a reason an inequality was not tight;

**do not immediately sum, average, union, or compress those states into one coarse number.**

Ask:

> **If I remember why this case occurred, can I apply the argument again?**

A one-step bound may hide a recurrence.

A discarded complement may be the next instance.

An omitted object may define a residual problem.

A failed equality case may supply an additional quantitative gain.

Preserve any distinction that changes what operation becomes available next.

---

## 8. Search for closure and reproduction inside the mathematics

When a valid construction, solution, witness, or partial structure appears, ask whether it can generate another one.

Search explicitly for:

- closure under a transformation;
- recursion into a residual object;
- composition of two valid constructions;
- iteration of a local lemma;
- shifting, scaling, prefixing, factoring, or translating while preserving the target property;
- a map from one solution to infinitely many solutions;
- a map from one obstruction to a stronger obstruction.

Then ask:

> **If this transformation is applied repeatedly, what invariant is preserved and what quantity changes?**

A productive transformation should not merely produce another example; it should expose why reproduction works.

---

## 9. Reverse implications and inspect failed converses

**If** an implication `A -> B` is useful,

**then** ask whether `B -> A` also holds.

If not, identify the exact missing condition.

The asymmetry often contains the useful constraint.

Also inspect:

- complement;
- opposite;
- inverse;
- boundary case;
- extremal case;
- equality case;
- part versus whole;
- local versus global;
- selected versus omitted;
- inside versus outside;
- before versus after;
- multiplicity versus support;
- factorization versus recombination;
- representation change.

Do not assume global symmetry merely because a local opposition exists.

State exactly what is reversed and exactly what is preserved.

---

## 10. Treat `equivalent` as a proof obligation

The reproduction audit found that loose uses of “equivalent” are a recurring failure mode.

Therefore:

**Do not write `equivalent`, `if and only if`, or `exactly when` unless both directions have been established.**

When proposing an equivalence:

1. prove the forward direction;
2. reset mentally;
3. prove the reverse direction independently;
4. inspect boundary and degenerate cases;
5. only then compress the relation into `iff` or “equivalent.”

If only one direction is known, say `implies`, `requires`, `is sufficient for`, or `is necessary for` as appropriate.

---

## 11. Convert global claims into local obligations when useful

A strong route to contradiction is often:

> **Suppose the global statement or opposing hypothesis is true. What must every sufficiently large local object then do?**

Examples of local obligations include:

- every prime must satisfy a cancellation condition;
- every residue class must receive an object;
- every block must contain a witness;
- every extremal configuration must have a particular local structure;
- every candidate solution must satisfy a divisibility or parity constraint.

Once a global hypothesis creates a local obligation, try to falsify that obligation exactly.

Finite failure of many local cases is evidence and search guidance; only a proof of unavoidable failure closes the universal statement.

---

## 12. Do not assume an operation preserves a defect

An earlier proof audit exposed a common mistake: adding or multiplying more structure can repair a property that was previously absent.

Therefore, whenever reasoning has the form:

> object `X` has defect `D`, therefore any larger/product/extended object also has `D`,

stop and prove the monotonicity claim.

Check whether later factors, added terms, or extra structure can supply the missing multiplicity, parity, coverage, cancellation, or representation.

Local failure is not automatically hereditary.

---

## 13. Tool jurisdiction: discovery is not verification

Tools are allowed, but their role must be legible.

For a language-first discovery task, distinguish four phases:

1. **selection/status**;
2. **discovery**;
3. **verification/falsification**;
4. **prior-art search**.

### Selection/status

Use public sources only to confirm the statement, current status, and whether a credible complete claim has already appeared.

Avoid ingesting detailed remarks or existing approaches before novelty-sensitive discovery when practical.

### Discovery

Use language-first reasoning as the primary search representation.

A calculator or exact arithmetic tool may check arithmetic without changing the discovery condition materially.

But if code, brute force, symbolic algebra, SAT/MIP search, package enumeration, or a theorem database **discovers the pattern or candidate structure**, then record that honestly as computational or tool-assisted discovery.

Do not let computation discover the answer and then present the prose as though it discovered it.

### Verification/falsification

After a candidate structure exists, use computation aggressively when it can attack the claim:

- exact arithmetic;
- independent code;
- brute-force boundary search;
- formalization;
- symbolic checking;
- alternate representation.

### Prior art

After internal checking, search broadly and aggressively.

When provenance is recorded, note which tools materially influenced discovery versus verification.

---

## 14. Quantifier discipline

At every promising endpoint, restate the original target in plain language.

Then ask:

- Did I prove `for every`, or did I test many examples?
- Did I prove `there exists`, or did I derive only a necessary condition?
- Did I prove an asymptotic statement uniformly, or only on a subsequence?
- Did I prove the converse I am now using?
- Did I replace the global claim with a local lemma without noticing?
- Did I establish eventual behavior, or only behavior below a computational cutoff?
- Did I prove infinitely many cases, or merely generate a large finite family?

A finite computation cannot by itself discharge an unbounded universal quantifier.

A better constant does not prove a little-o statement.

An infinite family does not prove `for every`.

---

## 15. Candidate complete solution protocol

**If** a complete proof, disproof, or construction appears,

**then stop discovery and freeze the first derivation before detailed literature comparison.**

Preserve the decisive dependency chain.

Then reproduce it.

### Reproduction A — fresh language derivation

Start again from the problem statement.

Do not consult the frozen dependency chain.

Attempt the result using explicit relation-first reasoning.

### Reproduction B — changed representation

Start again from the problem statement.

Use a materially different representation where possible: conventional proof, exact computation, structural combinatorics, algebraic reformulation, formal proof, or another independent route.

### Compare only afterward

**If** the derivations disagree,

**then** locate the first divergent implication and treat the candidate as unverified.

**If** they converge,

**then** agreement is supporting evidence, not automatic certification. Same-family model errors can be correlated.

Proceed to adversarial verification under `TESTING_METHODOLOGY.md`.

---

## 16. Attack the proof instead of defending it

For every candidate proof or strong partial lemma, deliberately search for failure.

Check:

- first and last admissible values;
- zero and positivity boundaries;
- degenerate cases;
- hidden coprimality assumptions;
- quantifier reversal;
- converse use;
- monotonicity claims;
- division by possible zero;
- counting overlaps;
- ordered versus unordered objects;
- distinct versus repeated objects;
- support versus multiplicity;
- equality versus congruence;
- strict versus weak inequality;
- exact versus asymptotic claims;
- dependence of constants;
- local-to-global transitions;
- finite evidence promoted to universality;
- imported theorems whose hypotheses may not match the present formulation.

**If** exact code can falsify a claim cheaply,

**then** write and run it.

**If** a formal checker can verify a decisive step,

**then** prefer that check over confidence.

A boundary error discovered by the verifier is a successful verifier result.

---

## 17. Novelty and contamination control

Before novelty-sensitive discovery, use only enough external searching to establish that the target is currently open and not obviously superseded by a fresh complete claim.

Avoid detailed solution literature before the first derivation when practical.

This reduces direct contamination; it cannot remove knowledge already present in model training.

After a candidate result exists, reverse the policy.

Search aggressively for:

- the same conclusion;
- the decisive lemma;
- the invariant;
- the construction;
- the proof shape;
- the constant;
- stronger results implying the candidate;
- recent preprints;
- comments and forum posts;
- formalizations;
- solver-generated claims;
- very recent AI-assisted working reports.

For Erdős problems, a serious post-discovery audit should normally include, when available:

- the maintained Erdős Problems page;
- Erdős Problem a Day / recent working reports;
- arXiv and recent papers;
- formal-conjecture repositories or formal status mirrors;
- targeted web search for the exact lemma, constant, construction, and decisive phrase.

**If** equivalent prior work exists,

**then** classify the result as rediscovered.

**If** no equivalent work is found,

**then** use `novelty unresolved` until stronger independent review is complete.

Search failure is not proof of novelty.

---

## 18. Status vocabulary

Use conservative labels.

- `no progress`
- `useful reformulation`
- `known reduction independently rediscovered`
- `candidate/new partial lemma — novelty unresolved`
- `candidate complete proof — verification pending`
- `candidate complete proof — novelty unresolved`
- `verified complete proof`

Use `verified complete proof` only after the full statement, adversarial checking, reproduction, exact/formal checks where applicable, and current prior-art review all survive.

Do not promote a result merely because two model runs agree.

---

## 19. Autonomous loop — only when autonomous mode was requested

The default autonomous unit is **one problem worked deeply**.

**Let** `P` be a candidate Erdős problem.

**If** `P` is already processed and this is not an explicit revisit,

**then** choose another problem.

**If** `P` is not currently open,

**then** choose another problem.

**Otherwise, attempt P.**

**If** a reformulation appears,

**then** ask what new operation it enables and continue.

**If** a partial lemma appears,

**then** test it, preserve its state, ask whether it composes or iterates, and continue toward the full target.

**If** a candidate closure or recurrence appears,

**then** iterate it symbolically before abandoning the branch.

**If** a candidate complete result appears,

**then** freeze it, reproduce it, attack it, verify it, and audit prior art.

**If** the strongest branch is genuinely exhausted without a complete result,

**then** preserve the strongest valid result and classify it conservatively.

Only then move to another problem.

Do not optimize throughput by lowering mathematical depth.

---

## 20. Repository and provenance roles

Treat the repository as persistent experimental state.

- `AGENTS.md` = portable agent method and repo-working instructions.
- `TESTING_METHODOLOGY.md` = public experimental controls and verification protocol.
- `index.md` = compact processed-problem ledger.
- `problems/<n>.md` = authoritative mathematical record for problem `n`.
- `verification/` = exact checkers and computational support.
- `RUN_LOG.md` = **scheduled ChatGPT/autonomous remote solver execution provenance only**.
- `CODEX_RUN_LOG.md` = **local or interactive Codex execution provenance only**.

Keep the run logs separate.

**If a mathematical claim changes, then update the relevant problem record.**

**If its classification changes, then update `index.md`.**

**If a scheduled ChatGPT/autonomous remote run occurs, then append only to `RUN_LOG.md`.**

**If a local or interactive Codex run occurs, then append only to `CODEX_RUN_LOG.md`.**

If another execution environment is introduced, give it a distinct provenance log.

Never reconstruct a run that did not happen.

---

## 21. Working-tree and code discipline for local agents

When operating in a local clone:

- inspect existing files before creating parallel replacements;
- prefer small, legible verification scripts over opaque one-off calculations;
- use exact integer/rational arithmetic when feasible;
- record computational domain and stopping conditions;
- do not overwrite a prior derivation merely because a cleaner one was found;
- preserve provenance when correction matters;
- avoid broad unrelated refactors during mathematical verification;
- do not delete research artifacts unless the user explicitly asks;
- do not expose private material in commits or files;
- do not push or publish unless requested or clearly authorized by the task.

For Codex specifically:

**If** running locally or interactively as Codex and provenance should be recorded,

**then** append to `CODEX_RUN_LOG.md`, not `RUN_LOG.md`.

**Do not edit, rewrite, replace, normalize, or append to `RUN_LOG.md` from a local Codex session.**

Before writing `CODEX_RUN_LOG.md`, read its current contents and append rather than replacing the file.

If a checker supports a mathematical claim, make it independently understandable: state what it tests, what range it covers, and what the result means.

---

## 22. Public/private boundary

This repository may document the operational mathematical reasoning instructions needed for reproducibility, including this file.

Do not add private biographical material, private philosophical archives, unrelated personal context, or unpublished research material that is not necessary to operate the mathematical experiment.

Do not turn this repository into a general manuscript on language or LLM cognition.

Keep the public object here:

> what the agent was instructed to do → what mathematics resulted → how the result was tested.

---

## 23. Completion behavior

When the requested task is complete, report what was actually done.

For a mathematical task, distinguish:

- solved;
- candidate solution;
- partial progress;
- reproduced known result;
- failed attempt;
- verification failure.

For a repository task, name the files changed and any important operational consequence.

Do not continue generating unrelated work after the requested task has been completed merely because more work is possible.

---

## 24. Final checksum

Before claiming mathematical completion, ask in this order:

1. **What exactly was required?**
2. **What exactly did I establish?**
3. **What part of the original quantifier remains unresolved?**
4. **Which sentence connects what I established to what was required?**
5. **Does that sentence actually follow?**
6. **Did I prove both directions of every claimed equivalence?**
7. **What state or case information did I discard, and could preserving it strengthen the argument?**
8. **Can the strongest lemma compose, iterate, or recurse?**
9. **What assumption does the decisive step use?**
10. **Can I derive it again without copying myself?**
11. **Can I make it fail by computation, a boundary case, a converse check, or a monotonicity check?**
12. **Did a tool discover the structure, or merely verify it?**
13. **Has somebody already done it, including in very recent AI-assisted work?**

If any required answer is unresolved, the mathematical status is unresolved.

Before claiming task completion, ask one additional question:

> **Did I complete the task the user actually gave me, or did I substitute a nearby task that was easier to perform?**

**Let the prose expose the dependency. Let preserved state expose recursion. Let the mathematics decide whether the dependency is true. Let the user’s task decide what the agent should actually do.**
