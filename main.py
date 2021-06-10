import pygame
import sys
from datetime import *
import os

from System import *
from Sound import *
from Dic import *
from Values import *

from Background import *
from Gun import *
from Jelly import *
from Player import *
from  Heart import *
from  Healkit import *

# 스크린에 출력하는 함수------------------------------------------------------------------
def redrawGameWindow(jellys,x,y):
    background=BackGround(ongame,Gameover)
    screen.blit(background[0], (x, y)) # 배경화면 출력
    screen.blit(background[1], (x+screen_W, y))
    text = font_scorecnt.render(str(Score), 1, ORANGE) # 텍스트, anti-aliasing(읽기 쉽게 렌더링), 색깔

    text_score=font_scoretext.render('SCORE', 1, ORANGE)
    text_healready = font_healReady.render(str(time_readyCnt), 1, ORANGE)
    text_healTime = font_healTime.render(str(time_HealTimeCnt), 1, ORANGE)
    img_Heal_Ready_Time=pygame.image.load(img_Dic + 'Heal_Ready_Time.png')
    jelly_score=pygame.image.load(img_Dic+'jelly_score.png')
    man.draw(screen)                 # 주인공 출력.
    if Score==0:
        screen.blit(text, (score_X, score_Y))    # 점수 출력
    else:
        screen.blit(text, (score_X-30, score_Y))    # 점수 출력
    screen.blit(text_score, (score_X-30, score_Y-20))    # 점수 출력

    for bullet in bullets:          # 총알 출력
        bullet.draw(screen)

    for heart in hearts:            # 하트 출력
        heart.draw(screen)

    for num in range(0,jelly_Num):      #젤리 출력
            jellys[num].draw(screen)
    if inHeal:                      #힐 출력
        if Heal.geted:
            text_healSize = font_healSize.render('+' + str(Heal.size), 1, GREEN)
            screen.blit(text_healSize, (Heal.x, Heal.y))  # 점수 출력
        else:
            Heal.draw(screen)

    if time_readyCnt>=0 and readyHeal:#힐 타임 이미지 흑백 출력

        screen.blit(img_Heal_Ready_Time, (img_Health_barX + img_Health_barW + 25, img_Health_barY + 3))  # 힐 대기 이미지 출력
        if time_readyCnt//10 == 0:
            screen.blit(text_healready, (img_Health_barX+img_Health_barW+40, img_Health_barY+53)) # 힐 대기 시간 출력(0~9초)
        else:
            screen.blit(text_healready, (img_Health_barX+img_Health_barW+35, img_Health_barY+53)) # 힐 대기 시간 출력


    if time_HealTimeCnt>=0 and inHeal:
        screen.blit(text_healTime, (Heal.x+19, Heal.y-25)) # 힐 유지 시간 출력 / 포션 위에 출력

    screen.blit(jelly_score, (screen_W-250, 20))

    pygame.display.update() #변경 사항 갱신
# 메인 메뉴 함수-----------------------------------------------------------------------------

def menu():
    Gameover = False
    ongame = False

    while not ongame:
        # 창을 닫거나 Esc를 누르면 게임 종료
        for event in pygame.event.get():
            if event.type == pygame.QUIT :  # or event.type == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: # 마우스 클릭 시 화면 전환
                ongame =True
                return ongame

        background=BackGround(ongame,Gameover)
        screen.blit(background, (0, 0))
        pygame.display.update()

# main 함수-----------------------------------------------------------------------------

pygame.init()
# 폰트 설정 / 폰트 이름, 사이즈, 굵기 true

# 힐 포션 숫자 폰트 지정
font_healTime = pygame.font.SysFont("comicsans", 30, True, False)
font_healTime = pygame.font.SysFont("comicsans", 30, True, False)
font_healReady= pygame.font.SysFont("comicsans", 30, True, False)
#게임 내 스코어 폰트 지정(숫자)
font_scorecnt = pygame.font.SysFont("comicsans", 50, True,False)
# 게임 내  스코어 폰트 지정(문자)
font_scoretext = pygame.font.SysFont("comicsans",30, True,False)
# 힐 획득 시 증가되는 체력 폰트 지정
font_healSize=pygame.font.SysFont("comicsans",30, True,False)
# 게임 오버 화면 폰트지정
font_endScore = pygame.font.SysFont("comicsans", 50, True, False)
font_cnt = pygame.font.SysFont("comicsans", 100, True, False)


