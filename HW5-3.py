import turtle
import math
import random
from tkinter.simpledialog import *

swidth, sheight = 500, 500
inStr = ""
radius = 0
tX, tY = [0] * 2

if __name__ == "__main__" :
    
    #프로그램 실행 창 설정
    turtle.title('거북이가 나선 모양의 글자쓰기')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.shape('turtle')
    turtle.penup()
    radius = 200

#2019038030 김진영

    inStr = askstring("문자열 입력", "거북이 쓸 문자열 입력")

    #글자 수만큼 반복
    #거북이 x좌표는 거리 * COS(3.14 * 각도/180)
    #거리 = radius, 각도는 두 바퀴 돈다고 했을 때 360*2 / len(inStr)
    for i in range(0, len(inStr)) :
        tX = radius * math.cos(3.14 * ((360*2)/len(inStr)*i) / 180)
        tY = radius * math.sin(3.14 * ((360*2)/len(inStr)*i) / 180)
        turtle.goto(tX,tY)
        r = random.random(); g = random.random(); b = random.random()
        turtle.pencolor((r,g,b))
        turtle.write(inStr[i], font=('맑은 고딕', 20, 'bold'))
        radius -= radius/len(inStr)
        
    turtle.done

    
    

        
        
        
        
        
