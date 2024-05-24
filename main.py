# import colorgram
import turtle as t
import random

hoppie = t.Turtle()
t.colormode(255)

hoppie.speed("fastest")
hoppie.penup()
hoppie.hideturtle()

# def extract_colors(num_colors):
#     """
#     extracts num_colors(int) number of colors from the image
#     returns the list of rgb values for the chosen colors
#     """
#     colors = colorgram.extract("hirst_image.jpg", num_colors)
#     rgb_colors_list = []
#
#     for color in colors:
#         rgb_colors_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
#     return rgb_colors_list
#
#
# colors = extract_colors(25)
# print(colors)

colors = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
          (122, 175, 156), (229, 236, 239), (226, 198, 131), (192, 87, 108), (11, 50, 64),
          (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77),
          (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18)]


def draw_dots(size, gap, steps):
    """
    outputs the dots in a square of side (gap * steps)
    the centre of screen coincides with the centre of square (provided steps are even)
    """

    for count in range(steps):
        x_pos = (-steps//2) * gap
        y_pos = (-steps//2 + count) * gap
        hoppie.setpos(x_pos, y_pos)
        hoppie.seth(0)

        for _ in range(steps):
            hoppie.dot(size, random.choice(colors))
            hoppie.forward(gap)


draw_dots(20, 50, 10)

my_screen = t.Screen()
my_screen.exitonclick()
