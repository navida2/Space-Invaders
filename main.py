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
game_over = False
#creates background
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load('background.png')
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
# ship = pygame.image.load('ship2.png')
# ship = pygame.transform.scale(ship, (100,100))

class ships(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.velocity = 7
        self.x = x
        self. y = y
        self.image = pygame.image.load('ship2.png')
        self.image = pygame.transform.scale(self.image, (50,70))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def update(self):
        keys = pygame.key.get_pressed()
        if not game_over:
            if keys[K_RIGHT]:
                self.rect.x += self.velocity
                print(self.rect.topright[0])
            if keys[K_LEFT]:
                print(self.rect.topleft[0])
                self.rect.x += -self.velocity
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
ship_group = pygame.sprite.Group()
ship = ships(SCREEN_WIDTH // 2 - 50, 820)
ship_group.add(ship)

# class ship(pygame.sprite.Sprite):
#     def __init__(x, y):
#         pass

def main():
    pygame.init()
    runner()

def runner():
    global RUN
    while RUN:
        CLOCK.tick(FPS)
        screen.blit(bg, (0,0))
        ship_group.draw(screen)
        ship_group.update()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

    pygame.quit()


if __name__ == "__main__":
    main()
    