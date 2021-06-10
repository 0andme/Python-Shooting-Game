# 모든 디렉터리 정리
from Values import *

img_Dic='im/'               # 이미지 폴더  최상위
img_userDic='im/player/'    # 주인공 폴더

img_jellyDic=[]             # 젤리 폴더 젤리 종류만큼 저장 (폭발 이미지 포함)
for i in range(0,jelly_Num):
    img_jellyDic.append('im/jelly'+str(i)+'/')

img_gunDic='im/gun/'        # 총 폴더 (발사구 이미지)
