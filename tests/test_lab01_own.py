import pytest
from basics import format_report, gc_percent, parse_counts


def test_gc_percent_boundary_cases():
    """Test boundary cases for 100% GC and 0% GC."""
    assert gc_percent(0, 10, 10, 0) == 100.0
    assert gc_percent(10, 0, 0, 10) == 0.0


def test_gc_percent_zero_total_raises_value_error():
    """Test that a zero total base count raises ValueError."""
    with pytest.raises(ValueError, match="Total base count cannot be zero."):
        gc_percent(0, 0, 0, 0)


def test_parse_counts_invalid_inputs():
    """Test parse_counts raises ValueError for non-numeric or negative inputs."""
    with pytest.raises(ValueError):
        parse_counts("10 20 A 40")
    with pytest.raises(ValueError):
        parse_counts("10 -5 20 30")