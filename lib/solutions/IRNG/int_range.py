# noinspection PyUnusedLocal
def generate(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Both start and end must be integers.")
    if start > end:
        raise ValueError("Start must be less than or equal to end.")

    return list(range(start, end + 1))
