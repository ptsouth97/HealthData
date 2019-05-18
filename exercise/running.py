#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.linear_model import LinearRegression
import numpy as np


def main():
	'''main loop'''

	# read exercise file into a dataframe
	data_file = 'com.samsung.health.exercise.201905162215.csv'

	#df = pd.read_excel(data_file, skiprows=1)
	df = pd.read_csv(data_file, skiprows=1)

	# select rows where the exercise code indicates running
	running = df.loc[df['exercise_type'] == 1002]

	# select rows after February 16, 2019 (when full 5 kilometer distance was run)
	running = running.loc[running['start_time'] > '2019-02-16 00:00:00.000']
	
	#mean_speed(running)
	#distance(running)
	duration(running)


def mean_speed(running):
	''' Plots mean speed of runs'''

	# slice the start time column and keep the date, but not the time
	x = running['start_time'].str.split(' ').str[0]

	# slice the mean_speed column
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


def distance(running):
	''' Plots distance of runs'''

	# slice the start time column and keep the date, but not the time
	x = running['start_time'].str.split(' ').str[0]

	# slice the distance column
	y = running['distance']

	# convert meters to kilometers
	y = y / 1000	

	# make a plot
	plt.plot(x, y, linestyle='none', marker='.')
	plt.title('Distance for runs (1002)')
	plt.xlabel('Date')
	plt.ylabel('Distance (kilometers)')
	plt.xticks(rotation='vertical')
	plt.tight_layout()
	plt.savefig('distance.jpg')
	plt.show()

	return


def duration(running):
	''' Plots duration of runs'''

	# reset the dataframe's index
	df = running.reset_index(drop=True)

	# exclude outliers that are 2 standard deviations or more away from the mean
	df = df[np.abs(df.duration - df.duration.mean()) <= (2*df.duration.std())]	

	# convert to datetime format
	dates = pd.to_datetime(df['start_time'])

	# calculate the number of days from start to finish of sample
	total_days = dates.iloc[-1] - dates.iloc[0]
	
	# create new series calculating the difference between each sample and the start date
	x = (dates - dates.iloc[0]).dt.days

	# slice the duration column
	y = df['duration']
    
	# convert milliseconds to minutes
	y = y / 1000 / 60

	# Create the regressor: reg
	reg = LinearRegression()
	
	# Create the prediction space
	prediction_space = np.linspace(x.iloc[0], x.iloc[-1], total_days.days).reshape(-1, 1)

	# convert x to numpy array (matrix) and reshape
	x = x.values.reshape(-1, 1)

	# Fit the model to the data
	reg.fit(x, y)

	# Compute predictions over the prediction space: y_pred
	y_pred = reg.predict(prediction_space)

	# Print R^2
	print(reg.score(x, y))

	# make a plot
	plt.plot(x, y, linestyle='none', marker='.')
	plt.plot(prediction_space, y_pred, color='red', linewidth=2)
	plt.title('Duration for runs (1002)')
	plt.xlabel('Date')
	plt.ylabel('Duration (minutes)')
	plt.xticks(rotation='vertical')
	plt.ylim(24, 30)
	plt.tight_layout()
	plt.savefig('duration.jpg')
	plt.show()

	return
	

if __name__ == '__main__':
	main()
