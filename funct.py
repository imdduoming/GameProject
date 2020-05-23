#컴퓨터 선공시
import random as rd
import time

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

def com_hit(player_pitch_list):#타자가 투수가 공던지면 배트 휘두름
    player_pitch_sum = sum(player_pitch_list)  # 세자리수 합
    cpitch = randpart(player_pitch_sum)
    return cpitch
def decision(playhit, compitch):
    bothcorrect = 0
    numcorrect = 0

    # 변수 초기화
    for i in range(0, 3):
        if playhit[i] == compitch[i]:  # 타자의 i번째 숫자/자리 판정
            bothcorrect += 1    #자릿수o숫자o
        if playhit[i] in compitch:
            numcorrect += 1   #자릿수x 숫자o
    if (bothcorrect == 0 and numcorrect == 0) or (bothcorrect == 0 and numcorrect == 1):
        return 'strike'#1out
    elif (bothcorrect == 0 and numcorrect == 2) or (bothcorrect == 1 and numcorrect == 1):
        return 'foul'
    elif (bothcorrect == 0 and numcorrect == 3) or (bothcorrect == 1 and numcorrect == 2):
        return 'singlehit'
    elif (bothcorrect == 2 and numcorrect == 2):
        return 'doublehit'
    elif (bothcorrect == 1 and numcorrect == 3):
        return 'triplehit'
    elif bothcorrect == 3 and numcorrect == 3:
        return 'homerun'
'''
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
'''
def defense_num(n=1):  # 투수의 수와 타자의 수 오차 구하기(선수비일때)
    num_pitch = 100 * player_pitch_list[0] + 10 * player_pitch_list[1] + player_pitch_list[2]
    num_hit = 100 * c_hit[0] + 10 * c_hit[1] + c_hit[2]
    hit_margin = abs(num_pitch - num_hit)
    return hit_margin


def user_defense(n=1):  # 수비수가 타자의 오차 예측하기
    defenSuc=False
    defense_predict = int(input("타자의 오차값을 예측하세요 : "))
    hit_margin = defense_num(1)  # 타자의 오차
    defense_margin = abs(defense_predict - hit_margin)  # 수비수의 오차
    if defense_margin <= 50:
        print("아웃! 수비를 성공하였습니다.")
        defenSuc=True
    elif defense_margin <= 100:
        user_defense(1)
    else:
        print("출루! 수비를 실패하였습니다.")

def playerhit(pitch):  # 원소 3개의 리스트를 받으면 합을 표출하고, 플레이어의 반응을 얻고 플레이어가 입력한 리스트 구하기
    com_sum = 0
    for i in pitch:
        com_sum += i
    print('투수가 던진 공의 합은 {}입니다.'.format(com_sum))
    a, b, c = input('합이 {}인 9 이하의 서로 다른 자연수 세 개를 고르시오(쉼표로 구분): '.format(com_sum)).split(',')
    hit = [a, b, c]
    play_hit = [int(i) for i in hit]
    return play_hit

def Cdefense_num(n=1): #투수의 수와 타자의 수 오차 구하기(컴퓨터가 수비할때)
    num_pitch = 100*com_pitch[0] + 10*com_pitch[1] + com_pitch[2]
    num_hit = 100*player_hit[0] + 10*player_hit[1] + player_hit[2]
    hit_margin = abs(num_pitch - num_hit)
    return hit_margin

def com_defense(n=1): #수비수(컴퓨터)가 타자의 오차 예측하기
    defen=False
    com_defense_predict = rd.randint(1, 987-123) #수비자(컴퓨터)가 예측한 오차값
    hit_margin = Cdefense_num(1) #실제 오차
    defense_margin = abs(com_defense_predict - hit_margin) #실제 값과 오차값의 차
    #1루타, 2루타, 3루타 상황에 따라 나눌 진 추후에 결정하기로.
    if (decision(player_hit, com_pitch) == 'strike') or (decision(player_hit, com_pitch) == 'homerun'):
        None
    else:
        if defense_margin <= 50:
            defen = True
            print("아웃! 수비를 성공하였습니다.")

        elif defense_margin <= 100:
            print('다시 한 번 수비를 시도합니다!')
            com_defense(1)
        else:
            print("출루! 수비를 실패하였습니다.")
def wait():
    print('잠시만 기다려 주세요.')
    print('      wait         ')
    print('       -           ')
    print('       -           ')
    print('       -           ')
    print()
    time.sleep(1)
    print()

base = [0, 0, 0, 0, 0]  # 타석 1루 2루 3루 홈
inning_score = 0  # 회당 플레이어 점수



def getonbase(n=1):
    global base, inning_score
    base[0] = 1  # 한명을 타석으로 보냄
    for _ in range(n):  # n루타 는 곧 n회의 한칸 진루
        for i in range(3,-1,-1):
            if base[i] > 0:  # i루에 사람이 있을경우 앞으로 보내야함, 3루부터 한칸씩 전진.
                base[i] -= 1
                base[i+1] += 1
    inning_score += base[4]  # 홈에 도착한 인원들을 점수로 합산
    base[4] = 0  # 홈 초기화

