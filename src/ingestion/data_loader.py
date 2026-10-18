from pathlib import Path
import pandas as pd

def load_dataset(source_type: str, source_location: str)->pd.Dataframe:
    '''Load dataset from its configured source.'''

    if source_type == 'csv':
        path = Path(source_location)
        if not path.exists():
            raise FileNotFoundError(f'Dataset file not found: {source_location}')

        return pd.read_csv(path)

    raise ValueError(f'Unsupported source type: {source_type}')

