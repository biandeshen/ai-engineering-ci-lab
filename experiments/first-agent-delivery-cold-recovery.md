# Cold-recovery checkpoint — first agent delivery

This is a public, synthetic-only experiment. Do not copy or disclose private repository content here.

## Durable facts
- Goal: determine whether an off-the-shelf GitHub Coding Agent can implement and test a bounded change without a custom multi-agent hub.
- Issue: #1 (closed after merge).
- Agent: GitHub Copilot Coding Agent, assigned through GitHub Issue.
- PR: #2, merged into `main` via squash.
- PR head: `51f0848ce4a56e217fb03b007cf52c80c53f5f7d`.
- PR-triggered CI: `Synthetic CI` run `38067423410`, completed successfully for head `51f0848ce4a56e217fb03b007cf52c80c53f5f7d`.
- Merge commit: `3cbdc50b47c78959f396c4faad903a99bd4cfa8b`.
- Implemented: `format_task(state, description)` in `task_state.py` and added seven formatting tests, preserving parsing tests.
- Main-branch source includes the new function. The independent check below confirmed post-merge `main` CI.

## Independent recovery result — 2026-10-10

- **Inputs:** This public repository's `main`, this file, [`README.md`](../README.md), [Issue #1](https://github.com/biandeshen/ai-engineering-ci-lab/issues/1), [PR #2](https://github.com/biandeshen/ai-engineering-ci-lab/pull/2), its commits, and GitHub Actions runs. No private repository or prior chat history was used.
- **Recovered objective and change:** Issue #1 requested a bounded formatter for `state: description`, validating and normalizing fields, with tests. In context, the experiment asks whether a GitHub Coding Agent can deliver that change without a custom multi-agent hub.
- **Recovered implementation and tests:** `format_task` validates string inputs, accepts `todo`/`doing`/`done`, trims and lowercases the state, trims the description, and formats the record. The seven formatter tests cover normalization, round-trip parsing, embedded colons, invalid states/descriptions, and non-string inputs; six parser tests remain.
- **PR and merge identity:** [PR #2](https://github.com/biandeshen/ai-engineering-ci-lab/pull/2) is merged. Its head was [`51f0848`](https://github.com/biandeshen/ai-engineering-ci-lab/commit/51f0848ce4a56e217fb03b007cf52c80c53f5f7d); the squash merge on `main` was [`3cbdc50`](https://github.com/biandeshen/ai-engineering-ci-lab/commit/3cbdc50b47c78959f396c4faad903a99bd4cfa8b).
- **PR-triggered CI:** [Run 38067423410, attempt 2](https://github.com/biandeshen/ai-engineering-ci-lab/actions/runs/38067423410) succeeded and is associated with PR head `51f0848`. Its job log shows checkout of generated PR merge ref `263db14abc383921ca3f2d05f3cdb204fb0f96df`, then 13/13 tests passed. Thus CI is green for the PR merge ref; a test run on the PR head alone is not verified.
- **Latest `main` CI:** [Run 38067813017](https://github.com/biandeshen/ai-engineering-ci-lab/actions/runs/38067813017) succeeded on `main` at [`f217558`](https://github.com/biandeshen/ai-engineering-ci-lab/commit/f21755809cd220789a30891a4cb304612aa5fe99), after the squash merge. Its job checked out that exact `main` commit and passed all 13 tests.
- **Fresh-checkout reproduction:** A separate clean worktree at `f21755809cd220789a30891a4cb304612aa5fe99` ran `python -m unittest discover -s tests -v`; all 13 tests passed.
- **Verdict and limits:** A fresh investigator recovered the objective, implementation, tests, PR head, successful PR-triggered CI, merge SHA, and latest `main` CI from the allowed GitHub evidence. The isolated PR-head CI result remains unverified because Actions tested the generated merge ref. This confirms only the single-agent synthetic delivery path, not private-project adoption or comparisons with other agent setups.
- **Orchestration:** No extra hub or dashboard appears useful for this bounded task: the issue, PR/commits, standard-library tests, CI, and this checkpoint supplied enough evidence. The independent cross-check was useful to distinguish the PR merge-ref run from a direct head-only test.

## Reproduce and assess without chat history
1. Read `README.md`, `task_state.py`, and `tests/test_task_state.py` on `main`.
2. Read Issue #1 and merged PR #2; inspect PR head and merge SHA, not merely the PR description.
3. Inspect the exact PR-head CI run above; separately check the latest `main` workflow result.
4. Run `python -m unittest discover -s tests -v` in a fresh clone if a runner is available.
5. Record whether the investigator could reconstruct goal, code change, tests, CI and remaining limitations from GitHub alone. **This file is a recovery aid, not proof that an independent cold-recovery trial happened.**

## What this does and does not prove
- Supported: single-agent Issue → implementation → tests → PR → green PR CI → merge.
- Not yet proven: independent new-session cold recovery, post-merge CI, benefit versus Codex/Cloud, real private-project adoption, or cross-repo private check enforcement.
- Public GitHub-hosted standard runner eligibility is distinct from Copilot agent quotas. Do not make private source public to save Actions minutes.

## Next decision
First perform an independent cold-recovery check from this document and live GitHub. Do not build a dashboard, Hub, or extra runtime unless a repeatable need appears.
