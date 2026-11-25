import os
import sys

SENTENCE = (
    "At two in the morning in Yogyakarta, my grandmother slid me nasi goreng "
    "still crackling from the wok, and I ate it with my hands because our fork "
    "had gone missing years ago."
)


def validate_sentence(sentence: str) -> list[str]:
    """Return a list of gate failures; an empty list means the sentence is valid."""
    errors: list[str] = []
    if not 1 <= len(sentence) <= 200:
        errors.append(
            f"length is {len(sentence)} characters, outside the 1-200 range"
        )
    if sentence != sentence.strip():
        errors.append("has leading or trailing whitespace")
    if "\n" in sentence or "\r" in sentence:
        errors.append("contains a newline")
    if not sentence.endswith((".", "!", "?")):
        errors.append("does not end with terminal punctuation")
    elif any(mark in sentence[:-1] for mark in ".!?"):
        errors.append("contains sentence-ending punctuation before the end")
    try:
        sentence.encode("utf-8")
    except UnicodeEncodeError as exc:
        errors.append(f"is not valid UTF-8: {exc}")
    return errors


def main() -> None:
    errors = validate_sentence(SENTENCE)
    if errors:
        for error in errors:
            print(f"error: entry sentence failed validation: {error}", file=sys.stderr)
        raise SystemExit(1)

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(
        os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline=""
    ) as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
