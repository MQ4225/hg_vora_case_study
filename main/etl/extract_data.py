from fredapi import Fred
import os

def fred_data_extract(series, data_type):

    # sets up connection to FRED and ALFRED API
    api_key = 'e2f2d8ab8888632704fef7441a95d3c2'
    fred = Fred(api_key=api_key)
    series = series

    # set up os path to load into the correct folders
    download_path = os.path.join(os.getcwd(),'main', 'downloaded_data')

    # first release
    if data_type == 'first':
        first_data_df = fred.get_series_first_release(series)
        first_data_df.to_csv(os.path.join(download_path, f'{series}_first_release.csv'))

    # latest release
    if data_type == 'latest':
        latest_data_df = fred.get_series(series)
        latest_data_df.to_csv(os.path.join(download_path, f'{series}_latest_release.csv'))

    # all data release dates
    if data_type == 'all':
        all_data_df = fred.get_series_all_releases(series)
        all_data_df.to_csv(os.path.join(download_path, f'{series}_all_release.csv'))

    # all vintage dates
    if data_type == 'vintage':
        vintage_data_df = fred.get_series_vintage_dates(series)
        vintage_data_df.to_csv(os.path.join(download_path, f'{series}_vintage_dates.csv'))

series = 'IR3TIB01USM156N'
data_type = 'latest'

fred_data_extract(series=series, data_type=data_type)



