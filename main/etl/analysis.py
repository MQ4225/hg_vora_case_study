import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from scipy import stats
from scipy.stats import ttest_ind, pearsonr

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

print(f"T-statistic: {t_stat:.2f}")
print(f"P-value: {pp_value:.4f}")

# calculate pearson correlation coefficient
correlation, p_value = pearsonr(data_set_1, data_set_2)

print(f"Correlation: {correlation:.2f}")
print(f"P-value: {p_value:.4f}")

# check significance
alpha = 0.05

if p_value < alpha:
    print("There is a significant difference between the two groups.")
else:
    print("There is no significant difference between the two groups.")

# plot data
plt.scatter(data_set_1, data_set_2)
plt.title("Scatter Plot of Data_1 vs. Data_2")
plt.xlabel("Data_1")
plt.ylabel("Data_2")
plt.grid(True)
plt.show()