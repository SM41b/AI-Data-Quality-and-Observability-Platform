from src.database.repository import(
    get_dataset,
    get_enabled_quality_rules,
)
from src.ingestion.data_loader import load_dataset
from src.profiler.data_profiler import profile_dataset
from src.quality.rule_runner import run_quality_rules

def _build_summary(results: list[dict]) -> dict:
    """Summarise individual rule results."""

    failed = [r for r in results if r["status"] == "FAILED"]
    failed_by_severity: dict[str, int] = {}

    for result in failed:
        severity = result["severity"]
        failed_by_severity[severity] = (
            failed_by_severity.get(severity, 0) + 1
        )

    if not results:
        status = "NO_RULES"
    elif failed:
        status = "FAILED"
    else:
        status = "PASSED"

    return {
        "status": status,
        "rules_executed": len(results),
        "rules_passed": len(results) - len(failed),
        "rules_failed": len(failed),
        "failed_by_severity": failed_by_severity,
    }

def run_dataset_quality(dataset_id: int) -> dict:
    """Load a registered dataset, profile it, run its enabled
    quality rules, and return a structured report."""

    dataset = get_dataset(dataset_id)

    if dataset is None:
        raise ValueError(
            f"Dataset with id {dataset_id} does not exist"
        )

    rules = get_enabled_quality_rules(dataset_id)
    df = load_dataset(
        dataset["source_type"],
        dataset["source_location"],
    )
    profile = profile_dataset(df)
    results = run_quality_rules(df, rules)

    return{
        "dataset":{
            "id": dataset["id"],
            "name": dataset["name"],
            "source_type": dataset["source_type"],
            "source_location": dataset["source_location"],
            "row_count": len(df),
             "column_count": len(df.columns),
        },
        "summary": _build_summary(results),
        "profile": profile,
        "results": results
    }

