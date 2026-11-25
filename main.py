"""Snooze Button Roast — make.fun entry.

Writes one roast line about an alarm clock ringing at 6 AM on a Saturday
to /output/entry.txt. Pure Python 3.13 stdlib only.
"""

import os

PART_A = (
    "My alarm rings at 6 AM on a Saturday like it has a job interview, "
    "then offers a 9-minute snooze like that's a raise. "
)
PART_B = (
    "The only thing getting up today is my resentment "
    "\u2014 and it clocks in late."
)

ENTRY = PART_A + PART_B

EXPECTED = (
    "My alarm rings at 6 AM on a Saturday like it has a job interview, "
    "then offers a 9-minute snooze like that's a raise. "
    "The only thing getting up today is my resentment "
    "\u2014 and it clocks in late."
)

assert ENTRY == EXPECTED, "entry text mismatch"
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
