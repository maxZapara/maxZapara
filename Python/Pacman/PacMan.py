import pygame
import random

pygame.init()
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)

width=800
height=660

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

class Eat(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Eat.png')
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self):
        if self.rect.collidepoint(pman.rect.centerx,pman.rect.centery):
            self.kill()

class SuperEat(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Supereat.png')
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self):
        if self.rect.collidepoint(pman.rect.centerx,pman.rect.centery):
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Pacman1.png')
        self.rect = self.image.get_rect(topleft=(x,y))
        self.dxy=0
        self.speed=5
    def update(self):
        keys = pygame.key.get_pressed()
        '''if (((keys[pygame.K_RIGHT]) and self.rect.x<width-25 and self.rect.y % 25 == 0) or (self turn an 'r' and self.rect.y % 25 == 0)):
            self.dxy=self.speed
            self.turn
            selt.detolt_ images 0 n self.defolt_images [1]
            e11f (Keys [pygane.K_RIGHT] or keys[pygane.K_dJ) and self.rect.xwidth-25:'''
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
        walls_collide = pygame.sprite.spritecollide(self,brick_group,False)
        for i in walls_collide:
            if self.dxy==-1:
                self.rect.left = i.rect.right
            if self.dxy==1:
                self.rect.right = i.rect.left
            if self.dxy==-2:
                self.rect.top = i.rect.bottom
            if self.dxy==2:
                self.rect.bottom = i.rect.top
        


with open('lvl1.txt') as f:
    map = f.readlines()

pman_group= pygame.sprite.Group()
pman=Player(100,100)
pman_group.add(pman)

brick_group=pygame.sprite.Group()

eat_group=pygame.sprite.Group()

superEat_group=pygame.sprite.Group()

x=0
y=0

for i in map:
    for c in i:
        if c=='-':
            brick=Brick(x,y)
            brick_group.add(brick)
        elif c==' ':
            eat=Eat(x,y)
            eat_group.add(eat)
        elif c=='+':
            supereat=SuperEat(x,y)
            superEat_group.add(supereat)
        
        x+=20
    x=0
    y+=20

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill (black)
    eat_group.draw(window)
    eat_group.update()
    superEat_group.draw(window)
    superEat_group.update()
    pman_group.draw(window)
    pman_group.update()
    brick_group.draw(window)
    
    pygame.time.delay(50)
    pygame.display.update()

pygame.quit()