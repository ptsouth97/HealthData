#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt


def main():
	''' Main function for testing purposes'''

	data_file = 'com.samsung.health.sleep.201903071432.csv'

	# Read in the data file
	df = pd.read_csv(data_file, skiprows=1)

	plot_hours(df)

	'''
	end_time = pd.to_datetime(df.iloc[208][7])
	start_time = pd.to_datetime(df.iloc[208][2])
	duration = end_time - start_time

	print('You slept for {}'.format(duration))
	'''


def plot_hours(df):
	''' Plots hours slept each night'''

	# add a duration column
	df['duration'] = (pd.to_datetime(df['end_time']) - pd.to_datetime(df['start_time']))

	# filter out days above 1 as erroneous
	df = df[df['duration'] < dt.timedelta(days=1)]

	# convert to timedelta and then convert minutes to hours
	df['duration'] = df['duration'].astype('timedelta64[m]') / 60

	# slice the start time column and keep the date, but not the time
	x = df['start_time'].str.split(' ').str[0]

	# slice the duration column	
	y = df['duration']

	# calculate average sleep duration
	sleep_mean = y.mean()

	# make a plot
	_ = plt.plot(x, y, linestyle='none', marker='.')
	_ = plt.axhline(y=sleep_mean, linestyle='--', color='red')
	_ = plt.title('Sleep duration')
	_ = plt.xlabel('Date')
	_ = plt.ylabel('Duration (hours)')
	_ = plt.xticks(rotation='vertical')
	_ = plt.tight_layout()
	_ = plt.savefig('sleep.jpg')
	plt.show()
	
	return


if __name__ == '__main__':
	main()
