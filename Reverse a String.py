def sol_1(s: list) -> list:
    """using slicing"""
    return s[::-1]


def sol_2(s: list) -> list:
    """using swapping"""
    n = len(s)
    for i in range(n//2):
        s[i], s[~i] = s[~i], s[i]
    return s


def sol_3(s: list) -> list:
    """using recursion"""
    def rec(s):
        l = len(s)
        if l < 2: return s
        return rec(s[l//2:]) + rec(s[:l//2])

    return rec(s)

