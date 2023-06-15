import pygame
import random
import math
from datetime import datetime

#configs


pygame.init()
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
startTime = datetime.now()

class Configs:

    screenWidth=1000
    screenHeight=1000
    screenSize=2000
    victoryCondition = 0
    agarInitialSize = 32
    minVgarInitialSize = 20
    maxVgarInitialSize = 45
    ballSize = 10
    timeLimit = 180
    vgarSpeed=[10,-10,9,-9,8,-8,7,-7,6,-6,5,-5]

    dontHighlighVgars = True
    keysUp= [pygame.K_UP, pygame.K_w,pygame.K_KP_8]
    keysDown=[pygame.K_DOWN,pygame.K_s,pygame.K_KP_5]
    keysLeft=[pygame.K_LEFT,pygame.K_a,pygame.K_KP_4]
    keysRight=[pygame.K_RIGHT,pygame.K_d,pygame.K_KP_6]
    vgarLifes=3
    #   keys = pygame.key.get_pressed()

color=['yellow','green','red','blue','orange','grey','brown','purple','sky blue','dimgray','forest green','pink','tomato','olive','black']

size_window = (Configs().screenWidth,Configs().screenHeight)
window = pygame.display.set_mode(size_window)
pygame.display.set_caption('Game MaxAgar')


        
class NameGenerator:
    def __init__(self):
        self.names3=['Їжачок',"Слоник","Максик","Хробак","Крот","Врагар","Котик","Карасик","Шарик","Голуб","Сокіл","Байбак","Суслик","Порося","Паладін","Мустанг","Телега","Комар"]
        self.names2=["Веселий","Злий","Кульгавий","Дотепний","Кмітливий","Швидкий","Лінивий","Сильний","Добрий","Прожорливий","Просто",""]
        self.names1=["Дуже","Трохи","Зовсім","Ледве","Майже","Не","Помірно","Повністю","","","Не дуже","+-"]
        self.name = f'{random.choice(self.names1)} {random.choice(self.names2)} {random.choice(self.names3)}' 
               
class Ball(pygame.sprite.Sprite):
    def __init__(self,poss,j):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(j)
        self.size=Configs().ballSize
        self.color=random.choice(color)
        self.image = pygame.Surface([self.size,self.size])
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=poss)
    def update(self,poss):
        radius = self.size/2*math.sqrt(2)
        if pygame.sprite.collide_rect(self,agar):
            self.rect.x=random.randint(-Configs().screenSize,Configs().screenSize)
            self.rect.y=random.randint(-Configs().screenSize,Configs().screenSize)
            agar.size+=0.5
            print(f'@@@@ My new rating: {agar.countRating(vgar_group)} from {len(vgar_group)}')
        lvl=pygame.sprite.spritecollide(self,vgar_group,False)
        for u in lvl:
            u.size+=0.9
            self.rect.x=random.randint(-Configs().screenSize,Configs().screenSize)
            self.rect.y=random.randint(-Configs().screenSize,Configs().screenSize)
        pygame.draw.circle(window,self.color,poss,radius)
            
class Agar(pygame.sprite.Sprite):
    def __init__(self,poss,g):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(g)
        self.size=Configs().agarInitialSize
        self.color=random.choice(color)
        self.image = pygame.Surface([self.size,self.size])
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=poss)
        self.font = pygame.font.Font('freesansbold.ttf', 15)

    def countRating(self,vgars):
        return sum(map(lambda x : x.size>self.size, vgars))
    
    def keyPressed(self, keysPressed, keysConfigured):
        for k in keysConfigured:
            if keysPressed[k] :
                return True
        return False
    
    def draw(self, poss):
        radius=self.size/2*math.sqrt(2)
        centerPos = (poss[0]+self.size/2,poss[1]+self.size/2)
        pygame.draw.circle(window,self.color,centerPos,radius)
        displayName=f'{round(self.size,2)}'
        text = self.font.render(displayName, True, pygame.Color('black'))
        textRect = text.get_rect()
        textRect.center = (centerPos[0],centerPos[1])
        window.blit(text, textRect)

    def update(self,poss):
        self.rect.update(self.rect.left,self.rect.top,self.size,self.size)

        keys = pygame.key.get_pressed()
        if self.keyPressed(keys, Configs.keysRight) and self.rect.x<=Configs().screenSize:
            self.rect.x+=7
        if self.keyPressed(keys, Configs.keysLeft) and self.rect.x>=-Configs().screenSize:
            self.rect.x-=7
        if self.keyPressed(keys, Configs.keysDown) and self.rect.y<=Configs().screenSize:
            self.rect.y+=7
        if self.keyPressed(keys, Configs.keysUp) and self.rect.y>=-Configs().screenSize:
            self.rect.y-=7
       
        lwl=pygame.sprite.spritecollide(self,vgar_group,False)
        for h in lwl:
            if self.size<=h.size:
                h.size+=(self.size/3)
                self.size=30
                self.rect.x=random.randint(-Configs().screenSize,Configs().screenSize)
                self.rect.y=random.randint(-Configs().screenSize,Configs().screenSize)
                print(f'$#%&@!! Мене проглотив {h.name}! New size {h.size}')
            if self.size>h.size:
                self.size+=(h.size/6)
                h.size=random.randint(20,45)
                h.killVgar()
                print(f'(^_^) Я проглотив {h.name}! New size {self.size}. My rating: {self.countRating(vgar_group)}')
  #              h.rect.x=random.randint(-size,size)
   #             h.rect.y=random.randint(-size,size)
 
        self.draw(poss)
        
