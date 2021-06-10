import pygame
from Dic import *
from Values import *

def BackGround(ongame, Gameover):

    if not Gameover:
        if ongame: # 게임 진행 중
            bg = []
            bg.append(pygame.image.load(img_Dic+'bg.jpg'))
            bg.append( pygame.image.load(img_Dic+'bg.jpg'))
        else :  # 게임 대기 화면
            bg = pygame.image.load(img_Dic + 'Ready.png')

    else:
        bg = pygame.image.load(img_Dic + 'gameover.jpg')

        #bg.append(pygame.image.load(img_Dic+'bg3_gameover.png'))

    return bg