# import colorgram
# colors = colorgram.extract("image.jpg", 84)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.b
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
    
# print(rgb_colors)

color_list = [(202, 110, 110), (240, 241, 241), (236, 243, 243), (149, 50, 50), (222, 136, 136), (53, 123, 123), (170, 41, 41), (138, 20, 20), (134, 184, 184), (197, 73, 73), 
(47, 86, 86), (73, 35, 35), (145, 149, 149), (14, 70, 70), (232, 165, 165), (160, 158, 158), (54, 
50, 50), (101, 77, 77), (183, 171, 171), (36, 74, 74), (19, 89, 89), (82, 129, 129), (147, 19, 19), (27, 102, 102), (12, 64, 64), (107, 153, 153), 
(176, 208, 208), (168, 102, 102), (66, 60, 60), (219, 183, 183), (178, 202, 202), (112, 141, 141), (254, 0, 0)]

# dot 그리기
# 왼쪽에서 오른쪽
# 10, 10, 50 걸음, 20 크기
# #모두 다른 색
# 100개

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.hideturtle()
a_height = 0

for _ in range(10):     
    tim.setpos(-200, -200 + a_height)
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    a_height += 50


screen = t.Screen()
screen.exitonclick()









###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)

# print(rgb_colors)