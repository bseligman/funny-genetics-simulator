#imports
from lib2to3.pytree import Base
import pygame
import random
import time
from pygame.locals import *
 
#########################################
#initlization, config
pygame.init()
clock = pygame.time.Clock()
vec = pygame.math.Vector2  #2D (Vector2)
HEIGHT = 700
WIDTH = 700
FPS = 60
FramePerSec = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation")

startanicon = 10
#########################################

#Color vars
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#simple class setup
class BaseSur:
    #mutations
    Mut_SIZE = 0
    Mut_HP = 0
    Mut_ATK = 0
    Mut_SPE = 0

    #base stats, and how they calculate
    size = 1 + Mut_SIZE
    health = size * 1.25 + Mut_HP
    attack = size * 1.33 + Mut_ATK
    speed = health * 1.03 + Mut_SPE

    #extra
    posX = random.randint(0,700)
    posY = random.randint(0,700)

#########################################
#generate starting animals
countnam = 0
for i in range(startanicon):
    tempname = "animal" + str(countnam)
    print(tempname)
    tempname = BaseSur()
    countnam += 1
print(BaseSur)

#gameloop
while True:
    #setups
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    #game stuff
    screen.fill(RED)

    #draw animals
    countnam = 0
    for i in range(startanicon):
        tempname = "animal" + str(countnam)
        pygame.draw.rect(screen, BLACK, pygame.Rect(tempname.posX, tempname.posY, tempname.Mut_SIZE,  tempname.Mut_SIZE))
        countnam += 1
    BaseSur.health = 1

    #update
    pygame.display.update()
#########################################
