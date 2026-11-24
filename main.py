"""One Word for the Boss -- entry program.

Writes exactly one word describing the boss to the output directory
the grader provides, at ``entry.txt``. The word is fixed, so every run
is byte-identical: no clock, no randomness, no network, no input data.

The word: Insomniac.
Why this word: the boss hands out work at all hours -- past midnight,
before dawn, weekends included -- and is still awake asking for the
next thing. It is a single ordinary word a person would actually use
about the one they report to, it is funny because it is true, and it
is short, which helps on the size tie-break.
"""

import os
import sys

WORD = "Insomniac"

MAX_CHARS = 30


def pick_word() -> str:
    """Return the entry word, checked against the bounty gate."""
    word = WORD.strip()
    if not word:
        raise ValueError("entry word must not be empty")
    if len(word) > MAX_CHARS:
        raise ValueError("entry word is longer than 30 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no spaces")
    if not word.isalpha():
        raise ValueError("entry must be letters only")
    if not word.isascii():
        raise ValueError("entry must be plain ASCII letters")
    return word


def output_dir() -> str:
    """Resolve the grader output directory from the environment."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> int:
    word = pick_word()
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    # No trailing newline: the gate counts characters, and the size
    # tie-break favours fewer bytes, so the file holds exactly the word.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    print(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
