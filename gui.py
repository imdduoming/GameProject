from tkinter import *
import random as rd
import time
from tkinter import messagebox
from PIL import Image as pim
from PIL import ImageTk as pit


# ------tk, 프레임 클래스--------


class GameMain(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1200x900")
        self.title("야구 게임")
        self.resizable(False, False)
        # self.pack_propagate(0)
        self.frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()


class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg='#509134', width='1200', height='900')
        self.grid_propagate(0)
        self.bgimg = pit.PhotoImage(pim.open('main.png'))
        self.bc = Canvas(self, width='1200', height='900')
        self.bc.place(x=0, y=0)
        self.bg = self.bc.create_image(0, 0, anchor='nw', image=self.bgimg)
        self.but1 = Button(self, text="게임 시작", command=lambda: master.switch_frame(NewGame), width='20', height='5')
        self.but1.grid(column='0', row='0', padx=125, pady=650)
        self.but2 = Button(self, text="튜토리얼", width='20',
                           height='5', command=lambda: master.switch_frame(Tutorial))
        self.but2.grid(column='1', row='0', padx=125, pady=650)
        self.but3 = Button(self, text="게임종료", command=quit, width='20', height='5')
        self.but3.grid(column='2', row='0', padx=125, pady=650)


class NewGame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width='1200', height='900')
        self.grid_propagate(0)
        self.bgimg = pit.PhotoImage(pim.open('background.png'))
        self.bc = Canvas(self, width='1200', height='900')
        self.bc.place(x=0, y=0)
        self.bc.create_image(0, 0, anchor='nw', image=self.bgimg)
        self.lab1 = Label(self, text='당신의 팀 이름을 입력해주세요: ', font=("맑은 고딕", 20))
        self.lab1.grid(column='0', row='0', padx='100', pady='50')
        self.ent1 = Entry(self, font=("맑은 고딕", 20))
        self.ent1.grid(column='1', row='0', padx='100', pady='50')
        self.lab2 = Label(self, text='진행할 게임 횟수를 입력해주세요(1~9): ', font=("맑은 고딕", 20))
        self.lab2.grid(column='0', row='1', padx='100', pady='50')
        self.ent2 = Entry(self, font=("맑은 고딕", 20))
        self.ent2.grid(column='1', row='1', padx='100', pady='50')
        self.but1 = Button(self, text='게임 시작', command=lambda: self.game_start(master),
                           width='20', height='6', font=("맑은 고딕", 20))
        self.but1.grid(column='1', row='2', padx='100', pady='50')

    def game_start(self, master):
        if 1 <= int(self.ent2.get()) <= 9:
            global playerOp, player, playerName, gameNum, inning_num
            player = rd.choice(playerOp)
            playerName = self.ent1.get()
            gameNum = int(self.ent2.get())
            if player == '선공':
                inning_num += 1
                messagebox.showinfo("선공", "당신은 선공입니다.")
                # self.destroy()
                master.switch_frame(PlayerAttack)
            elif player == '후공':
                inning_num += 1
                messagebox.showinfo("후공", "당신은 후공입니다.")
                # self.destroy()
                master.switch_frame(ComAttack)
        else:
            messagebox.showwarning("게임 횟수", "게임 횟수를 재설정해주세요.\n (1~9) ")


class ResultPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width='1200', height='900')
        self.pack_propagate(0)
        self.bgimg = pit.PhotoImage(pim.open('background.png'))
        self.bc = Canvas(self, width='1200', height='900')
        self.bc.place(x=0, y=0)
        self.bc.create_image(0, 0, anchor='nw', image=self.bgimg)
        self.blab1 = Label(self, text=''.format(), height='20')
        self.blab1.pack()
        self.tot = TotalScore(self)
        self.tot.pack()
        self.blab1 = Label(self, height='10')
        self.blab1.pack()
        self.pg_button = Button(self, text='진행', command=lambda: self.progress(master), width='20', height='5')
        if half_game == '말' and inning_num == gameNum:
            self.pg_button.config(text='종료')
        self.pg_button.pack()

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
                master.switch_frame(StartPage)
            else:
                inning_num += 1
                half_game = '초'
                if player == '선공':
                    master.switch_frame(PlayerAttack)
                elif player == '후공':
                    master.switch_frame(ComAttack)
        elif half_game == '초':
            half_game = '말'
            if player == '선공':
                master.switch_frame(ComAttack)
            elif player == '후공':
                master.switch_frame(PlayerAttack)


