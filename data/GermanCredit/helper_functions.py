def default_preprocessing(df):
    df['credit'] = df['credit'].replace({1.0: 0, 2.0: 1})
    return df