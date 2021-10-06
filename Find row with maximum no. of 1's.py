def sol_1(mat: list) -> int:
    """using sum, brute force"""
    sm = [sum(i) for i in mat]
    mx = max(sm)
    return sm.index(mx) if mx else -1



def sol_2(mat: list) -> int:
    """counting zeros"""
    ans, mx, n, m = -1, 0, len(mat), len(mat[0])

    for i in range(n):
        cur = m
        for j in mat[i]:
            if j == 0: cur -= 1

        if mx < cur: ans, mx = i, cur

    return ans


def sol_3(mat: list) -> int:
    """using binary search"""
    ans, mx, n, m = -1, 0, len(mat), len(mat[0])

    for i in range(n):
        l, h = 0, m-1
        while l <= h:
            mid = l + (h - l) // 2

            if (mat[i][mid - 1] == 0 and mat[i][mid] == 1) or (mid == 0 and mat[i][mid] == 1):
                if mx < m-mid:
                    ans, mx = i, m-mid
                break
            elif mat[i][mid] == 0:
                l= mid + 1
            else:
                h = mid - 1

    return ans



def sol_4(mat: list) -> int:
    """keeping track of first one index"""
    ans, ind, n = -1, len(mat[0])-1, len(mat)

    for i in range(n):
        j = ind
        while j >= 0 and mat[i][j]:
            j -= 1

        if ind > j:
            ind = j
            ans = i

    return ans
