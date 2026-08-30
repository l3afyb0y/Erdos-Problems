#!/usr/bin/env python3
"""Exact audit of the period-5040 prime fibres used in problems/203.md.

A prime q>3 has |<2,3> mod q| dividing 5040 iff q divides both
2^5040-1 and 3^5040-1.  Factoring their gcd therefore gives the complete
prime list for this bounded period.  The script also recomputes each subgroup
order and the exact reciprocal-density sum.
"""

from fractions import Fraction
from math import gcd, lcm
from sympy import factorint, n_order

L = 5040
G = gcd(pow(2, L) - 1, pow(3, L) - 1)
factors = factorint(G)
primes = sorted(q for q in factors if q > 3)

rows = []
for q in primes:
    h = lcm(int(n_order(2, q)), int(n_order(3, q)))
    assert L % h == 0
    rows.append((q, h))

density = sum((Fraction(1, h) for _, h in rows), Fraction(0, 1))

assert len(rows) == 31
assert density == Fraction(143, 140)

print("prime_count =", len(rows))
print("density_sum =", density)
print("rows =")
for q, h in rows:
    print(q, h)