class Vragar(pygame.sprite.Sprite):
    def __init__(self,poss,group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.size=random.randint(Configs().minVgarInitialSize,Configs().maxVgarInitialSize)
        self.color=random.choice(color)
        self.image = pygame.Surface([self.size,self.size])
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=poss)
        self.speedx=random.choice(Configs().vgarSpeed)
        self.speedy=random.choice(Configs().vgarSpeed)
        self.name=NameGenerator().name
        self.lifes=Configs().vgarLifes
        self.font = pygame.font.Font('freesansbold.ttf', 15)

    def draw(self, poss):
        pygame.draw.circle(window,self.color,poss,self.size/2*math.sqrt(2))
        displayName=f'{self.name} [{round(self.size,2)} ({self.lifes})]'
        if self.size < agar.size or Configs.dontHighlighVgars :
            color = 'white'
        else :
            color = 'red' 

        text = self.font.render(displayName, True, pygame.Color(color))
        textRect = text.get_rect()
        textRect.center = (poss[0],poss[1])
        window.blit(text, textRect)

    def killVgar(self):
        self.lifes-=1
        if self.lifes==0:
            self.kill()
        else:
            self.rect.x=random.randint(-Configs().screenSize,Configs().screenSize)
            self.rect.y=random.randint(-Configs().screenSize,Configs().screenSize)
            self.size=random.randint(20,45)

        
    def update(self,poss):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy 
        self.draw(poss)

        if self.rect.x>=Configs().screenSize or self.rect.x<=-Configs().screenSize:
            self.speedx=-self.speedx
        if self.rect.y>=Configs().screenSize or self.rect.y<=-Configs().screenSize:
            self.speedy=-self.speedy
        intersection=pygame.sprite.spritecollide(self,vgar_group,False)
        for v in intersection:
            if self.size<v.size:
                v.size+=(self.size/4)
                self.size=30
                self.killVgar()
            if self.size>v.size:
                self.size+=(v.size/4)
                v.kill()
      #          v.size=random.randint(20,45)
  #              v.rect.x=random.randint(-size,size)
 #               v.rect.y=random.randint(-size,size)
                print(f'{self.name} проглотив {v.name}! New size {self.size}')

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.x = 0
        self.y = 0
        self.width_2 = self.display.get_size()[0] // 2
        self.height_2 = self.display.get_size()[1] // 2

    def center_camera(self, player):
        self.x = player.rect.centerx - self.width_2
        self.y = player.rect.centery - self.height_2

    def draw_sprite(self, spritik):
        self.center_camera(spritik)
        for sprite in self.sprites():
            pos_x = sprite.rect.x - self.x
            pos_y = sprite.rect.y - self.y
            sprite.update((pos_x,pos_y))

camera=CameraGroup()


ball_group= pygame.sprite.Group()
for i in range(3500):
    x=random.randint(-Configs().screenSize,Configs().screenSize)
    y=random.randint(-Configs().screenSize,Configs().screenSize)
    ball=Ball((x,y),camera)
    ball_group.add(ball)

agar_group= pygame.sprite.Group()
agar=Agar((x,y),camera)
agar_group.add(agar)

vgar_group= pygame.sprite.Group()
for i in range(300):
    x=random.randint(-Configs().screenSize,Configs().screenSize)
    y=random.randint(-Configs().screenSize,Configs().screenSize)
    vgar=Vragar((x,y),camera)
    vgar_group.add(vgar)


run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    font = pygame.font.SysFont('veranda', 25,False, False)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_9]:
        Configs.dontHighlighVgars = False
        print('k9')
    if keys[pygame.K_0]:
       Configs.dontHighlighVgars = True
       print('k0')

    window.fill (black)

    camera.draw_sprite(agar)
    currentRating = agar.countRating(vgar_group)
    timeLeft = Configs().timeLimit - (datetime.now() - startTime).seconds

    textScore =f'My agar size:  {str(round(agar.size,2))}. Vgars left: {len(vgar_group)}. My rating: {currentRating}. Time left: {timeLeft} sec'
    textScoreImage = font.render(textScore, True, pygame.Color('white'))
    window.blit (textScoreImage, (10,10))

    if (currentRating == Configs().victoryCondition):
        run=False
        victoryFont = pygame.font.SysFont('veranda', 45,False, False)
        textVictory =f'VICTORY!!!!'
        textVictoryImage = victoryFont.render(textVictory, True, pygame.Color('red'))
        window.blit (textVictoryImage, (Configs().screenHeight * 0.4, Configs().screenHeight/2 - 50))
        textStats =f'My agar size:  {str(round(agar.size,2))}. Vgars left: {len(vgar_group)}. Time spent: {(datetime.now() - startTime).seconds} sec'
        textStatsImage = victoryFont.render(textStats, True, pygame.Color('red'))
        window.blit (textStatsImage, (Configs().screenHeight * 0.05, Configs().screenHeight/2 + 50))
    
    if timeLeft < 0:
        run=False
        victoryFont = pygame.font.SysFont('veranda', 45,False, False)
        textVictory =f'GAME OVER!!!!'
        textVictoryImage = victoryFont.render(textVictory, True, pygame.Color('grey'))
        window.blit (textVictoryImage, (Configs().screenHeight * 0.4, Configs().screenHeight/2 - 50))
        textStats =f'My agar size:  {str(round(agar.size,2))}. Vgars left: {len(vgar_group)}. My rating: {currentRating}'
        textStatsImage = victoryFont.render(textStats, True, pygame.Color('grey'))
        window.blit (textStatsImage, (Configs().screenHeight * 0.15, Configs().screenHeight/2 + 50))

    pygame.display.update()
    pygame.time.delay(50)

run=True
while run:
    pygame.time.delay(50)
pygame.quit()