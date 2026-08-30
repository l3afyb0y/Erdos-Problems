# Testing methodology

This repository is both a mathematical work log and an experimental record. This file documents the **testing and verification protocol** used to evaluate solver outputs. The operational reasoning instructions supplied to repository agents are versioned separately in [`AGENTS.md`](AGENTS.md). Private biographical context and the larger unpublished language/philosophy project are not part of this public testing record.

## Experimental object

The primary experimental unit is one attempt on one Erdős problem whose current public status is `OPEN` at selection time.

The experiment is interested in several increasingly strong outcomes:

1. a correct reformulation;
2. a correct partial lemma or reduction;
3. a mathematically new partial result;
4. a complete candidate proof, disproof, or construction;
5. a reproduced and adversarially verified complete result;
6. a complete result whose novelty also survives prior-art review.

These are different claims and must not be collapsed into one another.

## Model context is an experimental variable

The solver does not operate independently of its instructions or available context. Context therefore has to be treated as part of the experimental condition rather than as invisible background.

The repository-root [`AGENTS.md`](AGENTS.md) is the canonical shared instruction layer for repository-aware models. It gives the grammar-first discovery/control rules in explicit conditional form and tells agents how to interact with the mathematical ledger and verification protocol.

Before a repository-aware attempt, the model should read, in this order:

1. `AGENTS.md`;
2. `TESTING_METHODOLOGY.md`;
3. `index.md` when processed-problem state is relevant;
4. the executor-specific run log when provenance is relevant: `RUN_LOG.md` for the scheduled ChatGPT/autonomous remote solver, `CODEX_RUN_LOG.md` for local or interactive Codex;
5. the relevant `problems/<n>.md` when a processed problem is deliberately reopened.

The commit state of `AGENTS.md` should be regarded as part of run provenance. If its instructions materially change, later runs are not strictly the same experimental condition as earlier runs.

This matters especially when comparing:

- a high-context interactive ChatGPT run;
- an autonomous scheduled run;
- a locally cloned Codex run;
- a fresh verification model that is intentionally given less discovery context.

Those conditions may all be scientifically useful, but they should not be described as identical controls.

For final verification, less discovery context can be desirable. A verifier should ideally receive the problem statement, frozen mathematical proof, and verification target without being coached through the original discovery path. That makes agreement less correlated.

## Target selection

Before an attempt:

1. Read `index.md`, which is the processed-problem ledger.
2. Select only a problem currently listed as open by a maintained public source.
3. Skip problems already processed unless deliberately reopened for reproduction or verification.
4. Perform a narrow status/claim check sufficient to avoid spending an attempt on a problem that has already been credibly solved.
5. Avoid reading detailed existing approaches before the discovery pass unless necessary to understand the statement. This reduces direct solution contamination, but cannot remove information already present in model pretraining.

The public status source and date should be recorded in the problem entry.

## Discovery isolation

The first derivation is treated as the discovery artifact.

If a complete-looking result appears, freeze the derivation before doing a detailed literature search. Preserve enough of the argument to identify its decisive invariant, construction, or contradiction and the exact dependency chain.

A result is not promoted because it looks short, elegant, elementary, familiar, or highly confident.

## Reproduction protocol

A complete candidate should be reproduced before promotion.

At minimum:

1. **First derivation:** preserve the original solution attempt.
2. **Fresh derivation A:** restart from the problem statement without consulting the original wording or dependency chain.
3. **Fresh derivation B:** restart again using a meaningfully different representation when possible — for example conventional mathematics, computational reconstruction, or formal reasoning rather than the original prose route.
4. Compare the derivations only after the fresh attempts are complete.

Interpretation:

- If the derivations disagree, locate the first divergent implication and treat the candidate as unverified until resolved.
- If they converge on the same decisive structure and conclusion, this is supporting evidence, not certification. Repeated runs of the same model family can reproduce correlated errors.
- A different model family, formal proof assistant, exact checker, or independent mathematician is a stronger final reproduction layer.

