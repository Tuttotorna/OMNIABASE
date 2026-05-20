# Observation Contract

This document defines the public shape expected from OMNIABASE observations.

The goal is clarity.

A reviewer should understand what was observed, how representation changed, and what remained.

---

## Observation unit

An OMNIABASE observation should contain:

| Component | Required | Meaning |
|---|---:|---|
| object_id | yes | Stable identifier for the observed object |
| object | yes | The thing being observed |
| representation | yes | Current representation or base |
| representation_shift | yes | Declared transformation or base shift |
| observed_feature | yes | Property, trace, or feature extracted |
| invariant_residue | preferred | What remains stable across representations |
| result | yes | observed, stable, unstable, inconclusive |
| boundary | yes | What the observation does and does not claim |
| limitation | yes | What the result does not prove |

---

## Minimal JSON shape

A minimal observation artifact can use this shape:

    {{
      "object_id": "example-001",
      "object": "integer-or-structure",
      "representations": ["base-2", "base-3", "base-10"],
      "observed_feature": "declared feature",
      "invariant_residue": "what remained stable",
      "result": "observed | stable | unstable | inconclusive",
      "boundary": "measurement != inference != decision",
      "limitation": "What this observation does not prove"
    }}

---

## Result vocabulary

Use a small vocabulary:

    observed
    stable
    unstable
    inconclusive

Meaning:

- observed: a property was extracted;
- stable: a property persisted across the declared representation shift;
- unstable: a property changed or collapsed;
- inconclusive: the observation is insufficient.

---

## No silent promotion

An observation must not silently become a truth claim.

Representation stability is not final meaning.

Observation remains before measurement, inference, and decision.

