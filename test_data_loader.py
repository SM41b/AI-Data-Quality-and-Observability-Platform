from src.database.repository import get_dataset
from src.ingestion.data_loader import load_dataset

def main():
    dataset = get_dataset(1)

    if dataset is None:
        raise RuntimeError('Dataset not found')

    df = load_dataset(
        dataset['source_type'],
        dataset['source_location']
    )

    print(f'Loaded dataset: {dataset['name']}')
    print(f'Rows: {len(df)}')
    print(f'Columns: {len(df.columns)}')
    print(f'Column names: {list(df.columns)}')


if __name__ == "__main__":
    main()

    