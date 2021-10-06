def sol_1(ar: list, br: list) -> tuple:
    """using set methods """
    union = set(a + b)
    intersection = set(a).intersection(set(b))
    return (union, intersection)

