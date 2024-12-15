import pygame
from random import randint
from math import *
pygame.init()
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (200, 0, 0)
YELLOW = (0, 0, 200)
GREEN = (0, 200, 0)
blockSize = 60
rng = 5
WINDOW_HEIGHT = rng*blockSize
WINDOW_WIDTH = rng*blockSize

badshipx = randint(1,rng)
badshipy = randint(1,rng)

shipx = int(input("choose the x of your ship"))
shipy = int(input("choose the y of your ship"))

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

dis=pygame.display.set_caption("game grid")

clock = pygame.time.Clock()

from pygame.locals import(
    KEYDOWN,
    K_ESCAPE,
    QUIT,
    MOUSEBUTTONUP,
)

def drawGrid():
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)


running = True

class BadGuess(pygame.sprite.Sprite):
    def __init__(self):
        super(BadGuess, self).__init__()
        self.surf = pygame.Surface((blockSize, blockSize))
        self.surf.fill(GREEN)
        self.rect = self.surf.get_rect()

class Guess(pygame.sprite.Sprite):
    def __init__(self):
        super(Guess, self).__init__()
        self.surf = pygame.Surface((blockSize, blockSize))
        self.surf.fill(YELLOW)
        self.rect = self.surf.get_rect()

class BadShip(pygame.sprite.Sprite):
    def __init__(self):
        super(BadShip, self).__init__()
        self.surf = pygame.Surface((blockSize, blockSize))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect()

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.surf = pygame.Surface((blockSize, blockSize))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()

ship = Ship()
badship = BadShip()
guess = Guess()
badguess = BadGuess()
while running:
    drawGrid()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        
        elif event.type == MOUSEBUTTONUP:
            guessx,guessy = pygame.mouse.get_pos()
            guessx = ceil(guessx/blockSize)
            guessy = ceil(guessy/blockSize)
            print("you guess is : ",guessx,guessy)
            screen.blit(guess.surf, ((guessx-1)*blockSize, (guessy-1)*blockSize))
            if guessx == badshipx:
                if guessy == badshipy:
                    print("you found the ship at :",guessx,guessy)
                    screen.blit(badship.surf, ((badshipx-1)*blockSize, (badshipy-1)*blockSize))

            badguessx = randint(1,rng)
            badguessy = randint(1,rng)
            print("the ennemy guessed :",badguessx,badguessy)
            screen.blit(badguess.surf, ((badguessx-1)*blockSize, (badguessy-1)*blockSize))
            if badguessx == shipx:
                if badguessy == shipy:
                    print("you loose, your ship has been found at :",shipx,shipy)
                    screen.blit(badship.surf, ((badshipx-1)*blockSize, (badshipy-1)*blockSize))
                    
        elif event.type == pygame.QUIT:
            running = False
    screen.blit(ship.surf, ((shipx-1)*blockSize, (shipy-1)*blockSize))
    pygame.display.update()
    

