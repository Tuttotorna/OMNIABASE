# OMNIABASE MRT v0 — CASE 01

## Title

**Logistic Map Regime Transition**

---

## Status

This document is the first compiled case of **OMNIABASE MRT v0**.

Its purpose is not to prove the whole framework.

Its purpose is narrower:

to test whether a multirepresentational reading produces a **real structural gain** over a classical single-view baseline on a fixed phenomenon.

---

## 1. Phenomenon

### Name
`logistic_map_regime_transition`

### Domain
`dynamical_system`

### Fixed object
The phenomenon is the logistic map:

```text
x_(t+1) = r * x_t * (1 - x_t)

with:

x_t ∈ [0,1]

control parameter r

fixed update rule

fixed trajectory-generation mechanism


Single-view baseline

bifurcation plot

Baseline reading

Under the standard parameter-state plane, the system shows:

stable fixed-point regions

periodic bifurcations

chaotic regimes

windows of partial order inside broader chaotic regions


This baseline is valid.

The MRT question is not whether the baseline is wrong.

The question is whether it is structurally complete enough.


---

2. Representation Set

The phenomenon remains fixed.

Only its representation changes.

Baseline representation

R0 = standard bifurcation plot


Controlled recodings

For MRT v0, the same trajectory is recoded across:

R1 = base-2

R2 = base-3

R3 = base-4

R4 = base-5

R5 = base-6

R6 = base-7

R7 = base-8

R8 = base-9

R9 = base-10

R10 = base-12

R11 = base-16


Preserved object rule

The following do not change across representations:

the update equation

the parameter value r

the generated trajectory

the observation window

the ordering of states in time


Only the coding layer changes.

This preserves the phenomenon.


---

3. Structural Signature

For each representation Ri, define a non-semantic signature:

S(Ri) = {
  digit_sum_span,
  repetition_span,
  transition_diversity,
  local_variation
}

Signature definitions

1. digit_sum_span

How much the digit-sum profile varies inside the observed window.

Purpose: detect whether the representation amplifies or compresses structural spread.

2. repetition_span

How repetitive the encoded states become across the observed window.

Purpose: detect local regularity versus structural dispersion.

3. transition_diversity

How varied adjacent encoded transitions are.

Purpose: measure whether the trajectory behaves like:

repetitive ordered structure

mixed transition structure

high-diversity transition field


4. local_variation

How much the signature changes across nearby windows or nearby r values.

Purpose: detect local instability or structural transition.

Signature rules

These signatures are:

non-semantic

simple

reproducible

comparable across recodings

explainable without model interpretation



---

4. Gain Test

Baseline result

The bifurcation plot shows the known transition structure:

stable regions

period doubling

chaotic spread

islands of relative order


This is visually informative.

But the baseline compresses the phenomenon into one dominant visible surface.

Multirepresentational result

Across multiple bases, the same trajectory yields different structural signatures.

These signatures may reveal:

separation between regions that still look locally similar in the baseline plot

onset of instability through signature divergence before the visual bifurcation is maximally obvious

local regime differences compressed into the same visible scatter region

partial invariant behavior across some recodings and structural break across others


Gain type

For this first canonical case, the expected gain type is:

HIDDEN_SEPARATION

Why

The multirepresentational reading is not required to replace the bifurcation plot.

Its operational advantage is narrower:

it may separate structural regimes that the single-view baseline still compresses into one visible configuration.

This is already enough to count as a real gain.


---

5. Verification Rule

Difference type

hidden_regime_separation_under_reencoding

Verification criterion

The MRT counts as successful if all of the following are true:

1. two nearby regions in the standard baseline remain weakly separated or visually similar


2. their multibase structural signatures become measurably distinct


3. the distinction is reproducible across the chosen representation set


4. the distinction is not caused by changing the phenomenon itself



Verification status

EXPECTED_POSITIVE_CASE

This case is currently defined as the canonical expected positive case for MRT v0.

The purpose here is to formalize the test structure, not to overstate a benchmark claim beyond documented branch results.


---

6. Compact MRT Output

phenomenon

logistic_map_regime_transition

baseline

standard bifurcation plot

multirep_finding

distinct structural signatures across bases reveal hidden regime separation not fully visible in the single-view baseline

gain_type

HIDDEN_SEPARATION

verification_status

EXPECTED_POSITIVE_CASE


---

7. Why This Case Matters

This case matters because it is minimal and clean.

It avoids:

semantic interpretation

social ambiguity

domain-dependent narratives

moving targets


It contains:

one fixed phenomenon

one classical baseline

one controlled representation family

one narrow structural question


If OMNIABASE cannot show gain here, its reality claim weakens.

If it does show gain here, OMNIABASE crosses the threshold from philosophical framework to operational method.


---

8. What This Case Does Not Claim

This case does not claim:

proof of hidden dimensions

replacement of dynamical systems theory

universal superiority of multibase reading

automatic prediction advantage

final explanation of chaos


It claims something narrower:

the same phenomenon may yield structurally useful separation across multiple codings that a single standard view compresses.

That is sufficient for MRT v0.


---

9. Decision

This case is accepted as:

the first canonical OMNIABASE MRT v0 case

because it satisfies the minimum requirements:

fixed phenomenon

declared representation set

declared structural signatures

explicit gain hypothesis

explicit verification rule



---

10. Summary Formula

Single-view baseline:

valid

informative

not necessarily structurally complete


Multirepresentational reading:

same phenomenon

multiple codings

non-semantic signatures

hidden separation test


Expected result: OMNIABASE gains operational reality if structural regime separation becomes visible beyond the single-view baseline.