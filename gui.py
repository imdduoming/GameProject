from tkinter import *
import random as rd
import time
from tkinter import messagebox


# ------tk, 프레임 클래스--------


class GameMain(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1200x900")
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
        Label(self, text='진행할 게임 횟수를 입력해주세요(1~9): ').grid(column='0', row='1')
        self.ent2 = Entry(self)
        self.ent2.grid(column='1', row='1')
        Button(self, text='게임 시작', command=lambda: self.game_start()).grid(column='1', row='2')
        self.lab1 = Label(self, text='')
        self.lab1.grid(column='0', row='3', columnspan='2')
        self.lab2 = Label(self, text='')
        self.lab2.grid(column='0', row='4', columnspan='2')

    def game_start(self):
        if 1 <= int(self.ent2.get()) <= 9:
            global playerOp, player, playerName, gameNum, inning_num
            player = rd.choice(playerOp)
            playerName = self.ent1.get()
            gameNum = int(self.ent2.get())
            if player == '선공':
                inning_num += 1
                messagebox.showinfo("선공", "당신은 선공입니다.")
                self.destroy()
                self.master.switch_frame(pAttack)
            elif player == '후공':
                inning_num += 1
                messagebox.showinfo("후공", "당신은 후공입니다.")
                self.destroy()
                self.master.switch_frame(cAttack)
        else:
            messagebox.showwarning("게임 횟수", "게임 횟수를 재설정해주세요.\n (1~9) ")


class ResultPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.imsilabel = Label(text='점수표 오류로 인해 다시 쓰는중..')
        self.next_button = Button(self)
        self.next_button.pack()
        if inning_num == gameNum and half_game == '말':
            self.next_button.config(text="종료")
        else:
            self.next_button.config(text="진행")

    # noinspection PyMethodMayBeStatic
    def progress(self, master):
        global half_game, inning_num
        if half_game == '말':
            if inning_num == gameNum:
                if user_score > com_score:
                    messagebox.showinfo("승리", "당신의 승리입니다!")
                elif user_score == com_score:
                    messagebox.showinfo("무승부", "무승부입니다.")
                else:
                    messagebox.showerror("패배", "당신의 패배입니다.")
                master.switch_frame(GameMain)
            else:
                inning_num += 1
                half_game = '초'
                if player == '선공':
                    master.switch_frame(pAttack)
                elif player == '후공':
                    master.switch_frame(cAttack)
        elif half_game == '초':
            half_game = '말'
            if player == '선공':
                master.switch_frame(pAttack)
            elif player == '후공':
                master.switch_frame(cAttack)


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
        global inning_score, base
        inning_score = 0
        base = [0, 0, 0, 0, 0]
        while outNum < 3:
            self.bfr.base_update()
            self.sbo.sbo_update(strikeNum, ballNum, outNum)
            self.scr.score_update()
            self.but.button_reset()
            self.atn.all_reset()
            self.master.update()
            time.sleep(1.5)
            defen = 0
            player_hit = []
            num_list = list(range(1, 10))
            com_pitch = rd.sample(num_list, 3)  # 수비자(컴퓨터)의 투구(리스트)
            coms = sum(com_pitch)

            self.atn.pitch_update(coms)  # 컴퓨터가 던진 수 합
            self.atn.lab2.config(text='당신이 고른 수는')
            self.atn.master.update()

            self.wait_variable(self.but.n)
            player_hit.append(self.but.n.get())
            self.atn.box21.config(text=str(self.but.n.get()))
            self.atn.master.update()

            self.wait_variable(self.but.n)
            player_hit.append(self.but.n.get())
            self.atn.box22.config(text=str(self.but.n.get()))
            self.atn.master.update()

            self.wait_variable(self.but.n)
            player_hit.append(self.but.n.get())
            self.atn.box23.config(text=str(self.but.n.get()))
            self.atn.master.update()

            user_decision = decision(player_hit, com_pitch)
            self.atn.lab3.config(text=user_decision)
            self.atn.master.update()
            time.sleep(1.5)

            if user_decision == 'homerun':
                messagebox.showwarning("홈런", "홈런! 축하합니다!")
            elif (((
                           user_decision != 'homerun' and user_decision != 'foul') and user_decision != 'strike') and user_decision != 'ball'):
                defen = com_defense(com_pitch, player_hit)

            if defen == 1:
                messagebox.showerror("적 수비 성공", "적이 수비를 성공했습니다.")
            strikeNum, ballNum, outNum = attack_score(user_decision, defen, strikeNum, ballNum,
                                                      outNum)  # out횟수와 각 1,2,3,4루의 상황 결정
            global user_score, come_home
            user_score += come_home
            come_home = 0
            time.sleep(1.5)
        uin_score.append(inning_score)
        messagebox.showinfo("3 OUT", "3 OUT 으로 공수교대합니다.")
        master.switch_frame(ResultPage)


class cAttack(Frame):
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
        global inning_score, base
        inning_score = 0
        base = [0, 0, 0, 0, 0]
        while outNum < 3:
            self.bfr.base_update()
            self.sbo.sbo_update(strikeNum, ballNum, outNum)
            self.scr.score_update()
            self.but.button_reset()
            self.atn.all_reset()
            self.master.update()
            time.sleep(1)
            self.d_list = []
            self.defen = 2
            player_pitch = []

            self.atn.lab1.config(text='숫자 세개를 골라주세요!')
            self.atn.master.update()

            self.wait_variable(self.but.n)
            player_pitch.append(self.but.n.get())
            self.atn.box11.config(text=str(self.but.n.get()))
            self.atn.master.update()

            self.wait_variable(self.but.n)
            player_pitch.append(self.but.n.get())
            self.atn.box12.config(text=str(self.but.n.get()))
            self.atn.master.update()

            self.wait_variable(self.but.n)
            player_pitch.append(self.but.n.get())
            self.atn.box13.config(text=str(self.but.n.get()))
            self.atn.master.update()

            self.atn.lab1.config(text='내가 고른 수는')
            self.atn.lab2.config(text="상대가 숫자를 예측중입니다.")
            master.update()
            time.sleep(1.5)

            c_hit = com_hit(player_pitch)
            user_decision = decision(player_pitch, c_hit)
            self.atn.lab3.config(text=user_decision)
            self.atn.master.update()
            time.sleep(2)

            if (((
                         user_decision != 'homerun' and user_decision != 'foul') and user_decision != 'strike') and user_decision != 'ball'):
                while self.defen >= 2:
                    self.player_defense()
                    self.defen = user_defense(player_pitch, c_hit, self.d_list)
                    if self.defen == 1:
                        messagebox.showerror("수비 성공", "수비 성공! 적을 아웃시켰습니다.")
                        outNum += 1
                        break
                    elif self.defen == 0:
                        messagebox.showerror("수비 실패", "수비 실패! 적이 진루합니다.")
                        strikeNum, ballNum, outNum = attack_score(user_decision, self.defen, strikeNum, ballNum,
                                                                  outNum)
                        break
                    else:
                        self.atn.lab3.config(text='다시 입력해 주세요.')
            else:
                strikeNum, ballNum, outNum = attack_score(user_decision, 0, strikeNum, ballNum,
                                                          outNum)
            global com_score, come_home
            com_score += come_home
            come_home = 0
            time.sleep(1)
        cin_score.append(inning_score)
        messagebox.showinfo("3 OUT", "3 OUT 으로 공수교대합니다.")
        master.switch_frame(ResultPage)

    def player_defense(self):
        self.atn.lab2.config(text="상대의 안타! 얼마나 차이날까요?")
        self.atn.lab3.config(text="오차를 예측하세요")
        self.atn.box2_reset()
        self.but.button_reset()
        self.master.update()

        self.wait_variable(self.but.n)
        self.d_list.append(self.but.n.get())
        self.atn.box21.config(text=str(self.but.n.get()))
        self.atn.master.update()

        self.wait_variable(self.but.n)
        self.d_list.append(self.but.n.get())
        self.atn.box22.config(text=str(self.but.n.get()))
        self.atn.master.update()

        self.wait_variable(self.but.n)
        self.d_list.append(self.but.n.get())
        self.atn.box23.config(text=str(self.but.n.get()))
        self.atn.master.update()


#  ---------화면구성요소---------

class BaseFrame(Frame):
    def __init__(self):
        Frame.__init__(self, width='200', height='200', relief='solid', bd='1')
        self.c_base = Canvas(self, width='200', height='200')
        self.c_base.pack()
        self.base_update()
        self.master.update()

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


class SBO(Frame):  # 미완
    def __init__(self):
        Frame.__init__(self, width='150', height='100', relief='solid', bd='1')
        self.grid_propagate(0)
        for i in range(3):
            self.rowconfigure(i, weight=1)
        for i in range(3):
            self.columnconfigure(i, weight=1)
        self.S = Label(self, text='S ')
        self.S.grid(column=0, row=0, padx='2')
        self.S_count = Label(self, text='', fg='orange')
        self.S_count.grid(column=1, row=0)

        self.B = Label(self, text='B ', padx='2')
        self.B.grid(column=0, row=1)
        self.B_count = Label(self, text='', fg='green')
        self.B_count.grid(column=1, row=1)

        self.O = Label(self, text='O ', padx='2')
        self.O.grid(column=0, row=2)
        self.O_count = Label(self, text='', fg='red')
        self.O_count.grid(column=1, row=2)

    def sbo_update(self, s, b, o):
        s_st = '●' * s + '　' * (3 - s)
        b_st = '●' * b + '　' * (3 - b)
        o_st = '●' * o + '　' * (3 - o)
        self.S_count.config(text=s_st)
        self.B_count.config(text=b_st)
        self.O_count.config(text=o_st)


class ScoreBoard(Frame):
    def __init__(self):
        Frame.__init__(self, width='200', height='150', relief='solid', bd='1')
        self.grid_propagate(0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self.team_name1 = Label(self)
        self.team_name2 = Label(self)
        self.team_name1.grid(column='0', row='0')
        self.team_name2.grid(column='0', row='1')

        self.team_score1 = Label(self, text="0")
        self.team_score2 = Label(self, text="0")
        self.team_score1.grid(column='1', row='0')
        self.team_score2.grid(column='1', row='1')

        self.innnum = Label(self, text="0회")
        self.innnum.grid(column='0', row='2', columnspan='2')

        if player == '선공':
            self.team_name1.config(text=playerName)
            self.team_name2.config(text="COM")

        elif player == '후공':
            self.team_name1.config(text="COM")
            self.team_name2.config(text=playerName)

        self.innnum.config(text='{}회 {}'.format(inning_num, half_game))
        self.score_update()

    def score_update(self):
        if player == '선공':
            self.team_score1.config(text=user_score)
            self.team_score2.config(text=com_score)
        elif player == '후공':
            self.team_score2.config(text=user_score)
            self.team_score1.config(text=com_score)
        self.master.update()


class BallButton(Frame):
    def __init__(self):
        self.n = IntVar()
        Frame.__init__(self, width='400', height='200', relief='solid', bd='1')
        self.grid_propagate(0)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        for i in range(5):
            self.columnconfigure(i, weight=1)
        self.button0 = Button(self, width='9', height='4', text='')
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
        self.n.set(n)

    def button_reset(self):
        self.button1.config(state='normal')
        self.button2.config(state='normal')
        self.button3.config(state='normal')
        self.button4.config(state='normal')
        self.button5.config(state='normal')
        self.button6.config(state='normal')
        self.button7.config(state='normal')
        self.button8.config(state='normal')
        self.button9.config(state='normal')


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

    def all_reset(self):
        self.lab1.config(text='')
        self.box11.config(text='')
        self.box12.config(text='')
        self.box13.config(text='')
        self.lab2.config(text='')
        self.box21.config(text='')
        self.box22.config(text='')
        self.box23.config(text='')
        self.lab3.config(text='')

    def box1_reset(self):
        self.box11.config(text='')
        self.box12.config(text='')
        self.box13.config(text='')

    def box2_reset(self):
        self.box21.config(text='')
        self.box22.config(text='')
        self.box23.config(text='')

    def pitch_update(self, coms):
        self.lab1.config(text='상대방이 고른 숫자 3개의 합은')
        tfactor = str(int(coms / 10))
        ofactor = str(coms % 10)
        self.box12.config(text=tfactor)
        self.box13.config(text=ofactor)


class TotalScore(Frame):
    def __init__(self):
        Frame.__init__(self, width='800', height='600', relief='solid', bd='1')
        self.box0l = []
        self.tname1 = Label(self, width='5', height='4')
        self.tname2 = Label(self, width='5', height='4')
        self.tname1.grid(column=0, row=1)
        self.tname2.grid(column=0, row=2)
        for i in range(9):
            self.box0l.append(Label(self, width='7', height='2', relief='solid', text=str(i + 1)))
            self.box0l[i].grid(column=i + 1, row=0)
        self.box0l.append(Label(self, width='7', height='2', relief='solid', text='총점'))
        self.box0l[9].grid(column=10, row=0)
        self.box1l = []
        for i in range(10):
            self.box1l.append(Label(self, width='7', height='4', relief='solid'))
            self.box1l[i].grid(column=i + 1, row=1)
        self.box2l = []
        for i in range(10):
            self.box2l.append(Label(self, width='7', height='4', relief='solid'))
            self.box2l[i].grid(column=i + 1, row=2)
        if player == '선공':
            self.tname1.config(text=playerName)
            self.tname2.config(text='COM')
        elif player == '후공':
            self.tname2.config(text=playerName)
            self.tname1.config(text='COM')


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
    if bothcorrect == 0 and numcorrect == 0:
        return 'strike'  # 1out
    elif (bothcorrect == 0 and numcorrect == 1) or (bothcorrect == 0 and numcorrect == 2):
        return 'foul'
    elif bothcorrect == 1 and numcorrect == 1:
        return 'ball'
    elif (bothcorrect == 0 and numcorrect == 3) or (bothcorrect == 1 and numcorrect == 2):
        return 'singlehit'
    elif bothcorrect == 2 and numcorrect == 2:
        return 'doublehit'
    elif bothcorrect == 1 and numcorrect == 3:
        return 'triplehit'
    elif bothcorrect == 3 and numcorrect == 3:
        return 'homerun'


def defense_num(player_pitch_list, c_hit):  # 투수의 수와 타자의 수 오차 구하기(선수비일때)
    num_pitch = 100 * player_pitch_list[0] + 10 * player_pitch_list[1] + player_pitch_list[2]
    num_hit = 100 * c_hit[0] + 10 * c_hit[1] + c_hit[2]
    hit_margin = abs(num_pitch - num_hit)
    return hit_margin


def user_defense(player_pitch, c_hit, d_list):  # 수비수가 타자의 오차 예측하기
    d_predict = sum(d_list)
    hit_margin = defense_num(player_pitch, c_hit)  # 타자의 오차
    defense_margin = abs(d_predict - hit_margin)  # 수비수의 오차
    if defense_margin <= 50:
        defen = 1
        return defen

    elif defense_margin <= 100:
        defen = 2
        return defen
    else:
        defen = 0
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


def cdefense_num(com_pitch, player_hit):  # 투수의 수와 타자의 수 오차 구하기(컴퓨터가 수비할때)
    num_pitch = 100 * com_pitch[0] + 10 * com_pitch[1] + com_pitch[2]
    num_hit = 100 * player_hit[0] + 10 * player_hit[1] + player_hit[2]
    hit_margin = abs(num_pitch - num_hit)
    return hit_margin


def com_defense(com_pitch, player_hit):  # 수비수(컴퓨터)가 타자의 오차 예측하기
    com_defense_predict = rd.randint(1, 987 - 123)  # 수비자(컴퓨터)가 예측한 오차값
    hit_margin = cdefense_num(com_pitch, player_hit)  # 실제 오차
    defense_margin = abs(com_defense_predict - hit_margin)  # 실제 값과 오차값의 차
    if defense_margin <= 50:
        defen = 1  # 수비성공
        return defen

    elif defense_margin <= 100:
        com_defense(com_pitch, player_hit)

    else:
        defen = 0
        return defen


def getonbase(n=1):
    global base, inning_score, come_home
    base[0] = 1  # 한명을 타석으로 보냄
    for _ in range(n):  # n루타 는 곧 n회의 한칸 진루
        for i in range(3, -1, -1):
            if base[i] > 0:  # i루에 사람이 있을경우 앞으로 보내야함, 3루부터 한칸씩 전진.
                base[i] -= 1
                base[i + 1] += 1
    come_home = base[4]
    inning_score += base[4]  # 홈에 도착한 인원들을 합산
    base[4] = 0  # 홈 초기화


def gon_ball():
    global base
    if base[1] == 1:
        if base[2] == 1:
            getonbase(1)
        elif base[2] == 0:
            base[2] = 1
    elif base[1] == 0:
        base[1] = 1


def attack_score(user_decision, defen, strikeNum, ballNum, outNum):  # 타자의 결정에따라 상황 정해짐
    if user_decision == 'strike':
        strikeNum += 1
    elif user_decision == 'foul':
        if strikeNum != 2:
            strikeNum += 1
    elif user_decision == 'ball':
        ballNum += 1
        if ballNum == 4:  # 볼넷일 때
            ballNum = 0
            gon_ball()
    elif user_decision == 'singlehit':
        if defen == 0:
            getonbase(1)
        else:
            outNum += 1
    elif user_decision == 'doublehit':
        if defen == 0:
            getonbase(2)
        else:
            outNum += 1
    elif user_decision == 'triplehit':
        if defen == 0:
            getonbase(3)
        else:
            outNum += 1
    elif user_decision == 'homerun':
        getonbase(4)
    if strikeNum == 3:
        outNum += 1
        strikeNum = 0
        print(outNum, 'out 되었습니다.')
    return strikeNum, ballNum, outNum


if __name__ == '__main__':  # 이 py 파일이 실행되었을 때만 실행
    base = [0, 0, 0, 0, 0]  # 타석 1루 2루 3루 홈
    inning_score = 0
    user_score = 0
    com_score = 0
    uin_score = []
    cin_score = []
    come_home = 0

    playerOp = ['선공', '후공']
    player = ''
    playerName = ''
    inning_num = 0
    half_game = '초'
    gameNum = 0
    game = GameMain()
    game.mainloop()
