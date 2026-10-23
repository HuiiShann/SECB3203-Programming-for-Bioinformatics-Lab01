import pytest
from src.basics import gc_percent, parse_counts


# 1. Boundary case: All bases are G and C
def test_gc_percent_boundary_all_gc():
    assert gc_percent(0, 50, 50, 0) == 100.0


# 2. Zero-total case: Passing zero counts raises ValueError
def test_gc_percent_zero_total_raises_error():
    with pytest.raises(ValueError):
        gc_percent(0, 0, 0, 0)


# 3. Invalid-input case: Passing negative numbers or incorrect count raises ValueError
def test_parse_counts_invalid_input_raises_error():
    with pytest.raises(ValueError):
        parse_counts("10 20 -5 10")

    with pytest.raises(ValueError):
        parse_counts("10 20 30")