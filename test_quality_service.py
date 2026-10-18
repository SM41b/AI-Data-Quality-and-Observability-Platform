import json
from src.quality.quality_service import run_dataset_quality

def main():
    report = run_dataset_quality(1)

    print("\nDATASET")
    print(json.dumps(report["dataset"], indent=2))

    print("\nSUMMARY")
    print(json.dumps(report["summary"], indent=2))

    print("\nPROFILE (row/column counts only)")
    print(report["profile"]["dataset"])

    print("\nRESULTS")
    for r in report["results"]:
        print(
            f"{r['rule']:<9} | {r['column']:<6} | {r['status']:<6} | "
            f"{r['severity']:<8} | failed={r['failed_count']}"
        )

    print("\nNONEXISTENT DATASET")
    try:
        run_dataset_quality(9999)
    except ValueError as error:
        print(f"Raised ValueError as expected: {error}")

if __name__ == "__main__":
    main()  