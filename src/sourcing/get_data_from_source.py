
import os
import pandas as pd

def get_data_from_source(filename):

    df = pd.read_csv(filename,encoding='ISO-8859-1')
    df.drop(df.columns[[2,3,4]],axis=1,inplace=True)
    column_names = ["labels","text"]
    df.columns=column_names
    print(df.columns)
    return df
