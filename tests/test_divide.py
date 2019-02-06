"""
Tests the add() function of the calculator.
"""
import pytest
import math

from calculator import divide


def test_two_divide_two():
    """
    If given 2 and 2 as parameters, return 1
    """
    assert divide(2, 2) == 1

def test_without_parameters():
    """
    Given that no parameters are provided to the function, return a nan float
    """
    pass

def test_divide_by_zero():
    """
    Test when dividing an number by zero, return a nan float
    """
    assert divide(100, 0) is math.nan

def test_decimal_result():
    """
    Test a decimal result
    """
    assert divide(25, 2) == 12.5

def test_negative_values():
    """
    Test dividing with negative values
    """
    assert divide(100, -10) == -10

def test_dividing_by_decimal():
    """
    Test dividing a number by a decimal value
    """
    assert divide(100, .25) == 400
