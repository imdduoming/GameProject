from tkinter import *
import random as rd
import time


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
        master.switch_frame(SBO)


class BaseFrame(Frame):
    def __init__(self):
        global base
        Frame.__init__(self, width='200', height='200', relief='solid', bd='1')
        self.c_base = Canvas(self, width='200', height='200')
        self.c_base.pack()
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


class GameTest(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)


if __name__ == '__main__':  # 이 py 파일이 실행되었을 때만 실행
    base = [0, 0, 0, 0, 0]  # 타석 1루 2루 3루 홈
    inning_score = 0  # 회당 플레이어 점수
    playerOp = ['선공', '후공']
    player = None
    playerName = ''
    gameNum = 0
    game = GameMain()
    game.mainloop()
