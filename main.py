import pygame as pg

def animate_player():
    player.y += player_speed
    
    if player.top <= 0:
        player.top = 0
    
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT
def animate_ball():
        global ball_speed_x, ball_speed_y
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top >= HEIGHT or ball.bottom <= 0:
            ball_speed_y *= -1

        if ball.left >= WIDTH or ball.right <= 0:
            ball_speed_x *= -1

pg.init()

WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(("black"))

ball = pg.Rect(0, 0, 30, 30)
ball.center = (WIDTH // 2, HEIGHT // 2)

cpu = pg.Rect(0, 0, 20, 100)
cpu.centery = HEIGHT // 2

player = pg.Rect(0, 0, 20, 100)
player.midright = (WIDTH, HEIGHT // 2)

ball_speed_x = 6
ball_speed_y = 6
player_speed = 0

running = True 
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                player_speed = -6
            if event.key == pg.K_DOWN:
                player_speed = 6
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                player_speed = 0
            if event.key == pg.K_DOWN:
                player_speed = 0     

    animate_ball()
    animate_player()

    screen.fill('black')
    pg.draw.aaline(screen, 'white', (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    pg.draw.ellipse(screen,'white', ball) 
    pg.draw.rect(screen, 'white', cpu)
    pg.draw.rect(screen, 'white', player)

    pg.display.update()
    pg.time.Clock().tick(60)