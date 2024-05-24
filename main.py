import colorgram
import turtle as t
import random

hoppie = t.Turtle()


def extract_colors(num_colors):
    """
    extracts num_colors(int)
    :param num_colors:
    :return:
    """
    colors = colorgram.extract("hirst_image.jpg", num_colors)
    rgb_colors_list = []

    for color in colors:
        rgb_colors_list.append((color.rgb.r, color.rgb.g, color.rgb.b))

    return rgb_colors_list


colors = extract_colors(10)


def draw_dots(size, gap, steps):
    t.colormode(255)

    for count in range(steps):
        hoppie.penup()
        x_pos = (-steps//2) * gap
        y_pos = (-steps//2 + count) * gap
        hoppie.setpos(x_pos, y_pos)
        hoppie.seth(0)

        for _ in range(steps):
            hoppie.pendown()
            hoppie.dot(size, random.choice(colors))
            hoppie.penup()
            hoppie.forward(gap)


draw_dots(15, 40, 10)

my_screen = t.Screen()
my_screen.exitonclick()
