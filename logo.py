# import turtle as t
# t.color('white')
# t.begin_fill()
# t.fillcolor('#FBEAEB')
# t.pencolor('purple')
# t.pensize(12)
# t.circle(100, steps=9)
# t.end_fill()

# t.color('#FBEAEB')
# t.goto(0, 50)
# t.color('purple')
# t.write("YUSUF", align="center", font=("Comic Sans MS", 30, "normal"))
# t.done()

import turtle
import math

t = turtle.Turtle()


def set_anchor_position(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.pensize(2)
    t.speed(10)


def draw_circle(r, color):
    x_point = 0
    y_pont = -r
    set_anchor_position(x_point, y_pont)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def write_name(color):
    set_anchor_position(0, 0)
    t.pencolor(color)
    t.write("YUSUF", align="center", font=("Comic Sans MS", 30, "normal"))
    t.hideturtle()


if __name__ == '__main__':
    draw_circle(200, '#3D155F')
    draw_circle(150, '#DF678C')
    draw_circle(100, '#3D155F')
    write_name('#DF678C')
    turtle.done()