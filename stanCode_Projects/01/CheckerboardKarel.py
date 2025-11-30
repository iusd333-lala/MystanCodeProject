"""
File: CheckerboardKarel.py
Name: Cindy
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def fill_one_line():
    """
    Pre-condition: Karel faces on east (1,1)
    Post-condition: Karel faces on east (1,8), finished one horizontal line
    """
    if not front_is_clear(): # for 1*1 world
        put_beeper()
    else:
        while front_is_clear():
            put_beeper()
            move()
            if front_is_clear():
                move()


def next_line_left():
    turn_left()
    if front_is_clear():
        move()
        turn_left()


def next_line_right():
    turn_right()
    if front_is_clear():
        move()
        turn_right()


def turn_opposite_move_left():
    turn_left()
    turn_left()
    move()
    move()


def turn_opposite_move_right():
    turn_right()
    turn_right()
    move()
    move()


def check_beeper_same_line():
    """
    Pre-condition: Karel faces on east (1,8)
    Post-condition: Karel faces on east (1,8), turn opposite and move two steps to check if it has beepers on it,
    if yes, put beeper; if not, do nothing
    """
    turn_opposite_move_left()
    if on_beeper():
        turn_opposite_move_right()
        put_beeper()
    else:
        turn_opposite_move_right()


def turn_opposite():
    turn_right()
    turn_right()


def check_beeper_next_line_left():
    """
    Pre-condition: Karel faces on wear (2,8)
    Post-condition: Karel faces on east (2,8), turn left and move one step to check if it has beepers on it,
    if yes, back to original position and move one step forward; if not, back to original position and do nothing
    """
    turn_left()
    move()
    if on_beeper():
        turn_opposite()
        move()
        turn_left()
        move()
    else:
        turn_opposite()
        move()
        turn_left()


def main():

    if not front_is_clear():
        turn_left()
        fill_one_line()
    else:
        while left_is_clear():
                fill_one_line()
                check_beeper_same_line()
                next_line_left()
                check_beeper_next_line_left()
                fill_one_line()
                next_line_right()
        fill_one_line()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
