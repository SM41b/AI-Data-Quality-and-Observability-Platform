import pandas as pd

def check_not_null(df: pd.DataFrame, column: str) -> dict:
    missing_count = int(df[column].isnull().sum())
    total_count = len(df)

    return {
        "rule":"not null",
        "column":column,
        "status":"PASSED" if missing_count == 0 else "FAILED",
        "failed_count":missing_count,
        "total_count":total_count,
        "message":(
            "No missing values found" 
            if missing_count == 0 
            else f"{missing_count} missing values found.")
    }

def check_unique(df: pd.DataFrame, column: str) -> dict:
    duplicate_count = int(df[column].duplicated().sum())
    total_count = len(df)

    return {
        "rule":"unique",
        "column":column,
        "status": "PASSED" if duplicate_count == 0 else "FAILED",
        "failed_count": duplicate_count,
        "total_count": total_count,
        "message":(
            "All values are unique"
            if duplicate_count == 0
            else f"{duplicate_count} duplicate values found."
        )
    }

def check_numeric(df: pd.DataFrame, column: str) -> dict:
    numeric_values = pd.to_numeric(df[column], errors='coerce')

    invalid_count = int(numeric_values.isnull().sum())
    total_count = len(df)

    return{
        "rule":"numeric",
        "column":column,
        "status": "PASSED" if invalid_count == 0 else "FAILED",
        "failed_count" : invalid_count,
        "total_count": total_count,
        "message":(
            "All values are numeric"
            if invalid_count == 0
            else f"{invalid_count} non_numeric values found."
        )
    }

