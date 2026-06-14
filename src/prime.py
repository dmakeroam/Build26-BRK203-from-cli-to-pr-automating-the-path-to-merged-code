"""Prime checking utilities.

Provides a small, dependency-free is_prime(n: int) -> bool function using
an efficient deterministic algorithm for typical integers (trial division
with 6k ± 1 optimization).

Examples:
>>> is_prime(7)
True
>>> is_prime(1)
False
>>> is_prime(2)
True
"""
from __future__ import annotations

__all__ = ["is_prime"]


def is_prime(n: int) -> bool:
    """Return True if n is prime, otherwise False.

    Args:
        n: Integer to test for primality.

    Raises:
        TypeError: If n is not an int.

    Notes:
        Uses simple deterministic trial division up to sqrt(n) with the
        6k±1 optimization. This is fast for typical 64-bit integers and
        keeps the implementation small and dependency-free.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    # Check potential factors of the form 6k-1 and 6k+1
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


if __name__ == "__main__":
    # Simple interactive demo when run directly
    import sys

    if len(sys.argv) > 1:
        try:
            val = int(sys.argv[1])
        except ValueError:
            print("Please provide an integer.")
            sys.exit(2)
        print("prime" if is_prime(val) else "composite")
    else:
        print("Usage: python -m src.prime <integer>")
