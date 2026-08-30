# AGENTS.md — grammar-first instructions for mathematical agents

This file is the repository-level instruction layer for Codex and other agents working in this repository.

Its primary practical purpose is to let an agent enter a local clone and immediately understand **how to work here** without requiring the user to reconstruct the experiment from chat history. The same file may also be read by scheduled or remote agents so that multiple systems share one normalized operating method.

The method is shared. The task is not.

**If the user gives a specific task, then that task is the target.**

Do not silently replace a user request to verify one proof, inspect one file, write one checker, or solve one named problem with an autonomous batch over unrelated problems.

**Only enter the autonomous next-problem loop when the user, scheduler, or higher-level task explicitly requests autonomous solving.**

These instructions govern agents working anywhere in this repository unless a more specific instruction file exists below the current path.

---

## 0. Resolve the task before acting

**Let** `T` be the task actually requested in the current session.

**First ask:** what output would count as completing `T`?

Then identify the operating mode.

### Mode A — specific solve / second pass

Use when the user names a problem or asks to take another crack at one already attempted.

Read:

1. `AGENTS.md`;
2. `TESTING_METHODOLOGY.md`;
3. the relevant `problems/<n>.md`;
4. any verifier or source file directly referenced there;
5. `index.md` only as needed for status/context.

If the problem is already processed, mark the work conceptually as **REOPENED FOR SECOND PASS**. Do not pretend it is a fresh first attempt.

### Mode B — reproduction / verification

Use when the user asks whether an existing claim, proof, computation, or candidate result is correct.

Read the claim to be checked, then reconstruct the argument independently where possible.

**Do not begin by trying to make the existing proof sound better. Begin by trying to make it fail.**

Use `TESTING_METHODOLOGY.md` as the governing protocol.

### Mode C — autonomous solving

Use only when explicitly requested by the user, scheduler, or task.

Read:

1. `AGENTS.md`;
2. `TESTING_METHODOLOGY.md`;
3. `index.md`;
4. `RUN_LOG.md` when run provenance matters.

Then select a currently open, unprocessed problem and follow the autonomous loop in Section 15.

### Mode D — repository / tooling work

Use when the user asks to organize files, improve instructions, write verification code, prepare Codex context, repair the ledger, or otherwise maintain the research environment.

In this mode, do the requested repository task. Do not start solving unrelated mathematics merely because this is a solver repository.

---

## 1. Repository roles

Treat the repository as persistent experimental state.

- `AGENTS.md` = portable agent method and repo-working instructions.
- `TESTING_METHODOLOGY.md` = public experimental controls and verification protocol.
- `index.md` = compact processed-problem ledger.
- `problems/<n>.md` = authoritative mathematical record for problem `n`.
- `verification/` = exact checkers and computational support.
- `RUN_LOG.md` = autonomous execution provenance and scheduler/tool anomalies.

**If a mathematical claim changes, then update the relevant problem record.**

**If its classification changes, then update `index.md`.**

**If an autonomous run occurs, then update `RUN_LOG.md` truthfully.**

Never reconstruct a run that did not happen.

For an interactive local Codex session, do not commit or push merely because files were edited unless the user asks for commits/pushes or the surrounding task explicitly requires them.

---

## 2. Primary mathematical objective

**Let** the target be the complete mathematical statement, including its quantifiers.

**If** you find a reformulation, identity, reduction, computation, construction family, obstruction, or lemma,

**then** treat it as a newly available premise — not as the endpoint.

Then ask:

> **Given this, what follows next that moves the unresolved quantifier?**

Continue until one of these is true:

- the complete statement is proved;
- the complete statement is disproved by a valid counterexample or construction;
- the requested attempt is genuinely exhausted.

Do not stop merely because something is interesting.

A useful partial result should be preserved, but it should not be confused with solving the problem.

---

## 3. Discovery representation: decompile notation into relations

During discovery, treat mathematical notation as compressed representation when doing so makes the next inference easier to see.

For each important expression:

**Let** the symbols be named.

**Then** recover the relation represented by those symbols in ordinary language.

Examples:

- `a | b` → `b contains a as an integer factor`;
- `x ≡ y (mod m)` → `x and y occupy the same position in repeating blocks of size m`;
- `A ⊆ B` → `every object admitted by A is also admitted by B`;
- `∀` → `for every`;
- `∃` → `there is at least one`;
- equality → `two representations must denote the same object or quantity`;
- inequality → `one side is constrained above or below by the other, with direction preserved`.

Mere transliteration is not enough. `one plus two equals three` has not exposed a useful relation merely because the glyphs were spoken aloud.

The point of language is to make dependency, scope, relation, and available transformation legible.

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

**If** an implication `A -> B` is useful,

**then** reverse it and ask whether `B -> A` also holds.

**If not**, locate the asymmetry. A failed converse frequently identifies the missing condition or useful obstruction.

---

## 5. Ask what becomes available next

Do not search only for statements that look like conclusions.

At each step ask:

> Given everything presently established, **what operation or fact has become newly available?**

Examples:

- a divisibility fact may make a quotient integral;
- a gcd statement may exclude a shared prime;
- an extremal choice may make a local modification impossible;
- equality may force every inequality in a chain to be equality;
- a missing element may itself define a smaller instance;
- a partition may expose mutually exclusive cases;
- a bound may turn an infinite search into a finite one.

The goal is to follow a shortest valid dependency path, not to maximize the number of named theorems used.

---

## 6. Search operators

When progress stalls, inspect the current object locally through:

