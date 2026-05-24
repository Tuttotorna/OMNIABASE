import csv
import json
import math
from collections import Counter
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


@dataclass(frozen=True)
class BaseObservation:
    base: int
    digits: str
    length: int
    digit_sum: int
    digit_product_nonzero: int
    max_digit: int
    unique_digits: int
    entropy: float
    parity_digit_sum: int


@dataclass(frozen=True)
class NumberAudit:
    number: int
    status: str
    bases_observed: int
    min_base: int
    max_base: int
    length_variance: float
    digit_sum_variance: float
    entropy_variance: float
    unique_digit_variance: float
    normalized_fragility: float
    invariance_score: float
    hub_score: int
    most_compact_base: int
    longest_representation_base: int
    fragile: bool
    highly_invariant: bool


def digits_in_base(n: int, base: int) -> List[int]:
    if n < 0:
        raise ValueError("Only non-negative integers are supported.")
    if base < 2:
        raise ValueError("Base must be >= 2.")

    if n == 0:
        return [0]

    digits = []
    x = n
    while x > 0:
        digits.append(x % base)
        x //= base

    return list(reversed(digits))


def digit_symbol(d: int) -> str:
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if d < len(alphabet):
        return alphabet[d]
    return "{" + str(d) + "}"


def digit_string(digits: List[int]) -> str:
    return "".join(digit_symbol(d) for d in digits)


def variance(values: List[float]) -> float:
    if not values:
        return 0.0
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)


def entropy(values: List[int]) -> float:
    if not values:
        return 0.0
    total = len(values)
    counts = Counter(values)
    h = 0.0
    for count in counts.values():
        p = count / total
        h -= p * math.log2(p)
    return h


def parse_bases(spec: str) -> List[int]:
    raw = str(spec).strip()
    if not raw:
        raise ValueError("--bases cannot be empty")

    if ":" in raw:
        left, right = raw.split(":", 1)
        start = int(left.strip())
        end = int(right.strip())
        if start < 2 or end < 2:
            raise ValueError("Bases must be >= 2")
        if end < start:
            raise ValueError("Base range end must be >= start")
        return list(range(start, end + 1))

    bases = []
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        b = int(part)
        if b < 2:
            raise ValueError("Bases must be >= 2")
        bases.append(b)

    bases = sorted(set(bases))
    if not bases:
        raise ValueError("No bases parsed from --bases")
    return bases


def read_numbers_csv(path: str) -> List[int]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)

    numbers = []

    with p.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or "number" not in reader.fieldnames:
            raise ValueError("CSV input must contain a 'number' column.")

        for row in reader:
            raw = str(row.get("number", "")).strip()
            if not raw:
                continue
            n = int(raw)
            if n < 0:
                raise ValueError("Number must be non-negative: " + str(n))
            numbers.append(n)

    return numbers


def generate_numbers(number: Optional[int], start: Optional[int], end: Optional[int], input_path: Optional[str]) -> List[int]:
    modes = 0
    if number is not None:
        modes += 1
    if input_path is not None:
        modes += 1
    if start is not None or end is not None:
        modes += 1

    if modes != 1:
        raise ValueError("Choose exactly one input mode: --number, --start/--end, or --input.")

    if number is not None:
        if number < 0:
            raise ValueError("--number must be non-negative")
        return [number]

    if input_path is not None:
        return read_numbers_csv(input_path)

    if start is None or end is None:
        raise ValueError("Range mode requires both --start and --end.")
    if start < 0 or end < 0:
        raise ValueError("--start and --end must be non-negative")
    if end < start:
        raise ValueError("--end must be >= --start")

    return list(range(start, end + 1))


def observe_number_in_base(n: int, base: int) -> BaseObservation:
    ds = digits_in_base(n, base)
    nonzero_product = 1
    for d in ds:
        if d != 0:
            nonzero_product *= d

    return BaseObservation(
        base=base,
        digits=digit_string(ds),
        length=len(ds),
        digit_sum=sum(ds),
        digit_product_nonzero=nonzero_product,
        max_digit=max(ds) if ds else 0,
        unique_digits=len(set(ds)),
        entropy=round(entropy(ds), 12),
        parity_digit_sum=sum(ds) % 2,
    )


