from src.duplicate_count import duplicate_count


def test_duplicate_count_returns_zero():
    assert duplicate_count("1") == 0


def test_duplicate_count_returns_two():
    assert duplicate_count("He11o") == 1


def test_duplicate_count_rabcde_eturns_zero():
    assert duplicate_count("abcde") == 0
