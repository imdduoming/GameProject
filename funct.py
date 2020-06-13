#컴퓨터 선공시
import random as rd
import time
def blank_line():
    print(' ---------------------- ')
    print(' ---------------------- ')
    time.sleep(1.5)

def blank():
    print()
    print()
    time.sleep(1.5)

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
    if (bothcorrect == 0 and numcorrect == 0) :
        return 'strike'#1out
    elif (bothcorrect == 0 and numcorrect == 1) or (bothcorrect == 0 and numcorrect == 2):
        return 'foul'
    elif (bothcorrect == 1 and numcorrect == 1) :
        return 'ball'
    elif (bothcorrect == 0 and numcorrect == 3) or (bothcorrect == 1 and numcorrect == 2):
        return 'singlehit'
    elif (bothcorrect == 2 and numcorrect == 2):
        return 'doublehit'
    elif (bothcorrect == 1 and numcorrect == 3):
        return 'triplehit'
    elif bothcorrect == 3 and numcorrect == 3:
        return 'homerun'
'''

'''
def defense_num(n=1):  # 투수의 수와 타자의 수 오차 구하기(선수비일때)
    num_pitch = 100 * player_pitch_list[0] + 10 * player_pitch_list[1] + player_pitch_list[2]
    num_hit = 100 * c_hit[0] + 10 * c_hit[1] + c_hit[2]
    hit_margin = abs(num_pitch - num_hit)
    return hit_margin


def user_defense(defen=0):  # 수비수가 타자의 오차 예측하기

    defense_predict = int(input("타자의 오차값을 예측하세요 : "))
    hit_margin = defense_num(1)  # 타자의 오차
    defense_margin = abs(defense_predict - hit_margin)  # 수비수의 오차
    if defense_margin <= 50:
        defen=1
        print("아웃! 수비를 성공하였습니다.")
        return defen

    elif defense_margin <= 100:
        print('수비를 다시 한번 시도해주세요!')
        print()
        return user_defense(0)

    else:
        defen = 0
        print("출루! 수비를 실패하였습니다.")
        return defen




def playerhit(pitch):  # 원소 3개의 리스트를 받으면 합을 표출하고, 플레이어의 반응을 얻고 플레이어가 입력한 리스트 구하기
    com_sum = 0
    for i in pitch:
        com_sum += i
    print('투수가 던진 공의 합은 {}입니다.'.format(com_sum))
    a, b, c = input('합이 {}인 9 이하의 서로 다른 자연수 세 개를 고르시오(공백으로 구분): '.format(com_sum)).split()
    hit = [a, b, c]
    play_hit = [int(i) for i in hit]
    return play_hit

def Cdefense_num(n=1): #투수의 수와 타자의 수 오차 구하기(컴퓨터가 수비할때)
    num_pitch = 100*com_pitch[0] + 10*com_pitch[1] + com_pitch[2]
    num_hit = 100*player_hit[0] + 10*player_hit[1] + player_hit[2]
    hit_margin = abs(num_pitch - num_hit)
    return hit_margin

def com_defense(defen=0): #수비수(컴퓨터)가 타자의 오차 예측하기

    com_defense_predict = rd.randint(1, 987-123) #수비자(컴퓨터)가 예측한 오차값
    hit_margin = Cdefense_num(1) #실제 오차
    defense_margin = abs(com_defense_predict - hit_margin) #실제 값과 오차값의 차
    #1루타, 2루타, 3루타 상황에 따라 나눌 진 추후에 결정하기로.
    if (decision(player_hit, com_pitch) == 'strike') or (decision(player_hit, com_pitch) == 'homerun'):
        None
    else:
        if defense_margin <= 50:
            defen=1#수비성공
            print("아웃! 수비수가 수비를 성공하였습니다.")
            return defen


        elif defense_margin <= 100:
            print('수비수가 다시 한 번 수비를 시도합니다!')
            print()
            return com_defense(0)

        else:
            print("출루! 수비수가 수비를 실패하였습니다.")
            defen=0
            return defen



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

