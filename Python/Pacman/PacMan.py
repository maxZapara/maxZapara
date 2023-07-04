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

with open('lvl2.txt') as f:
    map = f.readlines()


brick_group=pygame.sprite.Group()

x=0
y=0

for i in map:
    for c in i:
        if c=='-':
            brick=Brick(x,y)
            brick_group.add(brick)
        x+=30
    x=-50
    y+=30

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill (black)
    brick_group.draw(window)
    pygame.time.delay(50)
    pygame.display.update()

pygame.quit()