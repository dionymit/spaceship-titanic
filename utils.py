import numpy as np


# Drop rows that have nan values
def drop_null_rows(df):
    rows_to_del = []
    for col in df.columns:
        rows_to_del += np.where(df[col].isnull())[0].tolist()
    cleaned = df.drop(rows_to_del)  # delete rows with null values
    return cleaned


# Convert bool to int
def boolean2int(df, boolean_feat):
    for col in boolean_feat:
        df[col] = df[col].astype(int)
    return df


# Drop columns
def drop_columns(df, columns):
    out = df.drop(columns=columns)
    return out
