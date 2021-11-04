from Demo_gui import WorkShop_Registration
from tkinter import *

windows = Tk()
windows.title("Login Page")
windows.geometry("700x400")
windows.configure(bg="#F0FFF0")

def function1(event):
    WorkShop_Registration()

def menthod2(event):
    l3.configure(fg="#0000FF")

def menthod3(event):
    l3.configure(fg="Black")

def fun1():
    exit(0)

f = ("Arial Bold",20)
l = Label(windows,text="Login",font=("Arial Black",25),width=30,bg="#8FBC8F")
l.place(x=10,y=10)

l1 = Label(windows,text="User ID",font=f,bg="#F0FFF0")
l1.place(x=60,y=80)

t1 = Entry(windows,width=20,font=f)
t1.place(x=240,y=80)

l2 = Label(windows,text="Password",font=f,bg="#F0FFF0")
l2.place(x=60,y=150)

t2 = Entry(windows,width=20,font=f,show="*")
t2.place(x=240,y=150)

b1 = Button(windows,text="Sign In",font=f,bg="#90EE90",width=10)
b1.place(x=190,y=225)

b2 = Button(windows,text="Cancel",font=f,bg="#FF6347",width=10,command=fun1)
b2.place(x=400,y=225)

l3 = Label(windows,text=" To Sign Up WorkShop Registration",font=("Arial Bold",15))
l3.place(x=170,y=300)
l3.bind('<Button>',function1)
l3.bind('<Enter>',menthod2)
l3.bind('<Leave>',menthod3)

windows.mainloop()