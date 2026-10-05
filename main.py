import pandas as pd
from src.profiler.data_profiler import profile_dataset

def main():
    df = pd.read_csv('data/sample/customer.csv')
    profile = profile_dataset(df)
    print(profile)


if __name__=='__main__':
    main()
