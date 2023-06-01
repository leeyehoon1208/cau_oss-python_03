# %%

import figure

myline = figure.line(10, 20)

width, height = myline.get_length()
try:
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError:
    print("please input positive numbe for width and height")

width, height = myline.get_length()
try:
    rectangle = figure.area_ellipse(width, height)
    print(rectangle)
except ValueError:
    print("please input positive numbe for width and height")

width, height = myline.get_length()
try:
    rectangle = figure.area_regular_triangle(width, height)
    print(rectangle)
except ValueError:
    print("please input positive numbe for width and height")

# %%
