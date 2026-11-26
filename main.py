"""Minutes of the meeting that should have been one line, kept to exactly that."""

import os

LINE = "Decision: do exactly what the original email said. The other fifty-nine minutes were just twelve of us reading it out loud, together, in a room booked for focus."

# House rule: the whole meeting must fit in a single line of at most 200 characters.
assert len(LINE) <= 200, "these minutes ran long, unlike the meeting should have"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
