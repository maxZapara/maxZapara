from typing import Any
import pygame
import random

pygame.init()
black = (0,0,0)
red = (255,0,0)
green = (152,251,152)
brown = (139,0,0)
white = (255,255,255)

width=600
height =500

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([w,h])
        self.image.fill('darkgreen')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class CARASEK(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('caras.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx=0
        self.dy=0
    def update(self):
        keys = pygame.key.get_pressed()
        self.dx=0
        self.dy=0
        if keys[pygame.K_RIGHT] and self.rect.x<width-55:
            self.dx=8       
        if keys[pygame.K_LEFT] and self.rect.x<width:
            self.dx=-8 
        if keys[pygame.K_DOWN] and self.rect.y<height-55:
            self.dy=8
        if keys[pygame.K_UP] and self.rect.y<height:
            self.dy=-8      
        self.rect.x+=self.dx
        walls_collide = pygame.sprite.spritecollide(self,walls_group,False)
        for i in walls_collide:
            if self.dx<0:
                self.rect.left = i.rect.right
            if self.dx>0:
                self.rect.right = i.rect.left
        
        self.rect.y+=self.dy
        walls_collide = pygame.sprite.spritecollide(self,walls_group,False)
        for i in walls_collide:
            if self.dy<0:
                self.rect.top = i.rect.bottom
            if self.dy>0:
                self.rect.bottom = i.rect.top
        if self.rect.collidepoint(okyn.rect.center):
            self.kill()
        if self.rect.collidepoint(kryk.rect.center):
            self.kill()
        if self.rect.collidepoint(gryk.rect.center):
            self.kill()
        if self.rect.collidepoint(jryk.rect.center):
            self.kill()

class BigBred(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('vodoroslya.png')
        self.Image = pygame.image.load('bred.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx=0
        self.dy=0
    def update(self):
        if pygame.sprite.collide_rect(self,caras):
            self.kill()
        
class Okyn(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('okyn.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx=3
        self.dy=0
    def update(self):
        self.rect.x+=self.dx
        if pygame.sprite.spritecollide(self,walls_group,False):
            self.dx=-self.dx 
            self.image=pygame.transform.flip(self.image,True,False)

class Kryk(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('kryk.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx=3
        self.dy=0

t = 10 #ширина стінок
wall_coords = [
    [0,0, t, height],
    [0,200,50,t],
    [width-t,0,t,height],
    [300,300,t,height],
    [0,0,width,t],
    [0,height-t,width,t],
    [160,0,t,200],
    [350,200,height,t],
    [450,2,t,100],
    [100,350,100,t],
    [150,350,t,50]
    

    #тут допишіть координати для побудови інших стін лабіринту
]
#створюємо групу спрайтів - стін
walls_group = pygame.sprite.Group()

caras_group= pygame.sprite.Group()
caras=CARASEK(470,50)
caras_group.add(caras)

bred_group= pygame.sprite.Group()
bred=BigBred(50,400)
bred_group.add(bred)
vred=BigBred(200,200)
bred_group.add(vred)
fred=BigBred(100,100)
bred_group.add(fred)
kred=BigBred(400,400)
bred_group.add(kred)

okyn_group= pygame.sprite.Group()
okyn=Okyn(250,250)
okyn_group.add(okyn)

kryk_group= pygame.sprite.Group()
kryk=Kryk(100,100)
kryk_group.add(kryk)

gryk=Kryk(200,200)
kryk_group.add(gryk)

jryk=Kryk(200,200)
kryk_group.add(jryk)

for c in wall_coords:
    wall = Wall (c[0], c[1], c[2], c[3])
    walls_group.add(wall)

size_window = (width, height)
window = pygame.display.set_mode(size_window)
pygame.display.set_caption('Game ')
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if random.randint(1,70)==1:
        jryk.rect.center=(random.randint(0,width),random.randint(0,height))
    if len(caras_group)<1:
        break
    window.fill ('blue')
    walls_group.draw(window)
    caras_group.draw(window)
    bred_group.draw(window)
    okyn_group.draw(window)
    kryk_group.draw(window)
    caras_group.update()
    bred_group.update()
    okyn_group.update()

    pygame.display.update()
    pygame.time.delay(50)
    
pygame.quit()