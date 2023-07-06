import pygame
import random

pygame.init()
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)

width=600
height =500

size_window = (width, height)
window = pygame.display.set_mode(size_window)
pygame.display.set_caption('Game ')


class Brick(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('brick.png')
        self.rect = self.image.get_rect(topleft=(x,y))
'''    def update(self,poss):
        window.blit(self.image,poss)'''

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Pacman.png')
        self.rect = self.image.get_rect(topleft=(x,y))
        self.dxy=0
        self.speed=3
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.dxy=1       
        if keys[pygame.K_LEFT]:
            self.dxy=-1 
        if keys[pygame.K_DOWN]:
            self.dxy=2
        if keys[pygame.K_UP]:
            self.dxy=-2
        if self.dxy==1:
            self.rect.x+=self.speed
        if self.dxy==-1:
            self.rect.x+=-self.speed
        if self.dxy==2:
            self.rect.y+=self.speed
        if self.dxy==-2:
            self.rect.y+=-self.speed
        


with open('lvl2.txt') as f:
    map = f.readlines()

pman_group= pygame.sprite.Group()
pman=Player(100,100)
pman_group.add(pman)

brick_group=pygame.sprite.Group()

x=0
y=0

for i in map:
    for c in i:
        if c=='-':
            brick=Brick(x,y)
            brick_group.add(brick)
        x+=15
    x=0
    y+=15

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill (black)
    pman_group.draw(window)
    pman_group.update()
    brick_group.draw(window)
    pygame.time.delay(50)
    pygame.display.update()

pygame.quit()