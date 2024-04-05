from src.duplicate_count import duplicate_count


def test_duplicate_count_returns_one():
    assert duplicate_count("1") == 1
