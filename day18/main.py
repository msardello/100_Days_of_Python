import colorgram
import random
from turtle import Turtle, Screen

my_colors = []
def extract_colors(nbr_of_colors):
    hirst_colors = colorgram.extract("image.jpg", nbr_of_colors)
    for color in hirst_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color = (r, g, b)
        my_colors.append(color)

# extract_colors(30)

screen = Screen()
screen.colormode(255)
my_hirst = Turtle()
my_hirst.penup()
my_hirst.speed("fastest")
my_hirst.hideturtle()


color_list = [(144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176),
              (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169),
              (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158),
              (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194),
              (175, 198, 201), (213, 182, 176), (37, 47, 45)]

y = -200
nbr_rows = 10
nbr_columns = 10

while nbr_rows > 0:
    x = -250
    for nbr in range(nbr_columns):
        my_hirst.teleport(x, y)
        # print(my_hirst.dot(20,random.choice(color_list)))
        my_hirst.dot(20, random.choice(color_list))
        x += 50
    y += 50
    nbr_rows -= 1



screen.exitonclick()