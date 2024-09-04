import pygame
from pygame.locals import *
import random
import json

#Declare Global Vars
FPS = 60
SCREEN_WIDTH = 864
SCREEN_HEIGHT = 936
RUN = True
CLOCK = pygame.time.Clock()
#creates background
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load('background.png')
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    pygame.init()
    runner()

def runner():
    global RUN
    while RUN:
        CLOCK.tick(FPS)
        screen.blit(bg, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
    pygame.quit()


if __name__ == "__main__":
    main()