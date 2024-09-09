import pygame
from pygame.locals import *
import random
import json

#Declare Global Vars
pygame.init()
FPS = 60
SCREEN_WIDTH = 864
SCREEN_HEIGHT = 936
RUN = True
CLOCK = pygame.time.Clock()
game_over = False
laser_frequency = 500
rock_frequency = 2000
SCORE = 0
last_laser = pygame.time.get_ticks() - laser_frequency
last_rock = pygame.time.get_ticks() - rock_frequency

font = pygame.font.SysFont('Bauhaus 92', 60)
white = (255, 255, 255)
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
            if keys[K_LEFT]:
                self.rect.x += -self.velocity
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH


class laser(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('lazer.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 815
        self.velocity = 5
    def update(self):
        if self.rect.bottom < 0:
            self.kill()
        self.rect.y -= self.velocity


class rock(pygame.sprite.Sprite):
    def __init__(self, x, size_multiplier, speed_multiplier, rotate):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('rock.png').convert_alpha()
        self.x = x
        self.rotate = rotate
        self.velocity = 1 * speed_multiplier
        self.size_multiplier = size_multiplier
        self.speed_multiplier = speed_multiplier
        self.image = pygame.transform.scale(self.image, (40*self.size_multiplier, 40 *self.size_multiplier))
        self.image = pygame.transform.rotate(self.image, self.rotate)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = -20
    def update(self):
        if not (0 < self.rect.center[0] < 860):
            self.kill()
        if self.rect.y > 864:
            self.kill()
        self.rect.y += self.velocity
        colliding_lasers = pygame.sprite.spritecollide(self, laser_group, False)
        if colliding_lasers:
            # Remove the rock
            self.kill()
            global SCORE
            SCORE += 1
            # Remove all colliding lasers
            for laser in colliding_lasers:
                laser.kill()

def __random_weights__():
    nums = [1,2,3]
    weights = [7,2,1]
    return random.choices(nums, weights,k=1)[0]
def __random_location__():
    return random.randint(5,800)

def __random_rotatation__():
    return random.randint(0, 360)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

ship_group = pygame.sprite.Group()
ship = ships(SCREEN_WIDTH // 2 - 50, 820)
ship_group.add(ship)
laser_group = pygame.sprite.Group()
rock_group = pygame.sprite.Group()

class Button():
    def __init__(self, x, y, img):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        screen.blit(self.img, (self.rect.x, self.rect.y))
        return action


def main():
    
    runner()

def runner():
    global RUN
    global last_laser
    global last_rock
    global game_over
    global SCORE
    start_image = pygame.image.load('new-removebg-preview.png')
    start_image = pygame.transform.scale(start_image, (150, 150))
    start_button = Button(500, 500, start_image)
    started = False
    game_over = True
    while RUN:
        CLOCK.tick(FPS)

        screen.blit(bg, (0,0))
      
        logo = pygame.image.load('logo-removebg-preview.png')
        logo = pygame.transform.scale(logo, (500, 300))
    
        
        if not started:
            screen.blit(logo, (180, 0))
            if start_button.draw():
                game_over = False   
                started = True
                print("HI")
           
            
        
     
        if not game_over:
            rock_group.draw(screen)
            rock_group.update()
            laser_group.draw(screen)
            laser_group.update()
            ship_group.draw(screen)
            ship_group.update()
            
            draw_text(str(SCORE), font, white, int(SCREEN_WIDTH)/ 2, 20)
            time_now = pygame.time.get_ticks()
            if time_now - last_laser > laser_frequency:
                lasers = laser(ship.rect.center[0] - 11)
                laser_group.add(lasers)
                last_laser = time_now
            if time_now - last_rock > rock_frequency:
                for i in range(random.randint(1,6)):
                    rocks = rock(__random_location__(), __random_weights__(), __random_weights__(), __random_rotatation__())
                    rock_group.add(rocks)
                    last_rock = time_now
        if pygame.sprite.groupcollide(ship_group, rock_group, False, False):
            game_over = True
            rock_group.empty()
            laser_group.empty()
            started = False
            
        laser_group.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
    