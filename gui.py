from tkinter import *
import random as rd
import time


# ------tk, 프레임 클래스--------


class GameMain(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1200x900+300+50")
        self.title("야구 게임")
        self.resizable(False, False)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(Frame):  # 시작 페이지, 버튼 위치 등은 사후 조정
    def __init__(self, master):  # master 는 부모를 의미한다. 즉, Tk를 의미
        Frame.__init__(self, master)
        Button(self, text="게임 시작", command=lambda: master.switch_frame(NewGame)).pack(anchor='center')  # ).pack()
        Button(self, text="튜토리얼").pack(anchor='center')  # , command=lambda: master.switch_frame(PageTwo)).pack()
        Button(self, text="게임종료", command=lambda: quit()).pack(anchor='center')


class NewGame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text='당신의 팀 이름을 입력해주세요: ').grid(column='0', row='0')
        self.ent1 = Entry(self)
        self.ent1.grid(column='1', row='0')
        Label(self, text='진행할 게임 횟수를 입력해주세요: ').grid(column='0', row='1')
        self.ent2 = Entry(self)
        self.ent2.grid(column='1', row='1')
        Button(self, text='게임 시작', command=lambda: self.game_start(master)).grid(column='1', row='2')
        self.lab1 = Label(self, text='')
        self.lab1.grid(column='0', row='3', columnspan='2')
        self.lab2 = Label(self, text='')
        self.lab2.grid(column='0', row='4', columnspan='2')

    def game_start(self, master):
        global playerOp, player, playerName, gameNum
        player = rd.choice(playerOp)
        playerName = self.ent1.get()
        gameNum = int(self.ent2.get())
        self.lab2.config(text="당신은 {}입니다.".format(player))
        self.master.update()
        time.sleep(2)
        if player == '선공':
            master.switch_frame(pAttack)
        elif player == '후공':
            quit()


class BaseFrame(Frame):
    def __init__(self):
        Frame.__init__(self, width='200', height='200', relief='solid', bd='1')
        self.c_base = Canvas(self, width='200', height='200')
        self.c_base.pack()
        self.base_update()

    def base_update(self):
        global base
        if base[1] == 1:  # 1루
            self.c_base.create_polygon(145, 73, 109, 109, 145, 145, 181, 109, fill='yellow', outline='black')
        else:
            self.c_base.create_polygon(145, 73, 109, 109, 145, 145, 181, 109, fill='white', outline='black')
        if base[2] == 1:  # 2루
            self.c_base.create_polygon(100, 29, 64, 65, 100, 101, 136, 65, fill='yellow', outline='black')
        else:
            self.c_base.create_polygon(100, 29, 64, 65, 100, 101, 136, 65, fill='white', outline='black')
        if base[3] == 1:  # 3루
            self.c_base.create_polygon(56, 73, 20, 109, 56, 145, 92, 109, fill='yellow', outline='black')
        else:
            self.c_base.create_polygon(56, 73, 20, 109, 56, 145, 92, 109, fill='white', outline='black')


class ResultPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        pass


