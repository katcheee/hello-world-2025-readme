# import required modules
from tkinter import *
from PIL import Image, ImageDraw, ImageTk

if not hasattr(Image, "Resampling"):  # Pillow<9.0
    Image.Resampling = Image

from random import randint
import seaborn as sns
from math import sin, cos, pi
import math

# create a palette of 64 colors (for 8x8 grid)
palette = list(sns.color_palette("Spectral", 64).as_hex())

# convert hex to rgb
get_rgb = lambda x: list(int(x[i : i + 2], 16) for i in (0, 2, 4))
palette = [elem.replace("#", "") for elem in palette]
rgb_palette = list(map(get_rgb, palette))

print(palette)
print(rgb_palette)

scaleFactor = 10
appWidth = 800
appHeight = 800
width = 100
height = 100

app = Tk()
app.geometry("400x400")

canvas = Canvas(app, bg="white")
canvas.pack(fill=BOTH, expand=1)

# create a blank image
myImage = Image.new("RGB", (appWidth * scaleFactor, appHeight * scaleFactor))

# create a drawing context
drawingContext = ImageDraw.Draw(myImage, "RGBA")

# STAR FUNCTION
def star_points(center_x, center_y, outer_radius, inner_radius, num_points=5):
    points = []
    for i in range(num_points * 2):
        angle = math.pi / num_points * i - math.pi / 2
        if i % 2 == 0:
            radius = outer_radius
        else:
            radius = inner_radius
        px = center_x + radius * math.cos(angle)
        py = center_y + radius * math.sin(angle)
        points.append((px, py))
    return points

def drawStar(x, y, outer_radius, inner_radius, color):
    drawingContext.polygon(
        star_points(x, y, outer_radius, inner_radius, 5), 
        fill=color,
        outline=None
    )

# ADD CIRCLE FUNCTION
def drawCircle(x, y, radius, color):
    drawingContext.ellipse((x, y, x + radius, y + radius), fill=color)

def drawMultipleStars(x, y, radius, color, number, star_size_multiplier):
    angle = pi * 2 / number
    for i in range(number):
        new_x = sin(angle * i) * radius / 2 + x
        new_y = cos(angle * i) * radius / 2 + y
        drawStar(new_x, new_y, 
                radius / 25 * star_size_multiplier, 
                radius / 50 * star_size_multiplier, 
                (*color, 255))

# ADD FUNCTION FOR MULTIPLE CIRCLES
def drawMultipleCircles(x, y, radius, color, number, circle_size_multiplier):
    angle = pi * 2 / number
    for i in range(number):
        new_x = sin(angle * i) * radius / 2 + x
        new_y = cos(angle * i) * radius / 2 + y
        circle_radius = radius / 25 * circle_size_multiplier
        # 50% transparent circles
        drawCircle(new_x, new_y, circle_radius, (*color, 128))

for i in range(8):
    for j in range(8):
        print("row", i, "col", j)
        
        size_multiplier = 1.5 + (i * 0.2)
        
        # Alternate between stars and circles
        if (i + j) % 2 == 0:
            drawMultipleStars(
                i * (width * scaleFactor),
                j * (height * scaleFactor),
                width * scaleFactor,
                rgb_palette[8 * i + j],
                16,
                size_multiplier
            )
        else:
            drawMultipleCircles(
                i * (width * scaleFactor),
                j * (height * scaleFactor),
                width * scaleFactor,
                rgb_palette[8 * i + j],
                16,
                size_multiplier
            )

# FIXED: Only resize and save once
myImage = myImage.resize((appWidth, appHeight), Image.Resampling.LANCZOS)
myImage.save("myImage.png", bitmap_format="png")

# convert to Tkinter PhotoImage
myImage = ImageTk.PhotoImage(myImage)
canvas.create_image(0, 0, image=myImage, anchor="nw")

app.mainloop()