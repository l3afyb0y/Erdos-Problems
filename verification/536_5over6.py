#!/usr/bin/env python3
"""Exact finite checks for the candidate Erdős #536 bound."""

import itertools
import math


def is_lcm_triangle(a, b, c):
    L = math.lcm(a, b)
    return L == math.lcm(a, c) == math.lcm(b, c)


def theorem_bound(N):
    return N - N // 6


def exact_f_bruteforce(N):
    triples = [
        sum(1 << (x - 1) for x in tri)
        for tri in itertools.combinations(range(1, N + 1), 3)
        if is_lcm_triangle(*tri)
    ]
    best = 0
    for mask in range(1 << N):
        bits = mask.bit_count()
        if bits <= best:
            continue
        if all((mask & t) != t for t in triples):
            best = bits
    return best


def check_fiber_corner(limit=200):
    for r in range(1, limit + 1):
        if math.gcd(r, 6) != 1:
            continue
        for i in range(1, 8):
            for j in range(1, 6):
                c = r * (2 ** i) * (3 ** j)
                if c > 100000:
                    continue
                a = r * (2 ** (i - 1)) * (3 ** j)
                b = r * (2 ** i) * (3 ** (j - 1))
                assert is_lcm_triangle(a, b, c)


def main():
    check_fiber_corner()
    exact = {}
    for N in range(1, 13):
        f = exact_f_bruteforce(N)
        exact[N] = f
        assert f <= theorem_bound(N), (N, f, theorem_bound(N))
    print("PASS: corner triples and exhaustive N<=12 checks")
    print("exact f(N):", exact)
    print("candidate bound:", {N: theorem_bound(N) for N in range(1, 13)})


if __name__ == "__main__":
    main()
