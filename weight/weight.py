#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt


def main():
	''' Main function for testing purposes'''

	data_file = 'com.samsung.health.weight.201909262148.csv'

	# Read in the data file
	df = pd.read_csv(data_file, skiprows=1)

	plot_weight(df)

	'''
	end_time = pd.to_datetime(df.iloc[208][7])
	start_time = pd.to_datetime(df.iloc[208][2])
	duration = end_time - start_time

	print('You slept for {}'.format(duration))
	'''


def plot_weight(df):
	''' Plots weight'''

	# add a pounds column
	df['pounds'] = df['weight'] * 2.20462

	# filter out days above 1 as erroneous
	# df = df[df['duration'] < dt.timedelta(days=1)]

	# convert to timedelta and then convert minutes to hours
	# df['duration'] = df['duration'].astype('timedelta64[m]') / 60

	# slice the time column and keep the date, but not the time
	x = df['create_time'].str.split(' ').str[0]

	# slice the duration column	
	y = df['pounds']

	# calculate average weight
	sleep_mean = y.mean()

	# make a plot
	_ = plt.plot(x, y, linestyle='none', marker='.')
	_ = plt.axhline(y=sleep_mean, linestyle='--', color='red')
	_ = plt.title('Weight')
	_ = plt.xlabel('Date')
	_ = plt.ylabel('weight (pounds)')
	_ = plt.xticks(rotation='vertical')
	_ = plt.tight_layout()
	_ = plt.savefig('weight.jpg')
	plt.show()
	
	return


if __name__ == '__main__':
	main()
