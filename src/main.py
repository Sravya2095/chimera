import os
import src.sourcing.get_data_from_source as sourcing
import src.explore.basic_check as explore
import src.data_cleaning.pre_processing as data_cleaning

input_file = "/Users/SravyaD/Documents/Data/Kaggle/DataSets/Spam/spam.csv"


if __name__ == "__main__":
    input_raw = sourcing.get_data_from_source(input_file)
    explore.get_lable_distribution(input_raw)
    data_cleaning.get_initial_dataFrame_cleanup(input_raw)









