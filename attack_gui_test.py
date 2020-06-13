from tkinter import *

# 절차지향으로 만든 기본적인 레이아웃
# 가급적 place를 사용 (배경에 맞춰야 할 수도 있음)

window = Tk()
window.title("야구 게임")
window.geometry("1200x900+300+50")
window.resizable(False, False)
window.configure(bg='#A9F5A9')

# 이미지
# image=PhotoImage(file="a.png")

# 출루 상황 표시
f_base = Frame(window, width='200', height='200', relief='solid', bd='1')
f_base.place(x=40, y=40)
c_base = Canvas(f_base, width='200', height='200')
c_base.pack()
c_base.create_polygon(145, 73, 109, 109, 145, 145, 181, 109, fill='white', outline='black')  # 1루
c_base.create_polygon(100, 29, 64, 65, 100, 101, 136, 65, fill='white', outline='black')  # 2루
c_base.create_polygon(56, 73, 20, 109, 56, 145, 92, 109, fill='white', outline='black')  # 3루

# 점수판
f_score = Frame(window, width='200', height='150', relief='solid', bd='1')
f_score.place(x=950, y=40)
f_score.grid_propagate(0)
f_score.columnconfigure(0, weight=1)
f_score.rowconfigure(0, weight=1)
f_score.columnconfigure(1, weight=1)
f_score.rowconfigure(1, weight=1)
team_name1 = Label(f_score, text="A TEAM")
team_name2 = Label(f_score, text="B TEAM")
team_name1.grid(column='0', row='0')
team_name2.grid(column='0', row='1')

team_score1 = Label(f_score, text="0")
team_score2 = Label(f_score, text="0")
team_score1.grid(column='1', row='0')
team_score2.grid(column='1', row='1')

# SBO
f_sbo = Frame(window, width='150', height='100', relief='solid', bd='1')
f_sbo.grid_propagate(0)
f_sbo.place(x=1000, y=700)
for i in range(3):
    f_sbo.rowconfigure(i, weight=1)
for i in range(3):
    f_sbo.columnconfigure(i, weight=1)
S = Label(f_sbo, text='S ')
S.grid(column=0, row=0, padx='2')
S_count = Label(f_sbo, text='●●　', fg='orange')
S_count.grid(column=1, row=0)

B = Label(f_sbo, text='B ', padx='2')
B.grid(column=0, row=1)
B_count = Label(f_sbo, text='●●●', fg='green')
B_count.grid(column=1, row=1)

O = Label(f_sbo, text='O ', padx='2')
O.grid(column=0, row=2)
O_count = Label(f_sbo, text='●　　', fg='red')
O_count.grid(column=1, row=2)


def number_select():
    button0.config(state='disabled')


# 버튼부분
self = Frame(window, width='400', height='200', relief='solid', bd='1')
self.place(x=400, y=600)
self.grid_propagate(0)
self.rowconfigure(0, weight=1)
self.rowconfigure(1, weight=1)
for i in range(5):
    self.columnconfigure(i, weight=1)
button0 = Button(self, width='9', height='4', command=lambda: number_select())
button1 = Button(self, width='9', height='4')
button2 = Button(self, width='9', height='4')
button3 = Button(self, width='9', height='4')
button4 = Button(self, width='9', height='4')
button5 = Button(self, width='9', height='4')
button6 = Button(self, width='9', height='4')
button7 = Button(self, width='9', height='4')
button8 = Button(self, width='9', height='4')
button9 = Button(self, width='9', height='4')

button0.grid(column='0', row='0')
button1.grid(column='1', row='0')
button2.grid(column='2', row='0')
button3.grid(column='3', row='0')
button4.grid(column='4', row='0')
button5.grid(column='0', row='1')
button6.grid(column='1', row='1')
button7.grid(column='2', row='1')
button8.grid(column='3', row='1')
button9.grid(column='4', row='1')

# 수비측 숫자합 제시부분

# 기타

window.mainloop()
print(f_base)