def firstattack(outNum):
    if decision(player_hit, com_pitch) == 'strike' or (defen == True):
        outNum += 1
    elif decision(player_hit, com_pitch) == 'singlehit':
        if (defen==False):
            getonbase(1)
        else:
            outNum+=1

    elif decision(player_hit, com_pitch) == 'doublehit':
        if (defen==False):
            getonbase(2)
        else:
            outNum+=1
    elif decision(player_hit, com_pitch) == 'triplehit':
        if (defen==False):
            getonbase(3)
        else:
            outNum+=1
    elif decision(player_hit, com_pitch) == 'homerun' :
        if (defen==False):
            getonbase(4)
        else:
            outNum+=1



def seconddefense(outNum):#사용자 먼저 공격시 공격 후 수비 할때
    #수비실패경우
    if((final_decision!='strike' or final_decision!='foul') and defenSuc==False):#n루타인 경우&&수비실패일때 점수 오르는경우
        if (final_decision == 'singlehit'):
            getonbase(1)
        elif (final_decision == 'doublehit'):
            getonbase(2)
        elif (final_decision == 'doublehit'):
            getonbase(3)
        elif(final_decision == 'doublehit') and (defenSuc == False):
            getonbase(4)
    elif(final_decision=='strike'):
        outNum += 1
    elif(defenSuc==True):
        outNum+=1





print()
print('Baseball Game Start!')
print()
print('Let\'s set options for the game.')
print()
gameNum=int(input('몇 회의 게임을 진행하실건가요?'))
playerNum=int(input('플레이어의 수를 결정해주세요!(1or2)'))
print()
print('게임은 시작되었습니다!')
print('선공과 후공은 랜덤으로 주어집니다.')
print()
wait()
user_score=0#사용자 최종 점수
com_score=0#컴퓨터 최종 점수
playerOp=['선공']#선공리스트
if(playerNum==1):#1인용 게임일때
    player=rd.choice(playerOp)
    if(player=='선공'):
        print('당신은 ',player,'이므로 먼저 공격할 차례입니다.')

        outNum = 0  # out 횟수
        base = [0, 0, 0, 0, 0]  # 타석 1루 2루 3루 홈
        inning_score = 0  # 회당 플레이어 점수
        # 먼저 공격할 경우
        while (outNum < 2):
            print('투수가 공 3개를 결정하는 중입니다.')
            wait()
            defen = False
            num_list = list(range(1, 10))
            com_pitch = rd.sample(num_list, 3)  # 수비자(컴퓨터)의 투구(리스트)
            player_hit = playerhit(com_pitch)  # 수비수의 합으로 공격 타자가 숫자고르기
            user_decision=decision(player_hit, com_pitch)
            print(decision(player_hit, com_pitch))
            com_defense(1)
            firstattack(outNum)#out횟수와 각 1,2,3,4루의 상황 결정

        print('3 out')
        print('당신은 3 out이 되었으므로 공수교대를 하겠습니다')
        print('당신이 이번 공격에서 얻은 점수는 ', inning_score, '입니다')
        print('현재 당신의 총 점수를 알려드리겠습니다.')
        wait()
        user_score=user_score+inning_score
        print('현재 당신의 총 점수는 ',user_score,'입니다.')

        #공수교대 되어 사용자가 1회안에서 선공격 후 수비하는 차례
        print('공수교대되어 지금은 ',gameNum,'회 말입니다.')
        print('당신은 수비를 할 차례입니다.')
        outNum=0
        while(outNum<3):
            print('당신은 투수가 되었습니다.')
            defenSuc=False
            inning_score=0
            player_pitch = map(int, input("원하시는 세자리 수를 입력하세요 : ").split())
            player_pitch_list = list(player_pitch)  # player 투수의 세자리수 입력
            player_pitch_sum = sum(player_pitch_list)
            print("타자가 수를 선택하고 있습니다.")
            wait()
            time.sleep(1)
            print("타자가 수를 선택하였습니다.")
            c_hit = com_hit(player_pitch_list)  # 투수의 합을 타자가 분할해서 숫자를 예측함
            final_decision = decision(c_hit, player_pitch_list)  # 투수와 타자 자리 비교 결정
            print(final_decision)
            user_defense(1)
            seconddefense(outNum)

        print('3 out')
        print('상대가 3 out이 되었으므로 ',gameNum,'회가 끝났습니다.')
        print('당신이 이번 공격에서 얻은 점수는 ', inning_score, '입니다')
        print('현재 당신의 총 점수를 알려드리겠습니다.')
        wait()
        com_score = com_score + inning_score
        print('현재 당신의 총 점수는 ', user_score, '입니다.')

        print('현재 score을 계산 중입니다.')
        wait()
        print('현재 score는 ',user_score,':',com_score,'입니다.')


                #파울경우 아직 고려안함
        print('수고하셨습니다.')
















