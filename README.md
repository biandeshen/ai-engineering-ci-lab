# AI Engineering CI Lab

Public, synthetic-only CI laboratory for testing the execution path of AI coding agents without exposing private repositories.

## Scope
- Only original synthetic fixtures and standalone test code are permitted.
- No private repository source, history, secrets, issue exports, artifacts, or production configuration.
- A green result here **does not** prove a private repository PR passed its own required checks.
- This lab does not receive privileged credentials or write back to private repositories.

## First experiment
Run the Python standard-library unit tests against a tiny task-state parser on push and pull request. The parser is a standalone synthetic fixture, not a copy of Orchestrator code. An agent can be asked to improve this code in a separate PR, and its actual diff, tests, and cold recovery can be assessed.

Run locally: `python -m unittest discover -s tests -v`.

Source experiment context: private Orchestrator issue #42. Do not publish private issue content here.
