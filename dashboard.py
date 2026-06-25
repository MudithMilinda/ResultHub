from tkinter import *
from PIL import Image, ImageTk
from tkmacosx import Button
from course import CourseClass
from student import studentClass

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # logo image
        img = Image.open("images/logo.png")
        img = img.resize((50, 50), Image.LANCZOS)
        self.logo_dash = ImageTk.PhotoImage(img)

        # title bar
        title = Label(
            self.root,
            text="Student Result Management System",
            compound=LEFT,
            image=self.logo_dash,
            font=("times new roman", 20, "bold"),
            bg="blue",
            fg="white"
        )
        title.place(x=0, y=0, relwidth=1, height=50)

        # menu frame
        M_Frame = LabelFrame(
            self.root,
            text="Menus",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="blue"
        )
        M_Frame.place(x=10, y=70, width=1340, height=80)

        # course buttons
        btn_course = Button(
            M_Frame,
            text="Course",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2",
            command=self.add_course
        )
        btn_course.place(x=20, y=10, width=200, height=40)

        # student buttons
        btn_student = Button(
            M_Frame,
            text="Student",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2",
            command=self.add_student
        )
        btn_student.place(x=240, y=10, width=200, height=40)

        # result buttons
        btn_result = Button(
            M_Frame,
            text="Result",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2"
        )
        btn_result.place(x=460, y=10, width=200, height=40)

        # view result buttons
        btn_view_result = Button(
            M_Frame,
            text="View Student Result",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2"
        )
        btn_view_result.place(x=680, y=10, width=200, height=40)

        # logout buttons
        btn_logout = Button(
            M_Frame,
            text="Logout",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2"
        )
        btn_logout.place(x=900, y=10, width=200, height=40)

        # exit buttons
        btn_exit = Button(
            M_Frame,
            text="Exit",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2",
            command=self.root.destroy
        )
        btn_exit.place(x=1120, y=10, width=200, height=40)

        # content window
        self.bg_img = Image.open("images/bg.jpg")
        self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=400, y=180, width=920, height=350)

        #total course
        self.lbl_course = Label(
            self.root,
            text="Total Course\n[ 0 ]",
            font=("times new roman", 20),
            bg="lightblue",
            fg="white"
        )
        self.lbl_course.place(x=400, y=550, width=300, height=100)

        #total student
        self.lbl_student = Label(
            self.root,
            text="Total Student\n[ 0 ]",
            font=("times new roman", 20),
            bg="lightblue",
            fg="white"
        )
        self.lbl_student.place(x=710, y=550, width=300, height=100)

        #total result
        self.lbl_result = Label(
            self.root,
            text="Total Result\n[ 0 ]",
            font=("times new roman", 20),
            bg="lightblue",
            fg="white"
        )
        self.lbl_result.place(x=1020, y=550, width=300, height=100)

        # footer
        footer = Label(
            self.root,
            text="Student Result Management System Contact us for any technical issue: 9876543210",
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white"
        )
        footer.pack(side=BOTTOM, fill=X)


    #course button function
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    #student button function
    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()