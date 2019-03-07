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
	df['duration'] = (pd.to_datetime(df['end_time']) - pd.to_datetime(df['start_time']))#.dt.components['seconds'] #.astype('timedelta64[h]')

	# filter out hours above 12 as erroneous
	#df = df[df['duration']<12]

	# slice the start time column and keep the date, but not the time
	x = df['start_time'].str.split(' ').str[0]
	
	y = df['duration']#.dt.datetime.time()

	print(type(y[0]))
	# make a plot
	plt.plot(x, y, linestyle='none', marker='.')
	plt.title('Sleep duration')
	plt.xlabel('Date')
	plt.ylabel('Duration (hours)')
	plt.xticks(rotation='vertical')
	plt.tight_layout()
	plt.savefig('sleep.jpg')
	plt.show()
	
	return


if __name__ == '__main__':
	main()
