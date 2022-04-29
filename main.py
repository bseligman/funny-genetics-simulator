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

#starting count of spawned entities
startanicon = 4
#########################################

#Color vars
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#simple class setup
class BaseSur:
    def __init__(self, Mut_SIZE, Mut_HP, Mut_ATK, Mut_SPE, size, health, attack, speed, posX, posY):
        #mutations
        self.Mut_SIZE = Mut_SIZE
        self.Mut_HP = Mut_HP
        self.Mut_ATK = Mut_ATK
        self.Mut_SPE = Mut_SPE

        #base stats, and how they calculate
        self.size = size * Mut_SIZE
        self.health = health + size * 1.25 + Mut_HP
        self.attack = attack + size * 1.33 + Mut_ATK
        self.speed = speed + health * 0.05 + Mut_SPE

        #extra
        self.posX = posX 
        self.posY = posY

#########################################
#generate starting animals
animal1 = BaseSur(50, 0, 0, 0, 1, 10, 2, 0, random.randint(0,700), random.randint(0,700))
animal2 = BaseSur(0, 0, 0, 0, 1, 10, 2, 0, random.randint(0,700), random.randint(0,700))
animal3 = BaseSur(0, 0, 0, 0, 1, 10, 2, 0, random.randint(0,700), random.randint(0,700))
animal4 = BaseSur(0, 0, 0, 0, 1, 10, 2, 0, random.randint(0,700), random.randint(0,700))

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
    pygame.draw.rect(screen, BLACK, pygame.Rect(animal1.posX, animal1.posY, animal1.Mut_SIZE,  animal1.Mut_SIZE))
    pygame.draw.rect(screen, BLACK, pygame.Rect(animal1.posX, animal1.posY, animal1.Mut_SIZE,  animal1.Mut_SIZE))
    pygame.draw.rect(screen, BLACK, pygame.Rect(animal1.posX, animal1.posY, animal1.Mut_SIZE,  animal1.Mut_SIZE))
    pygame.draw.rect(screen, BLACK, pygame.Rect(animal1.posX, animal1.posY, animal1.Mut_SIZE,  animal1.Mut_SIZE))

    #movement
    animal1.posX += random.randint(-10,10) * animal1.speed
    animal1.posY += random.randint(-10,10) * animal1.speed
    while animal1.posX > 650:
        animal1.posX = animal1.posX - 10.5 * animal1.speed
    while animal1.posY > 650:
        animal1.posY = animal1.posY - 10.5 * animal1.speed

    #check if touching

    #if touching food

    #if touching each other

    #update
    pygame.display.update()
#########################################