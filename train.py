from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")


        #background Image
        bgimg=Image.open(r"assets\Images\college_images\trainData2.png")
        bgimg = bgimg.resize((1530,790),Image.LANCZOS)
        self.bgimg1 = ImageTk.PhotoImage(bgimg)

        bgimg_label=Label(self.root,image=self.bgimg1)
        bgimg_label.place(x=0,y=0,width=1530,height=790)



        #Train Data Button
        imgSt=Image.open(r"assets\Images\college_images\facial-recognition_0.jpg")
        imgSt = imgSt.resize((400,150),Image.LANCZOS)
        self.photoimgSt = ImageTk.PhotoImage(imgSt)

        b1=Button(bgimg_label,image=self.photoimgSt,cursor="hand2")
        b1.place(x=150,y=320,width=400,height=150)

        b1_1 = Button(bgimg_label,text="Train Image Data",cursor="hand2",command=self.train_classifier,font="cosmicsansns 11 bold",bg="darkblue",fg="white")
        b1_1.place(x=150,y=470,width=400,height=30)





    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids) 


        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed")












if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()