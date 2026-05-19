# OMNIABASE

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19657833.svg)](https://doi.org/10.5281/zenodo.19657833)

**OMNIABASE** is the multi-base representation and structural observation layer of the MB-X.01 / OMNIA ecosystem.

Its central point is simple:

```text
base 10 is a representation habit, not a law of number
```

OMNIABASE studies what remains structurally stable when numbers, objects, or signals are observed across multiple representations.

It is not a numerology system.
It is not a truth oracle.
It is not a semantic judge.
It is not a decision engine.

Its role is representation-aware structural observation.

Core boundary:

```text
measurement != inference != decision
```

Core thesis:

```text
Structural truth = invariance under transformation
```

Decision remains external.

---

- [`docs/OMNIABASE_PUBLIC_POSITION.md`](docs/OMNIABASE_PUBLIC_POSITION.md)

## Public position

OMNIABASE public positioning is documented here:

- [`docs/OMNIABASE_PUBLIC_POSITION.md`](docs/OMNIABASE_PUBLIC_POSITION.md)

Core thesis:

```text
A number is not identical to its written representation.
```

Core question:

```text
What remains invariant when the same number is observed across many bases?
```

Core mathematical frame:

```text
n = sum_{i=0}^{k} d_i^(b) * b^i

O(n) = { (b, digits^(b)(n)) | b >= 2 }

P is base-invariant iff:
for all b >= 2:
  P(digits^(b)(n)) = constant
```

Core boundary:

```text
representation != number
observation != essence
measurement != inference != decision
```

OMNIABASE does not claim that base 10 is wrong.

It treats base 10 as one observer frame among many.

It measures what remains structurally stable across numerical representations.

---

## Core idea

A number is not exhausted by how humans usually write it.

Humans normally see numbers in base 10.

But base 10 is only one representation.

OMNIABASE asks what changes, what remains, and what becomes visible when the same object is observed across many bases.

The purpose is not to replace arithmetic.

The purpose is to separate the number from the representation used to view it.

---

## Minimal formalism

For an integer `n`, its representation in base `b` is:

```text
n = sum_{i=0}^{k} d_i^(b) * b^i

where:
  b >= 2
  d_i^(b) in {0, ..., b-1}
```

The multi-base observation of `n` is:

```text
O(n) = { d^(b)(n) | b >= 2 }
```

A property `P` is base-invariant iff:

```text
for all b >= 2:
  P(d^(b)(n)) = constant
```

This is the base layer of OMNIABASE.

Detailed formalism:

- [`docs/FORMALISM.md`](docs/FORMALISM.md)

---

## What OMNIABASE measures

OMNIABASE studies representation-dependent and representation-resistant structure.

It can ask:

- which patterns appear only in one base
- which patterns survive across many bases
- which structures are artifacts of notation
- which structures are stable under recoding
- which observations depend on a privileged representation
- which properties remain invariant under transformation

The output is structural evidence, not final truth.

---

## What OMNIABASE is not

OMNIABASE does not:

- prove mystical properties of numbers
- claim base 10 is wrong
- claim all representations are equally useful
- replace standard arithmetic
- replace mathematical proof
- infer semantic meaning
- make final decisions

It treats base choice as an observation lens.

---

## Why this matters

A pattern may look important in one representation and disappear in another.

A structure may look accidental in one base and become stable across several bases.

If a property survives representation changes, it has stronger structural status than a property visible only through one privileged notation.

This is the operational reason for multi-base observation.

---

## Repository type

This repository is currently a conceptual, demonstration, and documentation repository.

It contains foundation documents, public demonstrations, and a minimal example script.

It is not a full Python package with a dedicated source module.

The `pyproject.toml` exists for metadata and editable installation compatibility.

---

## Repository structure

```text
README.md                              public entrypoint
FOUNDATIONS.md                         foundational notes
ARCHITECTURE.md                        architecture notes
LEXICON.md                             terminology
OMNIABASE_MRT_v0.md                    multirepresentational test note
OMNIABASE_MRT_v0_CASE_01.md            example case
docs/                                  public demonstrations and proof notes
examples/                              minimal demo material
```

---

## Public entrypoints

- [`docs/OMNIABASE_SCOPE.md`](docs/OMNIABASE_SCOPE.md)
- [`docs/FORMALISM.md`](docs/FORMALISM.md)
- [`docs/REPOSITORY_STATUS.md`](docs/REPOSITORY_STATUS.md)
- [`docs/OMNIABASE_PUBLIC_DEMONSTRATION.md`](docs/OMNIABASE_PUBLIC_DEMONSTRATION.md)
- [`docs/FIRST_PUBLIC_DEMONSTRATION.md`](docs/FIRST_PUBLIC_DEMONSTRATION.md)

---

## Relationship to OMNIA

OMNIABASE is the representation layer.

OMNIA is the structural measurement layer.

OMNIA-INVARIANCE tests invariance and trajectory behavior.

OMNIA-VALIDATION records evidence and reproducibility.

```text
OMNIABASE        = representation / multi-base observation
OMNIA            = structural measurement
OMNIA-INVARIANCE = invariance / trajectory-space analysis
OMNIA-VALIDATION = evidence / reproducibility
Decision          = external layer
```

The separation remains strict:

```text
measurement != inference != decision
```

---

## Related repositories

- lon-mirror: https://github.com/Tuttotorna/lon-mirror
- OMNIA: https://github.com/Tuttotorna/OMNIA
- OMNIA-INVARIANCE: https://github.com/Tuttotorna/OMNIA-INVARIANCE
- OMNIA-VALIDATION: https://github.com/Tuttotorna/OMNIA-VALIDATION
- omnia-limit: https://github.com/Tuttotorna/omnia-limit
- OMNIAMIND: https://github.com/Tuttotorna/OMNIAMIND

---

## Citation

If you reference this repository, use the archived Zenodo record:

```text
DOI: 10.5281/zenodo.19657833
https://doi.org/10.5281/zenodo.19657833
```

Earlier archive record:

```text
10.5281/zenodo.19603445
```

Citation metadata is available in:

- [`CITATION.cff`](CITATION.cff)

---

## Summary

OMNIABASE is a representation-aware structural observation framework.

It studies what survives when observation changes.

Its central rule is:

```text
base 10 is a representation habit, not a law of number
Structural truth = invariance under transformation
measurement != inference != decision
```
