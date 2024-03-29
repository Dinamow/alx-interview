#!/usr/bin/python3
"""this is file module contains minOperations function"""


def minOperations(n):
    """
    minOperations function that calculates the min
    number of operations needed to reach n numbere
    of chars
    Args:
        n: number of characters, int
    Return:
        result: number of operations needed, int
    """

    if n <= 1:
        return 0

    result = 0
    i = 2
    while i <= n:
        if n % i == 0:
            result += i
            n /= i
            i -= 1
        i += 1
    return int(result)
