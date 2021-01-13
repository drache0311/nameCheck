from tkinter import *
import os
import random

try:
    os.chdir(sys._MEIPASS)
    print(sys._MEIPASS)
except:
    os.chdir(os.getcwd())

# cehckName.py 위치한 절대 경로
path_dir = os.path.dirname(os.path.realpath(__file__))
file_list = os.listdir(path_dir)
real_file_list = [x for x in file_list if(x.endswith(".PNG") or (x.endswith(".png")==True))]    # .png인 파일들 리스트에 저장
random.shuffle(real_file_list)  # 사원들 리스트 랜덤 섞기

xn=0    # 리스트 인자 카운트 변수
root=Tk() # tkinter 사용
root.title("이름 맞추기")
root.geometry("700x550")
root.resizable(0, 0)
image=PhotoImage(file=real_file_list[xn])   # 처음은 리스트 맨 처음 이미지 저장

def showimg():
    global xn
    global image
    textInput = txt.get(1.0, END+"-1c") # 텍스트에 입력한 값 불러오기

    # 사진과 이름이 일치하는지 확인
    if(textInput==real_file_list[xn].strip('.png')):    # 리스트에서 .png를 제외한 이름+직책 값과 텍스트 입력값을 비교
        xn+=1
        if(xn>=len(real_file_list)):
            xn=0
        image=PhotoImage(file=real_file_list[xn])
        label_2 = Label(root, image=image)
        label_2.place(x=0,y=150)

txt = Text(root, height=1)

btn = Button(root,text="next",command=showimg,width=7,height=1)
label_1 = Label(root,text="이름 맞추기 !",font="NanumGothic 20")
label_2 = Label(root, image=image)

txt.place(x=200,y=100)
label_1.place(x=200,y=10)
label_2.place(x=0,y=150)
btn.place(x=300,y=50)

root.mainloop()