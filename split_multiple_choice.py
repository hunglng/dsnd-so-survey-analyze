import pandas as pd


def create_dataframe(df, ds, name):
    '''
    INPUT
        df - Data Frame
        ds - Data Series
        name - Column Name for new data series
    OUTPUT
        return newly concat data frame
    '''
    count_ds = ds.str.split(pat=';').explode(
    ).str.strip().str.upper().value_counts()
    count_ds.rename(name, inplace=True)
    df = pd.concat([df, count_ds], axis=1, join="outer")

    return df

def create_dataframe_v2(df, ds, name):
    '''
    INPUT
        df - Data Frame
        ds - Data Series
        name - Column Name for new data series
    OUTPUT
        return newly concat data frame
    '''
    s = ds.shape[0]
    count_ds = ds.str.split(pat=';').explode().str.strip().str.upper().value_counts()
    count_ds.rename(name, inplace=True)
    count_ds = count_ds.apply(lambda x: x/s)
    df = pd.concat([df, count_ds], axis=1, join="outer")

    return df