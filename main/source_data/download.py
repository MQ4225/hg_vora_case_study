from fredapi import Fred

api_key = 'e2f2d8ab8888632704fef7441a95d3c2'

fred = Fred(api_key=api_key)

series = 'GDP'

# first release
first_data = fred.get_series_first_release(series)
print(first_data)

# latest release
latest_data = fred.get_series(series)

# all data release dates
all_data = fred.get_series_all_releases(series)

# all vintage dats
vintage_data = fred.get_series_vintage_dates(series)