
from tkinter import *

base = Tk()
base.title("SIGN UP PAGE ")
base.geometry("400x600")

l1 = Label(base,text="Enter Name :- ")
l1.place(x=10,y=20)

t1  = Entry(base,width=20)
t1.place(x=150,y=20)

l2 = Label(base,text="Enter Email :- ")
l2.place(x=10,y=80)

t2 = Entry(base,width=20)
t2.place(x=150,y=80)

l3 = Label(base,text="Enter Phone No :- ")
l3.place(x=10,y=140)

t3 = Entry(base,width=20)
t3.place(x=150,y=140)

l4 = Label(base,text="Enter City Name :- ")
l4.place(x=10,y=200)

t4 = Entry(base,width=20)
t4.place(x=150,y=200)

l5 = Label(base, text="Select Sex :- ")
l5.place(x=10, y=230)

r1 = Radiobutton(base, text="Male")
r1.place(x=80, y=230)

r2 = Radiobutton(base, text="Female")
r2.deselect()
r2.place(x=150, y=230)

b1 = Button(base, text="Sign Up")
b1.place(x=130,y=260)




base.mainloop()