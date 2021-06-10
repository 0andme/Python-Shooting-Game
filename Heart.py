import pygame
from Dic import *
from Values import *
from System import *


img_Heart_RED = pygame.image.load(img_Dic+'heart_red.png')
img_Heart_BLACK = pygame.image.load(img_Dic+'heart_black.png')

class Heart(object):
    def __init__(self,x,y,die):
        self.x = x
        self.y = y
        self.die=die

    def draw(self, screen):

        if not self.die:
            screen.blit(img_Heart_RED, (self.x, self.y))
        else:
            screen.blit(img_Heart_BLACK, (self.x, self.y))