import pandas as pd


def get_initial_dataFrame_cleanup(df):
    mapping = {'ham': 0, 'spam': 1}
    df["labels"]=df["labels"].apply(lambda x: mapping[x])
    print(df)
