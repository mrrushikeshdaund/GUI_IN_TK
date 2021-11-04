
from tkinter import *

base = Tk()
base.title(" Calculator ")
base.geometry("500x600")
base.configure(bg="#E0FFFF")


l1 = Label(base,text="Enter First Number :- ")
l1.place(x=100,y=30)

t1 = Entry(base,width=20)
t1.place(x=270,y=30)

l2 = Label(base,text="Enter Second Number :- ")
l2.place(x=100,y=100)

t2 = Entry(base,width=20)
t2.place(x=270,y=100)

def add():
    a = int(t1.get())
    b = int(t2.get())
    t3.delete(0,END)
    c = a + b
    t3.insert(0,str(c))

def sub():
    a = int(t1.get())
    b = int(t2.get())
    t3.delete(0,END)
    c = a - b
    t3.insert(0,str(c))

def mul():
    a = int(t1.get())
    b = int(t2.get())
    t3.delete(0,END)
    c = a * b
    t3.insert(0,str(c))

def div():
    a = int(t1.get())
    b = int(t2.get())
    t3.delete(0,END)
    c = a / b
    t3.insert(0,str(c))

b1 = Button(base,text="Addition",command=add)
b1.place(x=60,y=170)

b2 = Button(base,text="Subtraction",command=add)
b2.place(x=150,y=170)

b3 = Button(base,text="Divide",command=div)
b3.place(x=260,y=170)

b4 = Button(base,text="Multiplication",command=mul)
b4.place(x=340,y=170)

l3 = Label(base,text="Result is ")
l3.place(x=140,y=220)

t3 = Entry(base,width=30)
t3.place(x=220,y=220)

base.mainloop()
