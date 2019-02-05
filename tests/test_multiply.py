"""
Tests the multiply() function of the calculator.
"""
import pytest

from calculator import multiply


def test_two_times_two():
    """
    If given 5 and 5 as parameters, 25 should be returned
    """
    assert multiply(5, 5) == 25

def test_no_parameters():
    """
    If no parameters are provided, return 0
    """
    assert multiply() == 0

def test_three_parameters():
    """
    Given values 1, 2 and 3, the result should be 6
    """
    assert multiply(1, 2, 3) == 6

def test_negative_values():
    """
    Multiply negative numbers together
    """
    assert multiply(-5, -4) == 20

def test_one_negative_value():
    """
    Multiply where only one value is negative
    """
    assert multiply(5, -5) == -25

def test_decimal_values():
    """
    Mulitply using decimal values
    """
    assert multiply(100, .1) == 10
