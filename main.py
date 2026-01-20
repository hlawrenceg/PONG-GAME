import pygame as pg

pg.init()

WIDTH, HEIGHT = 800, 600

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
