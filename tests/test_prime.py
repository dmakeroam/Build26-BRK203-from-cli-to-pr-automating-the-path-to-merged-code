import random
import math

from src.prime import is_prime


def is_prime_naive(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def test_edge_cases():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(-7) is False


def test_small_primes_and_composites():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
    for p in primes:
        assert is_prime(p) is True
    for c in composites:
        assert is_prime(c) is False


def test_random_samples():
    random.seed(0)
    for _ in range(200):
        n = random.randint(0, 10000)
        assert is_prime(n) == is_prime_naive(n)


def test_moderate_primes():
    # A few moderate primes to ensure algorithm scales a bit
    moderately_large_primes = [10007, 10009, 49999]
    for p in moderately_large_primes:
        assert is_prime(p) is True