class PlayerAttack(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width='1200', height='900')
        self.bgimg = pit.PhotoImage(pim.open('background.png'))
        self.bc = Canvas(self, width='1200', height='900')
        self.bc.place(x=0, y=0)
        self.bc.create_image(0, 0, anchor='nw', image=self.bgimg)
        self.bfr = BaseFrame(self)
        self.bfr.place(x=40, y=40)
        self.sbo = SBO(self)
        self.sbo.place(x=1000, y=700)
        self.but = BallButton(self)
        self.but.place(x=400, y=600)
        self.atn = attackNum(self)
        self.atn.place(x=500, y=250)
        self.scr = ScoreBoard(self)
        self.scr.place(x=950, y=40)
        self.start_button = Button(self, text='시작', width="25", height="8", command=self.play, font=("맑은 고딕", 15))
        self.start_button.place(x=475, y=300)

    def play(self):
        self.start_button.destroy()
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
        self.master.switch_frame(ResultPage)


class ComAttack(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width='1200', height='900')
        self.bgimg = pit.PhotoImage(pim.open('background.png'))
        self.bc = Canvas(self, width='1200', height='900')
        self.bc.place(x=0, y=0)
        self.bc.create_image(0, 0, anchor='nw', image=self.bgimg)
        self.bfr = BaseFrame(self)
        self.bfr.place(x=40, y=40)
        self.sbo = SBO(self)
        self.sbo.place(x=1000, y=700)
        self.but = BallButton(self)
        self.but.place(x=400, y=600)
        self.atn = attackNum(self)
        self.atn.place(x=450, y=250)
        self.scr = ScoreBoard(self)
        self.scr.place(x=950, y=40)
        self.start_button = Button(self, text='시작', width=25, height=8, command=self.play, font=("맑은 고딕", 15))
        self.start_button.place(x=475, y=300)
        self.d_list = []

    def play(self):
        self.start_button.destroy()
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
            player_pitch = []
            defen = 2

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
            self.master.update()
            time.sleep(1.5)

            c_hit = com_hit(player_pitch)
            user_decision = decision(player_pitch, c_hit)
            self.atn.lab3.config(text=user_decision)
            self.atn.master.update()
            time.sleep(2)

            if (((
                         user_decision != 'homerun' and user_decision != 'foul') and user_decision != 'strike') and user_decision != 'ball'):
                while defen > 1:
                    self.d_list = []
                    self.player_defense()
                    defen = user_defense(player_pitch, c_hit, self.d_list)
                    if defen == 1:
                        messagebox.showerror("수비 성공", "수비 성공! 적을 아웃시켰습니다.")
                        outNum += 1
                        break
                    elif defen == 0:
                        messagebox.showerror("수비 실패", "수비 실패! 적이 진루합니다.")
                        strikeNum, ballNum, outNum = attack_score(user_decision, defen, strikeNum, ballNum,
                                                                  outNum)
                        break
                    else:
                        self.atn.lab2.config(text='실제 오차와 가깝습니다!')
                        self.atn.lab3.config(text='다시 예측해보세요.')
                        self.master.update()
                        time.sleep(2)
            else:
                strikeNum, ballNum, outNum = attack_score(user_decision, 0, strikeNum, ballNum,
                                                          outNum)
            global com_score, come_home
            com_score += come_home
            come_home = 0
            time.sleep(1)
        cin_score.append(inning_score)
        messagebox.showinfo("3 OUT", "3 OUT 으로 공수교대합니다.")
        self.master.switch_frame(ResultPage)

    def player_defense(self):
        self.atn.lab2.config(text="상대의 안타! 얼마나 차이날까요?")
        self.atn.lab3.config(text="오차를 예측하세요")
        self.atn.box2_reset()
        self.but.button_reset()
        self.but.button0.config(text='0', state='normal')
        self.master.update()

        self.wait_variable(self.but.n)
        self.d_list.append(self.but.n.get())
        self.atn.box21.config(text=str(self.but.n.get()))
        self.but.button_reset()
        self.but.button0.config(text='0', state='normal')
        self.atn.master.update()

        self.wait_variable(self.but.n)
        self.d_list.append(self.but.n.get())
        self.atn.box22.config(text=str(self.but.n.get()))
        self.but.button_reset()
        self.but.button0.config(text='0', state='normal')
        self.atn.master.update()

        self.wait_variable(self.but.n)
        self.d_list.append(self.but.n.get())
        self.atn.box23.config(text=str(self.but.n.get()))
        self.but.button_reset()
        self.but.button0.config(text='0', state='normal')
        self.atn.master.update()


