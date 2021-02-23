# import colorgram

# colors = colorgram.extract("image.jpg", 30)
# color_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     color_tuple = (r, g, b)
#
#     color_list.append(color_tuple)
#
# print(color_list)

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
color_list = [(131, 165, 206), (225, 151, 100), (32, 41, 59), (200, 134, 147), (166, 56, 46), (39, 104, 153), (141, 184, 161), (153, 58, 65), (170, 29, 33), (217, 80, 69), (158, 32, 29), (15, 96, 71), (50, 111, 90), (58, 50, 47), (50, 42, 46), (34, 61, 56), (170, 188, 222), (190, 99, 108), (32, 59, 108), (103, 127, 163), (34, 151, 210), (175, 200, 188), (66, 66, 56)]
tim.penup()

top_counter = 0
mid_counter = 0

x = -200
y = -200

tim.speed("fastest")
tim.hideturtle()

while top_counter < 10:
    tim.setx(x)
    tim.sety(y)
    y += 50
    tim.position()
    mid_counter = 0
    while mid_counter < 10:
        tim.dot(20, random.choice(color_list))
        tim.fd(50)
        mid_counter += 1

    top_counter += 1


screen = t.Screen()
screen.exitonclick()