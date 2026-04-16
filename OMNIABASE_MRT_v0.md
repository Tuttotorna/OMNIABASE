# OMNIABASE MRT v0 — Minimal Reality Test

## Status

This document defines the **Minimal Reality Test** for OMNIABASE.

Its purpose is not to prove the whole framework at once.

Its purpose is narrower:

to test whether a multirepresentational reading produces a **real structural gain** over a single-view baseline on a fixed phenomenon.

If no gain appears, OMNIABASE has no operational advantage in that case.

If a gain appears and is verifiable, OMNIABASE becomes real at that point.

---

## 1. Purpose

OMNIABASE becomes real only if, for the same phenomenon:

- the single-view reading gives one result
- the multirepresentational reading gives a stronger structural result
- the difference is explicit and verifiable

The Minimal Reality Test exists to measure exactly that.

This is not a philosophy test.

It is a gain test.

---

## 2. Allowed Outcomes

Every MRT must end in exactly one of the following outcomes:

### NO_GAIN
The multirepresentational reading adds no structural advantage over the baseline.

### EARLY_GAIN
The multirepresentational reading detects a structural transition, instability, or regime change earlier than the baseline.

### HIDDEN_SEPARATION
The multirepresentational reading separates structures that the baseline compresses into the same visible picture.

### RECOVERED_INVARIANT
The multirepresentational reading identifies a structure that remains stable across recodings and is not guaranteed by the single-view baseline alone.

No other outcome is valid in MRT v0.

---

## 3. Fixed Structure of the Test

Each MRT must contain exactly five fields:

1. **Phenomenon**
2. **Representation Set**
3. **Structural Signature**
4. **Gain Test**
5. **Verification Rule**

This structure is mandatory.

---

## 4. Field 1 — Phenomenon

Define one and only one phenomenon.

The phenomenon must be:

- fixed
- stable enough to be re-encoded
- already readable in a standard baseline representation

### Required format

- `name`
- `domain`
- `single_view_baseline`

### Example

- `name: logistic_map_regime_transition`
- `domain: dynamical_system`
- `single_view_baseline: bifurcation plot`

### Rule

The test is invalid if the object changes across representations.

OMNIABASE tests the same phenomenon across multiple views.
It does not compare different phenomena.

---

## 5. Field 2 — Representation Set

Define a closed set of admissible representations.

This set must be fixed before the test.

### Required format

- `R0 = baseline representation`
- `R1...Rn = controlled recodings`

### Allowed representation types in MRT v0

- numerical base change
- discretization change
- scale change
- temporal windowing
- coordinate simplification or derivation
- symbolic encoding

### Rule

Representations must preserve the phenomenon.

They may change how it is seen.
They must not change what it is.

---

## 6. Field 3 — Structural Signature

For each representation, extract a non-semantic structural signature.

### Required format

`S(Ri) = {s1, s2, ..., sk}`

### Allowed initial signature families

- dispersion
- span
- repetition
- transition diversity
- transition instability
- local stability
- window-to-window variation

### Rule

Each signature must satisfy all of the following:

- non-semantic
- simple
- reproducible
- explainable in one line
- comparable across representations

If the signature is opaque, the MRT loses force.

---

## 7. Field 4 — Gain Test

This field determines whether OMNIABASE adds real value beyond the baseline.

### Required format

- `baseline_result`
- `multirep_result`
- `gain_type`

Where `gain_type` must be one of:

- `NO_GAIN`
- `EARLY_GAIN`
- `HIDDEN_SEPARATION`
- `RECOVERED_INVARIANT`

### Interpretation

#### NO_GAIN
The multirepresentational reading does not outperform the baseline.

#### EARLY_GAIN
The multirepresentational reading reveals a structural shift earlier than the baseline.

#### HIDDEN_SEPARATION
The multirepresentational reading distinguishes structures merged by the baseline.

#### RECOVERED_INVARIANT
The multirepresentational reading isolates a stable structure that survives across recodings.

### Rule

If none of these four applies, OMNIABASE has no demonstrated operational gain in that case.

---

## 8. Field 5 — Verification Rule

The gain must be checkable.

This field defines how the difference between baseline and multirepresentational reading is verified.

### Required format

- `difference_type`
- `verification_criterion`
- `verification_status`

### Example difference types

- earlier regime detection
- stronger separation
- invariant recovered
- no measurable gain

### Rule

The verification rule must answer one question clearly:

**In what exact sense did the multirepresentational reading outperform, refine, or fail against the baseline?**

Without this, the result is not operational.

---

## 9. Canonical MRT Output Format

Every MRT must close with the following compact summary:

- `phenomenon`
- `baseline`
- `multirep_finding`
- `gain_type`
- `verification_status`

This is the minimum valid output.

---

## 10. Validity Conditions

An MRT is valid only if all of the following hold:

- the phenomenon is fixed
- the representation set is declared in advance
- the structural signatures are reproducible
- the gain type is one of the four allowed outcomes
- the verification rule is explicit

If one of these conditions fails, the MRT is invalid.

---

## 11. Failure Modes

The MRT fails when one of these occurs:

- the representations change the phenomenon instead of re-encoding it
- the signatures are too opaque to inspect
- the gain is claimed but not verified
- the result is only rhetorical
- the multirepresentational reading does not outperform the baseline in any explicit way

In those cases, the result must be classified as:

`NO_GAIN` or `INVALID_TEST`

---

## 12. First Recommended Test Case

The first recommended canonical case for MRT v0 is:

- `name: logistic_map_regime_transition`
- `domain: dynamical_system`
- `baseline: bifurcation plot`

Why this case:

- the baseline is classical and clear
- the phenomenon is fixed
- recoding is easy
- signatures are simple to define
- gain can be tested without semantic ambiguity

This makes it the best initial reality test for OMNIABASE.

---

## 13. Summary Formula

OMNIABASE becomes real in a case only if:

- one phenomenon is fixed
- multiple representations are applied
- structural signatures are extracted
- the multirepresentational reading yields one of four valid gains
- the gain is verified against the baseline

This is the purpose of MRT v0.

It is not a theory of everything.

It is the smallest acceptable test of operational reality.