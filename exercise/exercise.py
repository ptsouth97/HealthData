#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt


def main():
	'''main loop'''

	# read exercise file into a dataframe
	data_file = 'com.samsung.health.exercise.201804281858.xlsx'
	df = pd.read_excel(data_file, skiprows=1)

	# select rows where the exercise code indicates running
	running = df.loc[df['exercise_type'] == 1002]

	# slice the columns with the date and average speed
	x = running['start_time']
	y = running['mean_speed']

	# make a plot
	plt.plot(x, y, linestyle='none', marker='.')
	plt.xlabel('Date')
	plt.ylabel('Mean speed')
	plt.xticks(rotation='vertical')
	plt.show()


if __name__ == '__main__':
	main()
