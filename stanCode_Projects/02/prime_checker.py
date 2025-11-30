"""
File: prime_checker.py
Name: Cindy
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""


EXIT = -100


def main():
	print('Welcome to the prime checker!')
	n = int(input('n: '))
	if n == EXIT:
		print('Have a good one!')
	else:
		while True:
			if n == EXIT:
				print('Have a good one!')
				break
			else:
				if n % 2 == 1:
					print(str(n) + ' is a prime number.')
					n = int(input('n: '))
				else:
					print(str(n) + ' is not a prime number.')
					n = int(input('n: '))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
