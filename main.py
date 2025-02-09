import numpy as np
import pygame as pg

# Initialisation of Pygame library
pg.init()

clock = pg.time.Clock()

# Window settings
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
viewport = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_icon(pg.image.load('assets/icon.png'))
pg.display.set_caption('Transformations')

# Line object
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
    vector_abx = np.transpose(np.dot(ax,bx), scale_by)
    vector_aby = np.transpose(np.dot(ay,by), scale_by)

    scaled_a = [ax + vector_abx, ay + vector_aby]
    scaled_b = [bx + vector_abx, by + vector_aby]

    result = [scaled_a , scaled_b]
    print(result)
    return result


# Running loop
while True:
    for event in pg.event.get():
        # BEGIN events
        viewport.fill((255, 255, 255))

        # INPUT events
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Points moved")
                Line_pointA = translate(Line_pointA, (-1,-2.5))
                Line_pointB = translate(Line_pointB, (1, 2.5))

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
