from tkinter import *

base = Tk()
base.title("registration Form ")
base.geometry("500x700")
base.configure(bg="#FAFAD2")

f = ("Arial Bold",10)

l = Label(base,text="Registration Form ",font=("Arial Black",15))
l.place(x=150,y=20)

l1 = Label(base,text="Enter Name :- ",font=f)
l1.place(x=20,y=80)

t1 = Entry(base,font=f)
t1.place(x=190,y=80)

l2 = Label(base,text="Enter Email :- ",font=f)
l2.place(x=20,y=120)

t2 = Entry(base,font=f)
t2.place(x=190,y=120)

l3 =Label(base,text="Enter Mobile No :- ",font=f)
l3.place(x=20,y=160)

t3 = Entry(base,font=f)
t3.place(x=190,y=160)

l4 =Label(base,text="Enter City :- ",font=f)
l4.place(x=20,y=200)

t4 = Entry(base,font=f)
t4.place(x=190,y=200)

l5 = Label(base,text="Select Your Gender :- ",font=f)
l5.place(x=20,y=240)

s = IntVar()

r1 = Radiobutton(base,text="Male",font=f,variable=s,value=1)
r1.place(x=40,y=280)

r2 = Radiobutton(base,text="female",font=f,variable=s,value=2)
r2.place(x=120,y=280)

r3 = Radiobutton(base,text="Other",font=f,variable=s,value=3)
r3.place(x=210,y=280)

r1.select()


l6 = Label(base,text="Choose Languages",font=f)
l6.place(x=20,y=320)

ch = IntVar()
c1 = Checkbutton(base,text="C",font=f,variable=ch,offvalue=1,onvalue=2)
c1.place(x=30,y=360)

ch1 = IntVar()
c2 = Checkbutton(base,text="C++",font=f,variable=ch1,offvalue=1,onvalue=2)
c2.place(x=100,y=360)

ch2 = IntVar()
c3 = Checkbutton(base,text="JavaCore",font=f,variable=ch2,offvalue=1,onvalue=2)
c3.place(x=160,y=360)

ch3 = IntVar()
c4 = Checkbutton(base,text="Advance Java",font=f,variable=ch3,offvalue=1,onvalue=2)
c4.place(x=220,y=360)

ch4 = IntVar()
c5 = Checkbutton(base,text="Python",font=f,variable=ch4,offvalue=1,onvalue=2)
c5.place(x=350,y=360)

def save_details():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5 = int(s.get())
    if s5==1:
        s6 = str("Male")
    elif s5==2:
        s6 = str("Female")
    elif s5==3:
        s6 = str("Other")

    file1 = open("save_details.txt","a")
    file1.write(s1+","+s2+","+s3+","+s4+","+s6+","+"\n")
    file1.close()

    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0, END)
    t4.delete(0, END)
    t1.focus()

def cancel():
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t1.focus()





b1 = Button(base,text="Save",font=f,width=15,bg="#98FB98",command=save_details)
b1.place(x=50,y=430)

b2 =Button(base,text="Cancel",font=f,width=15,bg="#FF6347",command=cancel)
b2.place(x=250,y=430)

base.mainloop()
