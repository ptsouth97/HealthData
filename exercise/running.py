#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt


def main():
	'''main loop'''

	# read exercise file into a dataframe
	data_file = 'com.samsung.health.exercise.201903041229.csv'

	#df = pd.read_excel(data_file, skiprows=1)
	df = pd.read_csv(data_file, skiprows=1)

	mean_speed(df)
	distance(df)


def mean_speed(df):
	''' Plots mean speed of runs'''

	# select rows where the exercise code indicates running
	running = df.loc[df['exercise_type'] == 1002]

	# slice the columns with the date and average speed
	x = running['start_time']
	y = running['mean_speed']

	# make a plot
	plt.plot(x, y, linestyle='none', marker='.')
	plt.title('Mean speed for runs (1002)')
	plt.xlabel('Date')
	plt.ylabel('Mean speed (meters/second)')
	plt.xticks(rotation='vertical')
	plt.tight_layout()
	plt.savefig('mean_speed.jpg')
	plt.show()
	
	return


def distance(df):
	''' Plots distance of runs'''

	# select rows where the exercise code indicates running
	running = df.loc[df['exercise_type'] == 1002]

	# slice the columns with the data and distance
	x = running['start_time']
	y = running['distance']

	# make a plot
	plt.plot(x, y, linestyle='none', marker='.')
	plt.title('Distance for runs (1002)')
	plt.xlabel('Date')
	plt.ylabel('Distance (meters)')
	plt.xticks(rotation='vertical')
	plt.tight_layout()
	plt.savefig('distance.jpg')
	plt.show()

	return


if __name__ == '__main__':
	main()
