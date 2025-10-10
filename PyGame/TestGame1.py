import pygame as pg

#always initialize
pg.init()
#menu
screen = pg.display.set_mode((800, 600))
#title bar
pg.display.set_caption("Space Invaders")
icon = pg.image.load("./resources/play.png")
pg.display.set_icon(icon)
#Player
playerImg = pg.image.load('./resources/spaceship.png')
playerX = 370
playerY = 480
def player(x, y):
    screen.blit(playerImg, (x, y))
#Game loop
running = True
right = pg.K_RIGHT
left = pg.K_LEFT
playerX_change = 0
while running:
    screen.fill((0, 40, 70))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        #Keystroke <,>
        if event.type == pg.KEYDOWN:
            if event.key == left:
                    playerX_change = -0.5
            if event.key == right:
                playerX_change = 0.5
        if event.type == pg.KEYUP:
            if event.key == left or event.key == right:
                playerX_change = 0

    playerX += playerX_change
    player(playerX, playerY)
    pg.display.update()
    