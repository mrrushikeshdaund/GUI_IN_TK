from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

def adduser():
    win2 = Tk()
    win2.title("Add User Page")
    win2.geometry("1055x700")
    win2.configure(bg="#F0FFF0")

    def passwordcheck(e):
        s1 = t2.get()
        s2 = t3.get()

        if s1==s2:
            pass
        else:
            t2.delete(0,END)
            t3.delete(0,END)
            t2.focus()

    def add_data():
        s1 = t1.get()
        s2 = t2.get()
        s3 = t4.get()
        con = sqlite3.connect("central_lab.db")
        query = f"insert into login_user values('{s1}','{s2}',{s3})"
        con.execute(query)
        con.commit()
        con.close()
        messagebox.showinfo("Success","Add User Successfully...")


    def reset():
        a = messagebox.askyesno("Reset","Reset All...?")

        if a==1:
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)
            t1.focus()
        elif a==2:
            pass


    f = ("Arial Bold",30)

    l = Label(win2,width=36,text="Register User",font=("Arial Bold",35),bg="#000000",fg="#FFD700")
    l.place(x=5,y=10)

    l1 = Label(win2,text="Enter User ID  ",font=f,bg="#F0FFF0")
    l1.place(x=100,y=120)

    t1 = Entry(win2,font=f,bd=5)
    t1.place(x=500,y=120)

    l2 = Label(win2, text="Enter Password  ", font=f, bg="#F0FFF0")
    l2.place(x=100, y=220)

    t2 = Entry(win2, font=f, bd=5,show='*')
    t2.place(x=500, y=220)

    l3 = Label(win2, text="Re-Type Password  ", font=f, bg="#F0FFF0")
    l3.place(x=100, y=320)

    t3 = Entry(win2, font=f, bd=5,show='*')
    t3.place(x=500, y=320)

    l4 = Label(win2, text="Enter Mob No  ", font=f, bg="#F0FFF0")
    l4.place(x=100, y=420)

    t4 = Entry(win2, font=f, bd=5)
    t4.place(x=500, y=420)

    b1 = Button(win2,text="Submit",font=f,bg="#4169E1",width=10,bd=5,fg="#FFE2B7",command=add_data)
    b1.bind('<Enter>',passwordcheck)
    b1.place(x=250,y=550)

    b2 = Button(win2, text="Reset", font=f, bg="#4169E1", width=10, bd=5, fg="#FFE2B7",command=reset)
    b2.place(x=600, y=550)

    win2.mainloop()

