# OMNIABASE Formalism

## Integer representation in base b

For an integer `n`, its representation in base `b` is:

```text
n = sum_{i=0}^{k} d_i^(b) * b^i
```

with:

```text
b >= 2
d_i^(b) in {0, ..., b-1}
```

## Multi-base observation

The observation of `n` across all admissible bases is:

```text
O(n) = { d^(b)(n) | b >= 2 }
```

where `d^(b)(n)` is the digit sequence of `n` in base `b`.

## Base-invariant property

A property `P` is base-invariant iff:

```text
for all b >= 2:
  P(d^(b)(n)) = constant
```

## Interpretation

A property visible only in one base may be a representation artifact.

A property stable across multiple bases has stronger structural status.

This does not automatically make it semantic truth.

It makes it structural evidence under representation change.

## Minimal rule

```text
single representation = one view
multi-base observation = controlled variation of view
invariance across views = stronger structural signal
```
