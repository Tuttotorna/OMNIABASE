from __future__ import annotations

from typing import Any

from omnia import build_boundary_certificate
from omnia_limit import validate_certificate
from omnia_validation.enveloper import process_boundary_step


def _coerce_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _coerce_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _clamp_01(value: float) -> float:
    return max(0.0, min(1.0, value))


def _derive_base_invariance_deformation_index(measurement: dict[str, Any]) -> float:
    """Normalize multi-base / base-invariance signals into the backbone field.

    OMNIABASE is a Base-Invariance Producer / Adapter.

    It does not define BoundaryCertificate.
    It does not define ValidationEnvelope.
    It does not claim base-independent truth as final proof.
    It reports multi-base structural evidence into the canonical backbone.
    """

    if "ast_deformation_index" in measurement:
        return _coerce_float(measurement["ast_deformation_index"])

    if "deformation_index" in measurement:
        return _coerce_float(measurement["deformation_index"])

    if "base_variance" in measurement:
        return _coerce_float(measurement["base_variance"])

    if "cross_base_variance" in measurement:
        return _coerce_float(measurement["cross_base_variance"])

    if "representation_drift" in measurement:
        return _coerce_float(measurement["representation_drift"])

    if "digit_structure_drift" in measurement:
        return _coerce_float(measurement["digit_structure_drift"])

    if "base_sensitivity" in measurement:
        return _coerce_float(measurement["base_sensitivity"])

    if "symbolic_projection_loss" in measurement:
        return _coerce_float(measurement["symbolic_projection_loss"])

    if "base_invariance_score" in measurement:
        score = _clamp_01(_coerce_float(measurement["base_invariance_score"], 1.0))
        return 1.0 - score

    if "multi_base_stability_score" in measurement:
        score = _clamp_01(_coerce_float(measurement["multi_base_stability_score"], 1.0))
        return 1.0 - score

    if "representation_invariance_score" in measurement:
        score = _clamp_01(_coerce_float(measurement["representation_invariance_score"], 1.0))
        return 1.0 - score

    return _coerce_float(
        measurement.get(
            "drift_score",
            measurement.get("delta_omega", measurement.get("delta", 0.0)),
        )
    )


def _derive_boundary_state(measurement: dict[str, Any], deformation_index: float) -> tuple[bool, bool, str]:
    """Derive explicit boundary fields without making final mathematical claims."""

    should_continue = measurement.get("should_continue")
    saturation_detected = measurement.get("saturation_detected")

    gate = str(
        measurement.get(
            "gate",
            measurement.get("gate_status", measurement.get("status", "")),
        )
    ).upper()

    if should_continue is None:
        if gate in {"STOP", "NO_GO", "CLOSED", "GATE_CLOSED", "SATURATED"}:
            should_continue = False
        elif gate in {"GO", "CONTINUE", "OPEN", "GATE_OPEN"}:
            should_continue = True

    if saturation_detected is None:
        if gate in {"STOP", "NO_GO", "CLOSED", "GATE_CLOSED", "SATURATED"}:
            saturation_detected = True
        elif gate in {"GO", "CONTINUE", "OPEN", "GATE_OPEN"}:
            saturation_detected = False

    if should_continue is None and saturation_detected is None:
        saturation_detected = deformation_index <= 0.05
        should_continue = not saturation_detected

    if should_continue is None:
        should_continue = not bool(saturation_detected)

    if saturation_detected is None:
        saturation_detected = not bool(should_continue)

    reason = measurement.get("reason")
    if reason is None:
        reason = (
            "Base-invariance structural saturation reached"
            if bool(saturation_detected)
            else "Base-invariance measurement still yields structural information"
        )

    return bool(should_continue), bool(saturation_detected), str(reason)


