'''This week in section, your goal is to solve a Karel problem together using decomposition and stepwise refinement.

Here's the Link to the Section 2 Code!

Spread Beepers

In this task, Karel will always start by standing in front of a pile of beepers. Karel needs to pick up the entire pile of beepers and spread them out along the row so that there is exactly one beeper in each cell, and exactly as many cells with beepers as were in the original pile. Karel should spread the first beeper into the cell where the pile was.

Here is an example before and after:


You may assume that:

There is only one row in the world

Karel starts with infinite beepers in her bag (how will you make sure to only spread as many beepers as were in the original pile?)

The pile of beepers is on the second corner, directly in front of where Karel starts

The world is wide enough for all the beepers, and there will be empty cells at the end of the row at the end

Write the code to implement Spread Beepers Karel. Come up with a strategy first. Think, "what are the high-level steps Karel needs to take?" and make these steps into helper functions. Remember that your program should work for a pile of any size. 

Have extra time? Do one of these fun extensions!

Spread Multiple Rows of Beepers

Imagine instead of one row of beepers, there are multiple rows stacked on top of one another that we need to spread out!


Solution:'''

from karel.stanfordkarel import *

def main():
    move()
    while beepers_present():
        pick_beeper()
        if beepers_present():
            spread()
    put_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def spread():
    while beepers_present():
        move()
    put_beeper()
    return_back()

def return_back():
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    move()

def turn_around():
    turn_left()
    turn_left()
        
        
        # There is no need to edit code beyond this point
if __name__ == '__main__':
    main()

