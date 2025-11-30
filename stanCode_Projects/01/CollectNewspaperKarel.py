"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_opposite():
    turn_left()
    turn_left()

def move_to_news():
    """
    Pre-condition: Karel faces on east (4,3)
    Post-condition: Karel faces on east (3,5), ready to pick up the news
    """
    move()
    move()
    turn_right()
    move()
    turn_left()


def pick_news():
    move_to_news()
    move()
    pick_beeper()
    turn_opposite()
    move()


def back_to_home():
    """
    Pre-condition: Karel faces on west (3,5)
    Post-condition: Karel faces on north (3,3), ready to back home and read news
    """
    turn_left()
    move()
    turn_right()
    move()
    move()
    turn_right()
    move()


def  read_news():
    back_to_home()
    move()
    turn_right()
    put_beeper()

def main():
    pick_news()
    read_news()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