Same-model reproduction audits are therefore useful error detectors but are explicitly labeled as such.

## Adversarial proof checking

For every candidate proof or disproof, separately inspect:

- quantifier direction and scope;
- converse/implication reversals;
- hidden assumptions;
- positivity and zero cases;
- coprimality and divisibility edge cases;
- parity and residue boundaries;
- asymptotic uniformity;
- monotonicity assumptions;
- finite-to-universal extrapolation;
- use of external theorems and whether their hypotheses match the present formulation.

The verifier should try to **destroy** the argument, not restate it more persuasively.

## Exact computation

When a claim has a finite computational component:

1. Use exact arithmetic whenever feasible.
2. Record the tested domain precisely.
3. Record the search rule and stopping condition.
4. Distinguish exhaustive finite verification from sampling.
5. Re-run important computations independently from newly written code when practical.
6. Never treat finite evidence as a proof of an unbounded universal statement unless a separate argument reduces the universal claim to that finite domain.

Reproducing the same exact finite output is evidence that the computation is stable; it does not by itself prove an asymptotic or universal conjecture.

## Prior-art and novelty audit

Novelty is tested **after** a result has survived internal mathematical checking, except for the narrow pre-attempt status check.

Search for:

- the same conclusion;
- the decisive lemma or invariant;
- equivalent formulations;
- stronger results that imply the candidate;
- recent preprints, formalizations, forum notes, comments, or solver-generated claims not yet reflected in the main database.

Classification should distinguish:

- `known-reduction-rediscovered`;
- `candidate/new-partial-lemma — novelty unresolved`;
- `candidate-complete-proof — novelty unresolved`;
- `verified-complete-proof` only after correctness, reproduction, and prior-art gates have all been passed.

Absence from a quick search is not proof of novelty.

## External claims

If an argument depends on published bounds or theorems that were not re-proved during the audit, mark the conclusion as conditional on those external results applying exactly as quoted. Verification of the local algebra is not the same as verification of the imported theorem.

## Error correction

A reproduction pass is successful even when it finds an error.

When an error is found:

1. preserve the fact that the earlier claim existed when provenance matters;
2. correct the active problem record immediately;
3. state whether the error affected a local lemma, computation, equivalence, boundary case, or claimed solution status;
4. never silently retain the stronger false wording in `index.md`.

The 2026-08-30 reproduction audit is an example: it detected a false equivalence in #324, an overstated collision equivalence in #971, and a boundary qualification in #850.

## Automation and run provenance

Execution provenance is separated by agent/environment so one agent cannot overwrite another agent's operational history.

- `RUN_LOG.md` is reserved for the scheduled ChatGPT/autonomous remote solver.
- `CODEX_RUN_LOG.md` is reserved for local or interactive Codex sessions.

Each logged run should record, when relevant:

- scheduled time when known;
- observed execution/commit time;
- problem IDs or task selected;
- output classifications;
- whether a candidate complete solution triggered reproduction;
- tools materially used during discovery versus verification;
- relevant commit(s);
- scheduler, permission, context, or tool anomalies;
- the relevant agent-instruction commit when the instruction layer changed materially.

A missed, late, duplicated, interrupted, or silent run should be recorded rather than reconstructed as though it occurred normally.

Run logs are append-only provenance records in normal operation. Agents should read the existing log before appending and should not replace another executor's history to add their own run.

## Promotion rule

A public claim that an open Erdős problem has been solved requires all of the following:

**complete argument → fresh reproduction → adversarial verification → exact/formal checking where applicable → current prior-art audit → status wording that matches the evidence.**

Confidence, elegance, repeated wording, and finite computation are not substitutes for any missing gate.

## Verification layers

The intended hierarchy is:

1. discovery model under a recorded instruction/context condition;
2. same-model fresh reproduction;
3. representation-diverse verification and exact computation;
4. different model/system (for example Codex) or formal proof environment;
5. independent mathematical review when a genuinely novel complete result warrants it.

This hierarchy is designed to reduce correlated error while preserving the original discovery trace for later study.
