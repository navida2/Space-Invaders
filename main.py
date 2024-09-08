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
laser_frequency = 1000
last_laser = pygame.time.get_ticks() - laser_frequency
#creates background
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load('background.png')
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

class ships(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.velocity = 7
        self.x = x
        self. y = y
        self.image = pygame.image.load('ship2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,70))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def update(self):
        keys = pygame.key.get_pressed()
        if not game_over:
            if keys[K_RIGHT]:
                self.rect.x += self.velocity
                #print(self.rect.topright[0])
            if keys[K_LEFT]:
                #print(self.rect.topleft[0])
                self.rect.x += -self.velocity
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH


class laser(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('lazer.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 815
        self.velocity = 5
    def update(self):
        if self.rect.bottom < 0:
            self.kill()
        self.rect.y -= self.velocity


class rock(pygame.sprite.Sprite):
    def __init__(self, x, size_multiplier, speed_multiplier):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('rock.png').convert_alpha()
        self.x = x
        self.velocity = 1.5 * speed_multiplier
        self.size_multiplier = size_multiplier
        self.speed_multiplier = speed_multiplier
        self.image = pygame.transform.scale(self.image, (10*self.size_multiplier, 10 *self.size_multiplier))
        self.image.get_rect()
    
    def __random__(self):
        nums = [1,2,3]
        weights = [7,2,1]
        return random.choices(nums, weights,k=1)[0]

ship_group = pygame.sprite.Group()
ship = ships(SCREEN_WIDTH // 2 - 50, 820)
ship_group.add(ship)
laser_group = pygame.sprite.Group()
# lasers = laser(ship.rect.center[0] - 50)
# laser_group.add(lasers)


def main():
    pygame.init()
    runner()

def runner():
    global RUN
    global last_laser
    while RUN:
        CLOCK.tick(FPS)
        screen.blit(bg, (0,0))
        
        laser_group.draw(screen)
        laser_group.update()
        ship_group.draw(screen)
        ship_group.update()
        pygame.display.update()
        if not game_over:
            time_now = pygame.time.get_ticks()
            if time_now - last_laser > laser_frequency:
                lasers = laser(ship.rect.center[0] - 5)
                laser_group.add(lasers)
                last_laser = time_now
        laser_group.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

    pygame.quit()


if __name__ == "__main__":
    main()
    