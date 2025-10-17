import pygame as pg
import random
#always initialize
pg.init()
#menu
screen = pg.display.set_mode((800, 600))
#background image
background = pg.image.load('resources/bg1.jpg')

#title bar
pg.display.set_caption("Space Invaders")
ulicon = pg.image.load("resources/play.png")
pg.display.set_icon(ulicon)
#Player
playerImg = pg.image.load('resources/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
#player function
def player(x, y):
    screen.blit(playerImg, (x, y))
#Alien
alienImg = pg.image.load('resources/alien.png')
alienX = random.randint(0, 800)
alienY = random.randint(20, 150)
alienX_change = 0.3
alienY_change = 0

#Laser
laserImg = pg.image.load('resources/substract.png')
laserX = 0
laserY = 480
cannon_posR = 43
cannon_posL = -2
cannon_pos = 0
def cannon_alt():
    global cannon_pos
    if cannon_pos == cannon_posL:
        cannon_pos = cannon_posR
    elif cannon_pos == cannon_posR:
        cannon_pos = cannon_posL
    else:
        cannon_pos = cannon_posR
###laserX_change = 0
laserY_change = 0.5
laser_state = "ready"

#Alien function
def alien(x, y):
    screen.blit(alienImg, (x, y))

#Laser function
def fire_laser(x, y):
    screen.blit(laserImg, (x + cannon_pos, y + 10))

#keyboard input assignment
running = True
right = pg.K_RIGHT
left = pg.K_LEFT
sbar = pg.K_SPACE
#Game loop
while running:
    #screen.fill((0, 40, 70))
    #bg1
    screen.blit(background, (0, 0))
    #events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        #Keystroke <,>
        if event.type == pg.KEYDOWN:
            if event.key == left:
                    playerX_change = -0.5
            if event.key == right:
                playerX_change = 0.5
            if event.key == sbar:
                if laser_state == "ready":
                    laserX = playerX
                    laserY = 480
                    cannon_alt()
                    laser_state = "fire"
        if event.type == pg.KEYUP:
            if event.key == left or event.key == right:
                playerX_change = 0
   
    #player boundary
    playerX += playerX_change
    if playerX <= -20:
        playerX = 756
    elif playerX >= 756:
        playerX = -20
    #alien boundary
    alienX += alienX_change
    if alienX <= -20:
        alienX_change = 0.2
        alienY +=25
    elif alienX >= 756:
        alienX_change = -0.2
        alienY += 25
    #image printing
    player(playerX, playerY)
    alien(alienX, alienY)
    #laser movement
    if laser_state == "fire":
        laserY -= laserY_change
        fire_laser(laserX, laserY)
        if laserY < -60:
            laser_state = "ready"
    pg.display.update()
    