def _extract_base_invariance_extra_metrics(measurement: dict[str, Any]) -> dict[str, Any]:
    known_keys = {
        "ast_deformation_index",
        "deformation_index",
        "base_variance",
        "cross_base_variance",
        "representation_drift",
        "digit_structure_drift",
        "base_sensitivity",
        "symbolic_projection_loss",
        "base_invariance_score",
        "multi_base_stability_score",
        "representation_invariance_score",
        "drift_score",
        "delta_omega",
        "delta",
        "perturbation_step",
        "should_continue",
        "saturation_detected",
        "gate",
        "gate_status",
        "status",
        "reason",
    }

    return {
        key: value
        for key, value in measurement.items()
        if key not in known_keys and isinstance(value, (int, float, str, bool, type(None)))
    }


def adapt_base_invariance_measurement_to_boundary_certificate(
    measurement: dict[str, Any],
    *,
    target_repository: str = "OMNIABASE",
    certificate_id: str | None = None,
    timestamp: str | None = None,
) -> dict[str, Any]:
    """Adapt multi-base / base-invariance measurements into BoundaryCertificate.

    OMNIABASE is a Base-Invariance Producer / Adapter.

    It does not validate the contract directly.
    It does not emit a competing envelope.
    It does not claim final base-independent truth.
    """

    ast_deformation_index = _derive_base_invariance_deformation_index(measurement)
    perturbation_step = _coerce_int(measurement.get("perturbation_step", 0))
    should_continue, saturation_detected, reason = _derive_boundary_state(
        measurement,
        ast_deformation_index,
    )

    extra_metrics = _extract_base_invariance_extra_metrics(measurement)
    extra_metrics["domain"] = "base_invariance"

    for key in [
        "base_variance",
        "cross_base_variance",
        "representation_drift",
        "digit_structure_drift",
        "base_sensitivity",
        "symbolic_projection_loss",
        "base_invariance_score",
        "multi_base_stability_score",
        "representation_invariance_score",
    ]:
        if key in measurement:
            extra_metrics[key] = measurement[key]

    return build_boundary_certificate(
        target_repository=target_repository,
        ast_deformation_index=ast_deformation_index,
        perturbation_step=perturbation_step,
        should_continue=should_continue,
        saturation_detected=saturation_detected,
        reason=reason,
        certificate_id=certificate_id,
        timestamp=timestamp,
        extra_metrics=extra_metrics,
    )


def observe_base_invariance_envelope(envelope: dict[str, Any]) -> dict[str, Any]:
    """Observe a ValidationEnvelope from a base-invariance viewpoint.

    This is observation over validated backbone output.

    It is not a final claim about mathematical truth, ontology, or proof.
    """

    details = envelope.get("details", {})

    return {
        "observer": "OMNIABASE",
        "role": "base_invariance_producer_adapter",
        "observed_status": envelope.get("validation_status"),
        "target_repository": details.get("target_repository"),
        "certificate_id": details.get("certificate_id"),
        "saturation_detected": details.get("saturation_detected"),
        "ast_deformation_index": details.get("ast_deformation_index"),
        "perturbation_step": details.get("perturbation_step"),
        "base_independent_truth_claim": None,
        "backbone_contract_preserved": True,
    }


def run_base_invariance_backbone_flow(
    measurement: dict[str, Any],
    *,
    target_repository: str = "OMNIABASE",
    certificate_id: str | None = None,
    timestamp: str | None = None,
) -> dict[str, Any]:
    """Run a multi-base / base-invariance measurement through the backbone.

    Flow:

    multi-base / base-invariance measurement
      -> OMNIABASE adapter
      -> BoundaryCertificate-compatible artifact
      -> omnia-limit validate_certificate()
      -> OMNIA-VALIDATION process_boundary_step()
      -> ValidationEnvelope
      -> OMNIABASE observation

    OMNIABASE only adapts and observes.
    """

    raw_certificate = adapt_base_invariance_measurement_to_boundary_certificate(
        measurement,
        target_repository=target_repository,
        certificate_id=certificate_id,
        timestamp=timestamp,
    )

    validate_certificate(raw_certificate)
    envelope = process_boundary_step(raw_certificate)

    return observe_base_invariance_envelope(envelope)
