import numpy as np
import pygame as pg
import math

# Initialisation of Pygame library
pg.init()

clock = pg.time.Clock()

# Window settings
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
viewport = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_icon(pg.image.load('assets/icon.png'))
pg.display.set_caption('Transformations')

# Line vector object
Line_pointA = [100,50]
Line_pointB = [150,50]

# FUNCTIONS
# Vector translation (movement)
def translate(points_current, move_by_vector):
    new_points = np.add(points_current, move_by_vector)
    print(new_points)
    return new_points

# Scaling from origin
def scale(ax, ay, bx, by, scale_by):
    a = [[ax, ay], [bx, by]]
    vector_ab = np.transpose(a)

    result = vector_ab.dot(scale_by)

    print(result)
    return result

def rotate(ax, ay, bx, by, angle):
    pos = [[ax, ay], [bx, by]]
    angle_cos = math.cos(angle * math.pi / 180)
    angle_sin = math.sin(angle * math.pi / 180)
    r1 = [[angle_cos, -angle_sin], [angle_sin, angle_cos]]
    xxx = np.dot(r1, [[ax, ay], [bx, by]])
    return xxx

# Running loop
while True:
    for event in pg.event.get():
        # BEGIN events
        viewport.fill((255, 255, 255))

        # INPUT events
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.display.quit()
            pg.quit()

        if event.type == pg.KEYDOWN and event.key == pg.K_UP:
            pg.display.toggle_fullscreen()

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Points moved")
                Line_pointA = translate(Line_pointA, (-1,-2.5))
                Line_pointB = translate(Line_pointB, (1, 2.5))

            if event.button == 2:
                print("Points rotated")
                rotator = rotate(Line_pointA[0],Line_pointA[1],Line_pointB[0],Line_pointB[1], 10)
                Line_pointA = rotator[0]
                Line_pointB = rotator[1]

            if event.button == 3:
                print("Points scaled")
                scaler = scale(Line_pointA[0],Line_pointA[1],Line_pointB[0],Line_pointB[1], 1)
                Line_pointA = scaler[0]
                Line_pointB = scaler[1]

        # DRAW events
        pg.draw.line(viewport, (0,0,0), Line_pointA, Line_pointB)

        # UPDATE events
        # Limits the FPS to 30
        clock.tick(30)

        # Refresh of the window
        pg.display.flip()



#pg.quit()
