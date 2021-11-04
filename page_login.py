from tkinter import *
from tkinter import messagebox
import new_signup
import reset_password_form

base = Tk()
base.title(" Login page")
base.geometry("500x500")
base.configure(bg="#F5FFFA")

f = ("Arial Bold",20)

def signin():
    file1 = open("user_data.txt","r")
    data = file1.readlines()
    file1.close()
    for row in data:
        s1 = t1.get()
        s2 = t2.get()
        if list(row[0]) == s1 and list(row[1]) == s2:
            l5.place(x=100, y=320)
            break
        else:
            l6.place(x=100, y=320)




def reset():
    a = messagebox.askyesno("If you want to Clear textbox...?","If you want to clear text")
    if int(a)==1:
        t1.delete(0, END)
        t2.delete(0, END)
    if int(a)==0:
        pass

def enter(event):
    l4.configure(fg="#1E90FF")

def leave(event):
    l4.configure(fg="Black")

def enter1(event):
    l3.configure(fg="#1E90FF")

def leave1(event):
    l3.configure(fg="Black")

def signup(event):
    new_signup.signuppage()

def resetpasswordfunction(event):
    reset_password_form.changepassword()

l1 = Label(base,text="Enter User ID ",bg="#F5FFFA",font=f,bd=4)
l1.place(x=60,y=30)

t1 = Entry(base,font=f,width=23,bd=3)
t1.place(x=100,y=70)

l2 = Label(base,text="Enter User Password ",bg="#F5FFFA",font=f,bd=4)
l2.place(x=60,y=130)

t2 = Entry(base,font=f,width=23,show='*',bd=3)
t2.place(x=100,y=170)

b1 = Button(base,text="Sign In",width=10,bg="#1E90FF",font=f,bd=5,command=signin)
b1.place(x=50,y=250)

b2 = Button(base,text="Reset",width=10,bg="#1E90FF",font=f,bd=5,command=reset)
b2.place(x=280,y=250)

l3 = Label(base,text="New User..? Sign Up Here.",bg="#F5FFFA",bd=3,font=("Arial Bold",17))
l3.bind('<Enter>',enter1)
l3.bind('<Leave>',leave1)
l3.bind('<Button>',signup)
l3.place(x=100,y=370)

l4 = Label(base,text="Forget Password",bg="#F5FFFA",bd=3,font=("Arial Bold",17))
l4.bind('<Enter>',enter)
l4.bind('<Leave>',leave)
l4.bind('<Button>',resetpasswordfunction)
l4.place(x=160,y=410)

l5 = Label(base,text="Sign In Successfully..",bg="#F5FFFA",bd=3,font=("Arial Bold",15))
l6 = Label(base,text="Sign In Failed..",bg="#F5FFFA",bd=3,font=("Arial Bold",15),fg="#FF0000")

base.mainloop()