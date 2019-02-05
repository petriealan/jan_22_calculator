"""
Tests the subtract() function of the Calculator
"""
import pytest

from calculator import subtract

def test_two_minus_two():
    """
    If given 2 and 2 as parameters, 0 should be returned
    """
    assert subtract(2, 2) == 0

def test_no_parameters():
    """
    If no parameters are provided, return 0
    """
    assert subtract() == 0

def test_three_parameters():
    """
    If three parameters are given (10, 5, 1), should return 4
    """
    assert subtract(10, 5, 1) == 4

def test_negative_values():
    """
    Test negative test_decimal_values
    """
    assert subtract(5, -10) == 15

def test_negative_result():
    """
    If the resulting value is negative
    """
    assert subtract(2, 10) == -8

def test_decimal_values():
    """
    Test if -0.1 - 0.1 - 0.1 equals -0.3
    Use the pytest.approx to handle rounding errors
    """
    assert subtract(-0.1, 0.1, 0.1) == pytest.approx(-0.3)
