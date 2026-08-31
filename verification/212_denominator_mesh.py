#!/usr/bin/env python3
"""Finite sanity checks for the denominator-mesh lemma in problem #212.

This does NOT prove the asymptotic theorem.  It checks the exact
factorisation mechanism on the 3-4-5 reference triangle
A=(0,0), B=(3,0), C=(0,4).

For a mesh point P=(3m/D,4n/D), rational distance to A implies
M^2 = 9m^2 + 16n^2 for M = D*|AP|.  Hence
(M-3m)(M+3m)=16n^2.  The script exhaustively checks bounded m,n,D,
including the n=0 row using distance to C instead of A.
"""

from math import isqrt


def tau(n: int) -> int:
    n = abs(n)
    if n == 0:
        raise ValueError("tau(0) is undefined")
    ans = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            ans += 1 if d * d == n else 2
        d += 1
    return ans


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def check(max_D: int = 40, box_radius: int = 8) -> None:
    for D in range(1, max_D + 1):
        Mmax = box_radius * D
        for n in range(-box_radius * D, box_radius * D + 1):
            if n != 0:
                sols = [m for m in range(-Mmax, Mmax + 1)
                        if is_square(9 * m * m + 16 * n * n)]
                # Crude signed factor-pair bound used in the write-up.
                assert len(sols) <= 2 * tau(16 * n * n), (D, n, sols)
                for m in sols:
                    M = isqrt(9 * m * m + 16 * n * n)
                    assert (M - 3 * m) * (M + 3 * m) == 16 * n * n
            else:
                # Use C=(0,4).  D*|CP| has square 9m^2 + 16D^2.
                sols = [m for m in range(-Mmax, Mmax + 1)
                        if is_square(9 * m * m + 16 * D * D)]
                assert len(sols) <= 2 * tau(16 * D * D), (D, n, sols)
                for m in sols:
                    M = isqrt(9 * m * m + 16 * D * D)
                    assert (M - 3 * m) * (M + 3 * m) == 16 * D * D

    print(f"PASS: D<= {max_D}, |m|,|n| <= {box_radius}D")


if __name__ == "__main__":
    check()
