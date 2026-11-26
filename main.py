import os

LINE = "Decision: do exactly what the original email said — the other fifty-nine minutes were just twelve of us reading it out loud together."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
