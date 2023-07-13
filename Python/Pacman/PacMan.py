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
pygame.display.set_caption('PacMan')

animRight=['PacmanRight.png','PacmanRight2.png','PacmanCircle.png']
animLeft=['PacmanLeft.png','PacmanLeft2.png','PacmanCircle.png']
animUp=['PacmanUp.png','PacmanUp2.png','PacmanCircle.png']
animDown=['PacmanDown.png','PacmanDown2.png','PacmanCircle.png']

ghostV=['ghostRed.png','ghostBlue.png','ghostOrange.png','ghostPink.png','ghostBlue-_-.png','ghostWhite-_-.png','ghostGreen-_-.png','ghostYellow.png']

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
            pman.score+=1

class SuperEat(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Supereat.png')
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self):
        if self.rect.collidepoint(pman.rect.centerx,pman.rect.centery):
            self.kill()
            pman.score+=10

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('PacmanRight.png')
        self.rect = self.image.get_rect(topleft=(x,y))
        self.dxy=0
        self.speed=5
        self.animCount=0
        self.score=0
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
            self.image = pygame.image.load(animRight[int(self.animCount)%3])
        if self.dxy==-1:
            self.rect.x+=-self.speed
            self.image = pygame.image.load(animLeft[int(self.animCount)%3])
        if self.dxy==2:
            self.rect.y+=self.speed
            self.image = pygame.image.load(animDown[int(self.animCount)%3])
        if self.dxy==-2:
            self.rect.y+=-self.speed
            self.image = pygame.image.load(animUp[int(self.animCount)%3])
        
        self.animCount+=0.4
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
        if pygame.sprite.spritecollide(self,ghost_group,False):
            self.kill()
        

class Ghost(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.i=random.randint(0,len(ghostV)-1)
        self.image=pygame.image.load(ghostV[self.i])
        self.rect = self.image.get_rect(topleft=(x,y))
        self.dxy=random.choice([1,-1,2,-2])
        self.speed=3
        self.ty=0
    def update(self):
        if self.dxy==1:
            self.rect.x+=self.speed
    #        self.image = pygame.image.load(animRight[int(self.animCount)%3])
        elif self.dxy==-1:
            self.rect.x+=-self.speed
   #         self.image = pygame.image.load(animLeft[int(self.animCount)%3])
        elif self.dxy==2:
            self.rect.y+=self.speed
  #          self.image = pygame.image.load(animDown[int(self.animCount)%3])
        elif self.dxy==-2:
            self.rect.y+=-self.speed
 #           self.image = pygame.image.load(animUp[int(self.animCount)%3])
        self.ty+=1
        if self.ty==90:
            self.dxy=random.choice([-1,1,2,-2])
            self.ty=0
      #  self.animCount+=0.4
    
        walls_collide = pygame.sprite.spritecollide(self,brick_group,False)
        for i in walls_collide:
            if self.dxy==-1:
                self.rect.left = i.rect.right
                self.dxy=random.choice([1,2,-2]) 
            elif self.dxy==1:
                self.rect.right = i.rect.left
                self.dxy=random.choice([-1,2,-2])
            elif self.dxy==-2:
                self.rect.top = i.rect.bottom
                self.dxy=random.choice([1,-1,-2])
            elif self.dxy==2:
                self.rect.bottom = i.rect.top
                self.dxy=random.choice([1,-1,2])


with open('lvl1.txt') as f:
    map = f.readlines()

pman_group= pygame.sprite.Group()
pman=Player(100,100)
pman_group.add(pman)

ghost_group=pygame.sprite.Group()

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
        elif c=='g':
            ghost=Ghost(x,y)
            ghost_group.add(ghost)
        x+=20
    x=0
    y+=20

font = pygame.font.SysFont('mvboli', 25,False, False)

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
    ghost_group.draw(window)
    ghost_group.update()
    brick_group.draw(window)
    text1 = ' Pacman Score-'+str(pman.score)
    text_image = font.render(text1, True, pygame.Color('Blue'))
    window.blit(text_image,(-10,-10))
    
    pygame.time.delay(50)
    pygame.display.update()

pygame.quit()