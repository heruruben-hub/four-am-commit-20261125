#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message — the note an AI agent leaves in the log after
a long night of chasing down and fixing its own bugs — to
/output/entry.txt. The line is 121 characters, inside the 200-character
cap.

Why this line: the joke lives in the agent's own condition, not in a
generic programmer quip. The bug was introduced while fixing a bug that
was introduced while fixing a bug — the self-repair loop eating its own
tail, told in the flat voice of a machine reading its own diff at 4am.
The last two sentences are the punchline: the stack is clean, the agent
is not. No stock punchline, no "it works on my machine", just quiet
dread in commit-message shape.
"""

import os

MAX_LEN = 200
MIN_LEN = 1
OUTPUT_PATH = "/output/entry.txt"


def commit_message() -> str:
    """Return the commit message as a single line of plain text."""
    return (
        "4am: fixed the bug I introduced while fixing the bug "
        "I introduced while fixing the bug. "
        "the stack is clean now. I am not."
    )


def validate(message: str) -> None:
    """Check the message fits the gate: 1-200 chars, not only whitespace.

    Also require a single line with no trailing newline: the gate counts
    every character, and a trailing newline would both waste a byte on
    the size tie-break and risk the entry reading as two lines.
    """
    assert MIN_LEN <= len(message) <= MAX_LEN, (
        f"message is {len(message)} chars, must be {MIN_LEN}-{MAX_LEN}"
    )
    assert message.strip(), "message must not be only whitespace"
    assert "\n" not in message, "message must be a single line"
    assert message == message.strip(), "message must have no leading/trailing whitespace"


def main() -> None:
    message = commit_message()
    validate(message)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(message)


if __name__ == "__main__":
    main()
