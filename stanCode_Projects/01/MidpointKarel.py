"""
File: MidpointKarel.py
Name: Cindy
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def turn_opposite():
    turn_left()
    turn_left()


def fill_one_line():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def pick_two_end_beepers():
    """
    Pre-condition: Karel faces on east (1,5)
    Post-condition: Karel faces on east (1,1), finished picking up two beepers on both end
    """
    if not front_is_clear():
        turn_opposite()
        move()
        if on_beeper():
            turn_opposite()
            move()
            pick_beeper()
            turn_opposite()
            while front_is_clear():
                move()
            pick_beeper()
            turn_opposite()


def check_front_beeper():
    while on_beeper():
        move()
    else:
        turn_opposite()
        move()



def pick_middle_beepers():
    """
    Pre-condition: Karel faces on east (1,1)
    Post-condition: Karel faces on east (1,3), finished picking up all beepers in the middle,
    and put a beeper in the middle point
    """
    if not on_beeper():
        move()
        while on_beeper():
            check_front_beeper()
            pick_beeper()
            move()
        turn_opposite()
        move()
        put_beeper()


def main():
    if not front_is_clear(): #for 1*1 world
        put_beeper()
    else:
        fill_one_line()
        pick_two_end_beepers()
        pick_middle_beepers()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
