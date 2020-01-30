
import pandas as pd

def get_lable_distribution( df : pd.DataFrame):
    print("basic exploration of data")
    print("categories are :- ",pd.unique(df["labels"]))
    categories = pd.unique(df["labels"])
    for name in categories:
        print("number of items for category - ",name)
        print(df[df["labels"]==name]["labels"].count())
        print("average number of words in category {} are {}".format(name,str(df[df["labels"]==name]["text"].apply(lambda x: len(x.split())).mean())))





