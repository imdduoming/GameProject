from tkinter import *

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
c_base = Canvas(f_base)
# c_base.create_polygon(x1, y1, x2, y2, … , xn, yn)

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

team_score1 = Label(f_score, text="0점")
team_score2 = Label(f_score, text="0점")
team_score1.grid(column='1', row='0')
team_score2.grid(column='1', row='1')

# SBO

# 버튼부분

# 수비측 숫자합 제시부분

# 기타

window.mainloop()
