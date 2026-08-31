from fractions import Fraction
from itertools import combinations, product
from math import isqrt

# Exact verification for the edge-gluing experiment in Erdős problem #213.
# Coordinates are represented as (x,y) for the actual point x + i*sqrt(D)*y.
# Thus squared Euclidean norm is x^2 + D*y^2.

D = 2002

A = [
    [0,22270,22098,16637,9248,8908,8636],
    [22270,0,21488,11397,15138,20698,13746],
    [22098,21488,0,10795,14450,13430,20066],
    [16637,11397,10795,0,7395,11135,11049],
    [9248,15138,14450,7395,0,5780,5916],
    [8908,20698,13430,11135,5780,0,10744],
    [8636,13746,20066,11049,5916,10744,0],
]

B = [
    [0,66810,66555,66294,49928,41238,40290],
    [66810,0,32385,64464,32258,25908,52020],
    [66555,32385,0,34191,16637,33147,33405],
    [66294,64464,34191,0,34322,53244,26724],
    [49928,32258,16637,34322,0,20066,20698],
    [41238,25908,33147,53244,20066,0,32232],
    [40290,52020,33405,26724,20698,32232,0],
]


def sqrt_fraction(q):
    if q < 0:
        return None
    a, b = q.numerator, q.denominator
    x, y = isqrt(a), isqrt(b)
    if x*x == a and y*y == b:
        return Fraction(x, y)
    return None


def norm(z):
    return z[0]*z[0] + D*z[1]*z[1]


def sub(z, w):
    return (z[0]-w[0], z[1]-w[1])


def mul(z, w):
    return (z[0]*w[0]-D*z[1]*w[1], z[0]*w[1]+z[1]*w[0])


def inv(z):
    n = norm(z)
    return (z[0]/n, -z[1]/n)


def div(z, w):
    return mul(z, inv(w))


def conj(z):
    return (z[0], -z[1])


def embed(M):
    """Recover one exact Q(sqrt(D)) embedding from a distance matrix."""
    L = M[0][1]
    raw = [None]*7
    raw[0] = (Fraction(0), Fraction(0))
    raw[1] = (Fraction(L), Fraction(0))
    for i in range(2, 7):
        x = Fraction(L*L + M[0][i]**2 - M[1][i]**2, 2*L)
        yy = Fraction(M[0][i]**2) - x*x
        y = sqrt_fraction(yy / D)
        assert y is not None
        raw[i] = (x, y)

    # Fix point 2 above the x-axis and determine the remaining signs exactly.
    for signs in product([1, -1], repeat=4):
        pts = raw[:]
        for idx, sign in zip(range(3, 7), signs):
            pts[idx] = (raw[idx][0], sign*raw[idx][1])
        if all(norm(sub(pts[i], pts[j])) == M[i][j]**2
               for i, j in combinations(range(7), 2)):
            return pts
    raise AssertionError("distance matrix did not embed")


P = embed(A)
Q = embed(B)


def similarity(z, q0, q1, p0, p1, reflection):
    """Map directed edge q0q1 to p0p1, with optional reflection."""
    dz = sub(z, q0)
    dq = sub(q1, q0)
    if reflection:
        dz, dq = conj(dz), conj(dq)
    factor = div(sub(p1, p0), dq)
    moved = mul(factor, dz)
    return (p0[0] + moved[0], p0[1] + moved[1])


def collinear(p, q, r):
    return ((q[0]-p[0])*(r[1]-p[1]) ==
            (q[1]-p[1])*(r[0]-p[0]))


def determinant(matrix):
    M = [row[:] for row in matrix]
    n = len(M)
    out = Fraction(1)
    for c in range(n):
        pivot = next((r for r in range(c, n) if M[r][c]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != c:
            M[c], M[pivot] = M[pivot], M[c]
            out = -out
        pv = M[c][c]
        out *= pv
        for j in range(c, n):
            M[c][j] /= pv
        for r in range(c+1, n):
            f = M[r][c]
            if f:
                for j in range(c, n):
                    M[r][j] -= f*M[c][j]
    return out


def concyclic(points):
    # The actual y-column has a common sqrt(D) factor, which can be removed.
    rows = [[p[0], p[1], norm(p), Fraction(1)] for p in points]
    return determinant(rows) == 0


def unique_points(points):
    out = []
    for p in points:
        if p not in out:
            out.append(p)
    return out


def admissible(indices, points):
    for i, j in combinations(indices, 2):
        if sqrt_fraction(norm(sub(points[i], points[j]))) is None:
            return False
    for tri in combinations(indices, 3):
        if collinear(*(points[i] for i in tri)):
            return False
    for quad in combinations(indices, 4):
        if concyclic([points[i] for i in quad]):
            return False
    return True


best = 0
best_data = None
cases = 0

for i, j in combinations(range(7), 2):
    for k, l in combinations(range(7), 2):
        for reflection in [False, True]:
            Q2 = [similarity(z, Q[k], Q[l], P[i], P[j], reflection) for z in Q]
            points = unique_points(P + Q2)
            cases += 1

            found = None
            for size in range(len(points), best, -1):
                for subset in combinations(range(len(points)), size):
                    if admissible(subset, points):
                        found = subset
                        break
                if found is not None:
                    break

            if found is not None and len(found) > best:
                best = len(found)
                best_data = (i, j, k, l, reflection, len(points), found)

print("edge alignments", cases)
print("maximum admissible union subset", best)
print("witness alignment", best_data)

assert cases == 21*21*2
assert best == 7
