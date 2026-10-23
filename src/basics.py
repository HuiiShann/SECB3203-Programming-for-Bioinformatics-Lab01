"""Lab 1 - Python fundamentals for biological calculations."""


def gc_percent(a: int, c: int, g: int, t: int) -> float:
    """Return the GC percentage from the four base counts."""
    if a < 0 or c < 0 or g < 0 or t < 0:
        raise ValueError("Base counts cannot be negative.")

    total = a + c + g + t
    if total == 0:
        raise ValueError("Total base count cannot be zero.")

    return ((g + c) / total) * 100.0


def format_report(sample: str, length: int, gc: float) -> str:
    """Return a one-line report with units, e.g. 'Amplicon_01: 60 bases, GC 36.7%'."""
    return f"{sample}: {length} bases, GC {gc:.1f}%"


def parse_counts(text: str) -> tuple[int, int, int, int]:
    """Parse 'A C G T' counts separated by spaces or commas into a tuple of 4 ints."""
    tokens = text.replace(",", " ").split()

    if len(tokens) != 4:
        raise ValueError(
            f"Expected exactly 4 base counts, but got {len(tokens)}."
        )

    try:
        counts = [int(tok) for tok in tokens]
    except ValueError:
        raise ValueError("All counts must be valid whole numbers.")

    if any(c < 0 for c in counts):
        raise ValueError("Base counts cannot be negative.")

    return (counts[0], counts[1], counts[2], counts[3])