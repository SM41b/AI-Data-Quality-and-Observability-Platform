from src.database.repository import(
    get_dataset,
    get_enabled_quality_rules
)
from src.ingestion.data_loader import load_dataset
from src.quality.rule_runner import run_quality_rules

def main():
    dataset = get_dataset(1)

    if dataset is None:
        raise RuntimeError('Dataset not found.')
    
    rules = get_enabled_quality_rules(dataset['id'])

    df = load_dataset(
        dataset['source_type'],
        dataset['source_location']
    )

    results = run_quality_rules(df, rules)

    print(f'\nDataset: {dataset['name']}')
    print(f"Rows checked: {len(df)}")
    print(f"Rules executed: {len(results)}")

    print("\nQUALITY RESULTS")
    print("-" * 50)

    for result in results:
        print(
            f"Rule: {result['rule']} | "
            f"Column: {result['column']} | "
            f"Status: {result['status']} | "
            f"Severity: {result['severity']} | "
            f"Failed: {result['failed_count']} | "
            f"Message: {result['message']} | "
        )

if __name__ == "__main__":
    main()
