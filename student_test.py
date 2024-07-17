from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk




class Student_test:
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1530x790+00+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bd=2)
        main_frame.place(x=20,y=50,width=1480,height=600)
        
        
        Left_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)



        Right_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=680,height=580)







if __name__ == "__main__":
    root=Tk()
    obj=Student_test(root)
    root.mainloop()