def getonbase_ball(n=1):
    global base
    if base[1] == 1:
        if base[2] == 1:
            getonbase(1)
        elif base[2] == 0:
            base[2] == 1
    elif base[1] == 0:
        base[1] == 1



def attackscore(user_decision, defen, strikeNum, ballNum, outNum):   #타자의 결정에따라 상황 정해짐
    if user_decision == 'strike':
        strikeNum += 1
        print(strikeNum,'strike 입니다')
    elif user_decision == 'foul':
        if strikeNum != 2:
            strikeNum += 1
            print(strikeNum,'strike 입니다')
    elif user_decision == 'ball':
        ballNum += 1
        if ballNum == 4:   #볼넷일 때
            ballNum = 0
            getonbase_ball(1)
            print('볼넷입니다. 주자가 출루합니다.')
        else:
            print(ballNum, 'ball 입니다.')
    elif user_decision == 'singlehit':
        if (defen==0):
            getonbase(1)
            print('1루타 입니다.')
        else:
            outNum+=1
            print('1 out 되었습니다.')
    elif user_decision == 'doublehit':
        if (defen==0):
            getonbase(2)
            print('2루타 입니다.')
        else:
            outNum+=1
            print('1 out 되었습니다.')
    elif user_decision == 'triplehit':
        if (defen==0):
            getonbase(3)
            print('3루타 입니다.')
        else:
            outNum+=1
            print('1 out 되었습니다.')
    elif user_decision == 'homerun' :
            getonbase(4)
            print('Congratulations!')
            print('Homerun!')
    if(strikeNum==3):
        outNum+=1
        print(outNum,'out 되었습니다.')
    return strikeNum,ballNum,outNum

def user_attackend(inning_score,my_score):#사용자의 공격이 끝나고 점수계산
    blank_line()
    print('3 out')

    blank()
    print('당신이 이번 공격에서 얻은 점수는 ', inning_score, '입니다')
    print('현재 당신의 총 점수를 알려드리겠습니다.')
    wait()
    my_score=my_score+inning_score
    print('현재 당신의 총 점수는 ',my_score,'입니다.')
    return my_score

def com_attackend(inning_score,my_score):#컴퓨터의 공격이 끝나고 점수계산
    print('3 out')
    blank()

    blank_line()
    print('상대 팀이 이번 공격에서 얻은 점수는 ', inning_score, '입니다')
    print('합산된 상대의 총 점수를 알려드리겠습니다.')
    wait()
    my_score = my_score + inning_score

    print('현재 상대 팀의 총 점수는 ', my_score, '입니다.')
    return my_score

def game_end(i,user_score,com_score):#한회가 끝나고 점수계산하는 함수
    print('현재 score을 계산 중입니다.')
    wait()
    print('현재 score는 ', user_score, ':', com_score, '입니다.')
    print(i, '회가 모두 끝났습니다.')
    print('수고하셨습니다.')
    blank()


