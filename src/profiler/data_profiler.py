import pandas as pd
from pandas.api.types import is_numeric_dtype



def profile_dataset(df):

    profile_dict = {}

    num_rows = df.shape[0]
    num_cols = df.shape[1]

    # dataset key in dict
    profile_dict['dataset'] = {}
    profile_dict['dataset']['row_count'] = num_rows
    profile_dict['dataset']['column_count'] = num_cols

    # # columns key in dict
    profile_dict['columns'] = {}

    for column in df.columns:
        profile_dict['columns'][column]={}
        dtype = df[column].dtypes
        missing_values = df[column].isnull().sum()
        missing_percentage = float(round((missing_values/num_rows)*100,2))
        unique_values = df[column].nunique()

        profile_dict['columns'][column]['dtype'] = str(dtype)
        profile_dict['columns'][column]['missing_values'] = int(missing_values)
        profile_dict['columns'][column]['missing_percentage'] = missing_percentage
        profile_dict['columns'][column]['unique_values'] = int(unique_values)

        # computing statistics for numerical column
        if is_numeric_dtype(df[column]):
            statistics = df[column].describe()
            profile_dict['columns'][column]['statistics'] = statistics.to_dict()

    return profile_dict

