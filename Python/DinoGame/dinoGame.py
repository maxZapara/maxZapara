import pygame
import random
import time

pygame.init()

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
animCount=0
x=100
y=195
kx=40066
ky=219
ox=400
oy=50
ox2=0
ox3=300
speed=7
ovwer=30
spedo1=2
spedo=1
score=0

yroven=0

sped=7

bg = pygame.image.load('nev yorc1.jpg')
plaer1 = pygame.image.load('din1.png')
plaer2 = pygame.image.load('din2.png')
plaer3 = pygame.image.load('din3.png')
plaer4 = pygame.image.load('dinozloi.png')
cactys1 = pygame.image.load('kak1.png')
cactys2 = pygame.image.load('kak2.png')
cactys3 = pygame.image.load('kak3.png')
cactys4 = pygame.image.load('kak4.png')
cactys5 = pygame.image.load('kak5.png')
cactys6 = pygame.image.load('kak6.png')
cactys7 = pygame.image.load('kak7.png')
cactys8 = pygame.image.load('kak8.png')
oblak = pygame.image.load('oblak.png')
GO = pygame.image.load('G over.png')
bg1 = pygame.image.load('bground.png')
click_sound = pygame.mixer.Sound('ydar.mp3')
topok=pygame.mixer.Sound('toptop.mp3')
pygame.mixer.music.load('fon.mp3')
pygame.mixer.music.play (-1)
pygame.mixer.music.set_volume(0.3)
click_sound = pygame.mixer.Sound ('no-no-no.wav')
click_ound = pygame.mixer.Sound ('beg.wav') 

kn=random.randint(0,2)

walkLeft = [pygame.image.load('din1.png'), pygame.image.load('din2.png'), pygame.image.load('din3.png'), pygame.image.load('dinozloi.png')]
cactysList = [pygame.image.load('kak1.png'), pygame.image.load('kak2.png'), pygame.image.load('kak3.png'), pygame.image.load('kak4.png'), pygame.image.load('kak5.png'), pygame.image.load('kak6.png'), pygame.image.load('kak7.png'), pygame.image.load('kak8.png')]
bglist = [pygame.image.load('bground.png'),pygame.image.load('nev yorc1.jpg'),pygame.image.load('otcrN1d.jpg'),pygame.image.load('otcrN2.jpg')]

def restart():
    global sped
    global ovwer
    global spedo
    global spedo1
    global speed
    global x
    global y
    global kx
    global ky
    global ox
    global ox2
    global ox3
    global oy
    global animCount
    global score
    global yroven

    animCount=0
    x=100
    y=195
    kx=400
    ky=219
    ox=400
    oy=50
    ox2=0
    ox3=300
    speed=7
    ovwer=30
    spedo1=2
    spedo=1
    score=0
    yroven=0
    sped=7

width=700
height=400


make_jump=False
size_window = (width, height)
window = pygame.display.set_mode(size_window)
pygame.display.set_caption('Game ')
run=True

def jump():
    global make_jump, y, jump_count
    if jump_count>=-20:
        y-=jump_count/2.5
        jump_count-=1
    else:
        jump_count=20
        make_jump=False


jump_count=20
make_jump=False

font = pygame.font.SysFont('mvboli', 25,False, False)

font2 = pygame.font.SysFont('mvboli', 25,False, False)

def nado():
    if 0<1:
        time.sleep(3)
        window.blit(bglist[2],(0, 0))

while run:
    window.blit(bglist[1],(0, 0))
    
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if not make_jump:
        window.blit(walkLeft[animCount % 3], (x, y))
        animCount += 1
#        pygame.mixer.Sound.play (topok)
    else:
        window.blit(plaer1, (x, y))
    kx-=sped
    ox-=spedo1
    ox3-=spedo1
    ox2-=spedo
    if ox<-100:
        ox=800
    if ox2<-100:
        ox2=800
    if ox3<-100:
        ox3=800
    if kx<0:
        kx=700
        kn=random.randint(0,7)
        yroven+=1
        score+=1
        print('Рахунок',score)
        if kn==3 or kn==4 or kn==7:
            ky-=10
        else:
            ky=219
    if yroven==2:
        yroven-=3
        sped+=1
        print(sped)
    if keys[pygame.K_SPACE] and ovwer>=0:
        make_jump=True
        pygame.mixer.Sound.play (click_ound)
    if make_jump==True:
        jump()
    if x<kx<x+70 and y<ky<y+75:
        ovwer-=1
        print('Життя:',ovwer)
        pygame.mixer.Sound.play (click_sound)
    text2='HP-'+str(ovwer)
    text_image2 = font2.render(text2, True, pygame.Color('black'))
    window.blit (text_image2, (0, 0))

    text1 = 'Score-'+str(score)
    text_image = font.render(text1, True, pygame.Color('black'))
    window.blit (text_image, (0,20))

#         pygame.mixer.music.set_volume(0.3)
#        pygame.mixer.Sound.play (click_sound)
    if ovwer<=0:
        window.blit(GO,(100,100))
        sped=0
        spedo=0
        spedo1=0
        window.blit(walkLeft[3], (x, y))
        animCount=0
        make_jump=False
        kx=300
        y=195
        if keys[pygame.K_ESCAPE]:
            restart()
        score=0
        
    if score>=20:
        window.blit(bglist[0],(0, 0))
        sped=10
        ovwer=1
        if not make_jump:
            window.blit(walkLeft[animCount % 3], (x, y))
            animCount += 1
        else:
            window.blit(plaer1, (x, y))
        
        text2='HP-'+str(ovwer)
        text_image2 = font2.render(text2, True, pygame.Color('black'))
        window.blit (text_image2, (0,0))

        text1 = 'Score-'+str(score)
        text_image = font.render(text1, True, pygame.Color('black'))
        window.blit (text_image, (0,20))

#S DR
#    for i in range(1):
 #       if score>=5:
            #nado()
 #           window.blit(bglist[3],(0, 0))
            #window.blit(bglist[2],(0, 0))
# 
# 3          sped=0
   #         spedo1=0
    #        spedo=0
     #       ox=1111000
      #      ox2=10000
       #     ox3=119191991
            #nado()
        
       

    

    window.blit(oblak,(ox2,oy+50))
    window.blit(oblak,(ox3,oy-15))
    window.blit(oblak,(ox,oy))
    window.blit(cactysList[kn],(kx,ky))
#   window.blit(plaer1,(x,y)) 
#   window.fill (green)
    pygame.display.update()
    pygame.time.delay(50)




pygame.quit()