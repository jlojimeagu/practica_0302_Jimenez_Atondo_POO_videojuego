# pong!
import pygame
from pygame import gfxdraw


class Brick:
    "Draw Player 2"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 60, 20)

    def update(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 60, 20))


class Bar:
    "Draw Player 2"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, 60, 10))
        self.rect = pygame.Rect(self.x, self.y, 60, 10)


class Ball:
    "Draw Player 2"

    def __init__(self, xb, yb):
        self.xb = xb
        self.yb = yb

    def update(self):
        "The ball moves"
        global ball
        global ball_x, ball_y

        # sull'asse x Va verso sinistra
        if ball_x == "left":
            # sottraggo perchè vado a sinistra
            ball.xb -= vel_bal
            # se arriva a 10 rimbalza
            if ball.xb < 10:
                ball_x = "right"
        # va in basso
        if ball_y == 'down':
            # allora aumenta y quando va in basso (parte da 0 in alto)
            ball.yb += vel_bal
        if ball_y == 'up':
            # quando va in alto tolgo
            ball.yb -= vel_bal
            # se arriva in cima rimbalza in basso
            if ball.yb < 10:
                ball_y = 'down'
        # se va a destra aumenta x
        if ball_x == "right":
            ball.xb += vel_bal
            # a 480 rimbalza verso sinistra
            if ball.xb > 480:
                ball_x = "left"
        gfxdraw.filled_circle(screen, ball.xb, ball.yb, 5, GREEN)
        self.rect = pygame.Rect(self.xb, self.yb, 10, 10)


def collision():
    global ball, bar, ball_y

    if ball.rect.colliderect(bar):
        print("Collision detected")
        ball_y = "up"
        print(ball_y)
        print(ball.yb)
        speed_up()

    for brick in bricks:
        if ball.rect.colliderect(brick):
            if ball_y == "up":
                ball_y = "down"
            else:
                ball_y = "up"

    if ball.yb > 500:
        ball.xb, ball.yb = 500, 300


def exit(event):
    global loop

    if event.type == pygame.QUIT:
        loop = 0
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_ESCAPE:
            loop = 0
    return loop


def speed_up():
    global bar, vel_bal
    bar.x = pygame.mouse.get_pos()[0]
    if startx == bar.x:
        vel_bal = 2
        print("Normal speed")
    else:
        vel_bal = 3
        print("Speed up")


def create_bricks():
    "The bricks scheme"
    blist = """
11001
11111
01111
01010
""".splitlines()[1:]
    bricks = []
    h = 30
    w = 0
    for line in blist:
        for brick in line:
            if brick == "1":
                bricks.append(Brick(20 + w * 100, h))
            w += 1
            if w == 5:
                w = 0
                h += 50
    return bricks

def show_bricks():
    for brick in bricks:
        brick.update()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ball_x = 'left'
ball_y = 'down'
scorep1 = 0
scorep2 = 0
vel_bal = 2
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Game")
startx = 0
bar = Bar(10, 480)
ball = Ball(100, 100)
bricks = create_bricks()
pygame.mouse.set_visible(False)
loop = 1
while loop:
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        loop = exit(event)
    if pygame.mouse.get_pos()[0] > 10 and pygame.mouse.get_pos()[0] < 430:
        bar.x = pygame.mouse.get_pos()[0]
    ball.update()
    bar.update()
    collision()
    startx = bar.x
    show_bricks()
    pygame.display.update()
    clock.tick(120)


pygame.quit()