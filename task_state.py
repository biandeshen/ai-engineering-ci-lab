"""Synthetic task state parser for isolated CI exercises."""

VALID_STATES = frozenset({"todo", "doing", "done"})


def format_task(state: str, description: str) -> str:
    """Format a task record and reject invalid task fields."""
    if not isinstance(state, str) or not isinstance(description, str):
        raise TypeError("task state and description must be text")
    state = state.strip().lower()
    description = description.strip()
    if state not in VALID_STATES:
        raise ValueError(f"unknown state: {state}")
    if not description:
        raise ValueError("task description cannot be empty")
    return f"{state}: {description}"


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


def parse_tasks(text: str) -> list[tuple[str, str]]:
    """Parse task lines; report the physical line of the first invalid record."""
    if not isinstance(text, str):
        raise TypeError("task list must be text")
    result = []
    for number, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        try:
            result.append(parse_task(line))
        except ValueError as exc:
            raise ValueError(f"line {number}: {exc}") from exc
    return result
