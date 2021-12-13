import tkinter as tk
from tkinter import messagebox
from tkinter.constants import LEFT
from typing import Counter
# 필요한 라이브러리를 불러옵니다.
from typing import Counter
import RPi.GPIO as GPIO 
import time

# 사용할 GPIO핀의 번호를 선정합니다.
count=0
button_pin_b = 17
button_pin_y = 27
button_pin_r = 4




 # 불필요한 warning 제거
GPIO.setwarnings(False) 
# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM) 
# 버튼 핀의 INPUT설정 , PULL DOWN 설정 
GPIO.setup(button_pin_b, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin_y, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin_r, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LED 핀의 OUT설정

#GPIO 4번 핀을 출력으로 설정 
GPIO.setup(21, GPIO.OUT)
# PWM 인스턴스 p를 만들고  GPIO 4번을 PWM 핀으로 설정, 주파수  = 100Hz
p = GPIO.PWM(21, 100)  
# 4옥타브 도~시 , 5옥타브 도의 주파수 
Frq = [523,659,783,1046]
speed = 0.2 # 음과 음 사이 연주시간 설정 (0.5초)



led3_pin=13   #red 
led8_pin=19
led9_pin=26


def order_1():
    GPIO.setup(led3_pin, GPIO.OUT)
    GPIO.setup(led8_pin, GPIO.OUT)
    GPIO.setup(led9_pin, GPIO.OUT)
       
    print("red led ON!")
    GPIO.output(led3_pin,1)
    GPIO.output(led8_pin,0) 
    GPIO.output(led9_pin,0) 
    time.sleep(0.2)
    GPIO.output(led3_pin,0)
    GPIO.output(led8_pin,1) 
    GPIO.output(led9_pin,0) 
    time.sleep(0.2)
    GPIO.output(led3_pin,0)
    GPIO.output(led8_pin,0) 
    GPIO.output(led9_pin,1) 
    time.sleep(0.2)
    GPIO.output(led3_pin,1)
    GPIO.output(led8_pin,1) 
    GPIO.output(led9_pin,1)

    
    for fr in Frq:
        p.start(1) 
        time.sleep(speed)       #speed 초만큼 딜레이 (0.5s)
        GPIO.output(led3_pin,1) 
        p.ChangeFrequency(fr)    #주파수를 fr로 변경
        
 
        
        time.sleep(speed)       #speed 초만큼 딜레이 (0.5s)
        GPIO.output(led3_pin,0)
        GPIO.output(led8_pin,1) 
        p.ChangeFrequency(fr)    #주파수를 fr로 변경
        
    
          
        time.sleep(speed)       #speed 초만큼 딜레이 (0.5s)
        GPIO.output(led3_pin,0)
        GPIO.output(led8_pin,0) 
        GPIO.output(led9_pin,1) 
        p.ChangeFrequency(fr)    #주파수를 fr로 변경
        
        GPIO.output(led9_pin,0) 
        time.sleep(speed)       #speed 초만큼 딜레이 (0.5s)
        GPIO.output(led3_pin,1) 
        GPIO.output(led8_pin,1) 
        GPIO.output(led9_pin,1) 
        p.ChangeFrequency(fr)    #주파수를 fr로 변경
    p.stop(fr)
        
        
        

led2_pin=10   #yellow  
led6_pin=9
led7_pin=11

def order_2():    
    GPIO.setup(led2_pin, GPIO.OUT)
    GPIO.setup(led6_pin, GPIO.OUT)
    GPIO.setup(led7_pin, GPIO.OUT)
       
    print("yellow led ON!")
    GPIO.output(led2_pin,1)
    GPIO.output(led6_pin,0) 
    GPIO.output(led7_pin,0) 
    time.sleep(0.2)
    GPIO.output(led2_pin,0)
    GPIO.output(led6_pin,1) 
    GPIO.output(led7_pin,0) 
    time.sleep(0.2)
    GPIO.output(led2_pin,0)
    GPIO.output(led6_pin,0) 
    GPIO.output(led7_pin,1) 
    time.sleep(0.2)
    GPIO.output(led2_pin,1)
    GPIO.output(led6_pin,1) 
    GPIO.output(led7_pin,1)


    for fr in Frq:
        p.start(1) 
        time.sleep(speed)       #speed 초만큼 딜레이 (0.5s)
        GPIO.output(led2_pin,1) 
        p.ChangeFrequency(fr)    #주파수를 fr로 변경
 
        
        time.sleep(speed)       #speed 초만큼 딜레이 (0.5s)
        GPIO.output(led2_pin,0)
        GPIO.output(led6_pin,1) 
        p.ChangeFrequency(fr)    #주파수를 fr로 변경

    
          
        time.sleep(speed)       #speed 초만큼 딜레이 (0.5s)
        GPIO.output(led2_pin,0)
        GPIO.output(led6_pin,0) 
        GPIO.output(led7_pin,1) 
        p.ChangeFrequency(fr)    #주파수를 fr로 변경

        GPIO.output(led7_pin,0) 
        time.sleep(speed)       #speed 초만큼 딜레이 (0.5s)
        GPIO.output(led2_pin,1) 
        GPIO.output(led6_pin,1) 
        GPIO.output(led7_pin,1) 
        p.ChangeFrequency(fr)    #주파수를 fr로 변경
    p.stop(fr)


led1_pin=3  #blue led
led4_pin=24
led5_pin=23


def order_3():
    
    GPIO.setup(led1_pin, GPIO.OUT)
    GPIO.setup(led4_pin, GPIO.OUT)
    GPIO.setup(led5_pin, GPIO.OUT)

    print("blue led on")
    GPIO.output(led1_pin,1)
    GPIO.output(led4_pin,0) 
    GPIO.output(led5_pin,0) 
    time.sleep(0.2)
    GPIO.output(led1_pin,0)
    GPIO.output(led4_pin,1) 
    GPIO.output(led5_pin,0) 
    time.sleep(0.2)
    GPIO.output(led1_pin,0)
    GPIO.output(led4_pin,0) 
    GPIO.output(led5_pin,1) 
    time.sleep(0.2)
    GPIO.output(led1_pin,1)
    GPIO.output(led4_pin,1) 
    GPIO.output(led5_pin,1)

    for fr in Frq:
        p.start(1) 
        time.sleep(speed)       #speed 초만큼 딜레이 (0.5s)
        GPIO.output(led1_pin,1) 
        p.ChangeFrequency(fr)    #주파수를 fr로 변경
        
 
        
        time.sleep(speed)       #speed 초만큼 딜레이 (0.5s)
        GPIO.output(led1_pin,0)
        GPIO.output(led4_pin,1) 
        p.ChangeFrequency(fr)    #주파수를 fr로 변경
        
    
          
        time.sleep(speed)       #speed 초만큼 딜레이 (0.5s)
        GPIO.output(led1_pin,0)
        GPIO.output(led4_pin,0) 
        GPIO.output(led5_pin,1) 
        p.ChangeFrequency(fr)    #주파수를 fr로 변경
        
        GPIO.output(led5_pin,0) 
        time.sleep(speed)       #speed 초만큼 딜레이 (0.5s)
        GPIO.output(led1_pin,1) 
        GPIO.output(led4_pin,1) 
        GPIO.output(led5_pin,1) 
        p.ChangeFrequency(fr)    #주파수를 fr로 변경
    p.stop(fr)
    
def blue_button(channel):    
    
    GPIO.output(led1_pin,0) # LED OFF
    GPIO.output(led5_pin,0) 
    GPIO.output(led4_pin,0) # LED OFF
    
    print("blue LED OFF!")

def yellow_button(channel):    
    
    GPIO.output(led2_pin,0) # LED OFF
    GPIO.output(led6_pin,0) 
    GPIO.output(led7_pin,0) # LED OFF
    
    print("yellow LED OFF!")

def red_button(channel):    
    
    GPIO.output(led3_pin,0) # LED OFF
    GPIO.output(led8_pin,0) 
    GPIO.output(led9_pin,0) # LED OFF
    
    print("red LED OFF!")    
    
    

GPIO.add_event_detect(button_pin_b,GPIO.RISING,callback=blue_button, bouncetime=300)      
GPIO.add_event_detect(button_pin_y,GPIO.RISING,callback=yellow_button, bouncetime=300)      
GPIO.add_event_detect(button_pin_r,GPIO.RISING,callback=red_button, bouncetime=300)      
   


window = tk.Tk()




def add():
    global c1Var, c2Var, c3Var, c4Var
    sum = 0
    order = ""

    if c1Var.get() == 1:
        sum += 2000
        order += "아메리카노\n"
    if c2Var.get() == 1:
        sum += 4000
        order += "카페라떼\n"
    if c3Var.get() == 1:
        sum += 4000
        order += "카프치노\n"
    if c4Var.get() == 1:
        sum += 1000
        order += "에스프레소\n"
    label1['text'] = "금액: " + str(sum) + "원"
    label2['text'] = "선택: " + order

complete=False


def saler_window():
    global complete
    if complete:

        newWindow = tk.Toplevel(window)

        order1 = tk.Button(newWindow,text="order1 bell",command=order_1)   
        order2 = tk.Button(newWindow,text="order2 bell",command=order_2)
        order3 = tk.Button(newWindow,text="order3 bell",command=order_3)
        

        order1.grid(row=3, column=0)
        
        order2.grid(row=3, column=1)
        
        order3.grid(row=3, column=2) 

    
         

count=1

def new_window():

    print("ok")
    button1 = tk.Button(saler_window, text="1")
    button1.grid(row=3, column=0)
    button2 = tk.Button(saler_window, text="2")
    button2.grid(row=3, column=1)
    button3 = tk.Button(saler_window, text="3")
    button3.grid(row=3, column=2) 

def consumer_window():
    global complete
    global count

    label2.config(text="대기번호:"+str(count)+"번 \n 음료준비중입니다. 잠시만기다려주세요")
    count+=1
    if count>3:
        count=1

    button1.config(text="주문완료")
    complete=True
    saler_window()
    
    


      




window.title("CAFE")
window.geometry("300x400")
window.config(bg="white")
# center(window)
frame1 = tk.Frame(window)

tk.Label(window, text="CAFE")
label0 = tk.Label(window, text="CAFE", width=100, height=2, font="Arial 15")
label0.pack()
c1Var = tk.IntVar()
c2Var = tk.IntVar()
c3Var = tk.IntVar()
c4Var = tk.IntVar()
c1 = tk.Checkbutton(window, text="아메리카노         - 2000원",
                    variable=c1Var, command=add)
c2 = tk.Checkbutton(window, text="카페라떼           - 4000원",
                    variable=c2Var, command=add)
c3 = tk.Checkbutton(window, text="카프치노           - 4000원",
                    variable=c3Var, command=add)
c4 = tk.Checkbutton(window, text="에스프레소         - 1000원",
                    variable=c4Var, command=add)
                   




c1.pack()
c2.pack()
c3.pack()
c4.pack()

frame1.pack()
label1 = tk.Label(window, text="금액: 0원", width=100, height=2, pady="20")
label1.pack()
label2 = tk.Label(window, text="선택음료", width=100)
label2.pack()
button1 = tk.Button(window, text = '주문하기', bg='light pink', command=consumer_window)       #눌러지면 Ln11
button1.pack()



window.mainloop()