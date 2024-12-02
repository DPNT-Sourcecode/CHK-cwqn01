# noinspection PyUnusedLocal
def compute(int_array):
    # Input validation
    if not isinstance(int_array, list):
        raise ValueError("Input must be a list of integers.")

    if not all(isinstance(x, int) for x in int_array):
        raise ValueError("All elements in the array must be integers.")

    # Compute the sum of the array
    return sum(int_array)