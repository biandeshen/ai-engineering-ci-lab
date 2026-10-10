# Track A vs Track B — bounded comparison (2026-10-11)

## Scope and integrity
Both implementations use the same synthetic task-list parsing requirement and start from equivalent source at pre-A commit `1a292b632af01b423fab2f76b87165d84e32209d`. Track A: Copilot Issue #5 / merged PR #6. Track B: current assistant guided by existing private `engineering-orchestrator` Skill, Issue #7 / comparison-only draft PR #8. This is **not** a controlled model/agent A/B: executor and host differ. No private code was published.

## Direct code review
- Both implementations add `parse_tasks(text)` with a non-string TypeError, blank-line skip, physical 1-based line numbers, reuse of `parse_task`, and fail-fast ValueError chaining.
- Both add tests for empty/whitespace-only input, ordered records with embedded colons, non-string input, and missing colon/unknown state/empty description on physical line 3 after a blank line.
- Both change only `task_state.py` and `tests/test_task_state.py`. No new dependencies or workflow edits.
- Track A PR #6: 3 commits, 43 additions / 1 deletion, head `ff98245a58b275d69d00a117c1083c42ea35005a`, CI run `38068923799` succeeded, squash merged `e7e12cc6594b0548f625d5e80c9baf36a0461b72`.
- Track B PR #8: 2 commits, 40 additions / 1 deletion, head `3c3614d5cfa3ad55cbfb2cf480b8c8384a8b7f9a`, **no verified GitHub Actions run** for that head as of this checkpoint. Draft PR is non-mergeable against main because main already has A's implementation; do not force-merge duplicate code.
- A test assertions use `assertRaisesRegex`; B checks error text with two `assertIn` assertions. No observed requirement-level difference.

## Verdict
A is delivered and CI-verified. B is code-complete by review but **not independently CI-verified**. Neither approach demonstrates a measurable correctness advantage. A few lines of code or one fewer commit do not demonstrate cost or speed superiority; no reliable elapsed execution-time or token/cost data was collected. No evidence supports adding a custom orchestration hub for this task. The existing Skill can act as lightweight guidance, but incremental value remains unproven.

## Follow-up
If a stricter comparison is worth the cost, use separate clean branches at the same SHA, identical prompts, the same executor/model and independent CI, changing only whether the Skill is supplied. Otherwise stop the synthetic experiments and evaluate on one real bounded project task while keeping private repos private.
