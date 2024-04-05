from collections import Counter


def duplicate_count(text: str) -> int:
    # Create a Counter for all characters in the text
    char_counts = Counter(text.lower())
    # Count how many characters have a count greater than one
    duplicates = sum(1 for char, count in char_counts.items() if count > 1)
    return duplicates
