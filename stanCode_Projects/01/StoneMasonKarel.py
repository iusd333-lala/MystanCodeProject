"""
File: StoneMasonKarel.py
Name: Cindy
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def turn_opposite():
    turn_left()
    turn_left()


def fix_vertical_stone():
    """
    Pre-condition: Karel faces on east (1,1)
    Post-condition: Karel faces on east (5,1), finished one vertical stone
    """
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()


def go_back():
    """
    Pre-condition: Karel faces on north (5,1)
    Post-condition: Karel faces on east (1,1), go back to original position
    """
    turn_opposite()
    while front_is_clear():
        if on_beeper():
            move()
    turn_left()


def main():
    while front_is_clear():
        fix_vertical_stone()
        go_back()
        for i in range(4):
            move()
    fix_vertical_stone()
    go_back()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
