# -*- coding: utf-8 -*-
"""Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ouoz0yUakZPbam2PyNW-W7WLQ4EdRkjR
"""

pip install scipy

import pandas as pd
from scipy import stats

df=pd.read_csv('clean_yield_data.csv')

# Split the data into frail and non-frail groups
frail_group = df[df['Frailty'] == 'Y']['Grip strength']
non_frail_group = df[df['Frailty'] == 'N']['Grip strength']

# Display the groups for verification
print("Frail Group Grip Strength:\n", frail_group)
print("Non-Frail Group Grip Strength:\n", non_frail_group)

# Perform the unpaired two-sample t-test
t_stat, p_value = stats.ttest_ind(frail_group, non_frail_group, equal_var=False)

# Display the results
print(f'T-statistic: {t_stat}, P-value: {p_value}')

