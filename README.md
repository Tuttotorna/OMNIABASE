<!-- MB-X.01 LON RELEASE:START -->

## MB-X.01 / L.O.N. release state

Repository: Tuttotorna/OMNIABASE
Release tag: v2026.05.21
Release commit: 31a1380
Release DOI: 10.5281/zenodo.20322682

Boundary:

measurement != validation
validation != orchestration
orchestration != decision
decision != measurement

<!-- MB-X.01 LON RELEASE:END -->

# OMNIABASE

<!-- ZENODO DOI:START -->

## DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281%2Fzenodo.20322682.svg)](https://doi.org/10.5281/zenodo.20322682)

Zenodo DOI badge for this repository.

Repository: Tuttotorna/OMNIABASE
GitHub repository id: 1211833450
Release tag: v2026.05.21
Latest release DOI: 10.5281/zenodo.20322682

<!-- ZENODO DOI:END -->


## DOI

[![DOI](https://zenodo.org/badge/1211833450.svg)](https://zenodo.org/badge/latestdoi/1211833450)

Release DOI: [10.5281/zenodo.19657833](https://doi.org/10.5281/zenodo.19657833)

GitHub release: [OMNIABASE v1.0.0 release](https://github.com/Tuttotorna/OMNIABASE/releases/tag/v1.0.0)

## Start here

From a clean environment:

    git clone [OMNIABASE.git](https://github.com/Tuttotorna/OMNIABASE.git)
    cd OMNIABASE
    python -m pip install -e .
    pytest

If example scripts are available, run the smallest demonstration after tests pass.

The goal is to see the representation path:

    object -> representation -> base shift -> observation -> invariant residue

---

## What OMNIABASE does

OMNIABASE observes objects through multiple representations.

For numeric structures, this means refusing to privilege base 10 as the only observational frame.

The public idea is simple:

    the symbol is not the number
    the representation is not the object
    what survives representation shift is structurally more interesting

---

## What OMNIABASE does not do

OMNIABASE does not:

- claim base 10 is special;
- infer semantic truth;
- decide correctness;
- replace OMNIA;
- replace OMNIA-VALIDATION;
- prove metaphysical truth;
- convert representation-stability into final decision.

OMNIABASE observes representation behavior.

Interpretation and decision remain external.

---

## Public mental model

    A number is not how humans write it.
    A structure is not one representation.
    OMNIABASE looks across representations and asks what remains.

---

## Minimal formal base idea

For an integer n, a base-b representation can be written as:

    n = sum_i d_i^(b) * b^i

where:

    b >= 2
    0 <= d_i^(b) < b

The multi-base observation family is:

    O(n) = { representation of n in base b | b >= 2 }

A property P is base-invariant when:

    P(representation_b(n)) is stable across b

This does not mean P is truth.

It means P survived the declared representation shift.

---

## OMNIABASE contract

Every serious OMNIABASE observation should make clear:

| Component | Meaning |
|---|---|
| object | What is being observed |
| representation | Which representational frame is used |
| base shift | What representation change is applied |
| observation | What property, feature, or trace is extracted |
| invariant residue | What remains stable across representations |
| boundary | What the observation does and does not claim |

---

## Recommended reading order

1. [docs/QUICKSTART_OMNIABASE.md](docs/QUICKSTART_OMNIABASE.md)
2. [docs/REPRESENTATION_OVERVIEW.md](docs/REPRESENTATION_OVERVIEW.md)
3. [docs/BASE_INVARIANCE.md](docs/BASE_INVARIANCE.md)
4. [docs/OBSERVATION_CONTRACT.md](docs/OBSERVATION_CONTRACT.md)
5. [docs/BOUNDARY.md](docs/BOUNDARY.md)
6. [docs/OMNIABASE_MANIFEST.json](docs/OMNIABASE_MANIFEST.json)

---

## Ecosystem entry point

For the full ecosystem map, start here:

[lon-mirror](https://github.com/Tuttotorna/lon-mirror)

For public validation artifacts, start here:

[OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION)

For core structural measurement, start here:

[OMNIA](https://github.com/Tuttotorna/OMNIA)

---


## Boundary terms

    base 10 is a representation habit, not a law of number
    Structural truth = invariance under transformation


## Smoke-test required terms

    not a truth oracle
    Decision remains external

## Related repositories

| Repository | Role |
|---|---|
| [lon-mirror](https://github.com/Tuttotorna/lon-mirror) | Canonical public entry point |
| [OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION) | Public validation showroom |
| [OMNIA](https://github.com/Tuttotorna/OMNIA) | Core structural measurement engine |
| [OMNIABASE](https://github.com/Tuttotorna/OMNIABASE) | Representation invariance foundation |
| [omnia-limit](https://github.com/Tuttotorna/omnia-limit) | Stop / continue boundary layer |
| [OMNIA-RADAR](https://github.com/Tuttotorna/OMNIA-RADAR) | Structural signal detection layer |
| [OMNIA-INVARIANCE](https://github.com/Tuttotorna/OMNIA-INVARIANCE) | Structural invariance layer |
| [OMNIA-CONSTANT](https://github.com/Tuttotorna/OMNIA-CONSTANT) | Structural constant candidate layer |
| [OMNIAMIND](https://github.com/Tuttotorna/OMNIAMIND) | Structural cognition orchestration layer |
| [OMNIA-THREE-BODY](https://github.com/Tuttotorna/OMNIA-THREE-BODY) | Dynamic divergence stress test |
| [OMNIA-SECURITY](https://github.com/Tuttotorna/OMNIA-SECURITY) | Bounded structural security diagnostics |
| [OMNIA-CRYPTO](https://github.com/Tuttotorna/OMNIA-CRYPTO) | Bounded structural crypto diagnostics |

---

## Boundary and smoke-test required terms

    measurement != inference != decision

---

## License

MIT.
