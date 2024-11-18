from fredapi import Fred
import os
import pandas as pd

def fred_data_extract(series: str, data_type: str):

    # sets up connection to FRED and ALFRED API
    api_key = 'e2f2d8ab8888632704fef7441a95d3c2'
    fred = Fred(api_key=api_key)
     
    series = series

    # set up os path to load into the correct folders
    download_path = os.path.join(os.getcwd(),'main', 'downloaded_data')

    # first release
    if data_type == 'first':
        first_data_series = fred.get_series_first_release(series)
        first_data_df = pd.DataFrame(first_data_series)
        first_data_df = first_data_df.reset_index()
        first_data_df.columns = ['date', series]
        first_data_df.to_csv(os.path.join(download_path, f'{series}_first_release.csv'), index=False)

    # latest release
    if data_type == 'latest':
        latest_data_series = fred.get_series(series)
        latest_data_df = pd.DataFrame(latest_data_series)
        latest_data_df = latest_data_df.reset_index()
        latest_data_df.columns = ['date', series]
        latest_data_df.to_csv(os.path.join(download_path, f'{series}_latest_release.csv'), index=False)

    # all data release dates
    if data_type == 'all':
        all_data_series = fred.get_series_all_releases(series)
        all_data_df = pd.DataFrame(all_data_series)
        all_data_df = all_data_df.reset_index()
        all_data_df.columns = ['date', series]
        all_data_df.to_csv(os.path.join(download_path, f'{series}_all_release.csv'), index=False)

    # all vintage dates
    if data_type == 'vintage':
        vintage_data_df_series = fred.get_series_vintage_dates(series)
        vintage_data_df = pd.DataFrame(vintage_data_df_series)
        vintage_data_df = vintage_data_df.reset_index()
        vintage_data_df.columns = ['date', series]
        vintage_data_df.to_csv(os.path.join(download_path, f'{series}_vintage_dates.csv'), index=False)


