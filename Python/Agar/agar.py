import pygame
import random
import math

pygame.init()
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)

width=1000
height=1000
size=2000
color=['yellow','green','red','blue','orange','grey','brown','purple','white','sky blue','dimgray','forest green','pink','tomato','olive','black']

vgarSpeed=[10,-10,8,-8,7,-7,6,-6,5,-5]

size_window = (width, height)
window = pygame.display.set_mode(size_window)
pygame.display.set_caption('Game MaxAgar')

class Ball(pygame.sprite.Sprite):
    def __init__(self,poss,j):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(j)
        self.size=10
        self.color=random.choice(color)
        self.image = pygame.Surface([self.size,self.size])
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=poss)
    def update(self,poss):
        radius = self.size/2*math.sqrt(2)
        if pygame.sprite.collide_rect(self,agar):
            self.rect.x=random.randint(-size,size)
            self.rect.y=random.randint(-size,size)
            agar.size+=0.5
        lvl=pygame.sprite.spritecollide(self,vgar_group,False)
        for u in lvl:
            u.size+=0.9
            self.rect.x=random.randint(-size,size)
            self.rect.y=random.randint(-size,size)
        pygame.draw.circle(window,self.color,poss,radius)
            
class Agar(pygame.sprite.Sprite):
    def __init__(self,poss,g):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(g)
        self.size=30
        self.color=random.choice(color)
        self.image = pygame.Surface([self.size,self.size])
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=poss)
    def update(self,poss):
        #self.rect.update(self.rect.left,self.rect.top,self.size,self.size)
       
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x<=size:
            self.rect.x+=7
        if keys[pygame.K_LEFT] and self.rect.x>=-size:
            self.rect.x-=7
        if keys[pygame.K_DOWN] and self.rect.y<=size:
            self.rect.y+=7
        if keys[pygame.K_UP] and self.rect.y>=-size:
            self.rect.y-=7
       
        lwl=pygame.sprite.spritecollide(self,vgar_group,False)
        for h in lwl:
            if self.size<=h.size:
                h.size+=(self.size/3)
                self.size=30
                self.rect.x=random.randint(-size,size)
                self.rect.y=random.randint(-size,size)
            if self.size>h.size:
                self.size+=(h.size/6)
                h.size=random.randint(20,45)
                h.rect.x=random.randint(-size,size)
                h.rect.y=random.randint(-size,size)

        radius=self.size/2*math.sqrt(2)
        
        centerPos = (poss[0]+self.size/2,poss[1]+self.size/2)
        pygame.draw.circle(window,self.color,centerPos,radius)



class Vragar(pygame.sprite.Sprite):
    def __init__(self,poss,group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.size=random.randint(20,45)
        self.color=random.choice(color)
        self.image = pygame.Surface([self.size,self.size])
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=poss)
        self.speedx=random.choice(vgarSpeed)
        self.speedy=random.choice(vgarSpeed)
    def update(self,poss):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy 
        pygame.draw.circle(window,self.color,poss,self.size/2*math.sqrt(2))
        if self.rect.x>=size or self.rect.x<=-size:
            self.speedx=-self.speedx
        if self.rect.y>=size or self.rect.y<=-size:
            self.speedy=-self.speedy
        lul=pygame.sprite.spritecollide(self,vgar_group,False)
        for f in lul:
            if self.size<f.size:
                print('yes')
                f.size+=(self.size/4)
                self.size=30
                self.rect.x=random.randint(-size,size)
                self.rect.y=random.randint(-size,size)
                
            if self.size>f.size:
                self.size+=(f.size/4)
                f.size=random.randint(20,45)
                f.rect.x=random.randint(-size,size)
                f.rect.y=random.randint(-size,size)
                


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        #зчитуємо розміри екрану та визначаємо координати центра
        self.display = pygame.display.get_surface()
        self.x = 0
        self.y = 0
        self.width_2 = self.display.get_size()[0] // 2
        self.height_2 = self.display.get_size()[1] // 2

    def center_camera(self, player):
        #встановлюємо координати камери на головного героя
        self.x = player.rect.centerx - self.width_2
        self.y = player.rect.centery - self.height_2

    def draw_sprite(self, spritik):
        self.center_camera(spritik)
        # показуємо усі справйти з групи у нових координатах
        for sprite in self.sprites():
            pos_x = sprite.rect.x - self.x
            pos_y = sprite.rect.y - self.y
            sprite.update((pos_x,pos_y))

camera=CameraGroup()


ball_group= pygame.sprite.Group()
for i in range(3500):
    x=random.randint(-size,size)
    y=random.randint(-size,size)
    ball=Ball((x,y),camera)
    ball_group.add(ball)

agar_group= pygame.sprite.Group()
agar=Agar((x,y),camera)
agar_group.add(agar)

vgar_group= pygame.sprite.Group()
for i in range(70):
    x=random.randint(-size,size)
    y=random.randint(-size,size)
    vgar=Vragar((x,y),camera)
    vgar_group.add(vgar)


run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    font = pygame.font.SysFont('veranda', 25,False, False)

    window.fill (black)

    
#    ball_group.update()
 #   ball_group.draw(window)
  #  vgar_group.update()
   # vgar_group.draw(window)
    #agar_group.update()
    #agar_group.draw(window)
    camera.draw_sprite(agar)
    text1 ='My agar size: ' +str(round(agar.size,2))
    text_image = font.render(text1, True, pygame.Color('white'))
    window.blit (text_image, (10,10))
#    s=10
 #   for o in range(70):
  #      s+=10
   #     for q in vgar_group:
    #        text2 = str(q.size)
     #       text_image = font.render(text2, True, pygame.Color('white'))
      #      window.blit (text_image, (600,10+s))

    
    pygame.display.update()
    pygame.time.delay(50)

pygame.quit()