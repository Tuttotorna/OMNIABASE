
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_public_entrypoints_exist():
    required = [
        "README.md",
        "LICENSE",
        "CITATION.cff",
        "FOUNDATIONS.md",
        "ARCHITECTURE.md",
        "LEXICON.md",
        "docs/OMNIABASE_SCOPE.md",
        "docs/FORMALISM.md",
        "docs/REPOSITORY_STATUS.md",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_core_directories_exist():
    for rel in ["docs", "examples"]:
        assert (ROOT / rel).exists(), rel

def test_foundational_files_exist():
    required = [
        "OMNIABASE_MRT_v0.md",
        "OMNIABASE_MRT_v0_CASE_01.md",
        "docs/OMNIABASE_PUBLIC_DEMONSTRATION.md",
        "docs/FIRST_PROOF.md",
        "examples/omniacore.py",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_readme_boundary_terms():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "base 10 is a representation habit, not a law of number" in text
    assert "Structural truth = invariance under transformation" in text
    assert "measurement != inference != decision" in text
    assert "not a truth oracle" in text
    assert "Decision remains external" in text

def test_formalism_terms():
    text = (ROOT / "docs" / "FORMALISM.md").read_text(encoding="utf-8")
    assert "n = sum_" in text
    assert "O(n)" in text
    assert "base-invariant" in text
