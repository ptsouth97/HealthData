#!/usr/bin/python3

# exercise code types from:  http://img-developer.samsung.com/onlinedocs/health/android/data/EXERCISE_TYPE.html
# ***Not all codes shown here***

import pandas as pd
import matplotlib.pyplot as plt

data_file = 'com.samsung.health.exercise.201804281858.xlsx'
df = pd.read_excel(data_file, skiprows=1)


exercises = {1001:'walking', 1002:'running', 9001:'pilates', 13001:'hiking', 14001:'swimming', 15005:'treadmill'}
