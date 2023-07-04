import pygame
import random

pygame.init()
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)

width=600
height=540

size_window = (width, height)
window = pygame.display.set_mode(size_window)
pygame.display.set_caption('Game ')

width1=4290
height1 =540

def jump(y):
    global make_jump, jump_count
    if jump_count>=-30:
        y-=jump_count/2.5
        jump_count-=1
        print('gg')
    else:
        jump_count=30
        make_jump=False
    return y


jump_count=30
make_jump=False

pygame.display.set_caption('SuperMario by MZ4')

class Brick(pygame.sprite.Sprite):
    def __init__(self,poss,group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.image = pygame.image.load('brick.png')
        self.rect = self.image.get_rect(topleft=poss)
    def update(self,poss):
        window.blit(self.image,poss)

class Steals(pygame.sprite.Sprite):
    def __init__(self,poss,group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.image = pygame.image.load('Steals.png')
        self.rect = self.image.get_rect(topleft=poss)
    def update(self,poss):
        window.blit(self.image,poss)


class Question(pygame.sprite.Sprite):
    def __init__(self,poss,group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.image = pygame.image.load('Question.png')
        self.rect = self.image.get_rect(topleft=poss)
        self.use=False
    def update(self,poss):
        if pygame.sprite.spritecollide(self,mario_group,False) and not self.use:
            mario.score+=1
            print(mario.score)
            self.image = pygame.image.load('block.png')
            self.use=True
        window.blit(self.image,poss)



class Mario(pygame.sprite.Sprite):
    def __init__(self,poss,group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.image = pygame.image.load('din1.png')
        self.rect = self.image.get_rect(topleft=poss)
        self.dx=0
        self.dy=0
        self.ySpeed=0.1
        self.score=0
        self.jump=False
        self.easy=5
    def update(self,poss):
        global make_jump
        self.dx=0
        self.dy=0
        
        brick_collide=pygame.sprite.spritecollide(self,brick_group,False)
        # if brick_collide:
        #     self.ySpeed=0
        #     print(brick_collide)
        #     print(f'## y={self.rect.y}, x={self.rect.x}')
        #     #self.rect.y-=1
        #     #self.collideWallY(brick_collide)
        # else:
        #     self.rect.y+=self.ySpeed
        #     self.ySpeed+=0.1
        #     print(f'## y={self.rect.y}, x={self.rect.x}')
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP_4]:
            self.dx=-1
        if keys[pygame.K_KP_6]:
            self.dx=1
        if keys[pygame.K_KP_8]:
            self.dy=-1
        if keys[pygame.K_KP_5]:
            self.dy=1
        self.rect.x+=self.dx*10
        self.collideWallX(brick_collide)
        self.rect.y+=self.dy*self.easy
        self.collideWallY(brick_collide)
        self.Jump()

        #brick_collide_after_processing=pygame.sprite.spritecollide(self,brick_group,False)
        #if not brick_collide_after_processing:
        window.blit(self.image,poss)

    def collideWallX(self, brick_collide):
        brick_collide = pygame.sprite.spritecollide(self,brick_group,False)
        question_collide = pygame.sprite.spritecollide(self,question_group,False)
        for i in brick_collide:
            if self.dx==-1:
                self.rect.left = i.rect.right
            elif self.dx==1:
                self.rect.right = i.rect.left
        for u in question_collide:
            if self.dy==-1:
                self.rect.top = u.rect.bottom
            elif self.dy==1 or self.dy==0:
                self.rect.bottom = u.rect.top
    def collideWallY(self, brick_collide):
        brick_collide = pygame.sprite.spritecollide(self,brick_group,False)
        question_collide = pygame.sprite.spritecollide(self,question_group,False)
        if len(brick_collide):
            self.ySpeed=0
   #         print(brick_collide)
     #       print(f'## y={self.rect.y}, x={self.rect.x}')
            self.rect.y-=0.1
            #self.collideWallY(brick_collide)
        else:
            self.rect.y+=self.ySpeed
            self.ySpeed+=0.1
            #print(f'## y={self.rect.y}, x={self.rect.x}')

        for i in brick_collide:
            if self.dy==-1:
                self.rect.top = i.rect.bottom
            elif self.dy==1 or self.dy==0:
                 self.rect.bottom = i.rect.top
    def Jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            self.jump=True
        if self.jump==True:
            self.easy=7
        if keys[pygame.K_q]:
            self.ySpeed=0
 #      for u in question_collide:
  #         if self.dy==-1:
   #              self.rect.top = u.rect.bottom
    #        elif self.dy==1 or self.dy==0:
     #           self.rect.bottom = u.rect.top
    
            

'''class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        #зчитуємо розміри екрану та визначаємо координати центра
        self.display = pygame.display.get_surface()
        self.x = 0
        self.y = 0
        self.width_2 = self.display.get_size()[0] // 2
  #      self.height_2 = self.display.get_size()[1] // 2

    def center_camera(self, player):
        #встановлюємо координати камери на головного героя
        self.x = player.rect.centerx - self.width_2
  #      self.y = player.rect.centery - self.height_2
        self.y=player.rect.y
'''
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.x = 0
        self.y = 0
        self.width_2 = self.display.get_size()[0] // 2
        #self.height_2 = self.display.get_size()[1] // 2

    def center_camera(self, player):
        self.x = player.rect.centerx - self.width_2
        #self.y = player.rect.centery - self.height_2

    def draw_sprite(self, spritik):
        self.center_camera(spritik)
        for sprite in self.sprites():
            pos_x = sprite.rect.x - self.x
            #pos_y = sprite.rect.y - self.y
            sprite.update((pos_x,sprite.rect.y))

    def draw_sprite1(self, spritik):
        self.center_camera(spritik)
        # показуємо усі справйти з групи у нових координатах
        for sprite in self.sprites():
            pos_x = sprite.rect.x - self.x
  #          pos_y = sprite.rect.y - self.y
            sprite.update((pos_x,sprite.rect.y))
'''''''''''''''''''''    def center_camera(self, player):
        if not((self.x <= 5) and (player.rect.centerx - self.width_2 < self.x)) and not((self.x >= size-width-5) and (player.rect.centerx - self.width_2 > self.x)):
            self.x = player.rect.centerx - self.width_2'''''''''''''''''''''
        #self.y = player.rect.centery - self.height_2

with open('lvl1.txt') as f:
    map = f.readlines()

camera_group=CameraGroup()

brick_group=pygame.sprite.Group()
steals_group=pygame.sprite.Group()
question_group=pygame.sprite.Group()
mario_group=pygame.sprite.Group()
mario=Mario((50,50),camera_group)
mario_group.add(mario)
x=-50
y=0
for i in map:
    for c in i:
        if c=='-':
            brick=Brick((x,y),camera_group)
            brick_group.add(brick)
        elif c=='?':
            question=Question((x,y),camera_group)
            question_group.add(question)
        elif c=='#':
            steals=Steals((x,y),camera_group)
            steals_group.add(steals)
        x+=30
    x=-50
    y+=30

font = pygame.font.SysFont('mvboli', 25,False, False)

font2 = pygame.font.SysFont('mvboli', 50,False, False)

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    window.fill (black)

    text1 = ' Mario Score-'+str(mario.score)
    text_image = font.render(text1, True, pygame.Color('white'))
    
    text2 = ' Victory!!!!!!'
    text_image2 = font2.render(text2, True, pygame.Color('Yellow'))

    if make_jump:
        jump(mario.rect.y)
    camera_group.draw_sprite(mario)
    window.blit (text_image, (0,20))
    if mario.score==30:
        window.blit (text_image2, (200,200))
    '''brick_group.draw(window)
    question_group.draw(window)
    mario_group.draw(window)'''
    pygame.display.update()
    pygame.time.delay(50)


pygame.quit()