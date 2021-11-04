from tkinter import *
from tkinter import messagebox
def signuppage():
    win = Tk()
    win.title("Sign Up Page ")
    win.geometry("600x600")
    win.configure(bg="#F5FFFA")

    def savedata():
        s1 = t1.get()
        s3 = t3.get()
        s4 = t4.get()
        s5 = t5.get()

        file1 = open("user_data.txt","a")
        file1.write(s1+","+s3+","+s4+","+s5+"\n")
        file1.close()

        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
        t4.delete(0,END)
        t5.delete(0,END)
        messagebox.showinfo("User Create","User Create Successfully..!")

        t1.focus()

    def passwordcheck(event):
        p1 = t2.get()
        p2 = t3.get()
        if p1 == p2:
            pass
        else:
            t2.delete(0,END)
            t3.delete(0,END)
            messagebox.showerror("Warnings","Password is  not same please re-enter Password")
            t2.focus()

    def reset():
        a = messagebox.askyesno("Reset","if you want to clear ...?")
        if int(a)==1:
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)
            t5.delete(0, END)
        if int(a)==0:
            pass


    f = ("Arial Bold", 20)
    l1 = Label(win, text="Enter User ID ", font=f, bg="#F5FFFA")
    l1.place(x=20, y=20)

    t1 = Entry(win, width=18, font=f, bd=3)
    t1.place(x=280, y=20)

    l2 = Label(win, text="Enter Password ", font=f, bg="#F5FFFA")
    l2.place(x=20, y=100)

    t2 = Entry(win, width=18, font=f, bd=3,show='*')
    t2.place(x=280, y=100)

    l3 = Label(win, text="Confirm Password", font=f, bg="#F5FFFA")
    l3.place(x=20, y=180)

    t3 = Entry(win, width=18, font=f, bd=3,show='*')
    t3.bind('<Leave>', passwordcheck)
    t3.place(x=280, y=180)

    l4 = Label(win, text="Email address ", font=f, bg="#F5FFFA")
    l4.place(x=20, y=260)

    t4 = Entry(win, width=18, font=f, bd=3)
    t4.place(x=280, y=260)

    l5 = Label(win, text="Mobile Number", font=f, bg="#F5FFFA")
    l5.place(x=20, y=340)

    t5 = Entry(win, width=18, font=f, bd=3)
    t5.place(x=280, y=340)

    b1 = Button(win, text="Create User", width=10, bg="#1E90FF", bd=5, font=f,command=savedata)
    b1.bind('<Enter>', passwordcheck)
    b1.place(x=120, y=420)

    b2 = Button(win, text="Reset Fields", width=10, bg="#1E90FF", bd=5, font=f,command=reset)
    b2.place(x=360, y=420)

    win.mainloop()