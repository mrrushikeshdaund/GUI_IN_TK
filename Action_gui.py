
from tkinter import *
base = Tk()
base.geometry("500x600")
base.title(" Action Gui ")
f = ("Arial Black",20)

b1 = Button(base,width=10,height=20)
b1.pack()
def fun1():
    b1.configure(bg="yellow",text="b2 is press")

def fun2():
    b1.configure(bg="red", text="b3 is press")


b2 = Button(base,text="set yellow", font=f , command=fun1)
b2.pack()

b3 = Button(base,text="set red ",font=f,command=fun2)
b3.pack()

S1=StringVar()

r1 = Radiobutton(base,text="male",variable=S1,value="10")
r1.pack()

r2 =Radiobutton(base,text="female",variable=S1,value="20")
r2.pack()

base.mainloop()
