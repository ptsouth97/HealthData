#!/usr/bin/python3

import pandas as pd

data_file = 'com.samsung.health.sleep.201805102139.csv'

df = pd.read_csv(data_file, skiprows=1)

end_time = pd.to_datetime(df.iloc[208][7])
start_time = pd.to_datetime(df.iloc[208][2])
duration = end_time - start_time

print('You slept for {}'.format(duration))