Gameover = False
ongame = False
makeHeal = True
readyHeal =False
Score = 0
bgX = 0
bgY = 0
hearts=[]
jellys=[]
jelly_num_now=jelly_Num
mandie=False
Heartcnt=Heart_cnt_start
time_readyHeal = datetime.now()
man = player(player_X, player_Y, player_W, player_H)

for i in range(0,Heart_cnt_max): # 하트 리스트 생성
    if i>=Heart_cnt_start:
        mandie=True
    else: mandie=False
    hearts.append(Heart(HeartX+i*HeartSize,HeartY,mandie))

for num in range(0,jelly_Num):
    jelly_X_Start = screen_W / 3 * 2  # 젤리 출현 최소 x
    jelly_X_End = screen_W - jelly_W  # 젤리 출현 최대
    jellyX = random.randrange(jelly_X_Start, jelly_X_End)
    jellyY = random.randrange(img_Health_barY + 50 + 30, player_Y)
    jellys.append(Jelly(jellyX,jellyY,num,jelly_W,jelly_H,jelly_X_End))
bullets = []
while not Gameover:
    clock.tick(120)
    gunloop = 0  # 총알이 다중으로 발사되는 것을 막기 위한 것
      # 총알 리스트 작성

    if ongame==False and Gameover==False:   # 메뉴화면
        ongame=menu()
        Score = 0
        bgX = 0
        bgY = 0
        mandie=False
        makeHeal=True
        inHeal=False
        readyHeal=False
        Heartcnt = Heart_cnt_start
        man = player(player_X, player_Y, player_W, player_H)
        bullets = []
        jelly_num_now=jelly_Num


    for num in range(0,jelly_Num):
        if not jellys[num].visible :  # 젤리가 없으면 젤리 재생성
            jelly_X_Start = screen_W/3*2  # 젤리 출현 최소 x
            jelly_X_End = screen_W - jelly_W  # 젤리 출현 최대
            jelly_X = random.randrange(jelly_X_Start, jelly_X_End)
            jelly_Y = random.randrange(img_Health_barY+50+30, player_Y)
            # x좌표, y좌표, 젤리 번호, 적 가로, 적 세로, 가능한 최고 x좌표
            del jellys[num]
            newjelly=Jelly(jelly_X,jelly_Y,num,jelly_W,jelly_H,jelly_X_End)
            jellys.insert(num,newjelly)

            redrawGameWindow(jellys,bgX,bgY)



    if makeHeal: # 힐 생성 허용 플래그 T일때만 힐 생성
        # 힐 랜덤 위치 생성
        Heal_X_Start=screen_W/3
        Heal_X_End=screen_W - HealKitSize
        Heal_X=random.randrange(Heal_X_Start, Heal_X_End)
        Heal_Y=random.randrange(player_Y - 2 * player_H, player_Y)
        Healnum=random.randrange(1,4)
        #힐 현재상태 플래그 변경
        makeHeal = False
        inHeal=True
        readyHeal=False
        # 힐 생성
        Heal = HealKit(Heal_X, Heal_Y,Healnum)

        time_makeHeal = datetime.now()  # 힐 출현 시간 시작
        HealTime=random.randrange(HealTimeS,HealTimeE)
        time_HealTimeCnt=HealTime
        redrawGameWindow(jellys, bgX, bgY)


    for i in range(0, Heartcnt):
        hearts[i].die=False


    while ongame:
        clock.tick(27)

    # 젤리와 주인공과의 충돌 확인
        for num in range(0,jelly_Num):
            if man.hitbox[1] < jellys[num].hitbox[1] + jellys[num].hitbox[3] and man.hitbox[1] + man.hitbox[3] > jellys[num].hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > jellys[num].hitbox[0] and man.hitbox[0] < jellys[num].hitbox[0] + jellys[num].hitbox[2]:
                    # 젤리와 겹쳐져 있는 경우
                    manhited=man.hit()
                    if manhited: # 체력 0
                        Heartcnt-=1
                        hearts[Heartcnt].die=True
                        man.health=player_Health
                        redrawGameWindow(jellys, bgX, bgY)
                        break



        if Heartcnt<1:
            Gameover = True
            ongame = False
            break

    # 주인공과 힐 키트 충돌 확인
        if inHeal:
            if man.hitbox[1] < Heal.y + HealKitSize and man.hitbox[1] + man.hitbox[3] > Heal.y:
                if man.hitbox[0] + man.hitbox[2] > Heal.x and man.hitbox[0] < Heal.x + HealKitSize:
                    Heal.geted = True
                    man.health+= Heal.size            # 체력 증가
            # 최대 체력을 넘겼을 때
                    if man.health >player_Health:
                    # 현재 하트가 최대 일 때
                        if Heartcnt>=Heart_cnt_max:
                            man.health=player_Health  #최대 체력으로 제한
                        else:
                            Heartcnt+=1 # 하트 개수 증가
                            man.health-=player_Health # 체력 조정
                    # 힐 먹었으니 힐 삭제
                    redrawGameWindow(jellys, bgX, bgY)
                    del Heal
                    inHeal = False
                    makeHeal = False
                    readyHeal = True
                    time_readyHeal = datetime.now()  # 힐 대기 시작
                    HealCycle = random.randrange(HealCycleS, HealCycleE)  # 대기 시간 조정
                    time_readyCnt=HealCycle
                    break



    # 힐 삭제 재생성 관련
        if inHeal: # 힐이 있을 때

            if timedelta(seconds=HealTime) <=datetime.now( )-time_makeHeal: # 힐 타임이 끝났을 때
                Heal.geted=True
                redrawGameWindow(jellys,bgX,bgY)
                del Heal
                inHeal = False
                makeHeal=False
                readyHeal=True
                time_readyHeal = datetime.now()  # 힐 대기 시간
                HealCycle=random.randrange(HealCycleS,HealCycleE) # 대기 시간 조정
                time_readyCnt=HealCycle
                break
            else:
                if timedelta(seconds=HealTime-time_HealTimeCnt) <=datetime.now( )-time_makeHeal:#

                    redrawGameWindow(jellys, bgX, bgY)
                    time_HealTimeCnt-=1
                    break

        if readyHeal:
            if timedelta(seconds=HealCycle) <= datetime.now() - time_readyHeal: #힐 대기 시간<=현재 대기 시간

                makeHeal=True
                readyHeal=False
                redrawGameWindow(jellys, bgX, bgY)
                break
            else:
                if timedelta(seconds=HealCycle-time_readyCnt) <=datetime.now( )-time_readyHeal:#

                    redrawGameWindow(jellys, bgX, bgY)
                    time_readyCnt-=1
                    break


    #총이 연속적으로 나가는 것을 막기 위한 format
        if gunloop > 0:
            gunloop += 1
        if gunloop > 3:
            gunloop = 0

        # 창을 닫거나 Esc를 누르면 게임 종료
        for event in pygame.event.get():
            if event.type == pygame.QUIT : # or event.type == pygame.K_ESCAPE:
                ongame = False
                pygame.quit()
                sys.exit()


        #  총알에 맞았는지 확인하고 맞으면 처리하는 함수
        for bullet in bullets:
            delgun = False
            for num in range(0,jelly_Num):
                if bullet.y - bullet.radius < jellys[num].hitbox[1] + jellys[num].hitbox[3] and bullet.y + bullet.radius > jellys[num].hitbox[
            1]: # x좌표 확인
                    if bullet.x + bullet.radius > jellys[num].hitbox[0] and bullet.x - bullet.radius < jellys[num].hitbox[0] + \
                            jellys[num].hitbox[2]: #y 좌표 확인
                        # 젤리가 총에 맞은게 맞을 때
                        jellys[num].hited()                        # 젤리 때리기
                        delgun=True
                        # 젤리가 죽었을 때 점수 추가
                        if not jellys[num].die:
                            Score += jellys[num].score
                            redrawGameWindow(jellys,bgX,bgY)
            if delgun==True:
                bullets.pop(bullets.index(bullet))  # 총알 삭제

            # 화면 밖의 총알 삭제
            if bullet.x >= screen_W or bullet.x <-25:
               bullets.pop(bullets.index(bullet))

            else:
                bullet.x += bullet.vel # 총알의  x축 증가

        keys = pygame.key.get_pressed()
        mouse=pygame.mouse.get_pressed()
    #k 키를 누르면 총알 발사
        if mouse[0] or keys[pygame.K_k] : #슈팅 K

            if man.left:
                facing = -1
            else:
                facing = 1

            bullets.append(projectile(man.x +(man.width//2)+ (man.width*facing), man.y + man.height // 2, facing))
    # 왼쪽 -방향키 or a
        elif  (keys[pygame.K_LEFT]or keys[pygame.K_a])  and man.x > man.vel: # 왼쪽 A
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
    # 오른쪽 - 방향키 or d
        elif (keys[pygame.K_RIGHT]or keys[pygame.K_d])  and man.x < screen_W - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing=False
    # 방향키 안 눌렀을 때
        else:
            man.standing=True
            man.walkCount = 0

    # 점프 중이 아닐 때
        if not (man.isJump):
        # 점프키 -스페이스바,j
            if keys[pygame.K_j] or keys[pygame.K_SPACE]: # 점프 키 j space
                man.isJump = True
                man.walkCount = 0
        # 점프 중일 때
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10

        if man.x>screen_W-player_W: # 화면 밖으로 나가면  다시 원위치로 이동
            man.x=player_X

        leastdie=False
        for num in range(0,jelly_Num):
            if  jellys[num].x<jelly_W or jellys[num].y>=screen_H-jelly_H:# 화면 밖으로 나가면
                jellys[num].visible=False
                leastdie=True # 한 젤리라도 화면 밖으로 나가면

        if leastdie : # 젤리 하나라도 죽으면
            redrawGameWindow(jellys,bgX,bgY)
            break
        bgX-=10
        if  bgX<=-screen_W:
            bgX=0

        redrawGameWindow(jellys, bgX, bgY)

    overcount =OVERCOUNT

    while Gameover:# 게임 오버
    # 배경화면 변경
        screen.blit(BackGround(ongame, Gameover), (0, 0))

    # 폰트 색상 과 문자 위치 지정
        text_Score = font_endScore.render(str(Score), 1, ORANGE)
        textcnt = font_cnt.render(str(overcount ), 1, RED)  # 칼라
        
    # 점수 출력 x 위치 지정
        check=1
        checkScore=Score
        while True:
            if checkScore // 10 == 0:
                break

            checkScore=checkScore//10
            check += 1

        text_Score_Size_X = int (screen_W/2) -10*check
    #오버 카운트 출력 X 위치 조정
        if overcount//10==0:
            textcnt_Size_X= int(screen_W/2) -25
        else:
            textcnt_Size_X = int(screen_W / 2) -50
        textcnt_Size_Y= int(screen_H/2)-30

    # 점수와 count 출력 
        screen.blit(text_Score, (text_Score_Size_X, 150))  # 점수 출력
        screen.blit(textcnt, (textcnt_Size_X, textcnt_Size_Y))  # count
    # 키 입력 확인
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 마우스 클릭 시 게임화면으로 다시 전환 & 점수, 플레이어 위치, 배경화면 리셋
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ongame = True
                Gameover = False
                overcount=99
                man = player(player_X, player_Y, player_W, player_H)
                Score = 0
                bgX = 0
                bgY = 0
                Heartcnt=Heart_cnt_start
                mandie=False


        if overcount<0:     #1까지 카운트가 끝나면 자동으로 메인 화면으로 이동
            Gameover = False
            ongame = False
        elif overcount<=OVERCOUNT:
            pygame.display.update()
            overcount -= 1
            pygame.time.delay(1000)
        elif overcount== 99:
            break


