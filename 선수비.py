import random as rd
import datetime as dt

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

def com_hit(player_pitch):#타자가 투수가 공던지면 배트 휘두름
    player_pitch_int = [int(i) for i in player_pitch]
    player_pitch_sum = sum(player_pitch_int)  # 세자리수 합
    cpitch = randpart(player_pitch_sum)
    return cpitch

def decision(c_hit, player_pitch):
    correct = 0
    numcorrect = 0  # 변수 초기화
    for i in range(0, 3):
        if player_pitch[i] == c_hit[i]:  # 타자의 i번째 숫자/자리 판정 #자리,숫자 둘다같을 때
            correct += 1
        elif player_pitch[i] in c_hit:#숫자만 같고 자리 다를 때
            numcorrect += 1
    if correct == 0 and numcorrect == 0:#투수와 타자와 같은 숫자가 한 개도 없을 때
        return 'strike'
    elif correct == 0 and numcorrect == 1:#투수와 타자가 같은 숫자 1개 있지만 자리가 다를 때
        return 'singlehit'
    elif (correct == 1 and numcorrect == 0) or (correct == 0 and numcorrect == 2) or (numcorrect == 3):#1개의 자리와 숫자가 모두 동일하거나 숫자만 2개동일 숫자만 3개동일
        return 'doublehit'
    elif (correct == 2 and numcorrect == 0) or (correct == 1 and numcorrect == 2):
        return 'triplehit'
    elif correct == 3 and numcorrect == 0:#세개 모두 자리와 숫자동일
        return 'homerun'

def defense_num(n=1):  # 투수의 수와 타자의 수 오차 구하기
    num_pitch = 100 * player_pitch_int[0] + 10 * player_pitch_int[1] + player_pitch_int[2]
    num_hit = 100 * c_hit[0] + 10 * c_hit[1] + c_hit[2]
    hit_margin = abs(num_pitch - num_hit)
    return hit_margin


def defense(n=1):  # 수비수가 타자의 오차 예측하기
    defense_predict = int(input("타자의 오차값을 예측하세요 : "))
    hit_margin = defense_num(1)  # 타자의 오차
    defense_margin = abs(defense_predict - hit_margin)  # 수비수의 오차
    if defense_margin <= 50:
        print("아웃! 수비를 성공하였습니다.")
    elif defense_margin <= 100:
        defense()
    else:
        print("출루! 수비를 실패하였습니다.")

from datetime import timedelta

print()
print('Baseball Game Start!')
print()
print('Let\'s set options for the game.')
print()
gameNum=int(input('몇 회의 게임을 진행하실건가요?'))
playerNum=int(input('플레이어의 수를 결정해주세요!(1or2)'))
print()
print('선공과 후공은 랜덤으로 주어집니다.')
print()
playerOp=['선공','후공']#선공리스트
if(playerNum==1):#1인용 게임일때
    player=rd.choice(playerOp)
    if(player=='선공'):
        print('당신은',player,'이므로 먼저 공격할 차례입니다.')
        #먼저 공격할 경우
        print('투수가 공 3개를 결정하는 중입니다.')
        print('기다려주세요.')
        print()


    else:
        print('당신은',player,'이므로 먼저 수비할 차례입니다.')
        print()
        #먼저 수비할 경우
        print('당신은 투수가 되었습니다.')
        player_pitch = list(input("원하시는 세자리 수를 입력하세요 : "))  # player 투수의 세자리수 입력
        player_pitch_int = [int(i) for i in player_pitch]
        player_pitch_sum = sum(player_pitch_int)
        print("타자가 수를 선택하고 있습니다.")
        print("잠시만 기다려주세요 ...")
        now = dt.datetime.now()  # 현재 일시
        after_10s = timedelta(seconds=10)  # 10초 후
        now + after_10s
        c_hit = com_hit(player_pitch)#투수의 합을 타자가 분할해서 숫자를 예측함
        final_decision = decision(c_hit, player_pitch_int)#투수와 타자 자리 비교 결정
        print(final_decision)
        if (final_decision == 'singlehit') or (final_decision == 'doublehit') or (final_decision == 'triplehit'):
            defense(1)
