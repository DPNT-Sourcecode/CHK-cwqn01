# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    # Check if the inputs are valid numbers
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x + y
    else:
        raise ValueError("Both inputs must be numbers (int or float).")

