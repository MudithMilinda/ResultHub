from tkinter import *
from PIL import Image, ImageTk
from tkmacosx import Button
from tkinter import ttk, messagebox
import sqlite3

class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+88+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # title bar..............................
        title = Label(
            self.root,
            text="Add Student Results",
            font=("times new roman", 20, "bold"),
            bg="Orange",
            fg="white"
        )
        title.place(x=10, y=15, width=1180, height=35)

        #variables.................................
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []
        self.fetch_roll()

        #widgets................................
        lbl_select = Label(
            self.root,
            text="Select Student",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_select.place(x=50, y=100)

        lbl_name = Label(
            self.root,
            text="Name",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_name.place(x=50, y=160)

        lbl_course = Label(
            self.root,
            text="Course",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_course.place(x=50, y=220)

        lbl_marks_ob = Label(
            self.root,
            text="Marks Obtained",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_marks_ob.place(x=50, y=280)

        lbl_full_marks = Label(
            self.root,
            text="Full Marks",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_full_marks.place(x=50, y=340)


        #select...................................
        self.txt_student = ttk.Combobox(
            self.root,
            textvariable=self.var_roll,
            values=self.roll_list,
            font=("times new roman", 15, "bold"),
            state="readonly",
            justify=CENTER
        )
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.set("Select")

        #search button.......................................
        btn_search = Button(
            self.root,
            text="Search",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2",
            command=self.search
        )
        btn_search.place(x=500, y=100, width=100, height=28)


        # text field.......................................
        txt_name = Entry(
            self.root,
            textvariable=self.var_name,
            font=("times new roman", 20, "bold"),
            bg="lightblue",
            fg="black",
            state="readonly"
        )
        txt_name.place(x=280, y=160, width=320)

        txt_course = Entry(
            self.root,
            textvariable=self.var_course,
            font=("times new roman", 20, "bold"),
            bg="lightblue",
            fg="black",
            state="readonly"
        )
        txt_course.place(x=280, y=220, width=320)

        txt_marks = Entry(
            self.root,
            textvariable=self.var_marks,
            font=("times new roman", 20, "bold"),
            bg="lightblue",
            fg="black"
        )
        txt_marks.place(x=280, y=280, width=320)

        txt_full_marks = Entry(
            self.root,
            textvariable=self.var_full_marks,
            font=("times new roman", 20, "bold"),
            bg="lightblue",
            fg="black"
        )
        txt_full_marks.place(x=280, y=340, width=320)


        #add & clear button................................
        btn_add = Button(
            self.root,
            text="Submit",
            font=("times new roman", 15),
            bg="blue",
            activebackground="lightblue",
            fg="white",
            cursor="hand2",
            command=self.add
        )
        btn_add.place(x=300, y=420, width=120, height=35)

        btn_clear = Button(
            self.root,
            text="Clear",
            font=("times new roman", 15),
            bg="blue",
            activebackground="lightblue",
            fg="white",
            cursor="hand2",
            command=self.clear
        )
        btn_clear.place(x=430, y=420, width=120, height=35)


        #image..............................................
        self.bg_img = Image.open("images/result.jpg")
        self.bg_img = self.bg_img.resize((500, 300), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=630, y=100)


    # fetch roll no...........................................
    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select roll from student")
            rows = cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()


    #search student.........................................
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name,course from student where roll =?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row!= None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    
    # add result..........................................
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please first search student record", parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?", (self.var_roll.get(),self.var_course.get()))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Result already present, try different", parent=self.root)
                else:
                    per= (int(self.var_marks.get())*100)/ int(self.var_full_marks.get())
                    cur.execute(
                        "insert into result  (roll, name, course, marks, full_marks, per) values(?, ?, ?, ?, ?, ?)",(
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_course.get(),
                            self.var_marks.get(),
                            self.var_full_marks.get(),
                            str(per)
                        )   
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Result added successfully", parent=self.root)          
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    #clear.....................................
    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")






if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()