import pygame
from Dic import *
from Values import *
from System import  *

walkRight = [pygame.image.load(img_userDic+'R1.png'), pygame.image.load(img_userDic+'R2.png'), pygame.image.load(img_userDic+'R3.png'),
             pygame.image.load(img_userDic+'R4.png'), pygame.image.load(img_userDic+'R5.png'), pygame.image.load(img_userDic+'R6.png'),
             pygame.image.load(img_userDic+'R7.png'), pygame.image.load(img_userDic+'R8.png'), pygame.image.load(img_userDic+'R9.png')]
walkLeft = [pygame.image.load(img_userDic+'L1.png'), pygame.image.load(img_userDic+'L2.png'), pygame.image.load(img_userDic+'L3.png'),
            pygame.image.load(img_userDic+'L4.png'), pygame.image.load(img_userDic+'L5.png'), pygame.image.load(img_userDic+'L6.png'),
            pygame.image.load(img_userDic+'L7.png'), pygame.image.load(img_userDic+'L8.png'), pygame.image.load(img_userDic+'L9.png')]

char_standing=pygame.image.load(img_userDic+'standing.png')
img_health_bar_nohit=pygame.image.load(img_Dic+'health_bar_nohit.png')
img_health_bar_hit=pygame.image.load(img_Dic+'health_bar_hit.png')

class player(object):
    # 플레이어 변수들
    def __init__(self, x, y, width, height): # x 좌표, y 좌표, 가로 크기, 세로 크기
        self.x = x

        self.y = y
        self.width = width
        self.height = height
        self.vel = 10 # 이동 폭
        # 현재 방향
        self.left = False
        self.right = False
        self.walkCount = 0
        # 점프상태 플래그
        self.isJump = False
        self.jumpCount = 10
        # 서있는 상태 플래그
        self.standing = True
        self.hited =False
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)  # 타격 박스
        self.health = player_Health # 주인공 체력

    # 플레이어 화면에 출력 관련
    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not (self.standing): #현재 움직이는 상태일 때
            if self.left:
                screen.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                screen.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.isJump:
                screen.blit(char_standing, (self.x, self.y)) # 점프하는 이미지
            else: # 아무 버튼도 눌리지 않은 상태 일 때
                screen.blit(char_standing, (self.x, self.y))
        else: # 현재 정지 상태 일 때
            if self.right:
                screen.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                screen.blit(walkLeft[0], (self.x, self.y))
            elif self.isJump:
                screen.blit(char_standing, (self.x, self.y)) # 점프하는 이미지
            else:
                screen.blit(char_standing, (self.x, self.y)) # 가만히 서있는 이미지
        self.hitbox = (self.x , self.y , player_W, player_H)  # 상위 왼쪽 X, 상위 왼쪽 y, 가로, 세로

        # draw 체력 바 / (스크린, 칼라, (x ,y 좌표, 길이, 두께))
        if self.hited:
            screen.blit(img_health_bar_hit, (img_Health_barX, img_Health_barY))
            color = (255, 0, 0) # red
            self.hited=False
        else:
            screen.blit(img_health_bar_nohit, (img_Health_barX, img_Health_barY))
            color = (0, 128, 0)  # green

        pygame.draw.rect(screen,color, (player_Health_barX, player_Health_barY , self.health, player_Health_barH))

    # 젤리와 충돌했을 때 함수
    def hit(self):
        self.health-=del_Health                                # 현재 체력에서 del_Health 만큼 감소
        self.hited=True
        font1 = pygame.font.SysFont('comicsans', 50)           # 폰트 설정 (폰트 이름,크기)
        text = font1.render(str(-del_score), 1, (255, 0, 0))              # (텍스트, 부드럽게, 색상(red) )
        screen.blit(text, (self.hitbox[0], self.hitbox[1]-50)) # (텍스트, 캐릭터 x좌표, 캐릭터 좌표 위로 50)
        #pygame.display.update()                                # 변경 사항 스크린에 표시
        #pygame.time.delay(10)
        if self.health<=0:
            return True