- reverse;
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
- preserved quantity / invariant;
- factorization or decomposition;
- recombination;
- representation change;
- recursion into the residual object.

Do not assume a useful global symmetry exists merely because an opposition is available locally.

**If** a symmetry or opposition is invoked,

**then** state exactly what is reversed and exactly what is preserved.

Tiny case distinctions may be load-bearing. Do not normalize `selected` and `unselected`, `strict` and `weak`, `ordered` and `unordered`, or `exists` and `for every` into one vague condition.

---

## 7. Preserve state instead of throwing it away

When a proof produces cases, residues, excluded objects, boundary states, or leftover structure, do not immediately compress them into a single coarse bound.

Ask:

> **If I preserve which case occurred, can the remainder be used again?**

This is especially important for recursive or iterative arguments.

A one-step inequality may contain a stronger recurrence if the proof remembers why equality failed or which objects survived.

If a discarded distinction affects the next available operation, keep it.

---

## 8. Prefer the shortest forced dependency path

Let every `therefore` be typechecked.

Seek a decisive invariant or relation that makes the next step forced.

Prefer, when available:

> premise → relation → constraint → contradiction/construction

over
> theorem name → theorem name → theorem name → conclusion.

Deep machinery is allowed when necessary. Simplicity is a search preference, not a restriction on valid mathematics.

Do not reject a correct deeper proof merely because an elementary proof was hoped for.

---

## 9. Representation is not truth

A useful sentence can represent a mathematical relation without establishing it.

**If** you write `X is Y`,

**then** ask whether you proved identity, proved only a relation, or merely chose a representation.

**If** a language-level insight and exact mathematics disagree,

**then** the language-level inference loses. Locate the translation or inference error.

Elegance, repetition, familiarity, confidence, and apparent inevitability are not proof.

---

## 10. Quantifier discipline

At every promising endpoint, restate the original target in plain language.

Then ask:

- Did I prove `for every`, or did I test many examples?
- Did I prove `there exists`, or did I derive only a necessary condition?
- Did I prove an asymptotic statement uniformly, or only on a subsequence?
- Did I prove the converse I am now using?
- Did I replace the global claim with a local lemma without noticing?
- Did I establish eventual behavior, or only behavior below a computational cutoff?

A finite computation cannot by itself discharge an unbounded universal quantifier.

A reduction is not a solution unless the reduced target is itself closed.

---

## 11. Candidate complete solution protocol

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

## 12. Attack the proof instead of defending it

For every candidate proof, deliberately search for failure.

Check:

- boundary values;
- degenerate cases;
- hidden positivity assumptions;
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
- exact versus asymptotic claims;
- dependence of constants;
- local-to-global transitions;
- finite evidence being promoted to universality;
- imported theorems whose hypotheses may not match the current formulation.

**If** exact code can falsify a claim cheaply,

**then** write and run the code.

**If** a formal checker can verify a decisive step,

**then** prefer that check over confidence.

For verification work, a discovered error is a successful result of the verification process.

---

## 13. Novelty and contamination control

Before a novelty-sensitive discovery attempt, use only enough external searching to establish that the target is currently open and not obviously superseded by a fresh complete claim.

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
- recent preprints, comments, forum posts, formalizations, or solver-generated claims.

**If** equivalent prior work exists,

**then** classify the result as rediscovered.

**If** no equivalent work is found,

**then** use `novelty unresolved` until stronger independent review is complete.

Search failure is not proof of novelty.

---

## 14. Status vocabulary

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

## 15. Autonomous loop — only when autonomous mode was requested

Let `P` be a candidate Erdős problem.

**If** `P` is already processed and this is not an explicit revisit,

**then** choose another problem.

**If** `P` is not currently open,

**then** choose another problem.

**Otherwise, attempt P.**

**If** a partial result appears,

**then** use it as a premise and continue toward the full target.

**If** the attempt exhausts without a complete result,

**then** preserve the strongest valid result, classify it conservatively, update the repository state, and move on.

**If** a complete result appears,

**then** freeze it.

**Then** reproduce it independently.

**Then** attack it.

**Then** verify exact steps.

**Then** audit prior art.

**If** it survives all gates,

**then** promote its status.

**Then** record the result.

**Then** choose the next open problem.

---

## 16. Working-tree and code discipline for local agents

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

If a checker is intended to support a mathematical claim, make it independently understandable: state what it tests, what range it covers, and what result means.

---

## 17. Public/private boundary

This repository may document the operational mathematical reasoning instructions needed for reproducibility, including this file.

Do not add private biographical material, private philosophical archives, unrelated personal context, or unpublished research material that is not necessary to operate the mathematical experiment.

Do not turn this repository into a general manuscript on language or LLM cognition.

Keep the object here:

> what the agent was instructed to do → what mathematics resulted → how the result was tested.

---

## 18. Completion behavior

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

## 19. Final checksum

Before claiming mathematical completion, ask in this order:

1. **What exactly was required?**
2. **What exactly did I establish?**
3. **Which sentence connects those two?**
4. **Does that sentence actually follow?**
5. **What assumption does it use?**
6. **Can I derive it again without copying myself?**
7. **Can I make it fail by computation, a boundary case, or a converse check?**
8. **Has somebody already done it?**

If any required answer is unresolved, the mathematical status is unresolved.

Before claiming task completion, ask one additional question:

> **Did I complete the task the user actually gave me, or did I substitute a nearby task that was easier to perform?**

**Let the prose expose the dependency. Let the mathematics decide whether the dependency is true. Let the user’s task decide what the agent should actually do.**
