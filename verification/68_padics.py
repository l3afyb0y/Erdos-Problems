#!/usr/bin/env python3
"""Exact verifier for the p-adic obstruction recorded in problems/68.md.

Requires sympy. Scans every prime 5 <= p < LIMIT, computes n! modulo p^3,
finds the roots n! == 1 (mod p), determines their p-adic depths up to the
precision needed in this range, and evaluates the maximal-depth cancellation
sum modulo p.
"""

from sympy import primerange

LIMIT = 20_000


def obstruction_status(p: int):
    modulus = p ** 3
    fac = 1
    roots = []

    for n in range(1, p - 1):
        fac = (fac * n) % modulus
        if n < 2 or fac % p != 1:
            continue

        diff = (fac - 1) % modulus
        if diff == 0:
            # Precision would be insufficient if this happened.
            roots.append((n, 3, None))
        elif diff % (p * p) == 0:
            roots.append((n, 2, (diff // (p * p)) % p))
        else:
            roots.append((n, 1, (diff // p) % p))

    max_depth = max(depth for _, depth, _ in roots)
    if any(depth == 3 for _, depth, _ in roots):
        raise RuntimeError(f"increase p-adic precision for p={p}")

    residue = sum(
        pow(unit, -1, p)
        for _, depth, unit in roots
        if depth == max_depth
    ) % p
    return residue, roots


def main():
    cancellations = []
    total = 0

    for p in primerange(5, LIMIT):
        total += 1
        residue, roots = obstruction_status(p)
        if residue == 0:
            cancellations.append((p, [(n, e) for n, e, _ in roots]))

    print(f"primes checked: {total}")
    print(f"cancellations: {len(cancellations)}")
    for row in cancellations:
        print(row)

    assert total == 2260
    assert cancellations == [
        (139, [(69, 1), (122, 1), (137, 1)]),
        (2593, [(349, 1), (2243, 1), (2591, 1)]),
    ]
    print("PASS")


if __name__ == "__main__":
    main()