def audit_number(
    n: int,
    bases: List[int],
    fragile_threshold: float = 0.35,
    invariant_threshold: float = 0.85,
) -> Dict[str, Any]:
    observations = [observe_number_in_base(n, b) for b in bases]

    lengths = [o.length for o in observations]
    digit_sums = [o.digit_sum for o in observations]
    entropies = [o.entropy for o in observations]
    unique_digits = [o.unique_digits for o in observations]

    length_var = variance([float(x) for x in lengths])
    digit_sum_var = variance([float(x) for x in digit_sums])
    entropy_var = variance([float(x) for x in entropies])
    unique_var = variance([float(x) for x in unique_digits])

    max_possible = max(1.0, math.log2(max(bases) + 1))
    normalized_fragility = (
        min(1.0, length_var / max_possible)
        + min(1.0, digit_sum_var / ((max(bases) + 1) ** 2))
        + min(1.0, entropy_var / max_possible)
        + min(1.0, unique_var / max_possible)
    ) / 4.0

    invariance_score = 1.0 - normalized_fragility

    compact_length = min(lengths)
    long_length = max(lengths)

    most_compact_base = observations[lengths.index(compact_length)].base
    longest_representation_base = observations[lengths.index(long_length)].base

    digit_sum_counts = Counter(digit_sums)
    length_counts = Counter(lengths)
    entropy_bucket_counts = Counter(round(x, 2) for x in entropies)

    hub_score = (
        max(digit_sum_counts.values())
        + max(length_counts.values())
        + max(entropy_bucket_counts.values())
    )

    fragile = normalized_fragility >= fragile_threshold
    highly_invariant = invariance_score >= invariant_threshold

    if fragile:
        status = "BASE_FRAGILE"
    elif highly_invariant:
        status = "HIGHLY_INVARIANT"
    else:
        status = "MIXED"

    audit = NumberAudit(
        number=n,
        status=status,
        bases_observed=len(bases),
        min_base=min(bases),
        max_base=max(bases),
        length_variance=round(length_var, 12),
        digit_sum_variance=round(digit_sum_var, 12),
        entropy_variance=round(entropy_var, 12),
        unique_digit_variance=round(unique_var, 12),
        normalized_fragility=round(normalized_fragility, 12),
        invariance_score=round(invariance_score, 12),
        hub_score=int(hub_score),
        most_compact_base=most_compact_base,
        longest_representation_base=longest_representation_base,
        fragile=fragile,
        highly_invariant=highly_invariant,
    )

    return {
        "audit": asdict(audit),
        "observations": [asdict(o) for o in observations],
    }


def audit_many(
    numbers: Iterable[int],
    bases: List[int],
    fragile_threshold: float = 0.35,
    invariant_threshold: float = 0.85,
) -> Dict[str, Any]:
    audits = [
        audit_number(
            n=n,
            bases=bases,
            fragile_threshold=fragile_threshold,
            invariant_threshold=invariant_threshold,
        )
        for n in numbers
    ]

    audit_rows = [x["audit"] for x in audits]

    total = len(audit_rows)
    fragile = [a for a in audit_rows if a["fragile"]]
    invariant = [a for a in audit_rows if a["highly_invariant"]]

    summary = {
        "total_numbers": total,
        "bases_observed": len(bases),
        "min_base": min(bases) if bases else None,
        "max_base": max(bases) if bases else None,
        "fragile_numbers": len(fragile),
        "highly_invariant_numbers": len(invariant),
        "fragility_rate": len(fragile) / total if total else 0.0,
        "high_invariance_rate": len(invariant) / total if total else 0.0,
        "max_fragility": max([a["normalized_fragility"] for a in audit_rows], default=0.0),
        "max_invariance": max([a["invariance_score"] for a in audit_rows], default=0.0),
        "max_hub_score": max([a["hub_score"] for a in audit_rows], default=0),
        "problem_solved": "Produces reproducible many-base audits for numbers or number ranges.",
    }

    certificate = {
        "audit_type": "omniabase_many_base_audit",
        "summary": summary,
        "boundary": "measurement only; no arithmetic proof is claimed; no base is treated as privileged",
        "measurement_language": [
            "base_observation",
            "length_variance",
            "digit_sum_variance",
            "entropy_variance",
            "unique_digit_variance",
            "normalized_fragility",
            "invariance_score",
            "hub_score",
        ],
    }

    return {
        "summary": summary,
        "certificate": certificate,
        "audits": audits,
    }


