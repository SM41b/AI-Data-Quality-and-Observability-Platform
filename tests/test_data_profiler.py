import pandas as pd
from src.profiler.data_profiler import profile_dataset


def create_test_dataframe():
    data = {
        "id": [1, 2, 3, 4],
        "name": ["Alice", "Bob", "Alice", "David"],
        "age": [20, 25, None, 30],
        "city": ["Kolkata", "Delhi", "Kolkata", None]
    }
    data_frame = pd.DataFrame(data)
    return data_frame

def test_dataset_shape():
    df = create_test_dataframe()

    profile = profile_dataset(df)

    assert profile['dataset']['row_count'] == 4
    assert profile['dataset']['column_count'] == 4

def test_missing_values():
    df = create_test_dataframe()

    profile = profile_dataset(df)

    assert profile['columns']['age']['missing_values']==1
    assert profile['columns']['city']['missing_values']==1

def test_missing_percentage():
    df = create_test_dataframe()
    profile = profile_dataset(df)

    assert profile['columns']['age']['missing_percentage']==25.0
    assert profile['columns']['city']['missing_percentage']==25.0

def test_unique_values():
    df = create_test_dataframe()
    profile = profile_dataset(df)

    assert profile['columns']['name']['unique_values']==3
    assert profile['columns']['city']['unique_values']==2

def test_numeric_statistics():
    df = create_test_dataframe()
    profile = profile_dataset(df)

    age_stats =  profile['columns']['age']['statistics']
    assert age_stats['count']==3.0
    assert age_stats['min']==20.0
    assert age_stats['max']==30.0
