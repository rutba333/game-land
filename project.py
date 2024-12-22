import math
import pygame
import random
from pygame import mixer 

#initialize pygame
pygame.init()

#Constants
SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=2
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27

#create the screen
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#Background
background=pygame.image.load('bg.webp')

#sound 
mixer.music.load('background.mp3')
mixer.music.play(-1)#loop the background music indefinetly

#caption and icon
pygame.display.set_caption("Space invader")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player
playerImg=pygame.image.load('player.png')
playerX=PLAYER_START_X
playerY=PLAYER_START_Y
playerX_change=0

#Enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,SCREEN_WIDTH-64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

#bullet
bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=playerY
bulletX_change=BULLET_SPEED_Y
bullet_state="ready"

#score
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10


#game over text
over_font=pygame.font.Font('freesansbold.ttf',64)

#FPS control
clock=pygame.time.Clock()


def show_score(x,y):
    score=font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
    

def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))


def player(x,y):
    screen.blit(playerImg,(x,y))


def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))


def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))
