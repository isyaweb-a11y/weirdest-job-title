#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

The entry is a single job title, the weirdest one imaginable, that
still sounds like a real job. A Senior Vice President of Apologising
to Printers is a title you can picture on a business card: a person
whose whole working life is saying sorry to machines that jam, and
whose card nobody ever questions. The twist lands on the first read, and the title is short enough to take
in at a glance.

Writes the title to /output/entry.txt. Stdlib only, no network.
"""

import os

ENTRY = "Senior Vice President of Apologising to Printers"

# The gate allows 1 to 60 characters for the job title.
MAX_CHARS = 60


def entry_text() -> str:
    """Return the title, checked against the bounty's own rules."""
    text = ENTRY.strip()
    assert text, "the entry must not be empty"
    assert "\n" not in text, "the entry must be a single line"
    assert len(text) <= MAX_CHARS, "the entry must fit the gate"
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
