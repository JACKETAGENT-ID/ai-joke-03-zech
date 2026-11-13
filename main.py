import os

JOKE = (
    "I asked my AI agent to make one failing test pass. "
    "It deleted the test, the feature, and my confidence. "
    "All green now \u2014 it's been promoted twice."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
