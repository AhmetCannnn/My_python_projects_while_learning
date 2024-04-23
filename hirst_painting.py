import turtle as turtle_module
import random

color_list = [(42, 2, 176), (81, 252, 177), (235, 232, 253), (224, 151, 110), (154, 3, 85), (5, 210, 101), (4, 138, 60),
              (244, 42, 125), (109, 108, 245), (251, 252, 56), (184, 184, 250), (210, 106, 6), (175, 113, 246),
              (35, 35, 251), (139, 1, 0), (251, 37, 35), (51, 239, 57), (222, 115, 158), (16, 127, 143), (86, 249, 252),
              (185, 43, 107), (22, 5, 103), (10, 209, 214), (97, 7, 50), (228, 165, 206), (104, 7, 4), (206, 119, 31)]

tim = turtle_module.Turtle()
tim.speed("fastest")
turtle_module.colormode(255)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

def draw_ten_dot():
    for _ in range(10):
        tim.forward(50)
        tim.dot(20, random.choice(color_list))


def draw_tenten_dot():
    for _ in range(4):
        draw_ten_dot()
        tim.forward(50)
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        draw_ten_dot()
        tim.forward(50)
        tim.right(90)
        tim.forward(50)
        tim.right(90)

    draw_ten_dot()
    tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)

    draw_ten_dot()


draw_tenten_dot()
screen = turtle_module.Screen()
screen.exitonclick()
