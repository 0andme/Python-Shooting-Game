import random

# 색상
RED=(255,0,0)
ORANGE=(255,165,0)
YELLOW=(255,255,0)
GREEN=(0,128,0)
BLUE=(30,144,255)
BLACK=(0,0,0)
WHILTE=(255,255,255)

screen_W=960        # 스크린 가로
screen_H=480       # 스크린 세로

player_W=70         # 플레이어 가로
player_H=90         # 플레이어 세로
player_X=10         # 플레이어 초기 x
player_Y=300        # 플레이어 초기 y

jelly_W=50          # 젤리 가로
jelly_H=50          # 젤리 세로


jelly_Num=5     # 젤리의 종류
health_Jelly=10     # 젤리의 체력

player_Health = 250 # 주인공의 체력
Atk=5               # 주인공의 공격력

score_Jelly = 100   # 젤리 1 적중 시 얻는 점수
del_score = 10       # 주인공과 젤리가 충돌 시 깍이는 점수
del_Health =10      # 주인공과 젤리가 충돌 시 깍이는 주인공의 체력치

player_Health_barX = 100 # 주인공의 체력 바 x 좌표
player_Health_barY = 40 # 주인공의 체력 바 y 좌표
player_Health_barH = 38  # 주인공의  체력 바 높이=두께

img_Health_barX=player_Health_barX-50 # 체력 바 이미지 시작 x 위치 = 100-50=50
img_Health_barY=player_Health_barY-6# 체력 바 이미지 시작 y 좌표 = 40-6=34
img_Health_barH=50# 체력 바 이미지 높이 50
img_Health_barW=306



score_X=screen_W//2
score_Y=img_Health_barY+15

Heart_cnt_max=8
Heart_cnt_start=4
HeartX=img_Health_barX+10
HeartY=player_Health_barY+img_Health_barH
HeartSize=35

HealSize=150                    # 힐의 최대 사이즈
HealKitSize=50                  # 힐 이미지의 사이즈
Healnum=random.randrange(1,4)   # 힐 종류 3가지

HealTimeS=5                     # 힐 화면 유지시간 S
HealTimeE=10                    # 힐 화면 유지 시간 E
HealTime=random.randrange(5,10) # 힐 화면 유지 시간 (랜덤)
time_HealTimeCnt=HealTime       # 힐 유지시간 찍기 위한 변수

HealCycleS=10                   # 힐 대기 시간 S
HealCycleE=30                   # 힐 대기 시간 E
HealCycle=random.randrange(HealCycleS,HealCycleE)   # 힐 대기 시간 (랜덤)
time_readyCnt=HealCycle         # 힐 대기시간 찍기위한 변수



OVERCOUNT=60                    # 게임 자동 종료 시간 변수



