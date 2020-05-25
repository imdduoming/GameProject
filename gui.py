from tkinter import *

# 원활한 화면 전환을 위해서는 클래스를 이용해야 할듯

# 윈도우 설정
window = Tk()
window.title("야구 게임")
window.geometry("1200x900+300+50")
window.resizable(False, False)

# 페이지 이동 함수
def raise_frame(frame):
    frame.tkraise()

# 페이지 설정
front = Frame(window)

# 게임 시작 페이지
b_start = Button(front, text = '게임 시작', command=lambda:)

# 실행부분
window.mainloop()
