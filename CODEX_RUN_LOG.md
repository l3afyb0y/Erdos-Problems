# Codex run log

This file records operational provenance for **local or interactive Codex sessions** working in this repository.

It is deliberately separate from [`RUN_LOG.md`](RUN_LOG.md), which is reserved for the scheduled ChatGPT/autonomous remote solver. The separation prevents one agent from overwriting or normalizing another agent's execution history.

When a Codex run should be logged, append a compact entry recording:

- observed local time (and scheduled/intended time if relevant);
- task or problem ID;
- whether the run was discovery, second pass, reproduction, verification, or repository/tooling work;
- final classification or task result;
- whether a candidate complete result triggered reproduction;
- tools materially used during discovery versus verification;
- files changed;
- commits made, if any;
- anomalies, interruptions, permission changes, or context/instruction changes that may affect reproducibility.

Do not reconstruct runs that did not happen. Do not rewrite prior rows merely to make the experimental history cleaner.

## Runs

_No Codex runs have been reconstructed into this new file. Earlier Codex provenance, if needed, remains recoverable from Git history and local transcripts._
