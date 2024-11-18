import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from scipy import stats
from scipy.stats import ttest_ind, pearsonr


def analyze_data():
    
    # read csv file with merged data
    download_path = os.path.join(os.getcwd(),'main', 'downloaded_data')
    merged_df = pd.read_csv(os.path.join(download_path, 'merged_df.csv'))

    # seperate data from each column 
    data_set_1 = merged_df.iloc[:,1].to_list()
    data_set_2 = merged_df.iloc[:,2].to_list()

    # mean, median, mode
    mean_1 = np.mean(data_set_1)
    median_1 = np.median(data_set_1)
    mode_1 = stats.mode(data_set_1)

    mean_2 = np.mean(data_set_2)
    median_2 = np.median(data_set_2)
    mode_2 = stats.mode(data_set_2)

    # calculate t-test and 
    t_stat, pp_value = ttest_ind(data_set_1, data_set_2)

    # calculate pearson correlation coefficient
    correlation, p_value = pearsonr(data_set_1, data_set_2)

    # check significance
    alpha = 0.05

    if p_value < alpha:
        sig_check = "There is a significant difference between the two groups."
    else:
        sig_check = "There is no significant difference between the two groups."

    # place variables in library
    stats_dict = {
        'mean_1': mean_1,
        'median_1': median_1,
        'mode_1': mode_1,
        'mean_2': mean_2,
        'median_2': median_2,
        'mode_2': mode_2,
        't-stat': t_stat,
        'pp-value': pp_value,
        'p-value': p_value,
        'correlation': correlation,
        'significance': sig_check
    }

    # convert to dataframe
    stats_df = pd.DataFrame(stats_dict)

    # push to csv file
    stats_df.to_csv(os.path.join(download_path, f'stats_df.csv'), index=False)

