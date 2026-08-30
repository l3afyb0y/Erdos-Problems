#!/usr/bin/env python3
# pylint: disable=invalid-name  # Verifier filenames begin with their problem ID.
"""Exact checks for the offset and prefix lemmas in Erdős problem 261.

For a finite set D of positive offsets, define

    S = sum(1 / 2**d for d in D)
    T = sum(d / 2**d for d in D).

Then D represents the target n precisely when n = T / (1-S) is a positive
integer.  The checks below use Fraction throughout; no floating-point evidence
is used.  They verify the known consecutive-block construction and exhaustively
test the prefix transformation on every representable subset of {1, ..., 12}.
"""

from fractions import Fraction
from itertools import combinations


def parameters(offsets: tuple[int, ...]) -> tuple[Fraction, Fraction]:
    """Return S and T for a strictly increasing tuple of positive offsets."""
    assert offsets == tuple(sorted(set(offsets)))
    assert offsets and offsets[0] > 0
    s = sum((Fraction(1, 2**d) for d in offsets), Fraction())
    t = sum((Fraction(d, 2**d) for d in offsets), Fraction())
    return s, t


def represented_target(offsets: tuple[int, ...]) -> int | None:
    """Return the represented positive integer, or None when there is none."""
    s, t = parameters(offsets)
    if s >= 1:
        return None
    target = t / (1 - s)
    if target.denominator != 1 or target <= 0:
        return None
    return target.numerator


def multiplicative_order_of_two(odd_modulus: int) -> int:
    """Return the least positive h with 2**h = 1 modulo an odd modulus."""
    assert odd_modulus > 0 and odd_modulus % 2 == 1
    if odd_modulus == 1:
        return 1
    residue = 2 % odd_modulus
    order = 1
    while residue != 1:
        residue = (2 * residue) % odd_modulus
        order += 1
    return order


def prefix(offsets: tuple[int, ...], length: int) -> tuple[int, ...]:
    """Prepend offsets 1..length and shift the old offsets past the prefix."""
    assert length > 0
    return tuple(range(1, length + 1)) + tuple(length + d for d in offsets)


def predicted_prefixed_target(offsets: tuple[int, ...], length: int) -> int:
    """Return n-length+(2**(length+1)-2)/(1-S), which must be integral."""
    target = represented_target(offsets)
    assert target is not None
    s, _ = parameters(offsets)
    predicted = target - length + Fraction(2 ** (length + 1) - 2, 1 - s)
    assert predicted.denominator == 1
    return predicted.numerator


def check_consecutive_family() -> None:
    """Verify the known full-prefix construction for several exact lengths."""
    for length in range(2, 21):
        offsets = tuple(range(1, length + 1))
        expected = 2 ** (length + 1) - length - 2
        assert represented_target(offsets) == expected


def check_prefix_lemma() -> int:
    """Exhaustively check two valid prefix lengths for every small seed."""
    checked = 0
    universe = range(1, 13)
    for size in range(2, 13):
        for offsets in combinations(universe, size):
            target = represented_target(offsets)
            if target is None:
                continue
            s, _ = parameters(offsets)
            deficit = 1 - s
            assert deficit.numerator % 2 == 1
            base_length = multiplicative_order_of_two(deficit.numerator)
            for length in (base_length, 2 * base_length):
                lifted = prefix(offsets, length)
                predicted = predicted_prefixed_target(offsets, length)
                assert represented_target(lifted) == predicted
                checked += 1
    return checked


def check_nonconsecutive_example() -> None:
    """Verify the explicit lift from target 2 to target 220."""
    offsets = (2, 3, 4)
    assert represented_target(offsets) == 2
    lifted = prefix(offsets, 6)
    assert lifted == (1, 2, 3, 4, 5, 6, 8, 9, 10)
    assert predicted_prefixed_target(offsets, 6) == 220
    assert represented_target(lifted) == 220


def check_target_one_boundary() -> None:
    """Verify the separate non-greedy witness for target 1."""
    # Absolute indices (3, 6, 8) become offsets (2, 5, 7) from target 1.
    assert represented_target((2, 5, 7)) == 1


def main() -> None:
    """Run every exact arithmetic check and print the checked domains."""
    check_consecutive_family()
    checked = check_prefix_lemma()
    check_nonconsecutive_example()
    check_target_one_boundary()
    print("consecutive_family_lengths=2..20")
    print(f"exact_prefix_instances_checked={checked}")
    print("nonconsecutive_seed_target=2 prefix_length=6 lifted_target=220")
    print("boundary_target_1_absolute_indices=3,6,8")
    print("result=all_exact_fraction_checks_passed")


if __name__ == "__main__":
    main()
