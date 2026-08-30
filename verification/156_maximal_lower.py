#!/usr/bin/env python3
"""Exact finite verification for the candidate Erdős #156 lower bound.

For every N <= 12, enumerate all subsets of [N], retain the inclusion-maximal
Sidon sets, and verify m^3 + m >= 2N.
"""

from itertools import combinations


def is_sidon(S):
    vals = sorted(S)
    seen = set()
    for i, a in enumerate(vals):
        for b in vals[i:]:
            s = a + b
            if s in seen:
                return False
            seen.add(s)
    return True


def is_maximal_sidon(S, N):
    if not is_sidon(S):
        return False
    return all(
        not is_sidon(set(S) | {x})
        for x in range(1, N + 1)
        if x not in S
    )


def main():
    for N in range(1, 13):
        count = 0
        minimum = None
        for r in range(1, N + 1):
            for C in combinations(range(1, N + 1), r):
                S = set(C)
                if is_maximal_sidon(S, N):
                    count += 1
                    minimum = r if minimum is None else min(minimum, r)
                    assert r**3 + r >= 2 * N, (N, C)
        assert count > 0
        print(f"N={N:2d} maximal_sets={count:5d} minimum_size={minimum}")
    print("PASS: all maximal Sidon sets for N<=12 satisfy m^3+m>=2N")


if __name__ == "__main__":
    main()
