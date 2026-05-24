<!-- OMNIABASE_AUDITOR_TOP_START -->

# OMNIABASE

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20366410.svg)](https://doi.org/10.5281/zenodo.20366410)

## Concrete entrypoint: Omniabase Auditor

This repository now has a direct operational tool:

    python -m omniabase_auditor.cli --start 1 --end 1000 --bases 2:36 --out-dir report

It solves a concrete problem:

    given a number or a range of numbers,
    observe each number across many bases,
    measure what remains stable and what changes,
    produce JSON/CSV/HTML reports,
    and optionally fail CI when base-fragile numbers are detected.

In short:

    number -> many-base observation -> invariance report

## What problem does it solve?

Humans usually observe numbers through one privileged representation, often base 10.

OMNIABASE turns this into a reproducible measurement problem:

    What changes when the same number is observed across multiple bases?
    Which digit-derived properties remain stable?
    Which numbers are base-fragile?
    Which numbers are unusually invariant?
    Which numbers become structural hubs across base observations?

The rest of this repository explains the theory and research path.

The auditor is the practical entrypoint.

## Install

Clone the repository:

    git clone https://github.com/Tuttotorna/OMNIABASE.git
    cd OMNIABASE

Install locally:

    pip install -e .

The auditor only uses the Python standard library.

## Run

Audit a range:

    python -m omniabase_auditor.cli --start 1 --end 1000 --bases 2:36 --out-dir report

Audit one number:

    python -m omniabase_auditor.cli --number 255 --bases 2:36 --out-dir report_255

Audit numbers from CSV:

    python -m omniabase_auditor.cli --input examples/sample_numbers.csv --bases 2:36 --out-dir report_csv

## Input

The auditor accepts three input modes.

Single number:

    --number 255

Range:

    --start 1 --end 1000

CSV file:

    number
    7
    31
    255

Base range:

    --bases 2:36

Explicit bases:

    --bases 2,3,5,8,10,16,36

## Output

The auditor writes:

    report.json
    report.csv
    report.html
    fragile_numbers.jsonl
    invariant_numbers.jsonl
    certificate.json

Meaning:

    report.json
    Full structured many-base audit.

    report.csv
    Spreadsheet-friendly per-number summary.

    report.html
    Human-readable inspection report.

    fragile_numbers.jsonl
    One JSON object per base-fragile number.

    invariant_numbers.jsonl
    One JSON object per highly invariant number.

    certificate.json
    Reproducibility certificate with parameters and aggregate metrics.

## CI gate

The auditor can fail automatically when base-fragile numbers are detected:

    python -m omniabase_auditor.cli --start 1 --end 1000 --bases 2:36 --out-dir report --fail-on-fragile

Exit codes:

    0 = audit completed, no blocking condition
    2 = base-fragile numbers detected
    3 = invalid input or measurement boundary crossed

## What this is not

This is not a proof system.

It does not claim that base 10 is wrong.

It does not replace arithmetic.

It provides one concrete, reproducible operation:

    observe numbers across bases
    measure representation-dependent variation
    report invariance and fragility
    optionally fail CI

## Why the rest of the repository still matters

The rest of the repository documents the OMNIABASE idea:

    base-invariance
    representation shift
    multi-base observation
    non-privileged numerical representation
    observer decentering in arithmetic notation

The code above is the entrypoint.

The repository below is the derivation path.

<!-- OMNIABASE_AUDITOR_TOP_END -->

---

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

Zenodo DOI badge for this repository.

Repository: Tuttotorna/OMNIABASE
GitHub repository id: 1211833450
Release tag: v2026.05.21
Latest release DOI: 10.5281/zenodo.20322682

<!-- ZENODO DOI:END -->


## DOI

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

<!-- OMNIA_ECOSYSTEM_BOUNDARY_V1 -->

## Ecosystem Boundary

```text
measurement != inference != decision
```

This repository is part of the MB-X.01 / OMNIA ecosystem. Its outputs must be read as structural measurement, validation, detection, orchestration or adapter artifacts according to the repository role. They are not autonomous semantic truth claims and they do not make external decisions.
