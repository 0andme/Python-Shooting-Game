import pygame
from Dic import *
from Values import *
from System import *


img_HealKit1=pygame.image.load(img_Dic+'HealKit1.png')  # 작은 사이즈
img_HealKit2=pygame.image.load(img_Dic+'HealKit2.png')
img_HealKit3=pygame.image.load(img_Dic+'HealKit3.png') # 큰 사이즈

class HealKit(object):
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.vel = 5
        self.num=num
        self.hitbox = (self.x, self.y, HealKitSize, HealKitSize)  # hit 박스
        self.geted=False
        self.size=HealSize-50*(3-num)

    def draw(self, screen):
        #self.move()
        if not self.geted: # 미획득시
            if self.num == 1:
                img_HealKit=img_HealKit1
            elif self.num == 2:
                img_HealKit = img_HealKit2
            elif self.num == 3:
                    img_HealKit = img_HealKit3

            screen.blit(img_HealKit, (self.x, self.y))
            #color = (0, 128, 0)
            #pygame.draw.rect(screen, color, (self.x, self.y,HealKitSize, HealKitSize))

    #def  move(self):
        #if not self.geted: # 미획득시
            #self.x-=self.vel

