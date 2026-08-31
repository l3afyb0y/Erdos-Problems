#!/usr/bin/env python3
"""Finite adversarial check for the exact kernel-injection lemma in problem 208.

This does NOT verify Erdős Problem #208. It checks the exact finite inequality
recorded in problems/208.md on every maximal non-squarefree run ending below
LIMIT, for several choices of y > H/2.
"""

from math import floor, log

LIMIT = 50_000


def sieve_squarefree(limit: int):
    squarefree = [True] * (limit + 1)
    squarefree[0] = False
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    primes = []

    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            if p * p <= limit:
                for m in range(p * p, limit + 1, p):
                    is_prime[m] = False
                for m in range(p * p, limit + 1, p * p):
                    squarefree[m] = False
    return squarefree, primes


def main():
    squarefree, primes = sieve_squarefree(LIMIT)

    qprefix = [0] * (LIMIT + 1)
    for n in range(1, LIMIT + 1):
        qprefix[n] = qprefix[n - 1] + int(squarefree[n])

    def qcount(t: float) -> int:
        m = max(0, min(LIMIT, floor(t)))
        return qprefix[m]

    def check_run(X: int, H: int, y: float):
        assert y > H / 2
        assert all(not squarefree[X + i] for i in range(1, H + 1))

        small_sum = 0
        for p in primes:
            if p > y:
                break
            pp = p * p
            small_sum += (X + H) // pp - X // pp

        rhs = small_sum + qcount((X + H) / (y * y))
        assert H <= rhs, (X, H, y, small_sum, rhs)

    run_count = 0
    max_run = 0
    n = 1
    while n <= LIMIT:
        if squarefree[n]:
            n += 1
            continue

        start = n
        while n <= LIMIT and not squarefree[n]:
            n += 1
        H = n - start
        X = start - 1
        run_count += 1
        max_run = max(max_run, H)

        ys = [
            H / 2 + 0.01,
            max(float(H), H / 2 + 0.01),
            max(float(2 * H), H / 2 + 0.01),
            max(H * log(max(H, 2)), H / 2 + 0.01),
        ]
        for y in ys:
            check_run(X, H, y)

    print(
        f"PASS: checked {run_count} maximal non-squarefree runs ending <= {LIMIT}; "
        f"largest tested run length = {max_run}"
    )


if __name__ == "__main__":
    main()
