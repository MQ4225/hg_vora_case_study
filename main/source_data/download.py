from fredapi import Fred


def fred_data_extract(series, data_type):
    api_key = 'e2f2d8ab8888632704fef7441a95d3c2'
    fred = Fred(api_key=api_key)
    series = 'GDP'

    # first release
    if data_type == 'first':
        first_data = fred.get_series_first_release(series)
        print(first_data)

    # latest release
    if data_type == 'latest'
        latest_data = fred.get_series(series)
        print(latest_data)

    # all data release dates
    if data_type == 'all'
        all_data = fred.get_series_all_releases(series)
        print(all_data)

    # all vintage dates
    if data_type == 'all'
        vintage_data = fred.get_series_vintage_dates(series)
        print(vintage_data)

