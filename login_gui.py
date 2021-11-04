
from tkinter import *

base = Tk()
base.title("Login page")
base.geometry("300x300")
base.configure(bg="#ADFF2F")
f = ("Arial Bold",8)
l1 = Label(base,text="Enter username  :- ",font=f,fg="#B8860B")
l1.place(x=10,y=10)

t1 = Entry(base,width=15)
t1.place(x=140,y=10)

l2 = Label(base,text="Enter password :- ",font=f,bg="#B8860B")
l2.place(x=10,y=50)

t2 = Entry(base,width=15,show='*')
t2.place(x=140,y=50)

c1 = Checkbutton(base,text="Keep Sign in ",font=f)
c1.place(x=100,y=70)

b1 =Button(base,text=" Login ",font=f)
b1.place(x=50,y=100)




b2 = Button(base,text="Cancel",font=f)
b2.place(x=150,y=100)

base.mainloop()