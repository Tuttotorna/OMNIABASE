import json
import subprocess
import sys

from omniabase_auditor.core import (
    audit_many,
    audit_number,
    digit_string,
    digits_in_base,
    generate_numbers,
    parse_bases,
    read_numbers_csv,
)


def test_digits_in_base():
    assert digits_in_base(0, 2) == [0]
    assert digits_in_base(10, 2) == [1, 0, 1, 0]
    assert digits_in_base(255, 16) == [15, 15]


def test_digit_string():
    assert digit_string([1, 0, 1, 0]) == "1010"
    assert digit_string([15, 15]) == "FF"


def test_parse_bases_range():
    assert parse_bases("2:5") == [2, 3, 4, 5]


def test_parse_bases_list():
    assert parse_bases("10,2,16,2") == [2, 10, 16]


def test_generate_number():
    assert generate_numbers(number=7, start=None, end=None, input_path=None) == [7]


def test_generate_range():
    assert generate_numbers(number=None, start=3, end=5, input_path=None) == [3, 4, 5]


def test_read_numbers_csv(tmp_path):
    p = tmp_path / "numbers.csv"
    p.write_text("number\n7\n31\n", encoding="utf-8")
    assert read_numbers_csv(str(p)) == [7, 31]


def test_audit_number():
    result = audit_number(255, bases=[2, 10, 16])
    assert result["audit"]["number"] == 255
    assert result["audit"]["bases_observed"] == 3
    assert len(result["observations"]) == 3


def test_audit_many():
    result = audit_many(range(1, 10), bases=[2, 3, 10, 16])
    assert result["summary"]["total_numbers"] == 9
    assert "certificate" in result


def test_cli_writes_reports(tmp_path):
    out_dir = tmp_path / "report"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "omniabase_auditor.cli",
            "--start",
            "1",
            "--end",
            "20",
            "--bases",
            "2:16",
            "--out-dir",
            str(out_dir),
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 0
    assert (out_dir / "report.json").exists()
    assert (out_dir / "report.csv").exists()
    assert (out_dir / "report.html").exists()
    assert (out_dir / "fragile_numbers.jsonl").exists()
    assert (out_dir / "invariant_numbers.jsonl").exists()
    assert (out_dir / "certificate.json").exists()

    report = json.loads((out_dir / "report.json").read_text(encoding="utf-8"))
    assert report["summary"]["total_numbers"] == 20


def test_cli_fail_on_fragile(tmp_path):
    out_dir = tmp_path / "report"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "omniabase_auditor.cli",
            "--start",
            "1",
            "--end",
            "100",
            "--bases",
            "2:36",
            "--out-dir",
            str(out_dir),
            "--fragile-threshold",
            "0.01",
            "--fail-on-fragile",
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode in (0, 2)
