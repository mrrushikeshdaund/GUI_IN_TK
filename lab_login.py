import sqlite3
from tkinter import *
from tkinter import messagebox
import reg_user

windows = Tk()
windows.title("Login Page")
windows.geometry("700x400")
windows.configure(bg="#F0FFF0")

def signIn():
    s1 = t1.get()
    s2 = t2.get()
    con = sqlite3.connect("central_lab.db")
    cur = con.cursor()
    query = f"select * from login_user where user_id ='{s1}' and password ='{s2}'"
    cur.execute(query)
    data = cur.fetchone()
    if data[0]==s1 and data[1]==s2:
        print(data)
        con.close()
        messagebox.showinfo("success", "login successfully..!")

    else:
        messagebox.showerror("Error","invalid User..")

def check(e):
    if (t1.get() == "" or t2.get() == "") and (t1.get() == "" or t2.get() == ""):
        messagebox.showwarning("Waring", "Please Fill the Text Boxes")
    else:
        pass


def menthod2(event):
    l3.configure(fg="#0000FF")

def menthod3(event):
    l3.configure(fg="Black")

def fun1():
    exit(0)

def movereg(e):
    reg_user.adduser()

f = ("Arial Bold",20)
l = Label(windows,text="We!Come To Lab Login",font=("Arial Black",25),width=30,bg="#000000",fg="#FFD700")
l.place(x=10,y=10)

l1 = Label(windows,text="User ID",font=f,bg="#F0FFF0")
l1.place(x=60,y=80)

t1 = Entry(windows,width=20,font=f,bd=5)
t1.place(x=240,y=80)

l2 = Label(windows,text="Password",font=f,bg="#F0FFF0")
l2.place(x=60,y=150)

t2 = Entry(windows,width=20,font=f,show="*",bd=5)
t2.place(x=240,y=150)

b1 = Button(windows,text="Sign In",font=f,bg="#90EE90",width=10,command=signIn,highlightcolor="#4169E1",bd=5)
b1.bind('<Enter>',check)
b1.place(x=150,y=225)

b2 = Button(windows,text="Cancel",font=f,bg="#FF6347",width=10,command=fun1,highlightcolor="#4169E1",bd=5)
b2.place(x=420,y=225)

l3 = Label(windows,text=" To Sign Up Registration",font=("Arial Bold",15))
l3.place(x=240,y=330)
l3.bind('<Button>',movereg)
l3.bind('<Enter>',menthod2)
l3.bind('<Leave>',menthod3)

l4 = Label(windows,text="Forget Password.",font=("Arial Bold",15))
l4.place(x=270,y=300)
windows.mainloop()