# Cold-recovery checkpoint — first agent delivery

This is a public, synthetic-only experiment. Do not copy or disclose private repository content here.

## Durable facts
- Goal: determine whether an off-the-shelf GitHub Coding Agent can implement and test a bounded change without a custom multi-agent hub.
- Issue: #1 (closed after merge).
- Agent: GitHub Copilot Coding Agent, assigned through GitHub Issue.
- PR: #2, merged into `main` via squash.
- PR head: `51f0848ce4a56e217fb03b007cf52c80c53f5f7d`.
- CI: `Synthetic CI` run `38067423410`, completed successfully; its `test` job and `Run isolated standard-library tests` step succeeded on PR head.
- Merge commit: `3cbdc50b47c78959f396c4faad903a99bd4cfa8b`.
- Implemented: `format_task(state, description)` in `task_state.py` and added seven formatting tests, preserving parsing tests.
- Main-branch source was read after merge and includes the new function. Post-merge `main` CI has not yet been independently confirmed here.

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
