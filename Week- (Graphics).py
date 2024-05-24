''' Problem:
In this section, our goal is to work on a graphics problem together.

Problem: Random Circles

Write a program that draws a 20 circles at random positions with random colors on the canvas. You are provided with the constants N_CIRCLES (the number of circles to draw),
CANVAS_WIDTH and CANVAS_HEIGHT (the width and height of the canvas, respectively) and CIRCLE_SIZE (the width and height of each circle respectively). Specifically, your 
job is to implement the following function:

def draw_random_circle(canvas):

which takes as a parameter the canvas that will be used to draw all of the random circles. In order to choose a random color, we have a defined a function for you to use 
called random_color(). It will return a random color that you can use for a given circle. 

def random_color():
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)


Making all the necessary calls to your draw_random_circle(...) function should produce something that looks like this (of course with randomness yours will have the 
circles in different locations:



Solution: '''


from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

# inside  For  loop print n_circles
# inside for loop create circles  we have to generate randoom position for circles
# 




def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range(N_CIRCLES):
        generate_random_circles(canvas)

    

def  generate_random_circles(canvas):
        x = random.randint(0,CANVAS_WIDTH)
        y = random.randint(0,CANVAS_HEIGHT)
        color = random_color()
        canvas.create_oval(x,y, x + CIRCLE_SIZE, y+ CIRCLE_SIZE , color )

def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()
