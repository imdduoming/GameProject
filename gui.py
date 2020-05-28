from tkinter import *


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
        Label(self, text='전체 게임 완성시 구성 예정').pack()
        Button(self, text='돌아가기', command=lambda: master.switch_frame(StartPage)).pack()


if __name__ == '__main__':
    game = GameMain()
    game.mainloop()
