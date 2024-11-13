import os
import pandas as pd
import numpy as np 
from scipy import stats

# check downloaded_data folder to make sure there are two files
downloaded_files_path = os.path.join(os.getcwd(),'main', 'downloaded_data')

# produce the files in downloaded_data folder
files = os.listdir(downloaded_files_path)

for file in files: 
    print(file)

