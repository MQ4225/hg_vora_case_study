import os
import pandas as pd


def transform_data():

    # check downloaded_data folder to make sure there are two files
    download_path = os.path.join(os.getcwd(),'main', 'downloaded_data')

    # produce the files in downloaded_data folder
    files = os.listdir(download_path)

    # create empty dataframe
    # SQL: CREATE TABLE merged_df (column_names)
    merged_df = pd.DataFrame()

    # goes through files and merges based of date only joining where dates exist for both data sets
    for file in files: 
        df = pd.read_csv(os.path.join(download_path, file))

        if merged_df.empty:
            merged_df = df
        else:
            # SQL: SELECT (insert columns) FROM merged_df JOIN df on merged_df.date = df.date
            merged_df = pd.merge(merged_df, df, on='date', how='inner')

    # clean up nan values
    # SQL: SELECT ifnull(column_name, '0') as column_name from merged_df
    merged_df = merged_df.fillna(0)

    # save new data set to downloaded_data folder
    merged_df.to_csv(os.path.join(download_path, f'merged_df.csv'), index=False)