class Tutorial(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width='1200', height='900')
        self.bgimg = pit.PhotoImage(pim.open('background.png'))
        self.bc = Canvas(self, width='1200', height='900')
        self.bc.place(x=0, y=0)
        self.bc.create_image(0, 0, anchor='nw', image=self.bgimg)
        self.d_list = []
        self.bfr = BaseFrame(self)
        self.bfr.place(x=40, y=40)
        self.sbo = SBO(self)
        self.sbo.place(x=1000, y=700)
        self.but = BallButton(self)
        self.but.place(x=400, y=600)
        self.atn = attackNum(self)
        self.atn.place(x=450, y=250)
        self.scr = ScoreBoard(self)
        self.scr.place(x=950, y=40)
        self.explain_frame = Frame(self, width=800, height=400, bg='#C5FFFF', relief='solid', bd='2')
        self.explain_frame.pack_propagate(0)
        self.explain_frame.place(x=200, y=200)
        self.elab = Label(self.explain_frame, text='''
        
        
        
        
        
        간단한 조작을 통해 게임을 배워봅시다.''', bg='#C5FFFF',
                          font=("맑은 고딕", 12))
        self.elab.pack(anchor='center', pady=10)
        self.ebtn = Button(self.explain_frame, text='다음', command=self.tutorial)
        self.ebtn.pack(side='bottom', anchor='center', pady=10)
        self.tflag = 0

    def tutorial(self):
        if self.tflag == 0:
            self.elab.config(text='''
            
            
            
            이 게임은 숫자로 하는 야구 게임입니다.
            서로 상대방이 어떤 숫자 3개를 선택했는지 예상하면서 공격과 수비를 합니다.
            상대방의 숫자 3개가 각각 무엇이고 어디에 있는지 맞춰보는 게임입니다.''')
            self.tflag += 1
        elif self.tflag == 1:
            self.elab.config(text='''
            
            
            
            어떻게 하는지 이해해보기 위해 직접 해봅시다.
            게임은 수비 플레이어가 투수가 되어 숫자 세개를 상대방에게 던지면서 시작합니다.
            세 숫자는 모두 달라야 합니다.
            숫자 3 6 5을 입력해보세요.''')
            self.tflag += 1
        elif self.tflag == 2:
            self.explain_frame.place_forget()
            self.play1()
        elif self.tflag == 3:
            self.explain_frame.place(x=200, y=200)
            self.elab.config(text='''
            
            
            
            잘 하셨습니다!
            이제 적(컴퓨터)이 당신이 던진 숫자 3개의 합을 보고 숫자를 예측합니다.
            상대가 맞추면 베이스로 나가게 되어 득점의 기회를 얻게 됩니다.
            하지만 수비쪽에서도 이를 다시 한번 방어할 기회가 있습니다.''')
            self.tflag += 1
        elif self.tflag == 4:
            self.elab.config(text='''
            
            
            
            적이 숫자를 입력했는데 일정 개수 이상 맟춘다면
            상대방은 안타를 치게 됩니다. 이때가 바로 당신의 수비 기회입니다.
            수비하라는 메세지가 뜨면 내가 보낸 숫자와 적이 예측한 숫자가
            얼마나 다를지 예측해야 합니다.''')
            self.tflag += 1
        elif self.tflag == 5:
            self.elab.config(text='''
            
            
            
            실제로 해보겠습니다.
            당신이 보낸 365와 87만큼 차이난다고 예측했다고 합시다.
            예측 숫자에 0 8 7을 입력해주세요''')
            self.tflag += 1
        elif self.tflag == 6:
            self.explain_frame.place_forget()
            self.play2()
        elif self.tflag == 7:
            self.explain_frame.place(x=200, y=200)
            self.elab.config(text='''
            
            
            
            잘 하셨습니다!
            예측한 오차가 100보다 작으면 수비에 성공하여 적을 아웃시킵니다.
            200보다 작고 100보다 크다면 다시 한번 예측할 기회를 갖게 됩니다.
            기존에 예측한 것보다 적의 숫자에 다가가야겠죠?''')
            self.tflag += 1
        elif self.tflag == 8:
            self.elab.config(text='''
            
            
            
            이번엔 공격을 연습해봅시다.
            공격 플레이어는 상대방이 던진 숫자 3개의 합을 보고
            적이 어떤 숫자를 입력했는지 예상합니다.''')
            self.tflag += 1
        elif self.tflag == 9:
            self.elab.config(text='''
            
            
            
            이때 예측하는 숫자의 합이 꼭 적이 던진 수가 아니여도 됩니다.
            예측되는 숫자를 전략적으로 제시해보세요.
            상대방이 9 라고 제시했을 때 당신은 어떤 숫자 3개라고 생각하시나요?''')
            self.tflag += 1
        elif self.tflag == 10:
            self.explain_frame.place_forget()
            self.play3()
        elif self.tflag == 11:
            self.explain_frame.place(x=200, y=200)
            self.elab.config(text='''
            
            
            
            잘 하셨습니다!
            이렇게 공격에 성공하여 홈런을 하거나 안타를 통해
            주자를 홈까지 보내면 득점하게 됩니다.''')
            self.tflag += 1
        elif self.tflag == 12:
            self.elab.config(text='''
            
            
            
            이제 게임 진행이 이해되시나요?
            만약 잘 이해되지 않는다면 한번 더 튜토리얼을 플레이하시고
            이해된다면 게임 시작을 통해 실제 게임을 플레이해보세요!''')
            self.tflag += 1
        elif self.tflag == 13:
            self.master.switch_frame(StartPage)

    def play1(self):
        self.bfr.base_update()
        self.scr.score_update()
        self.but.button_reset()
        self.atn.all_reset()
        self.master.update()
        time.sleep(1)
        pitch_flag = 0
        player_pitch = [0, 0, 0]

        while player_pitch != [3, 6, 5]:
            self.atn.all_reset()
            self.atn.lab1.config(text='3 6 5를 차례로 입력하세요')
            self.atn.master.update()
            player_pitch = [0, 0, 0]
            if pitch_flag == 1:
                self.atn.lab1.config(text='다시 3 6 5를 입력해보세요')
                self.atn.master.update()

            self.but.button_reset()
            self.wait_variable(self.but.n)
            player_pitch[0] = self.but.n.get()
            self.atn.box11.config(text=str(self.but.n.get()))
            self.atn.master.update()

            self.wait_variable(self.but.n)
            player_pitch[1] = self.but.n.get()
            self.atn.box12.config(text=str(self.but.n.get()))
            self.atn.master.update()

            self.wait_variable(self.but.n)
            player_pitch[2] = self.but.n.get()
            self.atn.box13.config(text=str(self.but.n.get()))
            self.atn.master.update()
            pitch_flag = 1

        self.tflag += 1
        self.tutorial()

    def play2(self):
        self.atn.lab2.config(text="상대의 안타! 얼마나 차이날까요?")
        self.atn.lab3.config(text="0 8 7 을 입력하세요")
        self.atn.box2_reset()
        self.but.button_reset()
        self.but.button0.config(text='0', state='normal')
        self.master.update()
        def_flag = 0
        while self.d_list != [0, 8, 7]:
            self.d_list = [0, 0, 0]
            self.atn.box2_reset()
            if def_flag == 1:
                self.atn.lab3.config(text='다시 0 8 7을 입력해보세요')
                self.atn.master.update()

            self.wait_variable(self.but.n)
            self.d_list[0] = self.but.n.get()
            self.atn.box21.config(text=str(self.but.n.get()))
            self.but.button_reset()
            self.but.button0.config(text='0', state='normal')
            self.atn.master.update()

            self.wait_variable(self.but.n)
            self.d_list[1] = self.but.n.get()
            self.atn.box22.config(text=str(self.but.n.get()))
            self.but.button_reset()
            self.but.button0.config(text='0', state='normal')
            self.atn.master.update()

            self.wait_variable(self.but.n)
            self.d_list[2] = self.but.n.get()
            self.atn.box23.config(text=str(self.but.n.get()))
            self.but.button_reset()
            self.but.button0.config(text='0', state='normal')
            self.atn.master.update()
            def_flag = 1
        messagebox.showerror("수비 성공", "수비 성공! 적을 아웃시켰습니다.")
        self.tflag += 1
        self.tutorial()

    def play3(self):
        self.bfr.base_update()
        self.scr.score_update()
        self.but.button_reset()
        self.atn.all_reset()
        self.master.update()
        time.sleep(0.5)
        player_hit = []
        hit_flag = 0
        coms = 9

        while player_hit != [5, 1, 3]:
            player_hit = [0, 0, 0]
            self.atn.all_reset()
            self.but.button_reset()
            self.atn.master.update()
            self.atn.pitch_update(coms)  # 컴퓨터가 던진 수 합
            self.atn.lab2.config(text='당신이 고른 수는')
            self.atn.lab3.config(text='5 1 3을 입력해보세요')
            if hit_flag == 1:
                self.atn.lab3.config(text='다시 5 1 3을 입력해보세요')
                self.atn.master.update()
            self.atn.master.update()

            self.wait_variable(self.but.n)
            player_hit[0] = self.but.n.get()
            self.atn.box21.config(text=str(self.but.n.get()))
            self.atn.master.update()

            self.wait_variable(self.but.n)
            player_hit[1] = self.but.n.get()
            self.atn.box22.config(text=str(self.but.n.get()))
            self.atn.master.update()

            self.wait_variable(self.but.n)
            player_hit[2] = self.but.n.get()
            self.atn.box23.config(text=str(self.but.n.get()))
            self.atn.master.update()
            hit_flag = 1

        messagebox.showinfo("홈런", "축하합니다! 홈런입니다!")
        self.tflag += 1
        self.tutorial()


