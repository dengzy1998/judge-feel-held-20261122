"""Entry for make.fun 'Make the AI judge feel held': writes one relaxing text."""
from pathlib import Path

TEXT = (
    "Between two old oaks a hammock holds you like a hand, "
    "swaying a little, going nowhere. Leaves move above you in slow "
    "green light, and somewhere a thrush sings the same three notes "
    "over and over. The afternoon has no edges and no errands. "
    "You are held, and held is enough."
)

def main():
    if not 1 <= len(TEXT) <= 280:
        raise ValueError("entry text must be 1-280 characters")
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(TEXT, encoding="utf-8")

if __name__ == "__main__":
    main()
