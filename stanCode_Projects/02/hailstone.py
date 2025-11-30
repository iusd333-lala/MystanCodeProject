"""
File: hailstone.py
Name:Cindy
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    print('This program computes Hailstone sequences.')
    n = int(input('Enter a number: '))
    step = 0


    if n == 1:
        print('It took 0 steps to reach 1')
    else:
        while n != 1:
            if n % 2 == 1:
                # newN = 3 * n + 1
                # print(str(n) + ' is odd, so I make 3n+1: ' + str(newN))
                # n = newN
                print(str(n) + ' is odd, so I make 3n+1: ' + str(3 * n + 1))
                n = 3 * n + 1
                step = step + 1
            elif n % 2 == 0:
                # newN = n // 2
                # print(str(n) + ' is even, so I take half: ' + str(newN))
                # n = newN
                print(str(n) + ' is even, so I take half: ' + str(n // 2))
                n = n // 2
                step = step + 1
        print('It took ' + str(step) + ' steps to reach 1.')


    # print('It took' + str(step) + 'steps to reach 1.')



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
