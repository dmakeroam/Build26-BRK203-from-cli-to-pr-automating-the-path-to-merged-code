#!/usr/bin/env python3
"""CLI wrapper for the prime checker.

Usage:
    python src/cli.py 17
    echo 17 | python src/cli.py

Exit codes:
    0 - number is prime
    1 - number is composite
    2 - invalid usage or input
"""
import sys
import argparse
from prime_checker import is_prime


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(description="Check whether a number is prime")
    parser.add_argument("n", nargs="?", help="integer to check", type=int)
    args = parser.parse_args(argv)

    if args.n is None:
        data = sys.stdin.read().strip()
        if not data:
            parser.print_help()
            return 2
        try:
            n = int(data)
        except ValueError:
            print("Invalid integer on stdin", file=sys.stderr)
            return 2
    else:
        n = args.n

    try:
        prime = is_prime(n)
    except TypeError as e:
        print(str(e), file=sys.stderr)
        return 2

    if prime:
        print(f"{n} is prime")
        return 0
    else:
        print(f"{n} is not prime")
        return 1


if __name__ == "__main__":
    rc = main()
    sys.exit(rc)
