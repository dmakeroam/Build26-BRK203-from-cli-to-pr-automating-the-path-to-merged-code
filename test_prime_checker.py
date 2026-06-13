import os
import sys

# Ensure src is on sys.path so tests can import prime_checker
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from prime_checker import is_prime


def test_negative_zero_one():
    assert not is_prime(-5)
    assert not is_prime(0)
    assert not is_prime(1)


def test_small_primes():
    for p in [2, 3, 5, 7, 11, 13, 17, 19]:
        assert is_prime(p)


def test_small_composites():
    for c in [4, 6, 8, 9, 15, 21, 25]:
        assert not is_prime(c)


def test_large_prime_and_composite():
    # 104729 is the 10000th prime
    assert is_prime(104729)
    assert not is_prime(104730)


def test_type_error_for_non_int():
    try:
        is_prime(3.14)
        assert False, "TypeError not raised"
    except TypeError:
        pass
