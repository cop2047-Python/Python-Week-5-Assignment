# Author Name: James Lee
# Date: 6/12/2022
# Program Name: Lee_star_and_circle.py
# Purpose: Learn about functions by drawing a star and circle pattern multiple times

import turtle

LINE_LENGTH = 50.0                  # Length of each arm of the star
PATTERNS_IN_ROW = 3                 # Total number of circle-star patterns in a row
NUMBER_OF_ROWS = 3                  # Total number of rows to display
SCREEN_WIDTH = 1275                 # Screen width
SCREEN_HEIGHT = 655                 # Screen height
CIRCLE_RADIUS = LINE_LENGTH / 2     # Radius of each circle surrounding the star

# Global constants for the start of the pattern in each row and margins between each graphic
# are calculated based on the size of the LINE_LENGTH of the arm of the star. This helps to
# optimize the position of the circle-star patterns on the display.
if LINE_LENGTH < 100:
    PATTERN_START_X = -830 + 2 * LINE_LENGTH
    PATTERN_MARGIN_X = 1.5 * PATTERNS_IN_ROW * LINE_LENGTH
    PATTERN_MARGIN_Y = 100.0
else:
    PATTERN_START_X = -830 + LINE_LENGTH
    PATTERN_MARGIN_X = PATTERNS_IN_ROW * LINE_LENGTH
    PATTERN_MARGIN_Y = 1.5 * LINE_LENGTH

PATTERN_START_Y = 250 - CIRCLE_RADIUS   # Starting position on y-axis
PATTERN_PEN_COLOR = 'black'             # Turtle pen color
PATTERN_BG_COLOR = 'white'              # Background color of turtle graphics window
RIGHT_TURN_ANGLE = 144.0                # Offset amount for each arm of the star


def main():

    init_turtle()           # Initialize the turtle graphics window

    # The outer for loop sets up the turtle coordinates for each row.
    for i in range(NUMBER_OF_ROWS):
        # The x-axis value increases from left to right, and the y-value increases
        # from bottom to top. The point (0,0) is the center of the screen.
        line_x = PATTERN_START_X
        line_y = PATTERN_START_Y - 2 * i * PATTERN_MARGIN_Y
        turtle.penup()
        turtle.goto(line_x, line_y)
        # This inner loop fills the row with the circle-star pattern.
        # Each pattern in the row is offset by PATTERN_MARGIN_X in the x-axis
        for j in range(PATTERNS_IN_ROW):
            draw_circle_star(turtle.xcor() + PATTERN_MARGIN_X, turtle.ycor())

    turtle.done()


# The init_turtle function initializes the turtle graphics window.
# Global constants are used to set the size of the window, background
# color, and pen color. The speed of the turtle is set to max speed.

def init_turtle():
    turtle.Screen()
    turtle.reset()
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0)
    turtle.bgcolor(PATTERN_BG_COLOR)
    turtle.pencolor(PATTERN_PEN_COLOR)
    turtle.title('Python Turtle Graphics')
    turtle.showturtle()
    turtle.speed(0)


# The draw_circle_star function draws one star with 5 circles where
# each circle touches on 2 vertices. The pattern consists of one line
# with a circle drawn at the end of the line. This basic pattern is
# repeated five times to complete the star pattern. A "right turn angle"
# of 144 degrees creates the proper offset for each line-circle pair.
# line_x and line_y determine the x-y position of the circle-star on the display.

def draw_circle_star(line_x, line_y):
    turtle.penup()
    turtle.goto(line_x, line_y)
    turtle.pendown()
    for i in range(5):
        turtle.forward(LINE_LENGTH)
        turtle.right(RIGHT_TURN_ANGLE)
        turtle.circle(CIRCLE_RADIUS)
    turtle.penup()


# Call the main function
main()
