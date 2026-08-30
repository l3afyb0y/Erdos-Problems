# Erdos Problems in Language and terms

A working repository for an experiment in attacking **currently open Erdős problems** through both conventional mathematics and complete-prose mathematical reasoning.

The experiment treats mathematical notation as compressed representation. Discovery is conducted primarily in language: named operators, explicit conditional grammar, relations, reversals, oppositions, boundaries, and simple dependency chains. Candidate results are then compiled back into conventional mathematics and independently checked.

## Scope

Only problems whose current status in the Erdős Problems database is `open` are research targets here.

This repository may contain:

- the open problem statement and current source/status reference;
- conventional mathematical proofs, reductions, or lemmas discovered during the attempt;
- complete-prose versions of the same reasoning;
- exact verification code and recorded outputs where applicable;
- explicit status labels distinguishing partial progress from candidate or verified complete proofs.

The broader research methodology concerning language as a reasoning substrate for large language models is intentionally **not** published here.

## Experiment status labels

Each attempted open problem is labeled with one of:

1. `no-progress`
2. `useful-reformulation`
3. `known-reduction-rediscovered`
4. `candidate-partial-lemma`
5. `candidate-complete-proof`
6. `verified-complete-proof`

`verified-complete-proof` is used only after the argument survives exact checking and a current literature/status audit. A candidate proof is not represented as a new solution merely because its internal derivation succeeds.

## Intended layout

```text
problems/
  NNN/
    README.md          # statement, external status, experiment status
    mathematics.md     # conventional mathematical form
    prose.md           # complete prose / language form
    verify.*           # exact checker when useful
    verification.txt   # recorded verification output when useful

index.md               # running experiment ledger
```

## Experiment title

**Erdos Problems in Language and terms**

This is a working research record. Novelty, completeness, and correctness are separate questions and are recorded separately.
