from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os
from tkinter import messagebox



class Face_Recognition_System:
    def __init__(self,root,user) :
        self.root = root
        self.root.geometry("1530x790+00+0")
        self.root.title("Face Recognition System")


        #background Image
        bgimg=Image.open(r"assets\Images\college_images\bgnp.jpg")
        bgimg = bgimg.resize((1530,790),Image.LANCZOS)
        self.bgimg1 = ImageTk.PhotoImage(bgimg)

        bgimg_label=Label(self.root,image=self.bgimg1)
        bgimg_label.place(x=0,y=0,width=1530,height=790)


        #Student Button
        imgSt=Image.open(r"assets\Images\college_images\studentPortal.jpg")
        imgSt = imgSt.resize((180,150),Image.LANCZOS)
        self.photoimgSt = ImageTk.PhotoImage(imgSt)

        b1=Button(image=self.photoimgSt,cursor="hand2",command=self.student_details)
        b1.place(x=80,y=250,width=180,height=150)

        b1_1 = Button(text="Student Details",cursor="hand2",command=self.student_details)
        b1_1.place(x=80,y=400,width=180,height=30)

        if user=="Faculty":
            b1.config(state="disabled")
            b1_1.config(state="disabled")

        #Train Button
        train_Img=Image.open(r"assets\Images\college_images\chat.jpg")
        train_Img = train_Img.resize((180,150),Image.LANCZOS)
        self.phototrain_Img = ImageTk.PhotoImage(train_Img)

        b1=Button(image=self.phototrain_Img,cursor="hand2",command=self.train)
        b1.place(x=280,y=250,width=180,height=150)
        
        

        b1_1 = Button(text="Train Data",cursor="hand2",command=self.train)
        b1_1.place(x=280,y=400,width=180,height=30)

        if user=="Faculty":
            b1.config(state="disabled")
            b1_1.config(state="disabled")

        #Photoes Button
        sample_Img=Image.open(r"assets\Images\college_images\exit.jpg")
        sample_Img = sample_Img.resize((180,150),Image.LANCZOS)
        self.photosample_Img = ImageTk.PhotoImage(sample_Img)

        b1=Button(image=self.photosample_Img,cursor="hand2",command=self.openImages)
        b1.place(x=480,y=250,width=180,height=150)

        b1_1 = Button(text="Photoes",cursor="hand2",command=self.openImages)
        b1_1.place(x=480,y=400,width=180,height=30)

        #Attendance Button
        attendance_Img=Image.open(r"assets\Images\college_images\attendance_list.png")
        attendance_Img = attendance_Img.resize((180,150),Image.LANCZOS)
        self.photoattendance_Img = ImageTk.PhotoImage(attendance_Img)

        b1=Button(image=self.photoattendance_Img,cursor="hand2",command=self.attendance)
        b1.place(x=480,y=250,width=180,height=150)

        b1_1 = Button(text="Attendance",cursor="hand2",command=self.attendance)
        b1_1.place(x=480,y=400,width=180,height=30)


        #Face Recognize Button
        face_Img=Image.open(r"assets\Images\college_images\facialrecognition (1).png")
        face_Img = face_Img.resize((180,150),Image.LANCZOS)
        self.photoface_Img = ImageTk.PhotoImage(face_Img)

        b1=Button(image=self.photoface_Img,cursor="hand2",command=self.face_data)
        b1.place(x=680,y=250,width=180,height=150)

        b1_1 = Button(text="Face Recognition",cursor="hand2",command=self.face_data)
        b1_1.place(x=680,y=400,width=180,height=30)


        #Developer
        #Developer_Img=Image.open(r"assets\Images\college_images\developer.png")
        #Developer_Img = Developer_Img.resize((180,150),Image.LANCZOS)
        #self.photoDeveloper_Img = ImageTk.PhotoImage(Developer_Img)

        #b1=Button(image=self.photoDeveloper_Img,cursor="hand2",command=self.face_data)
        #b1.place(x=280,y=450,width=180,height=150)

        #b1_1 = Button(text="Developer",cursor="hand2",command=self.face_data)
        #b1_1.place(x=280,y=600,width=180,height=30)


        #Exit
        exit_Img=Image.open(r"assets\Images\college_images\exit.jpg")
        exit_Img = exit_Img.resize((180,150),Image.LANCZOS)
        self.photoexit_Img = ImageTk.PhotoImage(exit_Img)

        b1=Button(image=self.photoexit_Img,cursor="hand2",command=self.popupExit)
        b1.place(x=380,y=450,width=180,height=150)

        b1_1 = Button(text="Exit",cursor="hand2",command=self.popupExit)
        b1_1.place(x=380,y=600,width=180,height=30)

        #exit_Img=Image.open(r"assets\Images\college_images\exit.jpg")
        #exit_Img = exit_Img.resize((180,150),Image.LANCZOS)
        #self.photoexit_Img = ImageTk.PhotoImage(exit_Img)

        #b1=Button(image=self.photoexit_Img,cursor="hand2",command=self.popupExit)
        #b1.place(x=480,y=450,width=180,height=150)

        #b1_1 = Button(text="Exit",cursor="hand2",command=self.popupExit)
        #b1_1.place(x=480,y=600,width=180,height=30)

        


    def openImages(self):
        os.startfile("data")

        
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train(self):
        self.new_window = Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def popupExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":  
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()