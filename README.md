# Erdos Problems in Language and terms

A working mathematical record for an autonomous experiment attacking **currently open Erdős problems**.

The goal is not to accumulate reformulations. The goal is to obtain complete proofs, disproofs, or constructions. Partial lemmas are recorded only when a complete solution is not reached in that attempt.

## Public scope

Only problems whose current status in the Erdős Problems database is `open` are research targets here.
This is apart of a larger focus project pertaining to language and LLM reasoning abilities. This repo exists more as a corpus of data for later purposes than any meaningful expectations the model will succeed in solving all open problems.
Results of the experiment are currently promising, mostly in terms of it's ability to work unbelievably fast on these problems.
More information will likely be released in a preprint; this experiment is extremely volatile and difficult to control for, however, I've done my best to do so.

This repository contains only the mathematical output layer:

- the open problem statement and current source/status reference;
- conventional mathematical proofs, disproofs, reductions, constructions, or lemmas;
- complete-prose renderings of the particular mathematical argument;
- exact verification code and recorded outputs where applicable;
- independent reproduction results for candidate complete solutions;
- prior-art / novelty audit notes;
- explicit status labels distinguishing partial progress from complete proofs.

The broader research methodology concerning language as a reasoning substrate for large language models is intentionally **not** published here.

## Machine state

[`index.md`](index.md) is both the public ledger and the processed-problem state for autonomous runs. Before selecting a target, the solver checks the current Erdős database status and this ledger. A problem already present in the ledger is not selected again unless it is deliberately reopened for verification.

Every attempted open problem is recorded even when the attempt fails. This prevents repeated rediscovery from masquerading as new progress and allows the solver to keep moving through the open corpus.

## Result labels

1. `no-progress`
2. `useful-reformulation`
3. `known-reduction-rediscovered`
4. `candidate-partial-lemma`
5. `candidate-complete-proof`
6. `candidate-complete-proof — novelty unresolved`
7. `verified-complete-proof`

A complete candidate is reproduced independently before promotion. Repeated model agreement is supporting evidence, not proof by itself; the final mathematical argument must survive adversarial checking and a current prior-art audit.

`verified-complete-proof` therefore means all three are presently satisfied:

- **completeness:** the argument actually proves or disproves the full open statement;
- **correctness:** independent reconstruction and exact/adversarial checks did not break it;
- **novelty audit:** no prior equivalent complete result was found in the current search.

## Layout

```text
problems/
  NNN.md              # statement, mathematics, reproduction/verification, status

index.md              # running ledger and autonomous processed state
```

## Experiment title

**Erdos Problems in Language and terms**

Novelty, completeness, correctness, and reproducibility are recorded separately.
