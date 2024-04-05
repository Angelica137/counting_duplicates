def duplicate_count(text: str) -> int:
    count = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in count:
            count[char_lower] += 1
        else:
            count[char_lower] = 1
    unique_chars_count = 0
    for key in count:
        if count[key] == 1:
            unique_chars_count += 1
    return unique_chars_count
