from tkinter import *
from tkinter import ttk,messagebox,PhotoImage
from datetime import *
import sqlite3

def main_window():
    main_win = Tk()
    main_win.wm_attributes('-fullscreen','true')
    main_win.configure(bg="#F0FFF0")

    def add_student():
        clear()
        # Add Student
        fb = ("Bahnschrift Light", 21)
        lb1 = Label(main_win, text="Enter Student Roll No :-", bg="#F0FFF0", font=fb)
        t1 = Entry(main_win, width=25, font=fb, bd=5)

        lb2 = Label(main_win, text="Enter Student Name :-", bg="#F0FFF0", font=fb)
        t2 = Entry(main_win, width=25, font=fb, bd=5)

        lb3 = Label(main_win, text="Enter Student Email :-", bg="#F0FFF0", font=fb)
        t3 = Entry(main_win, width=25, font=fb, bd=5)

        lb4 = Label(main_win, text="Enter Student Mob No :-", bg="#F0FFF0", font=fb)
        t4 = Entry(main_win, width=25, font=fb, bd=5)

        lb5 = Label(main_win, text="Select Student Branch :-", bg="#F0FFF0", font=fb)
        list_branch = ['Computer Science & Engg', 'Mechanical Engg', 'Civil Engg']
        c1 = ttk.Combobox(main_win, value=list_branch, font=fb, state="readonly", width=25)
        c1.current(0)

        lb6 = Label(main_win, text="Select Student Year :-", bg="#F0FFF0", font=fb)
        list_year = ['First Year', 'Second Year', 'Third Year']
        c2 = ttk.Combobox(main_win, value=list_year, font=fb, state="readonly", width=25)
        c2.current(0)

        lb7 = Label(main_win, text="Select Student Class :-", bg="#F0FFF0", font=fb)
        list_class = ['A', 'B']
        c3 = ttk.Combobox(main_win, value=list_class, font=fb, state="readonly", width=25)
        c3.current(0)

        def save():
            con = sqlite3.connect("central_lab.db")
            s1 = t1.get()
            s2 = t2.get()
            s3 = t3.get()
            s4 = int(t4.get())
            s5 = str(c1.get())
            s6 = str(c2.get())
            s7 = str(c3.get())

            query = f"insert into student values('{s1}','{s2}','{s5}','{s6}','{s7}','{s3}',{s4})"

            con.execute(query)
            con.commit()
            con.close()
            messagebox.showinfo("Success","Add Student Successfully...!")
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)

        def reset():
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)


        b1 = Button(main_win, font=fb, width=10, bg="#000000", fg="#FFD700", text="Save", height=1,command=save)
        b2 = Button(main_win, font=fb, width=10, bg="#000000", fg="#FFD700", text="Reset", height=1,command=reset)

        l = Label(main_win, text="", width=80, font=("Tempus Sans ITC", 27), bg="#000000", fg="#FFD700")
        l.place(x=1, y=800)
        lh1 = Label(main_win,text="Insert Student Details",font=("Bahnschrift Light",26),bg="#F0FFF0")
        lh1.place(x=650,y=70)

        lb1.place(x=450,y=140)
        t1.place(x=850,y=140)



        lb2.place(x=450,y=220)
        t2.place(x=850,y=220)

        lb3.place(x=450,y=310)
        t3.place(x=850,y=310)

        lb4.place(x=450,y=400)
        t4.place(x=850,y=400)

        lb5.place(x=450,y=490)
        c1.place(x=850,y=490)

        lb6.place(x=450,y=570)
        c2.place(x=850,y=570)

        lb7.place(x=450,y=660)
        c3.place(x=850,y=660)

        b1.place(x=700,y=720)
        b2.place(x=1100,y=720)

    def issue_book():
        clear()

        def issued():
            s1 = t1.get()
            s2 = t2.get()
            s3 = t3.get()
            s4 = t4.get()
            s5 = str(datetime.today())

            con = sqlite3.connect("central_lab.db")
            query = f"insert into issue_book values({s1},'{s2}','{s3}','{s5}','{s4}')"
            con.execute(query)
            con.commit()
            con.close()
            messagebox.showinfo("Success","Book Issued Successfully....!")
            reset()
            t1.focus()

        def reset():
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)

        fb = ("Bahnschrift Light", 21)

        lb = Label(main_win, text="Issue Book ", font=("Bahnschrift Light", 30), bg="#F0FFF0")
        lb.place(x=650, y=80)

        lb1 = Label(main_win, text="Student Roll No :- ", font=fb, bg="#F0FFF0")
        lb1.place(x=500, y=200)

        t1 = Entry(main_win, width=25, bd=5, font=fb)
        t1.place(x=800, y=200)

        lb2 = Label(main_win, text="Enter Book ID :- ", font=fb, bg="#F0FFF0")
        lb2.place(x=500, y=300)

        t2 = Entry(main_win, width=25, bd=5, font=fb)
        t2.place(x=800, y=300)

        lb3 = Label(main_win, text="Enter Book Name :- ", font=fb, bg="#F0FFF0")
        lb3.place(x=500, y=400)

        t3 = Entry(main_win, width=25, bd=5, font=fb)
        t3.place(x=800, y=400)

        lb4 = Label(main_win, text="Enter Return Date :- ", font=fb, bg="#F0FFF0")
        lb4.place(x=500, y=500)

        t4 = Entry(main_win, width=25, bd=5, font=fb)
        t4.place(x=800, y=500)

        b1 = Button(main_win, text="Issued Book", width=15, font=fb, bg="#000000", fg="#FFD700", bd=5,command=issued)
        b1.place(x=550, y=650)

        b2 = Button(main_win, text="Reset", width=10, font=fb, bg="#000000", fg="#FFD700", bd=5,command=reset)
        b2.place(x=950, y=650)

    def return_book():
        clear()

        def return_():
            s1 = t1.get()
            s2 = t2.get()
            s4 = str(t4.get())

            con = sqlite3.connect("central_lab.db")
            cur = con.cursor()
            query = f"select return_date from issue_book where return_date = '{s4}'"
            cur.execute(query)
            data = cur.fetchone()
            con.close()
            print(str(data))


            if str(data[0]) == s4:
                con = sqlite3.connect("central_lab.db")
                q = f"delete from issue_book where student_id = '{s1} and book_id ='{s2}'"
                cur = con.cursor()
                cur.execute(q)
                con.commit()
                con.close()
                messagebox.showinfo("Success","Successfully..")

            else:
                messagebox.showerror("Due","paid due money then return it..!")

        def reset_all():
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)


        fb = ("Bahnschrift Light", 21)

        lb = Label(main_win, text="Return Book ", font=("Bahnschrift Light", 30), bg="#F0FFF0")
        lb.place(x=650, y=80)

        lb1 = Label(main_win, text="Student Roll No :- ", font=fb, bg="#F0FFF0")
        lb1.place(x=500, y=200)

        t1 = Entry(main_win, width=25, bd=5, font=fb)
        t1.place(x=800, y=200)

        lb2 = Label(main_win, text="Enter Book ID :- ", font=fb, bg="#F0FFF0")
        lb2.place(x=500, y=300)

        t2 = Entry(main_win, width=25, bd=5, font=fb)
        t2.place(x=800, y=300)

        lb3 = Label(main_win, text="Enter Book Name :- ", font=fb, bg="#F0FFF0")
        lb3.place(x=500, y=400)

        t3 = Entry(main_win, width=25, bd=5, font=fb)
        t3.place(x=800, y=400)

        lb4 = Label(main_win, text="Enter Return Date :- ", font=fb, bg="#F0FFF0")
        lb4.place(x=500, y=500)

        t4 = Entry(main_win, width=25, bd=5, font=fb)
        t4.place(x=800, y=500)

        b1 = Button(main_win, text="Return Book", width=15, font=fb, bg="#000000", fg="#FFD700", bd=5, command=return_)
        b1.place(x=550, y=650)

        b2 = Button(main_win, text="Reset", width=10, font=fb, bg="#000000", fg="#FFD700", bd=5, command=reset_all)
        b2.place(x=950, y=650)


    def add_new_book():
        clear()

        def book_save():
            con = sqlite3.connect("central_lab.db")
            s1 = t1.get()
            s2 = t2.get()
            s3 = t3.get()
            s4 = t4.get()

            query = f"insert into book values('{s1}','{s2}','{s3}','{s4}')"
            con.execute(query)
            con.commit()
            con.close()
            messagebox.showinfo("Success","Add book Successfully")
            reset()
            t1.focus()

        def reset():
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)
            t1.focus()


        fb = ("Bahnschrift Light", 21)

        lb = Label(main_win, text="Insert Book Details", font=("Bahnschrift Light", 30), bg="#F0FFF0")
        lb.place(x=650, y=80)

        lb1 = Label(main_win,text="Enter Book ID :- ",font=fb,bg="#F0FFF0")
        lb1.place(x=500,y=200)

        t1 = Entry(main_win,width=25,bd=5,font=fb)
        t1.place(x=800,y=200)

        lb2 = Label(main_win, text="Enter Book Name :- ", font=fb, bg="#F0FFF0")
        lb2.place(x=500, y=300)

        t2 = Entry(main_win, width=25, bd=5, font=fb)
        t2.place(x=800, y=300)

        lb3 = Label(main_win, text="Book Author :- ", font=fb, bg="#F0FFF0")
        lb3.place(x=500, y=400)

        t3 = Entry(main_win, width=25, bd=5, font=fb)
        t3.place(x=800, y=400)

        lb4 = Label(main_win, text="Book Publication :- ", font=fb, bg="#F0FFF0")
        lb4.place(x=500, y=500)

        t4 = Entry(main_win, width=25, bd=5, font=fb)
        t4.place(x=800, y=500)

        b1 = Button(main_win,text="Save",width=10,font=fb,bg="#000000",fg="#FFD700",bd=5,command=book_save)
        b1.place(x=550,y=650)

        b2 = Button(main_win, text="Reset", width=10, font=fb, bg="#000000", fg="#FFD700", bd=5,command=reset)
        b2.place(x=850, y=650)

    def book_history():
        clear()

        def search_for():
            s1 = t1.get()
            t2.configure(state=NORMAL)
            t3.configure(state=NORMAL)
            t4.configure(state=NORMAL)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)

            con = sqlite3.connect("central_lab.db")
            cur = con.cursor()
            qu = f"select * from book where book_id = '{s1}'"
            cur.execute(qu)
            data = cur.fetchone()
            con.close()

            t2.insert(0,data[1])
            t3.insert(0,data[2])
            t4.insert(0,data[3])
            t2.configure(state=DISABLED)
            t3.configure(state=DISABLED)
            t4.configure(state=DISABLED)
            messagebox.showinfo("Success","Book is Found Read TextBoxes")

        def reset():
            t2.configure(state=NORMAL)
            t3.configure(state=NORMAL)
            t4.configure(state=NORMAL)
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)
            t1.focus()
            t2.configure(state=DISABLED)
            t3.configure(state=DISABLED)
            t4.configure(state=DISABLED)



        fb = ("Bahnschrift Light", 21)

        lb = Label(main_win, text="Search for Book Details", font=("Bahnschrift Light", 30), bg="#F0FFF0")
        lb.place(x=650, y=80)

        lb1 = Label(main_win, text="Enter Book ID :- ", font=fb, bg="#F0FFF0")
        lb1.place(x=500, y=200)

        t1 = Entry(main_win, width=25, bd=5, font=fb)
        t1.place(x=800, y=200)

        lb2 = Label(main_win, text="Book Name :- ", font=fb, bg="#F0FFF0")
        lb2.place(x=500, y=300)

        t2 = Entry(main_win, width=25, bd=5, font=fb,state=DISABLED)
        t2.place(x=800, y=300)

        lb3 = Label(main_win, text="Book Author :- ", font=fb, bg="#F0FFF0")
        lb3.place(x=500, y=400)

        t3 = Entry(main_win, width=25, bd=5, font=fb,state=DISABLED)
        t3.place(x=800, y=400)

        lb4 = Label(main_win, text="Book Publication :- ", font=fb, bg="#F0FFF0")
        lb4.place(x=500, y=500)

        t4 = Entry(main_win, width=25, bd=5, font=fb,state=DISABLED)
        t4.place(x=800, y=500)

        b1 = Button(main_win, text="Check Out", width=10, font=fb, bg="#000000", fg="#FFD700", bd=5,command=search_for)
        b1.place(x=550, y=650)

        b2 = Button(main_win, text="Reset", width=10, font=fb, bg="#000000", fg="#FFD700", bd=5, command=reset)
        b2.place(x=850, y=650)


    def student_history():
        clear()


    def check_for_not_return_books():
        clear()

    def search_student_info():
        clear()

        def check_student():
            s1 = t1.get()
            t2.configure(state=NORMAL)
            t3.configure(state=NORMAL)
            t4.configure(state=NORMAL)
            t5.configure(state=NORMAL)
            t6.configure(state=NORMAL)
            t7.configure(state=NORMAL)
            con = sqlite3.connect("central_lab.db")
            cur = con.cursor()
            query = f"select * from student where roll no = {s1}"
            cur.execute(query)
            data = cur.fetchone()
            con.close()
            t2.insert(0, data[1])
            t3.insert(0,data[2])
            t4.insert(0,data[3])
            t5.insert(0,data[4])
            t6.insert(0,data[5])
            t7.insert(0,data[6])

            t2.configure(state=DISABLED)
            t3.configure(state=DISABLED)
            t4.configure(state=DISABLED)
            t5.configure(state=DISABLED)
            t6.configure(state=DISABLED)
            t7.configure(state=DISABLED)


        fb = ("Bahnschrift Light", 21)
        lb1 = Label(main_win, text="Enter Student Roll No :-", bg="#F0FFF0", font=fb)
        t1 = Entry(main_win, width=25, font=fb, bd=5)

        lb2 = Label(main_win, text="Student Name :-", bg="#F0FFF0", font=fb)
        t2 = Entry(main_win, width=25, font=fb, bd=5,state=DISABLED)

        lb3 = Label(main_win, text="Student Email :-", bg="#F0FFF0", font=fb)
        t3 = Entry(main_win, width=25, font=fb, bd=5,state=DISABLED)

        lb4 = Label(main_win, text="Student Mob No :-", bg="#F0FFF0", font=fb)
        t4 = Entry(main_win, width=25, font=fb, bd=5,state=DISABLED)

        lb5 = Label(main_win, text="Student Branch :-", bg="#F0FFF0", font=fb)
        t5 = Entry(main_win, width=25, font=fb, bd=5,state=DISABLED)

        lb6 = Label(main_win, text="Student Year :-", bg="#F0FFF0", font=fb)
        t6 = Entry(main_win, width=25, font=fb, bd=5,state=DISABLED)

        lb7 = Label(main_win, text="Student Class :-", bg="#F0FFF0", font=fb)
        t7 = Entry(main_win, width=25, font=fb, bd=5,state=DISABLED)

        b1 = Button(main_win, font=fb, width=10, bg="#000000", fg="#FFD700", text="Check Student", height=1,command=check_student)
        b2 = Button(main_win, font=fb, width=10, bg="#000000", fg="#FFD700", text="Reset", height=1)

        l = Label(main_win, text="", width=80, font=("Tempus Sans ITC", 27), bg="#000000", fg="#FFD700")
        l.place(x=1, y=800)
        lh1 = Label(main_win, text="Insert Student Details", font=("Bahnschrift Light", 26), bg="#F0FFF0")
        lh1.place(x=650, y=70)

        lb1.place(x=450, y=140)
        t1.place(x=850, y=140)

        lb2.place(x=450, y=220)
        t2.place(x=850, y=220)

        lb3.place(x=450, y=310)
        t3.place(x=850, y=310)

        lb4.place(x=450, y=400)
        t4.place(x=850, y=400)

        lb5.place(x=450, y=490)
        t5.place(x=850, y=490)

        lb6.place(x=450, y=570)
        t6.place(x=850, y=570)

        lb7.place(x=450, y=660)
        t7.place(x=850, y=660)

        b1.place(x=700, y=720)
        b2.place(x=1100, y=720)

    def return_book_reminder():
        clear()



    def logout(e):
        exit(0)

    def clear():
        for w in main_win.winfo_children():
            w.destroy()

        f = ("Tempus Sans ITC", 18)

        l = Label(main_win, text="", width=80, font=("Tempus Sans ITC", 27), bg="#000000", fg="#FFD700")
        l.place(x=1, y=800)

        l = Label(main_win, text="We!Come To Central Lab", width=80, font=("Tempus Sans ITC", 27), bg="#000000",
                  fg="#FFD700")
        l.place(x=0, y=10)

        l1 = Label(main_win, text="Logout", font=("Tempus Sans ITC", 20), bg="#000000", fg="#FFD700")
        l1.bind('<Button>', logout)
        l1.place(x=1385, y=23)

        b1 = Button(main_win, text="Return Book Reminder", font=f, width=25, bg="#000000", bd=10, fg="#FFD700",command=return_book_reminder)
        b1.place(x=10, y=710)

        b2 = Button(main_win, text="Issue Book", font=f, width=25, bg="#000000", bd=10, fg="#FFD700",command=issue_book)
        b2.place(x=10, y=230)

        b3 = Button(main_win, text="Return Book", font=f, width=25, bg="#000000", bd=10, fg="#FFD700",command=return_book)
        b3.place(x=10, y=390)

        b4 = Button(main_win, text="Add New Book", font=f, width=25, bg="#000000", bd=10, fg="#FFD700",command=add_new_book)
        b4.place(x=10, y=310)

        b5 = Button(main_win, text="Search for Book", font=f, width=25, bg="#000000", bd=10, fg="#FFD700",command=book_history)
        b5.place(x=10, y=470)

        b6 = Button(main_win, text="Student History", font=f, width=25, bg="#000000", bd=10, fg="#FFD700",command=student_history)
        b6.place(x=10, y=550)

        b7 = Button(main_win, text="Check For Not Return Books", font=f, width=25, bg="#000000", bd=10, fg="#FFD700",command=check_for_not_return_books)
        b7.place(x=10, y=150)

        b8 = Button(main_win, text="Search Student Information.", font=f, width=25, bg="#000000", bd=10, fg="#FFD700",command=search_student_info)
        b8.place(x=10, y=70)

        b9 = Button(main_win, text="Add Student", font=f, width=25, bg="#000000", bd=10, fg="#FFD700",command=add_student)
        b9.place(x=10, y=630)

    clear()


    main_win.mainloop()

main_window()