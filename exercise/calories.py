#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

def main():
  data_file = 'com.samsung.health.exercise.201804281858.xlsx'
  df = pd.read_excel(data_file, skiprows=1)
  plot_calories(df)
  
  
def plot_calories(data)
  '''plots calories'''

  x = data['start_time']
  y = data['calories']
  
  plt.plot(x, y)
  plt.show()
  

if __name__ == '__main__':
  main()
