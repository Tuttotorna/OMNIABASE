"""
OMNIACORE
Unified multirepresentational structural evaluation skeleton.

MB-X.01 / OMNIABASE
Massimiliano Brighindi
brighissimo@gmail.com

Purpose
-------
This file defines a minimal executable skeleton for a unified pipeline:

    object
    -> controlled transformations
    -> alignment
    -> normalization
    -> structural measurement
    -> bounded output profile

Boundary
--------
This module performs measurement only.
It does not perform semantic interpretation.
It does not perform decision-making.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple
import math


# ---------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------

TransformFn = Callable[[Any], Any]
AlignFn = Callable[[Mapping[str, Any]], Mapping[str, Any]]
NormalizeFn = Callable[[Mapping[str, Any]], Mapping[str, Any]]


@dataclass(frozen=True)
class TransformSpec:
    """
    One admissible transformation.

    name:
        Public identifier of the transform.

    fn:
        Callable that maps one input object into one transformed representation.
    """
    name: str
    fn: TransformFn


@dataclass
class StructuralProfile:
    """
    Measurement output only.

    omega:
        Coherence-like score. High means stronger invariance across transforms.

    delta_omega:
        Spread / divergence across transformed representations.

    kappa:
        Compatibility-like score. High means lower cross-transform disagreement.

    fragility:
        Sensitivity to representational change. High means easier collapse.

    sei:
        Structural extractability index. Placeholder bounded [0, 1].

    iri:
        Irreversibility-like index. Placeholder bounded [0, 1].

    stable_transforms:
        Transform names whose deviation stays below threshold.

    failed_transforms:
        Transform names that failed or exceeded allowed deviation.

    metadata:
        Internal diagnostic payload for later inspection.
    """
    omega: float
    delta_omega: float
    kappa: float
    fragility: float
    sei: float
    iri: float
    stable_transforms: List[str] = field(default_factory=list)
    failed_transforms: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------
# Core helper functions
# ---------------------------------------------------------------------

def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def safe_mean(values: Sequence[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def safe_variance(values: Sequence[float]) -> float:
    if not values:
        return 0.0
    mu = safe_mean(values)
    return sum((v - mu) ** 2 for v in values) / len(values)


def pairwise_abs_mean(values: Sequence[float]) -> float:
    if len(values) < 2:
        return 0.0

    total = 0.0
    count = 0
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            total += abs(values[i] - values[j])
            count += 1
    return total / count if count else 0.0


# ---------------------------------------------------------------------
# Default representation utilities
# ---------------------------------------------------------------------

def int_to_base(n: int, base: int) -> str:
    """
    Integer to positional base string.
    Supports bases 2..36.
    """
    if not (2 <= base <= 36):
        raise ValueError(f"Unsupported base: {base}")

    if n == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sign = "-" if n < 0 else ""
    n = abs(n)

    out: List[str] = []
    while n > 0:
        n, r = divmod(n, base)
        out.append(digits[r])

    return sign + "".join(reversed(out))


def base_transform(base: int) -> TransformSpec:
    """
    Canonical integer recoding transform.
    """
    def _transform(x: Any) -> Any:
        if not isinstance(x, int):
            raise TypeError(
                f"base{base} transform currently supports int input only, got {type(x).__name__}"
            )
        return int_to_base(x, base)

    return TransformSpec(name=f"base{base}", fn=_transform)


def default_align(representations: Mapping[str, Any]) -> Mapping[str, Any]:
    """
    Minimal alignment:
    - convert all representations to string
    - left-pad to equal length with '0'

    This is intentionally simple and transparent.
    More advanced branches can replace it.
    """
    as_str = {k: str(v) for k, v in representations.items()}
    max_len = max((len(v) for v in as_str.values()), default=0)
    return {k: v.rjust(max_len, "0") for k, v in as_str.items()}


def default_normalize(representations: Mapping[str, Any]) -> Mapping[str, List[float]]:
    """
    Minimal normalization:
    - map each aligned string into numeric sequence
    - digits/letters converted by ordinal rank
    - then scale into [0, 1] inside each representation

    This is not a final scientific normalization.
    It is an explicit placeholder.
    """
    normalized: Dict[str, List[float]] = {}

    for name, rep in representations.items():
        seq: List[float] = []
        for ch in str(rep):
            if ch.isdigit():
                seq.append(float(ord(ch) - ord("0")))
            elif "A" <= ch <= "Z":
                seq.append(float(ord(ch) - ord("A") + 10))
            elif ch == "-":
                seq.append(-1.0)
            else:
                seq.append(float(ord(ch)))

        if not seq:
            normalized[name] = []
            continue

        lo = min(seq)
        hi = max(seq)

        if math.isclose(lo, hi):
            normalized[name] = [0.0 for _ in seq]
        else:
            normalized[name] = [(v - lo) / (hi - lo) for v in seq]

    return normalized


def summarize_representation(rep: Sequence[float]) -> float:
    """
    Collapse one normalized representation into one scalar summary.
    Current choice: mean value.

    Replaceable.
    """
    return safe_mean(list(rep))


# ---------------------------------------------------------------------
# Measurement layer
# ---------------------------------------------------------------------

def measure_structure(
    normalized: Mapping[str, Sequence[float]],
    stability_threshold: float = 0.15,
) -> StructuralProfile:
    """
    Produce a bounded measurement profile from normalized representations.

    Current implementation is deliberately minimal:
    - each representation -> scalar summary
    - divergence from pairwise distances and variance
    - bounded proxies for omega/kappa/fragility/sei/iri

    This is a skeleton, not a final metric theory.
    """
    names = list(normalized.keys())
    summaries = {name: summarize_representation(normalized[name]) for name in names}
    values = list(summaries.values())

    variance = safe_variance(values)
    pairwise = pairwise_abs_mean(values)

    delta_omega = pairwise
    omega = math.exp(-pairwise)
    kappa = math.exp(-variance)
    fragility = clamp01((pairwise + variance) / 2.0)

    sei = clamp01(1.0 - fragility)
    iri = clamp01(variance)

    stable_transforms: List[str] = []
    failed_transforms: List[str] = []

    mu = safe_mean(values)
    for name, value in summaries.items():
        if abs(value - mu) <= stability_threshold:
            stable_transforms.append(name)
        else:
            failed_transforms.append(name)

    return StructuralProfile(
        omega=omega,
        delta_omega=delta_omega,
        kappa=kappa,
        fragility=fragility,
        sei=sei,
        iri=iri,
        stable_transforms=stable_transforms,
        failed_transforms=failed_transforms,
        metadata={
            "summaries": summaries,
            "variance": variance,
            "pairwise_abs_mean": pairwise,
            "stability_threshold": stability_threshold,
        },
    )


# ---------------------------------------------------------------------
# Main engine
# ---------------------------------------------------------------------

class OmniCore:
    """
    Unified structural pipeline.

    Contract
    --------
    evaluate(x):
        1. applies admissible transforms
        2. aligns transformed representations
        3. normalizes them
        4. measures bounded structural behavior

    Non-negotiable boundary
    -----------------------
    This class measures structure only.
    It does not infer meaning.
    It does not choose actions.
    """

    def __init__(
        self,
        transforms: Sequence[TransformSpec],
        align_fn: Optional[AlignFn] = None,
        normalize_fn: Optional[NormalizeFn] = None,
        stability_threshold: float = 0.15,
    ) -> None:
        if not transforms:
            raise ValueError("At least one transform is required.")

        self.transforms = list(transforms)
        self.align_fn = align_fn or default_align
        self.normalize_fn = normalize_fn or default_normalize
        self.stability_threshold = stability_threshold

    def generate_representations(self, x: Any) -> Dict[str, Any]:
        out: Dict[str, Any] = {}
        for spec in self.transforms:
            out[spec.name] = spec.fn(x)
        return out

    def evaluate(self, x: Any) -> StructuralProfile:
        raw = self.generate_representations(x)
        aligned = dict(self.align_fn(raw))
        normalized = dict(self.normalize_fn(aligned))
        profile = measure_structure(
            normalized,
            stability_threshold=self.stability_threshold,
        )

        profile.metadata["input"] = x
        profile.metadata["raw"] = raw
        profile.metadata["aligned"] = aligned
        profile.metadata["normalized"] = normalized
        return profile


# ---------------------------------------------------------------------
# Factory helpers
# ---------------------------------------------------------------------

def build_default_multibase_core(
    bases: Iterable[int] = (2, 8, 10, 16),
    stability_threshold: float = 0.15,
) -> OmniCore:
    transforms = [base_transform(b) for b in bases]
    return OmniCore(
        transforms=transforms,
        align_fn=default_align,
        normalize_fn=default_normalize,
        stability_threshold=stability_threshold,
    )


# ---------------------------------------------------------------------
# Minimal demo
# ---------------------------------------------------------------------

if __name__ == "__main__":
    core = build_default_multibase_core(bases=(2, 8, 10, 16))
    profile = core.evaluate(137)

    print("OMNIACORE demo")
    print("omega:", round(profile.omega, 6))
    print("delta_omega:", round(profile.delta_omega, 6))
    print("kappa:", round(profile.kappa, 6))
    print("fragility:", round(profile.fragility, 6))
    print("sei:", round(profile.sei, 6))
    print("iri:", round(profile.iri, 6))
    print("stable_transforms:", profile.stable_transforms)
    print("failed_transforms:", profile.failed_transforms)
    print("raw:", profile.metadata["raw"])