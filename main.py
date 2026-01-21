import pygame as pg

pg.init()

WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(("black"))

ball = pg.Rect(0, 0, 30, 30)
ball.center = (WIDTH // 2, HEIGHT // 2)

cpu = pg.Rect(0, 0, 20, 100)
cpu.centery = HEIGHT // 2

player = pg.Rect(0, 0, 20, 100)
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
       
        pg.draw.ellipse(screen,'white', ball)
        pg.draw.rect(screen, 'white', cpu)
        pg.draw.rect(screen, 'white', player)

        pg.display.update()