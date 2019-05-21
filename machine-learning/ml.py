#!/usr/bin/python3

import pandas as pd
import os


def main():
	''' main function for testing'''
	
	# read exercise file into a dataframe
	os.chdir('../exercise')
	exercise_data = 'com.samsung.health.exercise.201905162215.csv'
	exercise_df = pd.read_csv(exercise_data, skiprows=1)

	# convert end_time column from string to datetime
	exercise_df['end_time'] = exercise_df['end_time'].astype('datetime64')	

	# add a column with just the date extracted from the datetime stamp
	exercise_df['date'] = exercise_df['end_time'].dt.date

	# read sleep file into a dataframe
	os.chdir('../sleep')
	sleep_data = 'com.samsung.health.sleep.201903071432.csv'
	sleep_df = pd.read_csv(sleep_data, skiprows=1)
	os.chdir('..')

	# convert end_time column from string to datetime
	sleep_df['end_time'] = sleep_df['end_time'].astype('datetime64')

	# add a column with just the date extracted from the datetime stamp
	sleep_df['date'] = sleep_df['end_time'].dt.date

	# combine dataframes on the new date column
	#df = exercise_df.set_index('end_time').join(sleep_df.set_index('end_time'))
	df = exercise_df.merge(sleep_df, on='date')
	print(df)	


if __name__ == '__main__':
	main()
