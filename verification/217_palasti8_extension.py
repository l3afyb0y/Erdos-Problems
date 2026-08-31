#!/usr/bin/env python3
"""Exact verifier for the one-point extension obstruction in Erdős problem #217.

Coordinates are represented in the basis (u,v) -> (sqrt(3)u, v), so squared
Euclidean distance is 3(du)^2 + (dv)^2 and all arithmetic is rational.

The mathematical reduction is:
  * the Palásti 8-point configuration already has 7 distance values;
  * a 9-point crescent configuration has exactly 8 distance values;
  * hence the new point may introduce only one new distance value;
  * no four old points are concyclic, so that one new value can occur at most
    three times from the new point;
  * therefore at least five new edges use old distance values;
  * in particular, choose three such old centers. They are noncollinear, and
    subtracting their circle equations forces the new point by two rational
    linear equations.

Thus all possible one-point extensions of this fixed configuration lie in the
finite exact candidate set enumerated below.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product


P = [
    (Fraction(0), Fraction(1)),
    (Fraction(1), Fraction(0)),
    (Fraction(2), Fraction(0)),
    (Fraction(5, 2), Fraction(5, 2)),
    (Fraction(3, 2), Fraction(9, 2)),
    (Fraction(1, 2), Fraction(7, 2)),
    (Fraction(3, 2), Fraction(7, 2)),
    (Fraction(1), Fraction(2)),
]


def d2(p, q):
    """Squared Euclidean distance in the (u,v) coordinate basis."""
    du = p[0] - q[0]
    dv = p[1] - q[1]
    return 3 * du * du + dv * dv


def det(matrix):
    """Exact determinant by fraction-preserving Gaussian elimination."""
    a = [list(row) for row in matrix]
    n = len(a)
    out = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        p = a[col][col]
        out *= p
        for j in range(col, n):
            a[col][j] /= p
        for r in range(col + 1, n):
            f = a[r][col]
            if f == 0:
                continue
            for j in range(col, n):
                a[r][j] -= f * a[col][j]
    return out


def collinear(a, b, c):
    return det([[a[0], a[1], 1], [b[0], b[1], 1], [c[0], c[1], 1]]) == 0


def concyclic4(a, b, c, d):
    # Physical x = sqrt(3)u. A circle becomes
    # 3u^2 + v^2 + A u + B v + C = 0.
    rows = []
    for u, v in (a, b, c, d):
        rows.append([3 * u * u + v * v, u, v, 1])
    return det(rows) == 0


def radical_axis(i, j, s, t):
    """Return A,B,C for Au+Bv=C from two prescribed circle equations."""
    ui, vi = P[i]
    uj, vj = P[j]
    A = 6 * (uj - ui)
    B = 2 * (vj - vi)
    C = s - t + 3 * (uj * uj - ui * ui) + (vj * vj - vi * vi)
    return A, B, C


def solve2(e1, e2):
    A, B, C = e1
    D, E, F = e2
    delta = A * E - B * D
    if delta == 0:
        return None
    u = (C * E - B * F) / delta
    v = (A * F - C * D) / delta
    return u, v


def main():
    # Verify the published 8-point configuration itself.
    assert all(
        not collinear(P[i], P[j], P[k])
        for i, j, k in combinations(range(8), 3)
    )
    assert all(
        not concyclic4(P[i], P[j], P[k], P[l])
        for i, j, k, l in combinations(range(8), 4)
    )

    old = Counter(d2(P[i], P[j]) for i, j in combinations(range(8), 2))
    expected = Counter(
        {
            Fraction(1): 1,
            Fraction(19): 2,
            Fraction(21): 3,
            Fraction(3): 4,
            Fraction(4): 5,
            Fraction(7): 6,
            Fraction(13): 7,
        }
    )
    assert old == expected
    old_values = tuple(old.keys())

    # Every genuine extension has >=5 old-valued incident distances, hence is
    # captured by at least one triple of old centers with old prescribed radii.
    candidates = set()
    assignment_hits = 0
    for i, j, k in combinations(range(8), 3):
        for s, t, r in product(old_values, repeat=3):
            q = solve2(radical_axis(i, j, s, t), radical_axis(i, k, s, r))
            if q is None:
                continue
            if d2(q, P[i]) == s and d2(q, P[j]) == t and d2(q, P[k]) == r:
                assignment_hits += 1
                candidates.add(q)

    target_multiplicities = list(range(1, 9))
    at_least_five_old = []
    distinct_valid_extensions = []
    histogram_hits_including_coincidence = []

    for q in candidates:
        incident = [d2(q, p) for p in P]
        old_matches = sum(x in old for x in incident)
        if old_matches >= 5:
            at_least_five_old.append(q)

        all_counts = old.copy()
        all_counts.update(incident)
        histogram_ok = (
            len(all_counts) == 8
            and sorted(all_counts.values()) == target_multiplicities
        )
        if histogram_ok:
            histogram_hits_including_coincidence.append(q)
            if q not in P:
                distinct_valid_extensions.append(q)

    degenerate = (Fraction(3, 2), Fraction(9, 2))

    assert assignment_hits == 1163
    assert len(candidates) == 148
    assert len(at_least_five_old) == 46
    assert distinct_valid_extensions == []
    assert set(histogram_hits_including_coincidence) == {degenerate}
    assert degenerate in P
    assert d2(degenerate, degenerate) == 0

    print("old squared-distance multiplicities:", dict(sorted(old.items())))
    print("three-center/radius assignments checked:", 56 * 7**3)
    print("satisfying assignment hits:", assignment_hits)
    print("distinct exact candidates:", len(candidates))
    print(
        "candidates with >=5 old-valued incident distances:",
        len(at_least_five_old),
    )
    print("distinct valid one-point extensions:", len(distinct_valid_extensions))
    print("sole histogram hit allowing coincidence:", degenerate)


if __name__ == "__main__":
    main()
