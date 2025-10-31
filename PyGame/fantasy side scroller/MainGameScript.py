#this is my test comment to show how github works
#other comment



import pygame as pg
import os
##import random

#init
pg.init()

screen = pg.display.set_mode((880, 660))

#main menu
background_menu = pg.image.load("resources/spookybackground.png")
font = pg.font.Font('freesansbold.ttf', 36)

hmo1 = (20, 250, 40)
hmo2 = (140, 50, 80)
def main_menu_items(mo1, mo2):
    global hmo1, hmo2

    if mo1 == True:
        hmo1 = (20, 250, 40)
    else:
        hmo1 = (20, 140, 90)
    if mo2 == True:
        hmo2 = (250, 50, 50)
    else:
        hmo2 = (140, 50, 80)

    m1textX = 350
    m1textY = 250
    m1 = font.render("New Game", True, hmo1)
    screen.blit(m1, (m1textX, m1textY))
    m2textX = m1textX
    m2textY = 320
    m2 = font.render("Exit Game", True, hmo2)
    screen.blit(m2, (m2textX, m2textY))

#file debug check
if os.path.abspath("resources/spookybackground.png") and os.path.exists("resources/spookybackground.png"):
    print("checked file is ok")
else:
    print("something is wrong with this file")

#title bar
pg.display.set_caption("The Leaves")
ulicon = pg.image.load("resources/maple-leaf(1).png")
pg.display.set_icon(ulicon)
##ulicon = pg.image.load("")
##pg.set_icon(ulicon)

#Game

#Game images
starting1bg = pg.image.load("resources/startarea1.png")
playerufo = pg.image.load("resources/characters/ufo.png")
playerImg = playerufo
#Player position
playerX = 50
playerY = 600
CplayerX = 0
CplayerY = 0
def player(x, y):
    screen.blit(playerImg, (x, y))

#keyboard input assignment 
right = pg.K_RIGHT
left = pg.K_LEFT
up = pg.K_UP
down = pg.K_DOWN
sbar = pg.K_SPACE
enter = pg.K_RETURN

#functions
def moLoop(o1, o2):
    global mo1, mo2
    if o1 == False:
        mo1 = True
        mo2 = False
    elif o2 == False:
        mo1 = False
        mo2 = True

#Loop running
main_menu = True
game_running = True

#Menu Loop
mo1 = True
mo2 = False

while main_menu:
    #background test
    screen.blit(background_menu, (0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            main_menu = False
            game_running = False
        if event.type == pg.KEYDOWN:
            if event.key == enter and mo1 == True:
                main_menu = False
            elif event.key == enter and mo2 == True:
                main_menu = False
                game_running = False
            if event.key == down:
                moLoop(mo1, mo2)
            elif event.key == up:
                moLoop(mo1, mo2)
    #menu items
    main_menu_items(mo1, mo2)
    pg.display.update()

#Game Loop
gbg = starting1bg

while game_running:
    screen.blit(gbg, (0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_running = False
        #acceleration of player
        if event.type == pg.KEYDOWN:
            if event.key == up:
                CplayerY = -1.0
            elif event.key == down:
                CplayerY = 1.0
            if event.key == left:
                CplayerX = -1.1
            elif event.key == right:
                CplayerX = 1.1
        if event.type == pg.KEYUP:
            if event.key == left or event.key == right:
                CplayerX = 0
            if event.key == up or event.key == down:
                CplayerY = 0
    
    #player position
    playerX += CplayerX
    playerY += CplayerY
    #image printing
    player(playerX, playerY)    

    pg.display.update()
