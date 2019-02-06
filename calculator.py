"""
Calculator script
"""
import math

def add(*args):
    """
    add() Returns
    """
    return sum(args)

def subtract(*args):
    """Returns the result of subtracting values"""
    diff = args[0] - sum(args[1:])
    return diff

def multiply(*args):
    """Returns the product of the parameters passed"""
    for item in args:
        product *= item
    return product

def divide(*args):
    """Returns the result of dividing numbers passed"""
    if not args:
        return math.nan

    if len(args) == 1:
        return 1

    args = list(args)
    answer = args.pop(0)  # set the answer to the first value in args list
    for value in args:
        try:
            answer /= value
        except ZeroDivisionError:
            return math.nan
    return answer
