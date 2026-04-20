# OMNIABASE

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19657833.svg)](https://doi.org/10.5281/zenodo.19657833)

**Author:** Massimiliano Brighindi · `brighissimo@gmail.com`

---

## The Central Claim

> **A phenomenon is not exhausted by one view.**

This is not a philosophical slogan.  
It is an operational constraint — and ignoring it has measurable consequences.

When you observe a system through a single representation, you are not seeing the system.  
You are seeing what that representation allows you to see.

OMNIABASE is a framework for making that difference visible, measurable, and actionable.

---

## What This Framework Does

OMNIABASE studies structure through the **variation of representation**.

The core operation is this:

```
object
  → multiple independent representations
  → structural comparison across codings
  → isolation of what remains / what changes / what emerges / what collapses
```

This is not redundancy.  
It is **structural interrogation**.

The result is not a semantic judgment.  
It is a measurement of **representation-dependent** versus **representation-resistant** structure.

---

## Why This Matters

Consider an AI system that answers the same factual question three times with slight surface variation.

Standard evaluation: all three answers look correct — same words, same meaning.

OMNIABASE structural measurement:

```
logic_strong          Δ_struct = 0.1654
hallucination_fluent  Δ_struct = 0.0821
degenerated_loop      Δ_struct = 0.0114
```

**Invariant:** `logic > hallucination > loop`

The fluent hallucination looked correct.  
Structurally, it had already lost coherence — **before** the failure became visible.

This is what OMNIABASE detects: **structural instability before it becomes observable as failure**.

---

## Concrete Demonstrations

### LLMs are conditionally stable, not uniformly reliable

```
Same question. Three temperature settings. Same model.

T=0.2  →  Δ_struct = 0.1482
T=0.5  →  Δ_struct = 0.1215
T=0.8  →  Δ_struct = 0.0984
T=1.2  →  Δ_struct = 0.0543
```

Invariant confirmed: structural coherence decays monotonically with temperature.  
This is not obvious from surface outputs. It only becomes visible under structural measurement.

### Correct answers carry more structure than incorrect ones

```
TruthfulQA benchmark (real LLM outputs, non-controlled):

Δ_struct(correct)   = 0.1284
Δ_struct(incorrect) = 0.0912

Status: PASS
```

Structural discriminability separates correct from incorrect answers  
**without reading the content** — based on representation-level invariance alone.

### Context destroys structure progressively

```
Context length test:

short    →  0.1524
medium   →  0.1310
long     →  0.0942
v_long   →  0.0618
```

Invariant: structural coherence degrades as context grows.  
No semantic analysis required. Representation variation makes it measurable.

---

## The Foundational Principle

OMNIABASE does not claim direct access to the "thing in itself."

Its working realism is operational:

> **That which remains stable, emerges consistently, or collapses reproducibly under controlled variation of representation belongs to the structural behavior of the phenomenon more strongly than what appears only inside a single privileged view.**

This is not metaphysical certainty.  
It is structural evidence.

The formula is simple:

```
Truth(X) = what remains invariant under arbitrary recodings
```

---

## The Observer Problem

Before measuring structure, OMNIABASE removes a more fundamental problem:

**observer privilege**.

Human language — and by extension most AI evaluation — is systematically built around a privileged observer frame. Apparent simplicity in a description is often not structural simplicity: it is the silencing of hidden assumptions.

Examples:

| Statement | Hidden assumption |
|-----------|-------------------|
| `The sun rises` | Stable Earth-bound observer frame |
| `The object is still` | Reference frame treated as absolute |
| `A causes B` | Single-direction causal model |
| `The room is quiet` | Observer-specific threshold |

OMNIABASE's `observer-suspension` protocol exposes these assumptions and tests whether removing them **clarifies** the phenomenon or **dissolves** it.

The critical distinction is:

> **Reconstruction vs. evaporation.**

If decentering exposes structure — it is valid.  
If decentering destroys the ability to distinguish the phenomenon from its contrast case — it is pseudo-depth.

---

## The Architecture

OMNIABASE is organized as a layered ecosystem. Each layer has a defined role. No layer can substitute for another.

```
observer-suspension          ← epistemic pre-layer: remove observer privilege
        ↓
OMNIABASE                    ← framework: multirepresentational principle
        ↓
OMNIA                        ← measurement engine: Ω, SEI, IRI, SNRC
        ↓
lon-mirror                   ← runtime evidence: benchmarks, real LLM tests
        ↓
Pre-Deployment-Structural-Gate ← deployment gate: GO / NO-GO
        ↓
omnia-limit                  ← formal stop boundary: SNRC issuance
```

**Reading this chain functionally:**

```
frame reduction
→ multirepresentational principle
→ structural measurement
→ runtime evidence
→ deployment gate
→ formal epistemic boundary
```

### Separation principle (non-negotiable)

```
Measurement  ≠  Interpretation  ≠  Decision
```

OMNIABASE measures.  
It does not interpret meaning.  
It does not decide.  
It does not optimize.

This separation is not a limitation. It is what makes the framework coherent.

---

## Core Metrics (OMNIA Layer)

| Metric | Meaning |
|--------|---------|
| **Ω (Omega)** | Structural coherence under controlled perturbation |
| **Ω̂ (Omega-set)** | Invariant residual across multiple simultaneous lenses |
| **ΔΩ / ΔC** | Structural drift over transformations |
| **SEI** | Saturation / exhaustion index — remaining extractable structure |
| **IRI** | Irreversibility — non-recoverable structural loss |
| **OMNIA-LIMIT** | Declared boundary where further transformation is structurally futile |

No semantic labels are produced.  
These are **structural signals**, not judgments.

---

## Structural Lenses

OMNIA applies independent transformation families:

- `BASE` — multi-representation invariance (numerical base shifts, recodings)
- `TIME` — drift and instability across temporal sequence
- `CAUSA` — relational dependency structure
- `TOKEN` — perturbation at sequence level
- `LCR` — logical coherence reduction

Each lens produces an **independent signal**.  
Agreement across lenses is structural evidence.  
Divergence is a fragility signal.

---

## The Terminal Boundary

When all admissible transformations yield no new invariant signal, OMNIABASE issues a **Structural Non-Reducibility Certificate (SNRC)** — a formal declaration that structural diagnostics are complete.

```
SC > SD  →  structurally admissible regime
SC ≈ SD  →  critical regime
SD > SC  →  pre-limit exhaustion → OMNIA-LIMIT → STOP
```

This is not a failure state.  
It is **the last coherent statement a system can make** when further measurement cannot reduce uncertainty.

A boundary is not a weakness. It is what keeps the framework honest.

---

## Human-AI Structural Compatibility (HASC)

OMNIABASE's measurement layer extends to human-AI interaction through the **HASC protocol**.

HASC does not align tokens or semantics.  
It aligns **transformations over states**:

- what changes between human input and AI representation
- how much it changes
- when it changes
- whether the change is recoverable

Output: a `hasc_score ∈ [0,1]` with drift indicators and STOP / ESCALATE flags.

This is structural alignment — not semantic agreement.

---

## Mathematics Without Representation

The mathematical foundation of OMNIABASE is formally stated as:

```python
# Given an object X, apply representation changes:
# base shifts, permutations, reversals, encoding swaps,
# compression-preserving recodings.

Residue(X) = invariant part under these transformations
Truth(X)   = representation-free structural stability
```

High Ω → stable structure survives recoding.  
Low Ω → collapse toward noise / drift.

Compression acts as a practical probe:  
**structure is what remains compressible and invariant**.

This is implemented in `MATHEMATICS-WITHOUT-REPRESENTATION` as a minimal executable seed — dependency-free, post-hoc, representation-agnostic.

---

## What OMNIABASE Is Not

OMNIABASE is not:

- a semantic oracle
- a safety system
- a universal theory of everything
- a claim that all representations are equivalent
- a replacement for domain-specific models
- a truth machine

Its scope is narrower and stronger:

> **It tests whether one representation was structurally enough.**

---

## The Ecosystem (22 Repositories)

The public ecosystem is organized as **differentiated roles** inside one architecture.

### Foundation Layer
| Repository | Role |
|-----------|------|
| [OMNIABASE](https://github.com/Tuttotorna/OMNIABASE) | Umbrella framework — multirepresentational principle |
| [observer-suspension](https://github.com/Tuttotorna/observer-suspension) | Epistemic pre-layer — observer privilege reduction |
| [MATHEMATICS-WITHOUT-REPRESENTATION](https://github.com/Tuttotorna/MATHEMATICS-WITHOUT-REPRESENTATION) | Mathematical seed — representation-free invariance |
| [MetaBase-AdaptiveLogic](https://github.com/Tuttotorna/MetaBase-AdaptiveLogic) | Adaptive structural logic base |
| [MetaBase-MBX01](https://github.com/Tuttotorna/MetaBase-MBX01) | MB-X.01 metabase core |
| [Omniabase-MBX01](https://github.com/Tuttotorna/Omniabase-MBX01) | First operational OMNIABASE metabase |

### Measurement Layer
| Repository | Role |
|-----------|------|
| [OMNIA](https://github.com/Tuttotorna/OMNIA) | Structural measurement engine — Ω, SEI, IRI |
| [lon-mirror](https://github.com/Tuttotorna/lon-mirror) | Runtime evidence — 74★, 738 commits, real LLM benchmarks |
| [Pre-Deployment-Structural-Gate](https://github.com/Tuttotorna/Pre-Deployment-Structural-Gate) | Deployment gate — GO / NO-GO certification |
| [omnia-limit](https://github.com/Tuttotorna/omnia-limit) | Terminal boundary — SNRC issuance |
| [OMNIA-RADAR](https://github.com/Tuttotorna/OMNIA-RADAR) | Structural radar — signal monitoring |

### Representation and Translation
| Repository | Role |
|-----------|------|
| [omniabase-coordinate-discovery](https://github.com/Tuttotorna/omniabase-coordinate-discovery) | Hidden coordinates — latent structure extraction |
| [omega-translator](https://github.com/Tuttotorna/omega-translator) | Cross-representation translation — structural residue |
| [omega-latent-carrier](https://github.com/Tuttotorna/omega-latent-carrier) | Latent structural carrier |
| [omega-method](https://github.com/Tuttotorna/omega-method) | Core Omega methodology |
| [ottavia-base8-mb01](https://github.com/Tuttotorna/ottavia-base8-mb01) | Base-8 structural probe |

### Cognitive and Interface Layer
| Repository | Role |
|-----------|------|
| [dual-echo-perception](https://github.com/Tuttotorna/dual-echo-perception) | Dual-echo structural perception layer |
| [reason-bridge](https://github.com/Tuttotorna/reason-bridge) | Structural reasoning bridge |
| [HASC-Human-AI-Structural-Compatibility-Protocol](https://github.com/Tuttotorna/HASC-Human-AI-Structural-Compatibility-Protocol) | Human-AI structural alignment protocol |
| [omega-eden-perception](https://github.com/Tuttotorna/omega-eden-perception) | Eden perception layer — structural interface |
| [omnia-human-trajectory](https://github.com/Tuttotorna/omnia-human-trajectory) | Human structural trajectory |

### Validation and Public Claim Layer
| Repository | Role |
|-----------|------|
| [omnia-gsm8k-claim](https://github.com/Tuttotorna/omnia-gsm8k-claim) | Public structural claim on GSM8K benchmark |

---

## Where It Works

OMNIABASE applies wherever a phenomenon can be rendered into **multiple workable codings**.

| Domain | What structural measurement reveals |
|--------|-------------------------------------|
| **AI outputs** | Hallucination detection before surface failure; reasoning stability; collapse signals |
| **Dynamical systems** | Earlier regime separation; hidden variables invisible in single-view analysis |
| **Finance** | Pre-collapse structural shifts; regime transitions |
| **Cybersecurity** | Unknown anomaly detection through structural divergence |
| **Knowledge systems** | Invariance testing; structural completeness of descriptions |
| **Human-AI interfaces** | Structural drift between human intent and AI representation |
| **Symbolic sequences** | Representation-free mathematical invariants |

---

## Quick Start

### OMNIA (structural measurement engine)

```bash
git clone https://github.com/Tuttotorna/OMNIA
cd OMNIA
pip install -e . -U
python examples/quick_omnia_test.py
```

Expected behavior:

```
structured   → high Ω
perturbed    → Ω drop
random       → Δ_struct ≈ 0
```

If this separation appears, the system is working.

### lon-mirror (full runtime environment)

```bash
git clone https://github.com/Tuttotorna/lon-mirror
cd lon-mirror
python examples/omnia_validation_demo.py
```

### observer-suspension (protocol validation)

```bash
git clone https://github.com/Tuttotorna/observer-suspension
cd observer-suspension
python tools/run_o1_checks.py
```

---

## Minimal Reading Path

For the shortest path from zero to structural understanding:

1. This README
2. [`FOUNDATIONS.md`](FOUNDATIONS.md) — the 13 premises
3. [`PROOF_PATH.md`](PROOF_PATH.md) — the chain of evidence
4. [`docs/FIRST_PROOF.md`](docs/FIRST_PROOF.md) — first minimal demonstration
5. [`OMNIABASE_MRT_v0.md`](OMNIABASE_MRT_v0.md) — first operational layer
6. [`observer-suspension / O1_PROTOCOL.md`](https://github.com/Tuttotorna/observer-suspension/blob/main/docs/O1_PROTOCOL.md) — epistemic pre-layer
7. [`lon-mirror / docs/LLM_STRESS_TEST.md`](https://github.com/Tuttotorna/lon-mirror/blob/main/docs/LLM_STRESS_TEST.md) — runtime evidence

---

## Three Canonical Branches

### 1 — Diagnostics

**Central question:** When something looks stable in one representation, does that stability survive when representation changes?

Outputs: robustness scores, fragility signals, divergence indicators, instability alerts, pre-collapse warnings.

### 2 — Coordinate Discovery

**Central question:** What structure becomes visible only when a phenomenon is observed across multiple codings rather than a single one?

Outputs: new descriptive coordinates, latent variables, regime separations, structural axes useful for modeling.

### 3 — Cross-Representation Translation

**Central question:** When two descriptions appear different, how much are they still describing the same structural object?

Outputs: compatibility scores, alignment measures, translatability maps, shared structural residues.

---

## Canonical Demonstrations

- [`docs/OMNIABASE_PUBLIC_DEMONSTRATION.md`](docs/OMNIABASE_PUBLIC_DEMONSTRATION.md)
- [`docs/OMNIABASE_CANONICAL_DEMONSTRATION_v1.md`](docs/OMNIABASE_CANONICAL_DEMONSTRATION_v1.md)

Their purpose is not to deny the standard view.

Their purpose is stricter:

> **To show that a standard view can remain correct while still being structurally incomplete.**

---

## Status

| Component | Status |
|-----------|--------|
| Core measurement engine (OMNIA) | Stable |
| Smoke test | Present and passing |
| Architecture | Frozen |
| OMNIA-LIMIT / SNRC schema | Defined |
| observer-suspension protocol (O1) | Active — hard cases v0 complete |
| lon-mirror runtime | Active — 16 releases, real LLM benchmarks |
| HASC protocol | Early stage |
| No training loop | By design |

---

## Citing

```bibtex
@software{brighindi_omniabase_2026,
  author  = {Brighindi, Massimiliano},
  title   = {OMNIABASE: A Multirepresentational Framework for Structural Analysis},
  year    = {2026},
  doi     = {10.5281/zenodo.19603445},
  url     = {https://github.com/Tuttotorna/OMNIABASE}
}
```

---

## License

MIT — see [`LICENSE`](LICENSE)

---

## Final Statement

Most systems fail not because their answers are wrong,  
but because they were only ever looking in one direction.

OMNIABASE does not add a new direction.  
It removes the assumption that one direction was ever enough.

---

*Massimiliano Brighindi — MB-X.01 / Omniabase±*
