# Base Invariance

This document defines the minimal public idea behind OMNIABASE.

---

## Minimal formula

For an integer n, its representation in base b can be written as:

    n = sum_i d_i^(b) * b^i

with:

    b >= 2
    0 <= d_i^(b) < b

The observation family is:

    O(n) = {{ digits_b(n) | b >= 2 }}

A property P is base-invariant when:

    for all b >= 2, P(digits_b(n)) remains stable

---

## Meaning

A base-invariant property is not automatically semantic truth.

It is a property that survived a declared representation shift.

That distinction matters.

OMNIABASE does not say:

    this is true because it appears in many bases

It says:

    this property remained stable across the tested bases

---

## Practical use

Base-shift observation can help distinguish:

- properties of the object;
- properties of the representation;
- artifacts of base 10 habit;
- features that persist across multiple encodings.

---

## Boundary

Base invariance is evidence of structural persistence under a representation regime.

It is not:

- final proof;
- semantic truth;
- metaphysical truth;
- a downstream decision;
- a replacement for validation.

