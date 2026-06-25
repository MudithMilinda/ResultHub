from tkinter import *
from PIL import Image, ImageTk
from tkmacosx import Button
from tkinter import ttk, messagebox
import sqlite3

class studentClass:
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
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        #widget.............................
        #column 1...............................
        lbl_roll = Label(
            self.root,
            text="Roll No.",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_roll.place(x=10, y=60)

        lbl_name = Label(
            self.root,
            text="Name",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_name.place(x=10, y=100)

        lbl_email = Label(
            self.root,
            text="Email",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_email.place(x=10, y=140)

        lbl_gender = Label(
            self.root,
            text="Gender",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_gender.place(x=10, y=180)


        #state......................................
        lbl_state = Label(
            self.root,
            text="State",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_state.place(x=10, y=220)
        txt_state = Entry(
            self.root,
            textvariable=self.var_state,
            font=("times new roman", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
        txt_state.place(x=150, y=220, width=150)


        #city......................................
        lbl_city = Label(
            self.root,
            text="city",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_city.place(x=310, y=220)
        txt_city = Entry(
            self.root,
            textvariable=self.var_city,
            font=("times new roman", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
        txt_city.place(x=380, y=220, width=100)


        #pin......................................
        lbl_pin = Label(
            self.root,
            text="pin",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_pin.place(x=500, y=220)
        txt_pin = Entry(
            self.root,
            textvariable=self.var_pin,
            font=("times new roman", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
        txt_pin.place(x=560, y=220, width=120)


        lbl_address = Label(
            self.root,
            text="Address",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_address.place(x=10, y=260)


        #text entry fields | column 1...............................
        self.txt_roll = Entry(
            self.root,
            textvariable=self.var_roll,
            font=("times new roman", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
        self.txt_roll.place(x=150, y=60, width=200)

        txt_name = Entry(
            self.root,
            textvariable=self.var_name,
            font=("times new roman", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
        txt_name.place(x=150, y=100, width=200)

        txt_email = Entry(
            self.root,
            textvariable=self.var_email,
            font=("times new roman", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
        txt_email.place(x=150, y=140, width=200)

        self.txt_gender = ttk.Combobox(
            self.root,
            textvariable=self.var_gender,
            values=("Select", "Male", "Female", "Other"),
            font=("times new roman", 15, "bold"),
            state="readonly",
            justify=CENTER,
            fg="black"
        )
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)  # Set default value to "Select"



        #column 2...............................
        lbl_dob = Label(
            self.root,
            text="D.O.B",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_dob.place(x=360, y=60)

        lbl_contact = Label(
            self.root,
            text="Contact",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_contact.place(x=360, y=100)

        lbl_admission = Label(
            self.root,
            text="Admission",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_admission.place(x=360, y=140)

        lbl_course = Label(
            self.root,
            text="Course",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_course.place(x=360, y=180)

        #text entry fields | column 2...............................
        self.course_list = []

        #function call to update the list
        txt_dob = Entry(
            self.root,
            textvariable=self.var_dob,
            font=("times new roman", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
        txt_dob.place(x=480, y=60, width=200)

        txt_contact = Entry(
            self.root,
            textvariable=self.var_contact,
            font=("times new roman", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
        txt_contact.place(x=480, y=100, width=200)

        txt_admission = Entry(
            self.root,
            textvariable=self.var_a_date,
            font=("times new roman", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
        txt_admission.place(x=480, y=140, width=200)

        self.txt_course = ttk.Combobox(
            self.root,
            textvariable=self.var_course,
            values=self.course_list,
            font=("times new roman", 15, "bold"),
            state="readonly",
            justify=CENTER,
            fg="black"
        )
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.set("Empty")  # Set default value to "Select"



        #text address field.......................
        self.txt_address = Text( 
            self.root,
            font=("times new roman", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
        self.txt_address.place(x=150, y=260, width=540, height=100)

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
        lbl_search_roll = Label(
            self.root,
            text="Roll No.",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black"
        )
        lbl_search_roll.place(x=720, y=60)

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
            columns=("roll", "name", "email", "gender", "dob", "contact", "admission"),
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
        self.var_roll.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete("1.0", END)
        self.txt_roll.config(state=NORMAL)  # Set the course name entry to normal state


    #delete course........................................
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where course_name=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select a course to delete", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from course where course_name=?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Course deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    #course added........................................
    def get_data(self, ev):
        self.txt_roll.config(state="readonly")  # Set the course name entry to readonly
        self.txt_roll
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        #print(row)
        self.var_roll.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete("1.0", END)
        self.txt_description.insert(END, row[4])
    
    
    # add course to database..........................................
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where course_name=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Course Name already present, try different", parent=self.root)
                else:
                    cur.execute(
                        "insert into course (course_name, duration, charges, description) values(?, ?, ?, ?)",(
                            self.var_roll.get(),
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
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where course_name=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select course from list", parent=self.root)
                else:
                    cur.execute(
                        "update course set duration=?, charges=?, description=? where course_name=?",(
                            self.var_duration.get(),
                            self.var_charges.get(),
                            self.txt_description.get("1.0", END),
                            self.var_roll.get()
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
    obj = studentClass(root)
    root.mainloop()