class pAttack(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.bfr = BaseFrame()
        self.bfr.place(x=40, y=40)
        self.sbo = SBO()
        self.sbo.place(x=1000, y=700)
        self.but = BallButton()
        self.but.place(x=400, y=600)
        self.atn = attackNum()
        self.atn.place(x=450, y=250)
        self.scr = ScoreBoard()
        self.scr.place(x=950, y=40)
        strikeNum = 0
        ballNum = 0
        outNum = 0
        while outNum < 3:
            while (outNum == 0 and strikeNum < 3):
                defen = 0
                numsel = 0
                player_hit = []
                num_list = list(range(1, 10))
                com_pitch = rd.sample(num_list, 3)  # 수비자(컴퓨터)의 투구(리스트)
                coms = sum(com_pitch)
                self.atn.pitch_update(coms)  # 컴퓨터가 던진 수 합
                self.atn.lab2.config(text='당신이 고른 수는')
                self.atn.master.update()
                IntVar
                #
                # user_decision = decision(player_hit, com_pitch)
                # if (((
                #              user_decision != 'homerun' and user_decision != 'foul') and user_decision != 'strike') and user_decision != 'ball'):  # 홈런,파울,스트라이크,볼이 아닐때만 수비함
                #     pass
                # strikeNum, ballNum, outNum = attackscore(user_decision, defen, strikeNum, ballNum,
                #                                          outNum)  # out횟수와 각 1,2,3,4루의 상황 결정

        #     outNum_t += 1
        # print('당신은 총 ', outNum_t, 'out 되었습니다.')

    # user_attackend(inning_score, user_score)
    #
    # # 공수교대 되어 사용자가 1회안에서 선공격 후 수비하는 차례
    # print('공수교대되어 지금은 ', i, '회 말입니다.')
    # wait()
    # print('당신은 수비를 할 차례입니다.')
    # outNum_t = 0
    # inning_score = 0
    # while (outNum_t < 3):
    #
    #     strikeNum = 0
    #     outNum = 0
    #     ballNum = 0
    #     while (outNum == 0 and strikeNum < 3):
    #         player_pitch = map(int, input("원하시는 세자리 수를 입력하세요 (공백으로 구분): ").split())
    #         player_pitch_list = list(player_pitch)  # player 투수의 세자리수 입력
    #         player_pitch_sum = sum(player_pitch_list)
    #         defen = 0
    #         print("타자가 수를 선택하고 있습니다.")
    #         wait()
    #         time.sleep(1)
    #         print("타자가 수를 선택하였습니다.")
    #         c_hit = com_hit(player_pitch_list)  # 투수의 합을 타자가 분할해서 숫자를 예측함
    #         final_decision = decision(c_hit, player_pitch_list)  # 투수와 타자 자리 비교 결정
    #         print(final_decision)
    #         if (((
    #                      final_decision != 'homerun' and final_decision != 'foul') and final_decision != 'strike') and final_decision != 'ball'):  # 홈런과 파울이 아닐때만 수비함
    #             defen = user_defense(defen)
    #
    #             if defen == 1:  # 수비 성공하면
    #                 outNum += 1  # outNum++1
    #                 print('1 out 입니다.')
    #             elif (defen == 0):
    #                 strikeNum, ballNum, outNum = attackscore(final_decision, defen, strikeNum, ballNum, outNum)
    #
    #         elif (final_decision == 'homerun'):  # 홈런이면
    #             strikeNum, ballNum, outNum = attackscore(final_decision, defen, strikeNum, ballNum, outNum)
    #         elif (final_decision == 'strike'):
    #             strikeNum += 1
    #             print(strikeNum, 'strike 입니다')
    #         elif (final_decision == 'foul'):
    #             if (strikeNum != 2):
    #                 strikeNum += 1
    #                 print(strikeNum, 'strike 입니다')
    #         elif (final_decision == 'ball'):
    #             if final_decision == 'ball':
    #                 ballNum += 1
    #                 if ballNum == 4:  # 볼넷일 때
    #                     ballNum = 0
    #                     getonbase_ball(1)
    #                     print('볼넷입니다. 주자가 출루합니다.')
    #                 else:
    #                     print(ballNum, 'ball 입니다.')
    #
    #     outNum_t += 1
    #     print('상대 팀은 총 ', outNum_t, 'out 되었습니다.')
    #     print()
    #
    # com_attackend(inning_score, com_score)
    #
    # game_end(i, user_score, com_score)


class cAttack:
    pass


class aInning:
    def __init__(self):
        if player == '선공':
            pAttack
            cAttack
        elif player == '후공':
            cAttack
            pAttack
        pass


#  ---------화면구성요소---------


class SBO(Frame):  # 미완
    def __init__(self):
        Frame.__init__(self, width='150', height='100', relief='solid', bd='1')
        self.grid_propagate(0)
        for i in range(3):
            self.rowconfigure(i, weight=1)
        for i in range(3):
            self.columnconfigure(i, weight=1)
        S = Label(self, text='S ')
        S.grid(column=0, row=0, padx='2')
        S_count = Label(self, text='●●　', fg='orange')
        S_count.grid(column=1, row=0)

        B = Label(self, text='B ', padx='2')
        B.grid(column=0, row=1)
        B_count = Label(self, text='●●●', fg='green')
        B_count.grid(column=1, row=1)

        O = Label(self, text='O ', padx='2')
        O.grid(column=0, row=2)
        O_count = Label(self, text='●　　', fg='red')
        O_count.grid(column=1, row=2)

    def sbo_update(self, s, b, o):
        pass


class ScoreBoard(Frame):
    def __init__(self):
        Frame.__init__(self, width='200', height='150', relief='solid', bd='1')
        self.grid_propagate(0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        team_name1 = Label(self, text="A TEAM")
        team_name2 = Label(self, text="B TEAM")
        team_name1.grid(column='0', row='0')
        team_name2.grid(column='0', row='1')

        team_score1 = Label(self, text="0")
        team_score2 = Label(self, text="0")
        team_score1.grid(column='1', row='0')
        team_score2.grid(column='1', row='1')

        innnum = Label(self, text="0회")
        innnum.grid(column='0', row='2', columnspan='2')


class BallButton(Frame):
    def __init__(self):
        self.n = 0
        self.button_flag = 0
        Frame.__init__(self, width='400', height='200', relief='solid', bd='1')
        self.place(x=400, y=600)
        self.grid_propagate(0)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        for i in range(5):
            self.columnconfigure(i, weight=1)
        self.button0 = Button(self, width='9', height='4', text='0')
        self.button0.config(command=lambda: [self.number_select(0), self.button0.config(state='disabled')])
        self.button1 = Button(self, width='9', height='4', text='1')
        self.button1.config(command=lambda: [self.number_select(1), self.button1.config(state='disabled')])
        self.button2 = Button(self, width='9', height='4', text='2')
        self.button2.config(command=lambda: [self.number_select(2), self.button2.config(state='disabled')])
        self.button3 = Button(self, width='9', height='4', text='3')
        self.button3.config(command=lambda: [self.number_select(3), self.button3.config(state='disabled')])
        self.button4 = Button(self, width='9', height='4', text='4')
        self.button4.config(command=lambda: [self.number_select(4), self.button4.config(state='disabled')])
        self.button5 = Button(self, width='9', height='4', text='5')
        self.button5.config(command=lambda: [self.number_select(5), self.button5.config(state='disabled')])
        self.button6 = Button(self, width='9', height='4', text='6')
        self.button6.config(command=lambda: [self.number_select(6), self.button6.config(state='disabled')])
        self.button7 = Button(self, width='9', height='4', text='7')
        self.button7.config(command=lambda: [self.number_select(7), self.button7.config(state='disabled')])
        self.button8 = Button(self, width='9', height='4', text='8')
        self.button8.config(command=lambda: [self.number_select(8), self.button8.config(state='disabled')])
        self.button9 = Button(self, width='9', height='4', text='9')
        self.button9.config(command=lambda: [self.number_select(9), self.button9.config(state='disabled')])
        self.button0.grid(column='0', row='0')
        self.button1.grid(column='1', row='0')
        self.button2.grid(column='2', row='0')
        self.button3.grid(column='3', row='0')
        self.button4.grid(column='4', row='0')
        self.button5.grid(column='0', row='1')
        self.button6.grid(column='1', row='1')
        self.button7.grid(column='2', row='1')
        self.button8.grid(column='3', row='1')
        self.button9.grid(column='4', row='1')

    def number_select(self, n):
        self.n = n
        self.button_flag = 1


class attackNum(Frame):
    def __init__(self):
        Frame.__init__(self, width='300', height='300', relief='solid', bd='1')
        self.lab1 = Label(self)
        self.box11 = Label(self, width='9', height='4', relief='solid')
        self.box12 = Label(self, width='9', height='4', relief='solid')
        self.box13 = Label(self, width='9', height='4', relief='solid')
        self.lab2 = Label(self)
        self.box21 = Label(self, width='9', height='4', relief='solid')
        self.box22 = Label(self, width='9', height='4', relief='solid')
        self.box23 = Label(self, width='9', height='4', relief='solid')
        self.lab3 = Label(self)

        self.lab1.grid(column='0', row='0', columnspan='3')
        self.box11.grid(column='0', row='1', padx='2')
        self.box12.grid(column='1', row='1', padx='2')
        self.box13.grid(column='2', row='1', padx='2')
        self.lab2.grid(column='0', row='2', columnspan='3')
        self.box21.grid(column='0', row='3', padx='2')
        self.box22.grid(column='1', row='3', padx='2')
        self.box23.grid(column='2', row='3', padx='2')
        self.lab3.grid(column='0', row='4', columnspan='3')

    def pitch_update(self, coms):
        self.lab1.config(text='상대방이 고른 숫자 3개의 합은')
        tfactor = str(int(coms / 10))
        ofactor = str(coms % 10)
        self.box12.config(text=tfactor)
        self.box13.config(text=ofactor)


# ------함수--------

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


def com_hit(player_pitch_list):  # 타자가 투수가 공던지면 배트 휘두름
    player_pitch_sum = sum(player_pitch_list)  # 세자리수 합
    cpitch = randpart(player_pitch_sum)
    return cpitch


def decision(playhit, compitch):
    bothcorrect = 0
    numcorrect = 0

    # 변수 초기화
    for i in range(0, 3):
        if playhit[i] == compitch[i]:  # 타자의 i번째 숫자/자리 판정
            bothcorrect += 1  # 자릿수o숫자o
        if playhit[i] in compitch:
            numcorrect += 1  # 자릿수x 숫자o
    if (bothcorrect == 0 and numcorrect == 0):
        return 'strike'  # 1out
    elif (bothcorrect == 0 and numcorrect == 1) or (bothcorrect == 0 and numcorrect == 2):
        return 'foul'
    elif (bothcorrect == 1 and numcorrect == 1):
        return 'ball'
    elif (bothcorrect == 0 and numcorrect == 3) or (bothcorrect == 1 and numcorrect == 2):
        return 'singlehit'
    elif (bothcorrect == 2 and numcorrect == 2):
        return 'doublehit'
    elif (bothcorrect == 1 and numcorrect == 3):
        return 'triplehit'
    elif bothcorrect == 3 and numcorrect == 3:
        return 'homerun'


def defense_num(n=1):  # 투수의 수와 타자의 수 오차 구하기(선수비일때)
    num_pitch = 100 * player_pitch_list[0] + 10 * player_pitch_list[1] + player_pitch_list[2]
    num_hit = 100 * c_hit[0] + 10 * c_hit[1] + c_hit[2]
    hit_margin = abs(num_pitch - num_hit)
    return hit_margin


def user_defense(defen):  # 수비수가 타자의 오차 예측하기

    defense_predict = int(input("타자의 오차값을 예측하세요 : "))
    hit_margin = defense_num(1)  # 타자의 오차
    defense_margin = abs(defense_predict - hit_margin)  # 수비수의 오차
    if defense_margin <= 50:
        defen = 1
        print("아웃! 수비를 성공하였습니다.")
        return defen

    elif defense_margin <= 100:
        print('수비를 다시 한번 시도해주세요!')
        print()
        user_defense(1)
    else:
        defen = 0
        print("출루! 수비를 실패하였습니다.")
        return defen


def playerhit(pitch):  # 원소 3개의 리스트를 받으면 합을 표출하고, 플레이어의 반응을 얻고 플레이어가 입력한 리스트 구하기
    com_sum = 0
    for i in pitch:
        com_sum += i
    print('투수가 던진 공의 합은 {}입니다.'.format(com_sum))
    a, b, c = input('합이 {}인 9 이하의 서로 다른 자연수 세 개를 고르시오(쉼표로 구분): '.format(com_sum)).split(',')
    hit = [a, b, c]
    play_hit = [int(i) for i in hit]
    return play_hit


def Cdefense_num(n=1):  # 투수의 수와 타자의 수 오차 구하기(컴퓨터가 수비할때)
    num_pitch = 100 * com_pitch[0] + 10 * com_pitch[1] + com_pitch[2]
    num_hit = 100 * player_hit[0] + 10 * player_hit[1] + player_hit[2]
    hit_margin = abs(num_pitch - num_hit)
    return hit_margin


def com_defense(defen):  # 수비수(컴퓨터)가 타자의 오차 예측하기

    com_defense_predict = rd.randint(1, 987 - 123)  # 수비자(컴퓨터)가 예측한 오차값
    hit_margin = Cdefense_num(1)  # 실제 오차
    defense_margin = abs(com_defense_predict - hit_margin)  # 실제 값과 오차값의 차
    # 1루타, 2루타, 3루타 상황에 따라 나눌 진 추후에 결정하기로.
    if (decision(player_hit, com_pitch) == 'strike') or (decision(player_hit, com_pitch) == 'homerun'):
        None
    else:
        if defense_margin <= 50:
            defen = 1  # 수비성공
            print("아웃! 수비수가 수비를 성공하였습니다.")
            return defen


        elif defense_margin <= 100:
            print('수비수가 다시 한 번 수비를 시도합니다!')
            print()
            com_defense(1)

        else:
            print("출루! 수비수가 수비를 실패하였습니다.")
            defen = 0
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
        for i in range(3, -1, -1):
            if base[i] > 0:  # i루에 사람이 있을경우 앞으로 보내야함, 3루부터 한칸씩 전진.
                base[i] -= 1
                base[i + 1] += 1
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


'''
def ball(decision, ballNum):
    if decision == 'ball':
        ballNum += 1
        if ballNum == 4:   #볼넷일 때
            ballNum = 0
            getonbase_ball(1)
            print('볼넷입니다. 주자가 출루합니다.')
        else:
            print(ballNum, 'ball 입니다.')
    return ballNum
'''


def attackscore(user_decision, defen, strikeNum, ballNum, outNum):  # 타자의 결정에따라 상황 정해짐
    if user_decision == 'strike':
        strikeNum += 1
        print(strikeNum, 'strike 입니다')
    elif user_decision == 'foul':
        if strikeNum != 2:
            strikeNum += 1
            print(strikeNum, 'strike 입니다')
    elif user_decision == 'ball':
        ballNum += 1
        if ballNum == 4:  # 볼넷일 때
            ballNum = 0
            getonbase_ball(1)
            print('볼넷입니다. 주자가 출루합니다.')
        else:
            print(ballNum, 'ball 입니다.')
    elif user_decision == 'singlehit':
        if (defen == 0):
            getonbase(1)
            print('1루타 입니다.')
        else:
            outNum += 1
            print('1 out 되었습니다.')
    elif user_decision == 'doublehit':
        if (defen == 0):
            getonbase(2)
            print('2루타 입니다.')
        else:
            outNum += 1
            print('1 out 되었습니다.')
    elif user_decision == 'triplehit':
        if (defen == 0):
            getonbase(3)
            print('3루타 입니다.')
        else:
            outNum += 1
            print('1 out 되었습니다.')
    elif user_decision == 'homerun':
        getonbase(4)
        print('Congratulations!')
        print('Homerun!')
    if (strikeNum == 3):
        outNum += 1
        print(outNum, 'out 되었습니다.')
    return strikeNum, ballNum, outNum


def user_attackend(inning_score, my_score):  # 사용자의 공격이 끝나고 점수계산
    blank_line()
    print('3 out')

    blank()
    print('당신이 이번 공격에서 얻은 점수는 ', inning_score, '입니다')
    print('현재 당신의 총 점수를 알려드리겠습니다.')
    wait()
    my_score = my_score + inning_score
    print('현재 당신의 총 점수는 ', my_score, '입니다.')


def com_attackend(inning_score, my_score):  # 컴퓨터의 공격이 끝나고 점수계산
    print('3 out')
    print('상대 팀이 이번 공격에서 얻은 점수는 ', inning_score, '입니다')
    print('합산된 상대의 총 점수를 알려드리겠습니다.')
    wait()
    my_score = my_score + inning_score
    print('현재 상대 팀의 총 점수는 ', my_score, '입니다.')


def game_end(i, user_score, com_score):  # 한회가 끝나고 점수계산하는 함수
    print('현재 score을 계산 중입니다.')
    wait()
    print('현재 score는 ', user_score, ':', com_score, '입니다.')
    print(i, '회가 모두 끝났습니다.')
    print('수고하셨습니다.')


if __name__ == '__main__':  # 이 py 파일이 실행되었을 때만 실행
    base = [0, 0, 0, 0, 0]  # 타석 1루 2루 3루 홈
    inning_score = 0  # 회당 플레이어 점수
    playerOp = ['선공', '후공']
    player = None
    playerName = ''
    half_game = '초'
    gameNum = 0
    game = GameMain()
    game.mainloop()
