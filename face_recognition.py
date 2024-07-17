from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import csv
from tkinter import messagebox

class Face_Recognition:

    myhost="localhost"
    myusername="root"
    mypassword="admin"
    mydatabase="face_recognizer"

    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogniton System")

        #background Image
        bgimg=Image.open(r"assets\Images\college_images\bgnp.jpg")
        bgimg = bgimg.resize((1530,790),Image.LANCZOS)
        self.bgimg1 = ImageTk.PhotoImage(bgimg)

        bgimg_label=Label(self.root,image=self.bgimg1)
        bgimg_label.place(x=0,y=0,width=1530,height=790)


        #Mark Attendance Button
        imgSt=Image.open(r"assets\Images\college_images\attendance_6612108.png")
        imgSt = imgSt.resize((250,220),Image.LANCZOS)
        self.photoimgSt = ImageTk.PhotoImage(imgSt)

        b1=Button(bgimg_label,image=self.photoimgSt,cursor="hand2",command=self.face_recog_mark_attendance)
        b1.place(x=150,y=320,width=250,height=220)

        b1_1 = Button(bgimg_label,text="Mark Attendance",cursor="hand2",command=self.face_recog_mark_attendance)
        b1_1.place(x=150,y=550,width=250,height=30)


        #Detect face Button
        recog=Image.open(r"assets\Images\college_images\pngegg.png")
        recog = recog.resize((250,220),Image.LANCZOS)
        self.photorecog = ImageTk.PhotoImage(recog)

        b1=Button(bgimg_label,image=self.photorecog,cursor="hand2",command=self.face_recog)
        b1.place(x=430,y=320,width=250,height=220)

        b1_1 = Button(bgimg_label,text="Recognize Student",cursor="hand2",command=self.face_recog)
        b1_1.place(x=430,y=550,width=250,height=30)

    #==============Mark Attendance to Database==========================

    def mark_attendance_to_database(self,id,n,r,d,mail):
        now = datetime.now()
        d1=now.strftime("%Y-%m-%d")
        dtString = now.strftime("%H:%M:%S")
        try:
            conn=mysql.connector.connect(host=self.myhost,username=self.myusername,password=self.mypassword,database=self.mydatabase)
            my_cursor=conn.cursor()

            my_cursor.execute("select count(*) from attendance where ID = '"+str(id)+ "' and dateOfPresent = '"+d1+"'")
            check=my_cursor.fetchone()
            print(check)
            check=check[0]
            print(check)
            if check == 0:

                my_cursor.execute("INSERT INTO ATTENDANCE VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            id,
                                                                                            n,
                                                                                            r,
                                                                                            d,
                                                                                            d1,
                                                                                            dtString,
                                                                                            'Present',
                                                                                            mail
                                                                                        ))

                conn.commit()
                conn.close()
                messagebox.showinfo("success","Student Attendance has been Marked Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)




    #===========================face recognition=============
        
    def face_recog_mark_attendance(self):

        def draw_boundry(img,classifier,scaleFactor,miNeighbors,color,text,clf):
            grey_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(grey_image,scaleFactor,miNeighbors)

            coord =[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(grey_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host=self.myhost,username=self.myusername,password=self.mypassword,database=self.mydatabase)
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from student where ID = "+str(id))
                n=my_cursor.fetchone()
                if n is not None:
                    n=n[0]

                my_cursor.execute("select Department from student where ID = "+str(id))
                d=my_cursor.fetchone()
                if d is not None:
                    d=d[0]

                my_cursor.execute("select Roll from student where ID = "+str(id))
                r=my_cursor.fetchone()
                if r is not None:
                    r=r[0]

                my_cursor.execute("select Gender from student where ID = "+str(id))
                g=my_cursor.fetchone()
                if g is not None:
                    g=g[0]

                my_cursor.execute("select email from student where ID = "+str(id))
                mail=my_cursor.fetchone()
                if mail is not None:
                    mail=mail[0]
                #print("ID : ",id)
                #print("Name ",n)
                #n="+".join(n)

                if confidence>25:
                    cv2.putText(img,f"ID:{id}",(x,y-105),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll Number:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Gender:{g}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance_to_database(id,n,r,d,mail)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            
            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            if cv2.waitKey(1)==13:
                video_cap.release()
                cv2.destroyAllWindows()
                break

    def face_recog(self):

        def draw_boundry(img,classifier,scaleFactor,miNeighbors,color,text,clf):
            grey_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(grey_image,scaleFactor,miNeighbors)

            coord =[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(grey_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))
                print(id)
                conn=mysql.connector.connect(host=self.myhost,username=self.myusername,password=self.mypassword,database=self.mydatabase)
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from student where ID = "+str(id))
                n=my_cursor.fetchone()
                if n is not None:
                    n=n[0]

                my_cursor.execute("select Department from student where ID = "+str(id))
                d=my_cursor.fetchone()
                if d is not None:
                    d=d[0]

                my_cursor.execute("select Roll from student where ID = "+str(id))
                r=my_cursor.fetchone()
                if r is not None:
                    r=r[0]

                my_cursor.execute("select Gender from student where ID = "+str(id))
                g=my_cursor.fetchone()
                if g is not None:
                    g=g[0]
                #print("ID : ",id)
                #print("Name ",n)
                #n="+".join(n)

                if confidence>45:
                    cv2.putText(img,f"ID:{id}",(x,y-105),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll Number:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Gender:{g}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            
            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            if cv2.waitKey(1)==13:
                video_cap.release()
                cv2.destroyAllWindows()
                break

            
        
            



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()        