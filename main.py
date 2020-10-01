import datetime
import time
from tkinter import *
from playsound import playsound
from win10toast import ToastNotifier

def alarm(set_alarm):
    toast = ToastNotifier()
    while True:
        time.sleep(1)    
        date = datetime.datetime.now()
        now = date.strftime("%H:%M:%S")
        print(now)
        if now == set_alarm:
            print("alram clock")
            toast.show_toast("Alarm clock",duration=1)
            playsound("alarm.mp3")

def getvalue():
    set_alarm = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm)
root = Tk()
root.geometry("200x150")
info = Label(text="(24)Hour Min Sec").place(x = 50)
set_time =  Label(root,text = "Set Time", relief = "solid" , font=("Cambria" , 10, "bold")).place(x = 0, y=30)
#ebtry values
hour = StringVar()
min = StringVar()
sec = StringVar()
#entry widget
hour_E = Entry(root, textvariable = hour , bg="grey", width=4).place(x=60, y=30)
min_E = Entry(root, textvariable = min , bg="grey", width=4).place(x=90, y=30)
sec_E = Entry(root, textvariable = sec , bg="grey", width=4).place(x=120, y=30)
 
submit = Button(root, text="SET Alarm", width=10 , command=getvalue).place(x=50,y=70)

root.mainloop()