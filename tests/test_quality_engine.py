import pandas as pd
from src.quality.quality_engine import (check_not_null, check_numeric, check_unique)

def create_test_dataframe():
    return pd.DataFrame(
        {
            "id": [1, 2, 3, 4],
        "name": ["Alice", "Bob", "Alice", "David"],
        "age": [20, 25, None, 30],
        "salary": ["20000", "30000", "invalid", "50000"],
        }
    )

def test_not_null_passes():
    df = create_test_dataframe()
    result = check_not_null(df, 'name')

    assert result['status'] == "PASSED"
    assert result['failed_count'] == 0

def test_not_null_fails():
    df = create_test_dataframe()

    result = check_not_null(df, 'age')

    assert result['status'] == "FAILED"
    assert result['failed_count'] == 1

def test_unique_passes():
    df = create_test_dataframe()

    result = check_unique(df, 'id')

    assert result['status'] == 'PASSED'
    assert result['failed_count'] == 0

def test_unique_fails():
    df = create_test_dataframe()

    result = check_unique(df, 'name')

    assert result['status'] == 'FAILED'
    assert result['failed_count'] == 1

def test_numeric_passes():
    df = create_test_dataframe()
    
    result = check_numeric(df, 'id')
    
    assert result['status'] == 'PASSED'
    assert result['failed_count'] == 0

def test_numeric_fails():
    df = create_test_dataframe()
    
    result = check_numeric(df, 'salary')
    
    assert result['status'] == 'FAILED'
    assert result['failed_count'] == 1

