import os
from etl.extract_data import fred_data_extract
from etl.transform_data import transform_data
from etl.analysis import analyze_data


# Variable 1: 90 Day Treasury Rate
series_1 = 'IR3TIB01USM156N'

# Variable 2: Unemployment Rate
series_2 = 'unrate'

# Variables 3: GDP 
series_3 = 'GDP'

series_list =  [series_1, series_2, series_3]
data_type = 'latest'

def analysis_tool(series_list: list, data_type: str):

    # clear downloads folder
    # check downloaded_data folder to make sure there are two files
    download_path = os.path.join(os.getcwd(),'main', 'downloaded_data')

    # produce the files in downloaded_data folder
    files = os.listdir(download_path)

    for f in files: 
        os.remove(os.path.join(download_path, f))

    # extract data
    for series in series_list:
        fred_data_extract(series=series, data_type=data_type)
    
    # transform data
    transform_data()
    
    # analyze data
    analyze_data()

analysis_tool(series_list=series_list, data_type=data_type)