print()
print('Baseball Game Start!')
print()
print('Let\'s set options for the game.')
print()
gameNum=int(input('몇 회의 게임을 진행하실건가요?'))
#playerNum=int(input('플레이어의 수를 결정해주세요!(1or2)'))
print()
print('게임은 시작되었습니다!')
print('선공과 후공은 랜덤으로 주어집니다.')
print()
wait()
i=1
user_score=0#사용자 최종 점수
com_score=0#컴퓨터 최종 점수
playerOp=['선공','후공']#선공리스트
while(i<=gameNum):
    player=rd.choice(playerOp)
    if(player=='선공'):
        print('     Welcome     ')
        print()
        print(i,'회가 시작되었습니다!')
        wait()
        print('지금은',i,'회 초입니다.')
        blank()
        print('당신은 ',player,'이므로 먼저 공격할 차례입니다.')

        outNum_t = 0  # out 횟수
        base = [0, 0, 0, 0, 0]  # 타석 1루 2루 3루 홈
        inning_score = 0  # 회당 플레이어 점수
        # 먼저 공격할 경우
        while(outNum_t<3):

            strikeNum=0#strike횟수
            ballNum=0
            outNum=0
            while(outNum==0 and strikeNum<3):
                print('투수가 공 3개를 결정하는 중입니다.')
                wait()


                defen=0
                num_list = list(range(1, 10))
                com_pitch = rd.sample(num_list, 3)  # 수비자(컴퓨터)의 투구(리스트)
                player_hit = playerhit(com_pitch)  # 수비수의 합으로 공격 타자가 숫자고르기
                user_decision=decision(player_hit, com_pitch)
                print(user_decision)

                if (((user_decision != 'homerun' and user_decision != 'foul')and user_decision!='strike')and user_decision!='ball'):#홈런,파울,스트라이크,볼이 아닐때만 수비함
                    defen=com_defense(defen)

                strikeNum,ballNum,outNum=attackscore(user_decision,defen,strikeNum,ballNum,outNum)#out횟수와 각 1,2,3,4루의 상황 결정

            outNum_t+=1
            print('당신은 총 ',outNum_t,'out 되었습니다.')

        user_score=user_attackend(inning_score,user_score)

        #공수교대 되어 사용자가 1회안에서 선공격 후 수비하는 차례
        print('공수교대되어 지금은 ',i,'회 말입니다.')
        wait()
        print('당신은 수비를 할 차례입니다.')
        outNum_t=0
        inning_score=0
        while(outNum_t<3):
            print('당신은 투수가 되었습니다.')

            strikeNum=0
            outNum=0
            ballNum=0
            while (outNum == 0 and strikeNum < 3):
                player_pitch = map(int, input("원하시는 세자리 수를 입력하세요 (공백으로 구분): ").split())
                player_pitch_list = list(player_pitch)  # player 투수의 세자리수 입력
                player_pitch_sum = sum(player_pitch_list)
                defen=0
                defen_re=0
                print("타자가 수를 선택하고 있습니다.")
                wait()
                time.sleep(1)
                print("타자가 수를 선택하였습니다.")
                c_hit = com_hit(player_pitch_list)  # 투수의 합을 타자가 분할해서 숫자를 예측함
                final_decision = decision(c_hit, player_pitch_list)  # 투수와 타자 자리 비교 결정
                print(final_decision)
                if (((final_decision != 'homerun' and final_decision != 'foul')and final_decision!='strike')and final_decision!='ball'): # 홈런과 파울이 아닐때만 수비함
                    defen_re=user_defense(defen)
                  
                    if defen_re==1:#수비 성공하면
                        outNum+=1#outNum++1
                        print('1 out 입니다.')
                    elif (defen_re==0):
                        strikeNum,ballNum, outNum = attackscore(final_decision, defen, strikeNum,ballNum, outNum)

                elif (final_decision == 'homerun'):#홈런이면
                    strikeNum, ballNum,outNum = attackscore(final_decision, defen, strikeNum,ballNum, outNum)
                elif (final_decision == 'strike'):
                    strikeNum += 1
                    print(strikeNum, 'strike 입니다')
                elif (final_decision == 'foul'):
                    if (strikeNum != 2):
                        strikeNum += 1
                        print(strikeNum, 'strike 입니다')
                elif (final_decision =='ball'):
                    if final_decision == 'ball':
                        ballNum += 1
                        if ballNum == 4:  # 볼넷일 때
                            ballNum = 0
                            getonbase_ball(1)
                            print('볼넷입니다. 주자가 출루합니다.')
                        else:
                            print(ballNum, 'ball 입니다.')

            outNum_t += 1
            print('상대 팀은 총 ', outNum_t, 'out 되었습니다.')
            print()


        com_score=com_attackend(inning_score,com_score)



    elif(player=='후공'):
        print('     Welcome     ')
        print()
        print(i, '회가 시작되었습니다!')
        wait()
        print('지금은', i, '회 초입니다.')
        print()
        time.sleep(1)
        print('당신은 ',player,'이므로 먼저 수비할 차례입니다.')
        print()
        outNum_t = 0
        inning_score = 0
        while (outNum_t < 3):
            print('당신은 투수가 되었습니다.')

            strikeNum = 0
            outNum=0
            ballNum=0
            # ballNum=0
            while (outNum == 0 and strikeNum < 3):


                player_pitch = map(int, input("원하시는 세자리 수를 입력하세요(공백으로 구분): ").split())
                player_pitch_list = list(player_pitch)  # player 투수의 세자리수 입력
                player_pitch_sum = sum(player_pitch_list)
                print("타자가 수를 선택하고 있습니다.")
                wait()
                time.sleep(1)
                print("타자가 수를 선택하였습니다.")
                defen=0
                defen_re=0
                c_hit = com_hit(player_pitch_list)  # 투수의 합을 타자가 분할해서 숫자를 예측함
                final_decision = decision(c_hit, player_pitch_list)  # 투수와 타자 자리 비교 결정
                print(final_decision)

                if (((final_decision != 'homerun' and final_decision != 'foul')and final_decision!='strike')and final_decision!='ball'):  # 홈런과 파울이 아닐때만 수비함

                    defen_re=user_defense(defen)

                    if defen_re==1:
                        outNum+=1
                        print('1 out 입니다.')
                    elif defen_re==0:
                        strikeNum, ballNum,outNum = attackscore(final_decision, defen, strikeNum,ballNum, outNum)
                elif (final_decision=='homerun'):
                    strikeNum, ballNum,outNum = attackscore(final_decision, defen, strikeNum,ballNum, outNum)
                elif (final_decision=='strike'):
                    strikeNum+=1
                    print(strikeNum, 'strike 입니다')
                elif (final_decision=='foul'):
                    if (strikeNum != 2):
                        strikeNum += 1
                        print(strikeNum, 'strike 입니다')
                elif (final_decision=='ball'):
                    if final_decision == 'ball':
                        ballNum += 1
                        if ballNum == 4:  # 볼넷일 때
                            ballNum = 0
                            getonbase_ball(1)
                            print('볼넷입니다. 주자가 출루합니다.')
                        else:
                            print(ballNum, 'ball 입니다.')




            outNum_t += 1
            print('상대 팀은 총 ', outNum_t, 'out 되었습니다.')
            print()

        com_score=com_attackend(inning_score,com_score)


        # 공수교대 되어 사용자가 1회안에서 공격하는차례
        print('공수교대되어 지금은 ',i, '회 말입니다.')
        wait()
        print('')
        outNum_t = 0  # out 횟수
        base = [0, 0, 0, 0, 0]  # 타석 1루 2루 3루 홈
        inning_score = 0  # 회당 플레이어 점수
        # 먼저 공격할 경우
        while (outNum_t < 3):

            strikeNum = 0  # strike횟수
            ballNum=0
            outNum = 0
            while (outNum == 0 and strikeNum < 3):
                print('투수가 공 3개를 결정하는 중입니다.')
                wait()

                defen = 0  # 수비실패가 default
                num_list = list(range(1, 10))
                com_pitch = rd.sample(num_list, 3)  # 수비자(컴퓨터)의 투구(리스트)
                player_hit = playerhit(com_pitch)  # 수비수의 합으로 공격 타자가 숫자고르기
                user_decision = decision(player_hit, com_pitch)
                print(user_decision)
                if (((user_decision!= 'homerun' and user_decision != 'foul')and user_decision!='strike')and user_decision!='ball'):#홈런,파울,스트라이크,볼이 아닐때만 수비함
                    defen=com_defense(defen)

                strikeNum,ballNum,outNum=attackscore(user_decision,defen,strikeNum,ballNum,outNum)#out횟수와 각 1,2,3,4루의 상황 결정


            outNum_t += 1
            print('당신은 총 ', outNum_t, 'out 되었습니다.')
            print()

        user_score=user_attackend(inning_score,user_score)

    game_end(i,user_score,com_score)

    i+=1

print(gameNum,'회의 게임이 모두 종료되었습니다')
print()
print('모든 점수가 합산되는 중입니다')
wait()
print('최종 점수는',user_score,':',com_score,'입니다')
if(user_score>com_score):
    print()
    print('     Congratulations!    ')
    print()
    print('You Win!')
elif (user_score==com_score):
    print()
    print('     DRAW!     ')
    print()
else:
    print()
    print('     LOSE!     ')
    print()
    print('다음에 또 도전해주세요! ')













