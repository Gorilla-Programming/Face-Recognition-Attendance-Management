from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:

    myhost="localhost"
    myusername="root"
    mypassword="admin"
    mydatabase="face_recognizer"
    
    def __init__(self, root):

        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")



        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_searchBy=StringVar()
        self.var_searchId=StringVar()





        #background Image
        bgimg=Image.open(r"assets\Images\college_images\studentbg.png")
        bgimg = bgimg.resize((1530,790),Image.LANCZOS)
        self.bgimg1 = ImageTk.PhotoImage(bgimg)

        bg_img=Label(self.root,image=self.bgimg1)
        bg_img.place(x=0,y=0,width=1530,height=790)



        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=160, width=1510,height=620)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=600)

        img_left=Image.open(r"assets\Images\college_images\studentLeft.png") 
        img_left=img_left.resize((720,170), Image.LANCZOS)

        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=0,width=710,height=170)


        
        #current course Information
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=155,width=710,height=120)

        
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",textvariable=self.var_dep)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",textvariable=self.var_course)
        course_combo["values"]=("Select course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #YEAR
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=17,textvariable=self.var_year)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=20,textvariable=self.var_semester)
        semester_combo["values"]=("Select Semester","Semester 1","Semester 2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)



        #Class student info
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=10,y=275,width=710,height=300)


        #student id
        studentId_label=Label(class_student_frame,text="ID:",font=("times new roman",12,"bold"))
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)


        studentID_entry=Entry(class_student_frame,width=20,font=("times new roman",13,"bold"),textvariable=self.var_id)
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #student name
        studentName_label=Label(class_student_frame,text="Name:",font=("times new roman",12,"bold"))
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        studentName_entry=Entry(class_student_frame,width=20,font=("times new roman",13,"bold"),textvariable=self.var_name)
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)



        #class division
        class_div_label=Label(class_student_frame,text="Division:",font=("times new roman",12,"bold"))
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)


        class_div_entry=Entry(class_student_frame,width=20,font=("times new roman",13,"bold"),textvariable=self.var_div)
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        # Roll No
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"))
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)


        roll_no_entry=Entry(class_student_frame,width=20,font=("times new roman",13,"bold"),textvariable=self.var_roll)
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)


        gender_entry=Entry(class_student_frame,width=20,font=("times new roman",13,"bold"),textvariable=self.var_gender)
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        # DOB
        dob_label=Label(class_student_frame,text="Date of Birth:",font=("times new roman",12,"bold"))
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)


        dob_entry= Entry(class_student_frame,width=20,font=("times new roman",13,"bold"),textvariable=self.var_dob)
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"))
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)


        email_entry= Entry(class_student_frame,width=20,font=("times new roman",13,"bold"),textvariable=self.var_email)
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #Phone No
        phone_label=Label(class_student_frame,text="Mobile:",font=("times new roman",12,"bold"))
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)


        phone_entry= Entry(class_student_frame,width=20,font=("times new roman",13,"bold"),textvariable=self.var_phone)
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"))
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)


        address_entry= Entry(class_student_frame,width=20,font=("times new roman",13,"bold"),textvariable=self.var_address)
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"))
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)


        teacher_entry= Entry(class_student_frame,width=20,font=("times new roman",13,"bold"),textvariable=self.var_teacher)
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,text="Take Photo Sample", value="YES",variable=self.var_radio1)
        radiobtn1.grid(row=6,column=0,padx=10,pady=5,sticky=W)


        radiobtn2 = ttk.Radiobutton(class_student_frame,text="No Photo Sample", value="NO",variable=self.var_radio1)
        radiobtn2.grid(row=6,column=1,padx=10,pady=5,sticky=W)

        #button Frame


        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=205,width=700,height=35)


        save_btn= Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        save_btn.grid(row=0,column=0)

        update_btn= Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        update_btn.grid(row=0,column=1)

        delete_btn= Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        delete_btn.grid(row=0,column=2)

        reset_btn= Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=240,width=700,height=35)

        take_photo_sample_btn= Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,font=("times new roman",13,"bold"),bg="blue",fg="white",width=34)
        take_photo_sample_btn.grid(row=0,column=0)

        update_photo_sample_btn= Button(btn_frame1,text="Update Photo Sample",font=("times new roman",13,"bold"),bg="blue",fg="white",width=34)
        update_photo_sample_btn.grid(row=0,column=1)

        #Right Frame
        Right_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=680,height=580)


        img_right=Image.open(r"assets\Images\college_images\list.png") 
        img_right=img_right.resize((720,170), Image.LANCZOS)

        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=10,y=0,width=710,height=170)


        #search

        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),bg="white")
        search_frame.place(x=5,y=185,width=665,height=70)


        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15,textvariable=self.var_searchBy)
        search_combo["values"]=("Select","Roll No","Name","Email","Phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry= Entry(search_frame,width=15,font=("times new roman",12,"bold"),textvariable=self.var_searchId)
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn= Button(search_frame,text="Search",command=self.filter_data, font=("times new roman",12,"bold"),bg="blue",fg="white",width=13)
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn= Button(search_frame,text="Show All",command=self.fetch_data,font=("times new roman",12,"bold"),bg="blue",fg="white",width=13)
        showAll_btn.grid(row=0,column=4,padx=4)


        #Table Frame

        table_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=260,width=665,height=250)


        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("Department","Course","Year","Semester","ID","Name","Division","Roll","Gender","DOB","Email","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("Roll",text="Roll")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host=self.myhost,username=self.myusername,password=self.mypassword,database=self.mydatabase)
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO STUDENT VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student Details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host=self.myhost,username=self.myusername,password=self.mypassword,database=self.mydatabase)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                #print(data)
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #=============================Filter Data=======================================

    def filter_data(self):
        conn=mysql.connector.connect(host=self.myhost,username=self.myusername,password=self.mypassword,database=self.mydatabase)
        my_cursor=conn.cursor()
        if self.var_searchBy.get() == "Roll No": 
            my_cursor.execute("select * from student where roll = "+ str(self.var_searchId.get()))
        elif self.var_searchBy.get() == "Name":
            my_cursor.execute("select * from student where Name like '%"+ str(self.var_searchId.get())+"%'")
        elif self.var_searchBy.get() == "Email":
            my_cursor.execute("select * from student where email like '%"+ str(self.var_searchId.get())+"%'")
        elif self.var_searchBy.get() == "Phone":
            my_cursor.execute("select * from student where phone = "+ str(self.var_searchId.get()))
        else:
             my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
            print(data)
            self.student_table.insert("",END,values=i)
        conn.commit()
        conn.close()





    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host=self.myhost,username=self.myusername,password=self.mypassword,database=self.mydatabase)
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s, Email=%s, Phone = %s, PhotoSample=%s, Teacher =%s ,Semester =%s where id = %s",(
                        self.var_dep.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_radio1.get(),
                        self.var_teacher.get(),
                        self.var_semester.get(),
                        self.var_id.get()

                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("success","Student Detail successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete","Do you want to Delete this student's record ?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host=self.myhost,username=self.myusername,password=self.mypassword,database=self.mydatabase)
                    my_cursor=conn.cursor()
                    sql = "delete from student where id = %s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                messagebox.showinfo("success","Student Detail Deleted successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)


    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")                    

                    
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host=self.myhost,username=self.myusername,password=self.mypassword,database=self.mydatabase)
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update student set Department=%s, Email=%s, Phone = %s, PhotoSample=%s, Teacher =%s ,Semester =%s ,Name = %s, Gender=%s, DOB=%s,Address=%s,Roll=%s,Division=%s where id = %s",(
                                                                                                                                        self.var_dep.get(),
                                                                                                                                        self.var_email.get(),
                                                                                                                                        self.var_phone.get(),
                                                                                                                                        self.var_radio1.get(),
                                                                                                                                        self.var_teacher.get(),
                                                                                                                                        self.var_semester.get(),
                                                                                                                                        self.var_name.get(),
                                                                                                                                        self.var_gender.get(),
                                                                                                                                        self.var_dob.get(),
                                                                                                                                        self.var_address.get(),
                                                                                                                                        self.var_roll.get(),
                                                                                                                                        self.var_div.get(),
                                                                                                                                        self.var_id.get()

                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()



                #LOAD
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum neighbour=5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                ids = self.var_id.get()
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(ids)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id) ==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating datasets completed!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)



                






if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()