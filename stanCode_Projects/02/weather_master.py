"""
File: weather_master.py
Name: Cindy
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


EXIT = -100
COLD = 16


def main():
	print('stanCode ' + '"' + 'Weather 4.0' + '"' + '!')
	data = int(input('Next Temperature: (or -100 to quit)? '))
	if data == EXIT:
		print('No temperature were entered.')
	else:
		highest = data
		lowest = data
		if data < COLD:
			cold_day = 1
		else:
			cold_day = 0
		while True:
			data = int(input('Next Temperature: (or -100 to quit)? '))
			if data == EXIT:
				break
			if data > highest:
				highest = data
			if data < lowest:
				lowest = data
			if data < COLD:
				cold_day = cold_day + 1


		ave = (highest + lowest) / 2
		print('Highest Temperature: ' + str(highest))
		print('Lowest Temperature: ' + str(lowest))
		print('Average: ' + str(ave))
		print(str(cold_day) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
