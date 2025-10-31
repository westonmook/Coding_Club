import pygame as pg
import random


#always initialize
pg.init()

screen = pg.display.set_mode((800, 600))

#background image
background = pg.image.load('resources/bg1.jpg')

#sound
###mixer.music.load('filename.wav')
##-1 is a musical loop
## var = mixer.Sound('filename.wav') for calling smaller sounds
## var.play()
###mixer.music.play(-1)

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
alienImg = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
q_of_aliens = 8
#alien_t_switch = 0
#old variables
for i in range(q_of_aliens):
    alienImg.append(pg.image.load('resources/alien.png'))
    alienX.append(random.randint(0, 800))
    alienY.append(random.randint(20, 150))
    alienX_change.append(0.3)
    alienY_change.append(0)

#Laser
laserImg = pg.image.load('resources/substract.png')
laserX = 0
laserY = 480
cannon_posR = 43
cannon_posL = -2
cannon_pos = 0
    #cannon
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

#alien explosion
explosionImg = pg.image.load('resources/explode.png')

#Scoring
score = 0
##font always .ttf
font = pg.font.Font('freesansbold.ttf', 36)
textX = 10
textY = 10
def show_score(x, y):
    scorer = font.render("Aliens Obliterated : " + str(score), True, (75, 205, 95))
    screen.blit(scorer, (x, y))

#Game Over
GOfont = pg.font.Font('freesansbold.ttf', 80)
def game_over():
    gotext = font.render("Aliens Obliterated... YOU!", True, (245, 205, 95))
    screen.blit(gotext, (250,300))

#Alien function
def alien(x, y, i):
    screen.blit(alienImg[i], (x, y))

def alien_respawn(i):
    global alienX, alienY, alien_t_switch
    #alien_t_switch += 1
    #if alien_t_switch == 3:
        #alienImg[i] = pg.image.load('resources/alien2.png')
    alienX[i] = random.randint(0, 800)
    alienY[i] = random.randint(20, 200)

#Laser function
def fire_laser(x, y):
    screen.blit(laserImg, (x + cannon_pos, y + 10))

#collision
def isCollision(alienX, alienY, laserX, laserY, i):
    distance = ((alienX - laserX)**2 + (alienY - laserY)**2)**0.5
    if distance < 24:
        return True
    else:
        return False

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
    for i in range(q_of_aliens):

        #Game Over
        if alienY[i] > 640:
            for j in range(q_of_aliens):
                alienY[j] = 2000
            game_over()
            break

        alienX[i] += alienX_change[i]
        if alienX[i] <= -20:
            alienX_change[i] = 0.2
            alienY[i] +=25
        elif alienX[i] >= 756:
            alienX_change[i] = -0.2
            alienY[i] += 35

        #collision
        collision = isCollision(alienX[i], alienY[i], laserX, laserY, i)
        if collision:
            laserY = 480
            laser_state = "ready"
            score += 1
            #print("your score is: " + str(score))
            alien_respawn(i)
        alien(alienX[i], alienY[i], i)

    #image printing
    player(playerX, playerY)
    
    #laser movement
    if laser_state == "fire":
        laserY -= laserY_change
        fire_laser(laserX, laserY)
        if laserY < -60:
            laser_state = "ready"
    #score
    show_score(textX, textY)

    pg.display.update()
    