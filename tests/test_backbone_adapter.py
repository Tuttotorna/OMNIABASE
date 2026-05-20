from omniabase import (
    adapt_base_invariance_measurement_to_boundary_certificate,
    observe_base_invariance_envelope,
    run_base_invariance_backbone_flow,
)
from omnia_limit import validate_certificate


def test_adapt_base_invariance_measurement_to_boundary_certificate_continue_flow():
    measurement = {
        "base_invariance_score": 0.82,
        "perturbation_step": 2,
        "gate_status": "CONTINUE",
        "base_family": "integer_bases_2_to_16",
        "observed_property": "digit_structure",
    }

    raw_certificate = adapt_base_invariance_measurement_to_boundary_certificate(
        measurement,
        target_repository="OMNIABASE",
        certificate_id="omniabase-boundary-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    cert = validate_certificate(raw_certificate)

    assert cert.certificate_id == "omniabase-boundary-cert"
    assert cert.target_repository == "OMNIABASE"
    assert round(cert.ast_deformation_index, 2) == 0.18
    assert cert.perturbation_step == 2
    assert cert.should_continue is True
    assert cert.saturation_detected is False
    assert raw_certificate["metrics"]["domain"] == "base_invariance"
    assert raw_certificate["metrics"]["base_family"] == "integer_bases_2_to_16"
    assert raw_certificate["metrics"]["observed_property"] == "digit_structure"
    assert raw_certificate["metrics"]["base_invariance_score"] == 0.82


def test_run_base_invariance_backbone_flow_stop_flow():
    measurement = {
        "multi_base_stability_score": 0.97,
        "perturbation_step": 5,
        "gate_status": "STOP",
        "base_family": "all_integer_bases",
        "observed_property": "residual_structure",
    }

    observation = run_base_invariance_backbone_flow(
        measurement,
        target_repository="OMNIABASE",
        certificate_id="omniabase-stop-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    assert observation["observer"] == "OMNIABASE"
    assert observation["role"] == "base_invariance_producer_adapter"
    assert observation["observed_status"] == "GATE_CLOSED_SATURATION_REACHED"
    assert observation["certificate_id"] == "omniabase-stop-cert"
    assert observation["target_repository"] == "OMNIABASE"
    assert observation["saturation_detected"] is True
    assert round(observation["ast_deformation_index"], 2) == 0.03
    assert observation["perturbation_step"] == 5
    assert observation["base_independent_truth_claim"] is None
    assert observation["backbone_contract_preserved"] is True


def test_run_base_invariance_backbone_flow_continue_flow():
    measurement = {
        "cross_base_variance": 0.21,
        "perturbation_step": 1,
        "gate_status": "CONTINUE",
        "base_family": "finite_basis_sample",
        "observed_property": "representation_length",
    }

    observation = run_base_invariance_backbone_flow(
        measurement,
        target_repository="OMNIABASE",
        certificate_id="omniabase-continue-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    assert observation["observer"] == "OMNIABASE"
    assert observation["role"] == "base_invariance_producer_adapter"
    assert observation["observed_status"] == "GATE_OPEN_MEASUREMENT_REQUIRED"
    assert observation["certificate_id"] == "omniabase-continue-cert"
    assert observation["target_repository"] == "OMNIABASE"
    assert observation["saturation_detected"] is False
    assert observation["ast_deformation_index"] == 0.21
    assert observation["perturbation_step"] == 1
    assert observation["base_independent_truth_claim"] is None
    assert observation["backbone_contract_preserved"] is True


def test_observe_existing_envelope_without_base_independent_truth_claim():
    envelope = {
        "envelope_id": "omniabase-env",
        "timestamp": "2026-05-20T20:00:00Z",
        "validation_status": "GATE_CLOSED_SATURATION_REACHED",
        "details": {
            "target_repository": "OMNIA",
            "certificate_id": "existing-omniabase-cert",
            "saturation_detected": True,
            "ast_deformation_index": 0.04,
            "perturbation_step": 9,
        },
    }

    observation = observe_base_invariance_envelope(envelope)

    assert observation["observer"] == "OMNIABASE"
    assert observation["role"] == "base_invariance_producer_adapter"
    assert observation["observed_status"] == "GATE_CLOSED_SATURATION_REACHED"
    assert observation["certificate_id"] == "existing-omniabase-cert"
    assert observation["target_repository"] == "OMNIA"
    assert observation["base_independent_truth_claim"] is None
    assert observation["backbone_contract_preserved"] is True
