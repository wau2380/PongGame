import pygame, sys
import random
from pygame.locals import *
from math import *

pygame.init()
screen=pygame.display.set_mode((600,400))
WHITE=(255,255,255) ; Hello = (255,100,255)
BLACK = (0,0,0)
FPS = pygame.time.Clock()
size=screen.get_size()

class Ball:
    def __init__(self):
        # self.direction = (pi/3)+(pi/3)*random.random() 
        # self.direction += random.randint(0,1)*pi;
        self.direction = radians(90)
        self.dx=int( 10*sin(self.direction) )
        self.dy=int( 10*cos(self.direction) )
        self.x=size[0]//2 #screen size의 반
        self.y=size[1]//2
        self.r=10

            
    def setNextPosition(self,bars):
            
            if self.x>(size[0]-20) or self.x<20: 
              self.x=size[0]//2 #screen size의 반
              self.y=size[1]//2
            
            if self.y>(size[1]-20) or self.y<20:
                self.dy *= -1
                
            if (self.x <= (bars[0].bx+15) and bars[0].by-40 <= self.y and bars[0].by+40 >= self.y ):
              self.direction = radians((bars[0].by-self.y)+90)
              print(self.direction)
              self.dx=int( 10*sin(self.direction) )
              self.dy=int( 10*cos(self.direction) )
              #self.dx *= -1
             
              
            if (self.x >= (bars[1].bx-15) and (bars[1].by-40) <= self.y and (bars[1].by+40) >= self.y):
              self.direction = radians((bars[1].by-self.y)+90)
              self.dx=int( 10*sin(self.direction) )
              self.dy=int( 10*cos(self.direction) )
              self.dx *= -1
           

            self.x += self.dx
            self.y += self.dy
    def draw(self):
        pygame.draw.circle(screen,BLACK,(self.x, self.y),self.r,0)

class Bar:
    def __init__(self,kb,x):
        self.kb=kb
        self.bx=x
        self.by=size[1]//2

    def move(self,pk): #pressed_keys
        if pk[self.kb[0]]:
            self.by-=10
        if pk[self.kb[1]]:
            self.by+=10
     #drawing
        pygame.draw.line(screen, Hello,(self.bx, self.by-40),(self.bx,self.by+40),6)


#Bar객체를 생성하여 Bars리스트에 담기
Bars = [Bar((K_a,K_z),10),  Bar((K_k, K_m),590) ]
B = Ball()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressedKey=pygame.key.get_pressed()
    screen.fill(WHITE)
     
    #입력된 키를 이용하여 Bar를 화면에 보여주는 코드 작성하기 
    for b in Bars:
        b.move(pressedKey)
        
        
    B.setNextPosition(Bars)
    B.draw()
    
    pygame.display.update()
    FPS.tick(24)
