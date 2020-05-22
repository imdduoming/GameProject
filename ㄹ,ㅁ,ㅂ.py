#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#(ㄹ)
player_pitch=list(input("원하시는 세자리 수를 입력하세요 : ")) #player 투수의 세자리수 입력     
player_pitch_int=[int(i) for i in player_pitch] 
player_pitch_sum=sum(player_pitch_int)

#(ㅁ)
def randpart(n):  # 합(n)을 받았을 때, 임의의 3개 한자리 수로 분할하는 함수
    from random import randint
    while True:
        if n < 12:  # n은 항상 6보다 큼
            i = 1
            f = n - 3
        elif n < 18:
            i = 1
            f = 9
        else:
            i = n - 17
            f = 9
        a = randint(i, f)

        if n - a < 11:
            i = 1
            f = n - a - 1
        else:
            i = n - a - 9
            f = 9

        b = randint(i, f)
        c = n - a - b
        if a != b and b != c and c != a:
            res = [a, b, c]
            return res

def com_hit(player_pitch):    
    player_pitch_int=[int(i) for i in player_pitch] 
    player_pitch_sum=sum(player_pitch_int) #세자리수 합
    cpitch = randpart(player_pitch_sum)
    return cpitch

c_hit=com_hit(player_pitch)
 
#print("상대는 {}라고 예측하고 휘둘렀습니다.".format(c_hit))  # 컴퓨터 타자의 예측
print("타자가 수를 선택하고 있습니다.")

def decision(c_hit,player_pitch):
    correct = 0
    numcorrect = 0  # 변수 초기화
    for i in range(0, 3):
        if player_pitch[i] == c_hit[i]:# 타자의 i번째 숫자/자리 판정
            correct += 1
        elif player_pitch[i] in c_hit:
            numcorrect += 1
    if correct == 0 and numcorrect == 0:
        return 'strike'
    elif correct == 0 and numcorrect == 1:
        return 'singlehit'
    elif (correct == 1 and numcorrect == 0) or (correct == 0 and numcorrect == 2) or (numcorrect == 3):
        return 'doublehit'
    elif (correct == 2 and numcorrect == 0) or (correct == 1 and numcorrect == 2):
        return 'triplehit'
    elif correct == 3 and numcorrect == 0:
        return 'homerun'

final_decision=decision(c_hit,player_pitch_int)    
print(final_decision)

#(ㅂ)
def defense_num(n=1): #투수의 수와 타자의 수 오차 구하기
    num_pitch=100*player_pitch_int[0]+10*player_pitch_int[1]+player_pitch_int[2]
    num_hit=100*c_hit[0]+10*c_hit[1]+c_hit[2]
    hit_margin=abs(num_pitch-num_hit)
    return hit_margin

def defense(n=1): #수비수가 타자의 오차 예측하기
    defense_predict=int(input("타자의 오차값을 예측하세요 : ")) 
    hit_margin=defense_num(1) #타자의 오차
    defense_margin=abs(defense_predict-hit_margin) #수비수의 오차 
    if defense_margin<=50:
        print("아웃! 수비를 성공하였습니다.")
    elif defense_margin<=100:
            defense()
    else:
        print("출루! 수비를 실패하였습니다.")
    
if (final_decision=='singlehit') or (final_decision=='doublehit') or (final_decision=='triplehit'):
    defense(1)

