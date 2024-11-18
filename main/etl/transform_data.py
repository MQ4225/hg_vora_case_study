import os
import pandas as pd


def transform_data():

    # check downloaded_data folder to make sure there are two files
    download_path = os.path.join(os.getcwd(),'main', 'downloaded_data')

    # produce the files in downloaded_data folder
    files = os.listdir(download_path)

    # create empty dataframe
    merged_df = pd.DataFrame()

    # goes through files and merges based of date only joining where dates exist for both data sets
    for file in files: 
        df = pd.read_csv(os.path.join(download_path, file))

        if merged_df.empty:
            merged_df = df
        else:
            merged_df = pd.merge(merged_df, df, on='date', how='inner')

    # clean up nan values
    merged_df = merged_df.fillna(0)

    # save new data set to downloaded_data folder
    merged_df.to_csv(os.path.join(download_path, f'merged_df.csv'), index=False)








