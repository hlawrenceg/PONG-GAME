import pygame as pg
import random 

#reset ball to center
def reset_ball():
    global ball_speed_x, ball_speed_y #access to make changes
    ball.x = WIDTH // 2 - 2 #center ball
    ball.y = random.randint(10,100) 
    ball_speed_x *= random.choice([1, -1]) 
    ball_speed_y *= random.choice([1, -1]) 

#update points
def point_won(winner):
    global cpu_points, player_points
    if winner == 'cpu':
        cpu_points += 1
    if winner == 'player':
        player_points += 1 

def animate_cpu():
    global cpu_speed
    
    # NYTT: SJEKKER OM SPILLET ER AI ELLER 2 PLAYER
    if game_mode == 'ai':
        if ball.centery <= cpu.centery:
            cpu_speed = -6
        if ball.centery >= cpu.centery:
            cpu_speed = 6
    else:
        # NYTT: CPU STYRES AV PLAYER 2 I 2 PLAYER MODE
        cpu_speed = player2_speed

    cpu.y += cpu_speed
    
    if cpu.top <= 0:
        cpu.top = 0
    if cpu.bottom >= HEIGHT:
        cpu.bottom = HEIGHT
        
def animate_player():
    player.y += player_speed
    
    #keep player on screen
    if player.top <= 0:
        player.top = 0
    
    #don't go off bottom
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT

def animate_ball():
        global ball_speed_x, ball_speed_y
        ball.x += ball_speed_x #6 pixels per frame
        ball.y += ball_speed_y #6 pixels per frame

        if ball.top >= HEIGHT or ball.bottom <= 0:
            ball_speed_y *= -1

        if ball.left >= WIDTH:
            point_won('cpu')
            reset_ball()
            
        if ball.right <= 0:
            point_won('player')
            reset_ball()

        if ball.colliderect(player) or ball.colliderect(cpu):
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
cpu_speed = 6

# NYTT: SPEED FOR PLAYER 2
player2_speed = 0

# NYTT: GAME MODE (AI ELLER 2 PLAYER)
game_mode = 'ai'

cpu_points, player_points = 0, 0

score_font = pg.font.Font(None, 74)

running = True 
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        #when pressing key
        if event.type == pg.KEYDOWN:

            # NYTT: BYTT MELLOM AI OG 2 PLAYER
            if event.key == pg.K_1:
                game_mode = 'ai'
            if event.key == pg.K_2:
                game_mode = 'pvp'

            if event.key == pg.K_UP:
                player_speed = -6
            if event.key == pg.K_DOWN:
                player_speed = 6

            # NYTT: PLAYER 2 KONTROLLER (W / S)
            if event.key == pg.K_w:
                player2_speed = -6
            if event.key == pg.K_s:
                player2_speed = 6

        #when releasing key
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                player_speed = 0
            if event.key == pg.K_DOWN:
                player_speed = 0

            # NYTT: STOPPER PLAYER 2 NÅR KNAPP SLIPPES
            if event.key == pg.K_w or event.key == pg.K_s:
                player2_speed = 0     

    animate_ball()
    animate_player()
    animate_cpu()
    
    screen.fill('black')
    cpu_score = score_font.render(str(cpu_points), True, 'white')
    player_score = score_font.render(str(player_points), True, 'white')
    screen.blit(cpu_score, (WIDTH // 4, 10))
    screen.blit(player_score, (WIDTH * 3 // 4, 10))

    #draw objects
    pg.draw.aaline(screen, 'white', (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    pg.draw.ellipse(screen,'white', ball) 
    pg.draw.rect(screen, 'white', cpu)
    pg.draw.rect(screen, 'white', player)

    pg.display.update()
    pg.time.Clock().tick(60)