def write_json(path: str, obj: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_csv_report(path: str, result: Dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    fields = [
        "number",
        "status",
        "bases_observed",
        "min_base",
        "max_base",
        "length_variance",
        "digit_sum_variance",
        "entropy_variance",
        "unique_digit_variance",
        "normalized_fragility",
        "invariance_score",
        "hub_score",
        "most_compact_base",
        "longest_representation_base",
        "fragile",
        "highly_invariant",
    ]

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for item in result["audits"]:
            row = item["audit"]
            writer.writerow({k: row.get(k, "") for k in fields})


def html_escape(x: Any) -> str:
    return (
        str(x)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def write_html_report(path: str, result: Dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    summary = result["summary"]

    rows = []
    for item in result["audits"]:
        a = item["audit"]
        if not a["fragile"] and not a["highly_invariant"]:
            continue
        rows.append(
            "<tr>"
            + "<td>" + html_escape(a["number"]) + "</td>"
            + "<td>" + html_escape(a["status"]) + "</td>"
            + "<td>" + html_escape(a["normalized_fragility"]) + "</td>"
            + "<td>" + html_escape(a["invariance_score"]) + "</td>"
            + "<td>" + html_escape(a["hub_score"]) + "</td>"
            + "<td>" + html_escape(a["most_compact_base"]) + "</td>"
            + "<td>" + html_escape(a["longest_representation_base"]) + "</td>"
            + "</tr>"
        )

    html = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Omniabase Audit Report</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 32px;
      line-height: 1.45;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
    }}
    th, td {{
      border: 1px solid #ddd;
      padding: 8px;
      vertical-align: top;
    }}
    th {{
      background: #f2f2f2;
    }}
    .box {{
      background: #f8f8f8;
      padding: 16px;
      margin-bottom: 24px;
      border: 1px solid #eee;
    }}
  </style>
</head>
<body>
  <h1>Omniabase Audit Report</h1>

  <div class="box">
    <p><b>Total numbers:</b> {total_numbers}</p>
    <p><b>Bases observed:</b> {bases_observed}</p>
    <p><b>Base range:</b> {min_base} to {max_base}</p>
    <p><b>Fragile numbers:</b> {fragile_numbers}</p>
    <p><b>Highly invariant numbers:</b> {highly_invariant_numbers}</p>
    <p><b>Fragility rate:</b> {fragility_rate:.6f}</p>
    <p><b>High invariance rate:</b> {high_invariance_rate:.6f}</p>
    <p><b>Max fragility:</b> {max_fragility}</p>
    <p><b>Max invariance:</b> {max_invariance}</p>
    <p><b>Max hub score:</b> {max_hub_score}</p>
  </div>

  <h2>Flagged Numbers</h2>

  <table>
    <tr>
      <th>Number</th>
      <th>Status</th>
      <th>Fragility</th>
      <th>Invariance</th>
      <th>Hub Score</th>
      <th>Most Compact Base</th>
      <th>Longest Representation Base</th>
    </tr>
    {rows}
  </table>

  <h2>Boundary</h2>
  <p>This is a many-base measurement report. It does not prove arithmetic claims and does not privilege base 10.</p>
</body>
</html>
""".format(
        total_numbers=summary["total_numbers"],
        bases_observed=summary["bases_observed"],
        min_base=summary["min_base"],
        max_base=summary["max_base"],
        fragile_numbers=summary["fragile_numbers"],
        highly_invariant_numbers=summary["highly_invariant_numbers"],
        fragility_rate=summary["fragility_rate"],
        high_invariance_rate=summary["high_invariance_rate"],
        max_fragility=summary["max_fragility"],
        max_invariance=summary["max_invariance"],
        max_hub_score=summary["max_hub_score"],
        rows="".join(rows),
    )

    p.write_text(html, encoding="utf-8")


def write_jsonl_filtered(path: str, result: Dict[str, Any], mode: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    with p.open("w", encoding="utf-8") as f:
        for item in result["audits"]:
            a = item["audit"]
            if mode == "fragile" and not a["fragile"]:
                continue
            if mode == "invariant" and not a["highly_invariant"]:
                continue
            f.write(json.dumps(item, ensure_ascii=False) + "\n")


def write_all_reports(out_dir: str, result: Dict[str, Any]) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    write_json(str(out / "report.json"), result)
    write_csv_report(str(out / "report.csv"), result)
    write_html_report(str(out / "report.html"), result)
    write_jsonl_filtered(str(out / "fragile_numbers.jsonl"), result, "fragile")
    write_jsonl_filtered(str(out / "invariant_numbers.jsonl"), result, "invariant")
    write_json(str(out / "certificate.json"), result["certificate"])
