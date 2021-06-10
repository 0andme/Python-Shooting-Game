import pygame
from Dic import *
from Values import *
from System import *


class Jelly(object):
    global walkRight, walkLeft,jelly_ex
    def __init__(self, x, y, num,width, height, end):
        self.x = x
        self.y =y
        self.xx=x
        self.xy=y/x
        self.yy=y
        self.end = end
        self.num = num
        self.score=(num+1)*50
        self.width = width
        self.height = height
        self.path = [x, end]        # 젤리의 이동 반경
        self.path_Widith = end-x    # 이동 반경의 넓이
        self.walkCount = 0
        self.vel = -3                # 걸음 방향, 속도
        self.hitbox = (self.x, self.y, jelly_W, jelly_H)  # hit 박스
        self.health = health_Jelly
        self.die=False

        self.visible = True
        self.walkRight = [pygame.image.load(img_jellyDic[self.num] + 'R1E.png'),
                     pygame.image.load(img_jellyDic[self.num] + 'R2E.png'),
                     pygame.image.load(img_jellyDic[self.num] + 'R3E.png'),
                     pygame.image.load(img_jellyDic[self.num] + 'R4E.png'),
                     pygame.image.load(img_jellyDic[self.num] + 'R5E.png'),
                     pygame.image.load(img_jellyDic[self.num] + 'R6E.png'),
                     pygame.image.load(img_jellyDic[self.num] + 'R7E.png'),
                     pygame.image.load(img_jellyDic[self.num] + 'R8E.png'),
                     pygame.image.load(img_jellyDic[self.num] + 'R9E.png'),
                     pygame.image.load(img_jellyDic[self.num] + 'R10E.png'),
                     pygame.image.load(img_jellyDic[self.num] + 'R11E.png')]
        self.walkLeft = [pygame.image.load(img_jellyDic[self.num] + 'L1E.png'),
                    pygame.image.load(img_jellyDic[self.num] + 'L2E.png'),
                    pygame.image.load(img_jellyDic[self.num] + 'L3E.png'),
                    pygame.image.load(img_jellyDic[self.num] + 'L4E.png'),
                    pygame.image.load(img_jellyDic[self.num] + 'L5E.png'),
                    pygame.image.load(img_jellyDic[self.num] + 'L6E.png'),
                    pygame.image.load(img_jellyDic[self.num] + 'L7E.png'),
                    pygame.image.load(img_jellyDic[self.num] + 'L8E.png'),
                    pygame.image.load(img_jellyDic[self.num] + 'L9E.png'),
                    pygame.image.load(img_jellyDic[self.num] + 'L10E.png'),
                    pygame.image.load(img_jellyDic[self.num] + 'L11E.png')]
        self.jelly_ex = pygame.image.load(img_jellyDic[num] + 'explosion1.png')
        self.jelly_health=[pygame.image.load(img_Dic + 'jelly_health0.png'),pygame.image.load(img_Dic + 'jelly_health1.png')]


    # 젤리 스크린에 출력
    def draw(self, screen):
        self.move()
        
        if self.visible :# 젤리가 스크린에 보여질 상태이면 == 안 죽었으면
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                screen.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                screen.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            if self.health<=health_Jelly/2:
                screen.blit(self.jelly_health[0], (self.x, self.y-20))
                #pygame.draw.rect(screen,  GREEN, (self.hitbox[0], self.hitbox[1] - 20, jelly_W, 10))  # 전체 체력 바 / x y 좌표, 가로, 세로
            else:
                screen.blit(self.jelly_health[1], (self.x, self.y-20))
                #pygame.draw.rect(screen,RED,(self.hitbox[0], self.hitbox[1] - 20, jelly_W - (5 * (10 - self.health)), 10)) # 현재 체력 표시 바 50픽셀안에 표시
            self.hitbox = (self.x , self.y , jelly_W, jelly_H)
        if self.die:
            # 젤리가 죽었을 때
            screen.blit(self.jelly_ex, (self.x, self.y))  # 폭발 이미지로 변경




    def move(self):
        if self.vel < 0:
            if self.x>0:
                #self.vel=-self.vel
                self.x+=self.vel
                self.y = -self.xy * (self.x -self.xx ) + self.yy

    # 젤리가 맞았을 때
    def hited(self):
        # hitSound.play()
        self.health -= Atk
        if self.health<=0:
            self.visible = False
            self.die=True



