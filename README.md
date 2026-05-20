# OMNIABASE

**Representation invariance foundation.**

OMNIABASE is the representation layer of the MB-X.01 / OMNIA ecosystem.

Its role is narrow:

    representation -> base shift -> observation -> invariant residue

It asks one question:

    what remains stable when the representation changes?

OMNIABASE is not the ecosystem landing page.

It is not the validation showroom.

It is not the core OMNIA measurement engine.

It is the foundation for observing representation-dependence before stronger structural measurement.

Canonical boundary:

    measurement != inference != decision

---

## Start here

From a clean environment:

    git clone https://github.com/Tuttotorna/OMNIABASE.git
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

## Related repositories

| Repository | Role |
|---|---|
| [lon-mirror](https://github.com/Tuttotorna/lon-mirror) | Canonical ecosystem entry point |
| [OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION) | Public validation showroom |
| [OMNIA](https://github.com/Tuttotorna/OMNIA) | Core structural measurement engine |
| [OMNIA-RADAR](https://github.com/Tuttotorna/OMNIA-RADAR) | Structural signal detection layer |
| [OMNIA-INVARIANCE](https://github.com/Tuttotorna/OMNIA-INVARIANCE) | Transformation and invariance layer |
| [omnia-limit](https://github.com/Tuttotorna/omnia-limit) | Stop / continue boundary layer |
| [OMNIA-CONSTANT](https://github.com/Tuttotorna/OMNIA-CONSTANT) | Stable-region falsification layer |

---

## Ecosystem entry point

For the full ecosystem map, start here:

    https://github.com/Tuttotorna/lon-mirror

For public validation artifacts, start here:

    https://github.com/Tuttotorna/OMNIA-VALIDATION

For core structural measurement, start here:

    https://github.com/Tuttotorna/OMNIA

---

## License

MIT.

