"""Simple prime checking utilities.

Target: Python 3.10
"""
import math


def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise.

    Raises TypeError if n is not an int.

    Algorithm: simple trial division using math.isqrt and checking odd divisors.
    Time complexity: O(sqrt(n)). Suitable for small-to-moderate integers.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True
