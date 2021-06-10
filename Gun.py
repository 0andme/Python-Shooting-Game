import pygame
from Dic import *
from Values import *
from System import *


mis = pygame.image.load(img_gunDic+'gunShoot.png')

class projectile(object):
    def __init__(self,x,y,facing):
        self.x = x
        self.y = y
        self.radius = 20 #총알의 반지름
        self.size=40 # 총알 이미지 크기
        self.facing = facing # 총알의 증가 방향
        self.vel = 10  * facing #총알 이동 거리

    def draw(self,screen):
        screen.blit(mis, (self.x-self.radius, self.y-self.radius))
