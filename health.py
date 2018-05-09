#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

data_file = 'com.samsung.health.exercise.201804281858.xlsx'

df = pd.read_excel(data_file, skiprows=1)

x = df['start_time']
y = df['mean_speed']

plt.plot(x, y, linestyle='none', marker='.')
plt.xlabel('Date')
plt.ylabel('Mean speed')
plt.xticks(rotation='vertical')
plt.show()