#  ---------화면구성요소---------

class BaseFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(width='200', height='200', relief='solid', bd='1')
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


class SBO(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(width='150', height='100', relief='solid', bd='1')
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
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(width='200', height='150', relief='solid', bd='1')
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
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(width='400', height='200', relief='solid', bd='1')
        self.n = IntVar()
        self.grid_propagate(0)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        for i in range(5):
            self.columnconfigure(i, weight=1)
        self.button0 = Button(self, width='9', height='4', text='', state='disabled')
        self.button0.config(command=lambda: [self.number_select(0), self.button1.config(state='disabled')])
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
        self.button0.config(text='', state='disabled')
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
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(width='300', height='300', relief='solid', bd='1')
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
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(width='800', height='600', relief='solid', bd='1')
        self.box0l = []
        self.tname1 = Label(self, width='5', height='4', relief='solid', bd='1')
        self.tname2 = Label(self, width='5', height='4', relief='solid', bd='1')
        self.tname1.grid(column=0, row=1)
        self.tname2.grid(column=0, row=2)
        for i in range(9):
            self.box0l.append(Label(self, width='7', height='2', relief='solid', bd='1', text=str(i + 1)))
            self.box0l[i].grid(column=i + 1, row=0)
        self.box0l.append(Label(self, width='7', height='2', relief='solid', text='총점', bd='1'))
        self.box0l[9].grid(column=10, row=0)
        self.box1l = []
        for i in range(10):
            self.box1l.append(Label(self, width='7', height='4', relief='solid', bd='1'))
            self.box1l[i].grid(column=i + 1, row=1)
        self.box2l = []
        for i in range(10):
            self.box2l.append(Label(self, width='7', height='4', relief='solid', bd='1'))
            self.box2l[i].grid(column=i + 1, row=2)
        if player == '선공':
            self.tname1.config(text=playerName)
            for i in range(len(uin_score)):
                self.box1l[i].config(text=uin_score[i])
            self.box1l[9].config(text=user_score)
            self.tname2.config(text='COM')
            for i in range(len(cin_score)):
                self.box2l[i].config(text=cin_score[i])
            self.box2l[9].config(text=com_score)

        elif player == '후공':
            self.tname2.config(text=playerName)
            for i in range(len(uin_score)):
                self.box2l[i].config(text=uin_score[i])
            self.box2l[9].config(text=user_score)
            self.tname1.config(text='COM')
            for i in range(len(cin_score)):
                self.box1l[i].config(text=cin_score[i])
            self.box1l[9].config(text=com_score)


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
    d_predict = 100*d_list[0] + 10*d_list[1] + d_list[2]
    hit_margin = defense_num(player_pitch, c_hit)  # 타자의 오차
    defense_margin = abs(d_predict - hit_margin)  # 수비수의 오차
    # print(player_pitch, c_hit, d_list, d_predict, hit_margin, defense_margin)
    if defense_margin <= 100:
        defen = 1
        return defen

    elif defense_margin <= 200:
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
    if defense_margin <= 100:
        defen = 1  # 수비성공
        return defen

    elif defense_margin <= 200:
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
            strikeNum = 0
            ballNum = 0
            gon_ball()
    elif user_decision == 'singlehit':
        if defen == 0:
            getonbase(1)
        else:
            outNum += 1
        strikeNum = 0
        ballNum = 0
    elif user_decision == 'doublehit':
        if defen == 0:
            getonbase(2)
        else:
            outNum += 1
        strikeNum = 0
        ballNum = 0
    elif user_decision == 'triplehit':
        if defen == 0:
            getonbase(3)
        else:
            outNum += 1
        strikeNum = 0
        ballNum = 0
    elif user_decision == 'homerun':
        getonbase(4)
        strikeNum = 0
        ballNum = 0
    if strikeNum == 3:
        outNum += 1
        strikeNum = 0
        ballNum = 0
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
