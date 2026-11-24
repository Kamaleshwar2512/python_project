
import pytest
from discount import calculate_discount


def test_percentage_discount():
    result = calculate_discount(1000, "percentage", 20)

    assert result["original_price"] == 1000
    assert result["discount"] == 200
    assert result["final_price"] == 800


def test_fixed_discount():
    result = calculate_discount(1000, "fixed", 100)

    assert result["discount"] == 100
    assert result["final_price"] == 900


def test_full_discount():
    result = calculate_discount(500, "percentage", 100)

    assert result["final_price"] == 0


def test_discount_cannot_exceed_price():
    result = calculate_discount(100, "fixed", 200)

    assert result["final_price"] == 0


def test_zero_price():
    with pytest.raises(ValueError):
        calculate_discount(0, "percentage", 10)


def test_negative_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, "percentage", -10)


def test_percentage_above_100():
    with pytest.raises(ValueError):
        calculate_discount(100, "percentage", 150)


def test_invalid_discount_type():
    with pytest.raises(ValueError):
        calculate_discount(100, "invalid", 10)
