s_num=''
b_num=''
o_num=''

for i in range(7):
    final_decision=input()

    if final_decision=='strike' or final_decision=='foul':
        s_num=s_num+'o'
        if (final_decision=='foul') and (s_num=='ooo'):
            s_num='oo'
    if final_decision=='ball':
        b_num=b_num+'o'
    if s_num=='ooo':
        o_num=o_num+'o'
        s_num=''
        b_num=''

from tkinter import *

window=Tk()
window.title('S,B,O')
window.geometry('50x80')

S=Label(window, text='S ')
S.grid(column=0, row=0)
S_count=Label(window, text=s_num, fg='orange')
S_count.grid(column=1,row=0)

B=Label(window, text='B ')
B.grid(column=0, row=1)
B_count=Label(window, text=b_num, fg='green')
B_count.grid(column=1, row=1)

O=Label(window, text='O ')
O.grid(column=0, row=2)
O_count=Label(window, text=o_num, fg='red')
O_count.grid(column=1, row=2)

window.mainloop()



#out이나 출루를 하게 되면 s_num='',b_num='',o_num=''으로 설정(if문)

