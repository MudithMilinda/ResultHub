from tkinter import *
from PIL import Image, ImageTk
from tkmacosx import Button
from tkinter import ttk, messagebox
import sqlite3

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+88+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # title bar..............................
        title = Label(
            self.root,
            text="Manage Course Details",
            font=("times new roman", 20, "bold"),
            bg="blue",
            fg="white"
        )
        title.place(x=10, y=15, width=1180, height=35)

        # variables...........................
        self.var_course_name = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        #widget.............................
        lbl_course_name = Label(
            self.root,
            text="Course Name",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_course_name.place(x=10, y=60)

        lbl_duration = Label(
            self.root,
            text="Duration",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_duration.place(x=10, y=100)

        lbl_charges = Label(
            self.root,
            text="Charges",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_charges.place(x=10, y=140)

        lbl_description = Label(
            self.root,
            text="Description",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_description.place(x=10, y=180)


        #text entry fields.......................
        self.txt_course_name = Entry(
            self.root,
            textvariable=self.var_course_name,
            font=("times new roman", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
        self.txt_course_name.place(x=150, y=60, width=200)

        txt_duration = Entry(
            self.root,
            textvariable=self.var_duration,
            font=("times new roman", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
        txt_duration.place(x=150, y=100, width=200)

        txt_charges = Entry(
            self.root,
            textvariable=self.var_charges,
            font=("times new roman", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
        txt_charges.place(x=150, y=140, width=200)

        self.txt_description = Text( 
            self.root,
            font=("times new roman", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
        self.txt_description.place(x=150, y=180, width=500, height=130)

        #buttons...............................
        self.btn_add = Button(
            self.root,
            text="Save",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2",
            command=self.add
        )
        self.btn_add.place(x=150, y=400, width=110, height=40)

        self.btn_update = Button(
            self.root,
            text="Update",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2",
            command=self.update
        )
        self.btn_update.place(x=270, y=400, width=110, height=40)

        self.btn_delete = Button(
            self.root,
            text="Delete",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2",
            command=self.delete
        )
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = Button(
            self.root,
            text="Clear",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2",
            command=self.clear
        )
        self.btn_clear.place(x=510, y=400, width=110, height=40)


        #search panel...........................
        self.var_search = StringVar()
        lbl_search_course_name = Label(
            self.root,
            text="Course Name",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_search_course_name.place(x=720, y=60)

        txt_search_course_name = Entry(
            self.root,
            textvariable=self.var_search,
            font=("times new roman", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
        txt_search_course_name.place(x=870, y=60, width=180)

        btn_search = Button(
            self.root,
            text="Search",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2",
            command=self.search
        )
        btn_search.place(x=1070, y=60, width=120, height=28)

        #content window...........................
        self.C_Frame = Frame(
            self.root, 
            bd=2, 
            relief=RIDGE,
            bg="white"
        )
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(
            self.C_Frame,
            columns=("cid", "name", "duration", "charges", "description"),
            yscrollcommand=scrolly.set,
            xscrollcommand=scrollx.set
        )
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")
        self.CourseTable["show"] = "headings"

        self.CourseTable.column("cid", width=100)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("duration", width=100)
        self.CourseTable.column("charges", width=100)
        self.CourseTable.column("description", width=100)

        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()


 
    #clear fields.........................................
    def clear(self):
        self.show()
        self.var_course_name.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete("1.0", END)
        self.txt_course_name.config(state=NORMAL)  # Set the course name entry to normal state


    #delete course........................................
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course_name.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where course_name=?", (self.var_course_name.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select a course to delete", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from course where course_name=?", (self.var_course_name.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Course deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    #course added........................................
    def get_data(self, ev):
        self.txt_course_name.config(state="readonly")  # Set the course name entry to readonly
        self.txt_course_name
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        #print(row)
        self.var_course_name.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete("1.0", END)
        self.txt_description.insert(END, row[4])
    
    
    # add course to database..........................................
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course_name.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where course_name=?", (self.var_course_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Course Name already present, try different", parent=self.root)
                else:
                    cur.execute(
                        "insert into course (course_name, duration, charges, description) values(?, ?, ?, ?)",(
                            self.var_course_name.get(),
                            self.var_duration.get(),
                            self.var_charges.get(),
                            self.txt_description.get("1.0", END)
                        )   
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Course added successfully", parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    #update course details..........................................
    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course_name.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where course_name=?", (self.var_course_name.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select course from list", parent=self.root)
                else:
                    cur.execute(
                        "update course set duration=?, charges=?, description=? where course_name=?",(
                            self.var_duration.get(),
                            self.var_charges.get(),
                            self.txt_description.get("1.0", END),
                            self.var_course_name.get()
                        )   
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Course updated successfully", parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    # show all courses in table
    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    


    #search course.........................................
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute(f"select * from course where course_name LIKE '%{self.var_search.get()}%'")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()