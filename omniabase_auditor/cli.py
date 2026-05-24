import argparse
import sys
from pathlib import Path

from .core import audit_many, generate_numbers, parse_bases, write_all_reports


def main():
    parser = argparse.ArgumentParser(
        prog="omniabase-audit",
        description="Audit numbers across many bases and measure invariance/fragility.",
    )

    parser.add_argument("--number", type=int, default=None, help="Audit one non-negative integer.")
    parser.add_argument("--start", type=int, default=None, help="Start number for range mode.")
    parser.add_argument("--end", type=int, default=None, help="End number for range mode.")
    parser.add_argument("--input", default=None, help="CSV file with a 'number' column.")
    parser.add_argument("--bases", default="2:36", help="Base range like 2:36 or explicit list like 2,3,10,16.")
    parser.add_argument("--out-dir", default="omniabase_report", help="Output directory.")
    parser.add_argument("--fragile-threshold", type=float, default=0.35, help="Threshold for BASE_FRAGILE status.")
    parser.add_argument("--invariant-threshold", type=float, default=0.85, help="Threshold for HIGHLY_INVARIANT status.")
    parser.add_argument("--fail-on-fragile", action="store_true", help="Exit with code 2 if fragile numbers are found.")

    args = parser.parse_args()

    try:
        bases = parse_bases(args.bases)
        numbers = generate_numbers(
            number=args.number,
            start=args.start,
            end=args.end,
            input_path=args.input,
        )

        result = audit_many(
            numbers=numbers,
            bases=bases,
            fragile_threshold=args.fragile_threshold,
            invariant_threshold=args.invariant_threshold,
        )
        write_all_reports(args.out_dir, result)

    except Exception as e:
        print("ERROR:", str(e))
        sys.exit(3)

    s = result["summary"]

    print("")
    print("OMNIBASE AUDIT")
    print("==============")
    print(f"total_numbers:              {s['total_numbers']}")
    print(f"bases_observed:             {s['bases_observed']}")
    print(f"base_range:                 {s['min_base']}:{s['max_base']}")
    print(f"fragile_numbers:            {s['fragile_numbers']}")
    print(f"highly_invariant_numbers:   {s['highly_invariant_numbers']}")
    print(f"fragility_rate:             {s['fragility_rate']:.6f}")
    print(f"high_invariance_rate:       {s['high_invariance_rate']:.6f}")
    print(f"max_fragility:              {s['max_fragility']}")
    print(f"max_invariance:             {s['max_invariance']}")
    print(f"max_hub_score:              {s['max_hub_score']}")
    print("")
    print(f"WROTE: {Path(args.out_dir) / 'report.json'}")
    print(f"WROTE: {Path(args.out_dir) / 'report.csv'}")
    print(f"WROTE: {Path(args.out_dir) / 'report.html'}")
    print(f"WROTE: {Path(args.out_dir) / 'fragile_numbers.jsonl'}")
    print(f"WROTE: {Path(args.out_dir) / 'invariant_numbers.jsonl'}")
    print(f"WROTE: {Path(args.out_dir) / 'certificate.json'}")
    print("")

    if args.fail_on_fragile and s["fragile_numbers"] > 0:
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
