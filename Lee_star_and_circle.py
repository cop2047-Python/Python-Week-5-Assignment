# Author Name: James Lee
# Date: 6/12/2022
# Program Name: Lee_star_and_circle.py
# Purpose: Learn about functions by drawing a star and circle pattern

import turtle

PATTERN_ORIGIN_X = 0
PATTERN_ORIGIN_Y = 0
PATTERN_PEN_COLOR = 'black'
PATTERN_BG_COLOR = 'white'
LINE_LENGTH = 100
CIRCLE_RADIUS = 50
SCALE_FACTOR = 1


def main():
    turtle.Screen()
    turtle.setup(1275, 655, 0, 0)
    turtle.bgcolor(PATTERN_BG_COLOR)
    turtle.pencolor(PATTERN_PEN_COLOR)
    turtle.showturtle()
    line_x = -500
    line_y = 200
    turn_angle = 44

    for i in range(3):
        line(line_x, line_y, 0)
        turtle.left(turn_angle)
        circle(-400, 150)
        line(-400, 200, -144)
        circle(-300, 150)

    star(0, 0, 100)
    turtle.done()


def line(start_x, start_y, turn):
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.pencolor(PATTERN_PEN_COLOR)
    turtle.forward(LINE_LENGTH)


def circle(x, y):
    turtle.penup()
    turtle.goto(x, y - CIRCLE_RADIUS)
    turtle.pendown()
    turtle.circle(CIRCLE_RADIUS)


def star(x, y, reach):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(5):
        turtle.forward(reach)
        turtle.right(144)


main()
