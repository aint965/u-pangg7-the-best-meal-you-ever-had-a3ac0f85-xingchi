import os

SENTENCE = (
    "At two in the morning in Yogyakarta, my grandmother slid me nasi goreng "
    "still crackling from the wok, and I ate it with my hands because our fork "
    "had gone missing years ago."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
