import pygame as pg

pg.init()

WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(("white"))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        pg.display.update()
    