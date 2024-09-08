import pandas as pd


def preprocessing(df, region_df):
    # Filtering the summer olympics
    df = df[df['Season'] == 'Summer']
    # Merging the dataframes
    df = df.merge(region_df, how='left', on='NOC')
    # Dropping the duplicate columns, by using OneHotEncoding
    df.drop_duplicates(inplace=True)
    # By using OneHotEncoding
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df

