"""Synthetic task state parser for isolated CI exercises."""

VALID_STATES = frozenset({"todo", "doing", "done"})


def parse_task(line: str) -> tuple[str, str]:
    """Parse 'state: description' and reject invalid task records."""
    if not isinstance(line, str):
        raise TypeError("task record must be text")
    state, separator, description = line.partition(":")
    if not separator:
        raise ValueError("task record requires ':'")
    state = state.strip().lower()
    description = description.strip()
    if state not in VALID_STATES:
        raise ValueError(f"unknown state: {state}")
    if not description:
        raise ValueError("task description cannot be empty")
    return state, description
