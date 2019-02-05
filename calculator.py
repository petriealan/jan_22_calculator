"""
Calculator script
"""
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
    for item in args:
        result /= item
    return result
