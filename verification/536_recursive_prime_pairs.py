#!/usr/bin/env python3
"""Exact sanity checks for the recursive prime-pair upper bound in Erdős #536.

This script does two things:
1. computes the exact finite-N recursive counting bound for any supplied sequence
   of disjoint prime pairs;
2. brute-forces the true optimum for N <= 12 and confirms it never exceeds the
   recursive bound.

No finite check proves the asymptotic theorem; the theorem is proved combinatorially
in problems/536.md. This file checks arithmetic, floor effects, and small boundary cases.
"""

from fractions import Fraction
from itertools import combinations
from math import gcd, lcm


def coprime_count(N: int, Q: int) -> int:
    return sum(gcd(n, Q) == 1 for n in range(1, N + 1))


def coprime_and_not_divisible_count(N: int, Q: int, p: int) -> int:
    return sum(gcd(n, Q) == 1 and n % p != 0 for n in range(1, N + 1))


def recursive_bound(N: int, pairs: list[tuple[int, int]]) -> int:
    """Exact finite-N bound obtained by iterating the fibre-origin recurrence."""
    Q = 1
    total = 0
    for p, q in pairs:
        assert gcd(Q, p * q) == 1
        total += coprime_and_not_divisible_count(N, Q, p)
        total += coprime_and_not_divisible_count(N, Q, q)
        total -= 2 * coprime_count(N, Q * p * q)
        Q *= p * q
    total += coprime_count(N, Q)
    return total


def asymptotic_bound(pairs: list[tuple[int, int]]) -> Fraction:
    """Return 1 - sum d_{j-1}/(p_j q_j), with d_Q = phi(Q)/Q."""
    density = Fraction(1, 1)
    saving = Fraction(0, 1)
    for p, q in pairs:
        saving += density * Fraction(1, p * q)
        density *= Fraction(p - 1, p) * Fraction(q - 1, q)
    return Fraction(1, 1) - saving


def forbidden_triples(N: int) -> list[int]:
    """Return forbidden triples encoded as bitmasks."""
    masks = []
    for a, b, c in combinations(range(1, N + 1), 3):
        if lcm(a, b) == lcm(a, c) == lcm(b, c):
            masks.append((1 << (a - 1)) | (1 << (b - 1)) | (1 << (c - 1)))
    return masks


def exact_optimum(N: int) -> int:
    """Brute-force the exact optimum. Intended only for N <= 12."""
    bad = forbidden_triples(N)
    best = 0
    for mask in range(1 << N):
        size = mask.bit_count()
        if size <= best:
            continue
        if all(mask & triple != triple for triple in bad):
            best = size
    return best


def main() -> None:
    pair_sets = [
        [(2, 3)],
        [(2, 3), (5, 7)],
        [(2, 3), (5, 7), (11, 13)],
        [(2, 3), (5, 7), (11, 13), (17, 19)],
    ]

    print("Asymptotic recursive bounds:")
    for pairs in pair_sets:
        b = asymptotic_bound(pairs)
        print(f"  {pairs}: {b} = {float(b):.12f}")

    assert asymptotic_bound(pair_sets[0]) == Fraction(5, 6)
    assert asymptotic_bound(pair_sets[1]) == Fraction(173, 210)
    assert asymptotic_bound(pair_sets[2]) == Fraction(24691, 30030)

    print("\nExact small-N checks:")
    for N in range(1, 13):
        optimum = exact_optimum(N)
        bounds = [recursive_bound(N, pairs) for pairs in pair_sets]
        assert all(optimum <= b for b in bounds)
        assert all(bounds[i + 1] <= bounds[i] for i in range(len(bounds) - 1))
        print(f"  N={N:2d}: optimum={optimum:2d}, bounds={bounds}")

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
