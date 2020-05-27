# 함수/변수 이름 같은건 맞춰서 수정해주시고 이상한 부분 있으시면 카카오톡해주세요

# ㄴ의 플레이어 타구
def playerhit(pitch):  # 원소 3개의 리스트를 받으면 합을 표출하고, 플레이어의 반응을 얻는 함수
    psum = 0
    for i in pitch:
        psum += i
    print('투수가 던진 공은 {}입니다.'.format(psum))
    phit = input('합이 {}인 세 수를 고르시오:'.format(psum))
    hit = [0, 0, 0]
    hit[0], hit[1], hit[2] = map(int, phit.split(','))  # 숫자 분할을 ','를 사용하였는데, 다른 방식을 사용중이시면 변경해주세요
    return hit

    # 만약 합이 psum과 다른 세 수를 골랐다면 어떻게 될까요? 게임 규칙에 대한 생각입니다.


# ㅁ의 컴퓨터 타구
def com_hit(pitch):
    def randpart(n):  # 합(n)을 받았을 때, 임의의 3개 한자리 수로 분할하는 함수
        import random as rd
        def numsel(n):  # n과 9보다 작은 숫자 선택
            if 4 <= n <= 11:
                a = rd.randint(1, n - 3)
            elif 1 <= n <= 3:
                a = rd.randint(1, n)
            else:
                a = rd.randint(1, 9)
            return a

        while True:  # 조건 만족시 분할을 반환하고 반복문 종료/조건 불만족시 재실행
            num1 = numsel(n)
            num2 = numsel(n - num1)
            num3 = n - num1 - num2
            if 9 >= num3 != num2 and num1 != num2 and num3 != num1:
                res = [num1, num2, n - num1 - num2]
                return res

    psum = 0
    for i in pitch:
        psum += i
    chit = randpart(psum)
    print("상대는 {}라고 예측하고 휘둘렀습니다.".format(cpitch))  # randpart 에서 얻은 리스트를 플레이어에게 제시함
    return chit


# 타구의 판정 함수
def decision(pitch, hit):
    correct = 0
    numcorrect = 0  # 변수 초기화
    for i in range(0, 3):
        if hit[i] == pitch[i]:  # 타자의 i번째 숫자/자리 판정
            correct += 1
        elif hit[i] in pitch:
            numcorrect += 1
    if correct == 0 and numcorrect == 0:
        return 'strike'
    elif correct == 0 and numcorrect == 1:
        return 'singlehit'
    elif (correct == 1 and numcorrect == 0) or (correct == 0 and numcorrect == 2):
        return 'doublehit'
    elif correct == 2 and numcorrect == 0:
        return 'triplehit'
    elif correct == 3 and numcorrect == 0:
        return 'homerun'


print(decision([9, 1, 2], ['9', '2', '1']))
# 일단 str으로 반환하는 함수를 짰습니다. 하지만 어떤 상황에서 str을 사용할 수 없을 수 있으니 내키시는대로 바꾸셔도 좋습니다.
# 그리고 지금 타구의 판정 규칙을 잘 몰라서 임의로 제가 부여했습니다. 필요에 따라 변경해주세요.

# 게임 흐름에 따라 (player/computer)hit -> (player/computer)pitch -> decision -> 진루
# 이중 pitch와 decision을 만들었습니다.

base = [0, 0, 0, 0, 0]  # 타석 1루 2루 3루 홈
inning_score = 0  # 회당 플레이어 점수


def getonbase(n=1):
    global base, inning_score
    base[0] = 1  # 한명을 타석으로 보냄
    for _ in range(n):  # n루타 는 곧 n회의 한칸 진루
        for i in range(3, -1, -1):
            if base[i] > 0:  # i루에 사람이 있을경우 앞으로 보내야함, 3루부터 한칸씩 전진.
                base[i] -= 1
                base[i + 1] += 1
    inning_score += base[4]  # 홈에 도착한 인원들을 점수로 합산
    base[4] = 0  # 홈 초기화


# 점수판 테스트

from tkinter import *

f_score = Tk()
f_score.geometry('200x200')

blank_u = Label(f_score).grid(column='0', row='0', columnspan='3', sticky='news')

team_name1 = Label(f_score, text="A TEAM")
team_name2 = Label(f_score, text="B TEAM")
team_name1.grid(column='1', row='1',sticky = 'news')
team_name2.grid(column='1', row='2',sticky = 'news')

team_score1 = Label(f_score, text="0점")
team_score2 = Label(f_score, text="0점")
team_score1.grid(column='2', row='1')
team_score2.grid(column='2', row='2')

f_score.mainloop()