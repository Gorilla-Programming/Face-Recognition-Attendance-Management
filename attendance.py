from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import os
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog
from tkinter import messagebox


class Attendance:

    myhost="localhost"
    myusername="root"
    mypassword="admin"
    mydatabase="face_recognizer"

    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
    
        #background Image
        bgimg=Image.open(r"assets\Images\college_images\studentbg.png")
        bgimg = bgimg.resize((1530,790),Image.LANCZOS)
        self.bgimg1 = ImageTk.PhotoImage(bgimg)

        bg_img=Label(self.root,image=self.bgimg1)
        bg_img.place(x=0,y=0,width=1530,height=790)

         

        main_frame=Frame(bg_img, bd=2, bg="white") 
        main_frame.place(x=10,y=160, width=1500,height=630)

        #left side frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details ",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=600)

        img_left=Image.open(r"assets\Images\college_images\attendanceManagement.png") 
        img_left=img_left.resize((720,220), Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=710,height=220)


        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white") 
        left_inside_frame.place(x=0,y=225, width=720,height=350)

        #Labels and Entry
         
        #Attendance id
        attendanceId_label=Label(left_inside_frame,text="Attendance Id:",font=("times new roman",12,"bold"))
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"),state="readonly")
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Name
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"))
        name_label.grid(row=0,column=2,padx=4,pady=8)

        name_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"),state="readonly")
        name_entry.grid(row=0,column=3,pady=8)

        #Roll
        roll_label=Label(left_inside_frame,text="Roll Number:",font=("times new roman",12,"bold"))
        roll_label.grid(row=1,column=0,padx=4,pady=8)

        roll_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"),state="readonly")
        roll_entry.grid(row=1,column=1,pady=8)

        #Date
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"))
        date_label.grid(row=1,column=2,padx=4,pady=8)

        date_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"),state="readonly")
        date_entry.grid(row=1,column=3,pady=8)

        #Department
        department_label=Label(left_inside_frame,text=" Department:",font=("times new roman",12,"bold"))
        department_label.grid(row=2,column=0,padx=4,pady=8)

        department_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"),state="readonly")
        department_entry.grid(row=2,column=1,pady=8)

        #Time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"))
        time_label.grid(row=2,column=2,padx=4,pady=8)

        time_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"),state="readonly")
        time_entry.grid(row=2,column=3,pady=8)


        #Attendance
        attLabel = Label(left_inside_frame,text="Attendace Status",bg="white",font="cosmicsansns 11 bold")
        attLabel.grid(row=3,column=0)

        self.attStatus=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="cosmicsansns 11 bold",state="readonly")
        self.attStatus["values"]=("Status","Present","Absent")
        self.attStatus.grid(row=3,column=1,pady=8)
        self.attStatus.current(0)




        #button Frame


        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=300,width=700,height=35)


        save_btn= Button(btn_frame,text="Export CSV",command=self.exportCsv,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        save_btn.grid(row=0,column=0)

        update_btn= Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        update_btn.grid(row=0,column=1)

        delete_btn= Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        delete_btn.grid(row=0,column=2)

        reset_btn= Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        reset_btn.grid(row=0,column=3)

     
        #Right Frame
        Right_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)


        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.attendanceReportTable=ttk.Treeview(table_frame,column=("Id","Roll Number","Name","Department","Date","Time","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)

        self.attendanceReportTable.heading("Id",text="Id")
        self.attendanceReportTable.heading("Roll Number",text="Roll Number")
        self.attendanceReportTable.heading("Name",text="Name")
        self.attendanceReportTable.heading("Department",text="Department")
        self.attendanceReportTable.heading("Date",text="Date")
        self.attendanceReportTable.heading("Time",text="Time")
        self.attendanceReportTable.heading("Attendance",text="Attendance")

        self.attendanceReportTable["show"]="headings"

        self.attendanceReportTable.pack(fill=BOTH,expand=1)

        self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data_from_database()




    #======================fetchData===========================


    def fetch_data_from_database(self):
        conn=mysql.connector.connect(host=self.myhost,username=self.myusername,password=self.mypassword,database=self.mydatabase)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from attendance")
        data=my_cursor.fetchall()

        if len(data)!= 0:
            self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
            for i in data:
                #print(data)
                self.attendanceReportTable.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Export csv
    def exportCsv(self):
        try:
            connection=mysql.connector.connect(host=self.myhost,username=self.myusername,password=self.mypassword,database=self.mydatabase)
            cursor = connection.cursor()
            sql_query = "SELECT * FROM attendance"
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([i[0] for i in cursor.description])
                csv_writer.writerows(rows)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        cursor.close()
        connection.close()

    def get_cursor(self, event=""):
        cursor_row=self.attendanceReportTable.focus()
        content=self.attendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_time.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    #============================Reset data============================

    def reset_data(self):
        self.var_atten_attendance.set("Status")
        self.var_atten_date.set("")
        self.var_atten_time.set("")
        self.var_atten_dep.set("")
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_atten_id.set("")

    #==========================Update Data===============================

    def update_data(self):
        if self.var_atten_attendance.get() == "Status" or self.var_atten_date.get() == "" or self.var_atten_time.get() == "" or self.var_atten_dep.get() == "" or self.var_atten_name.get() == "" or self.var_atten_roll.get() == "" or self.var_atten_id.get() == "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update attendance details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host=self.myhost,username=self.myusername,password=self.mypassword,database=self.mydatabase)
                    my_cursor=conn.cursor()
                    my_cursor.execute("update attendance set attendance=%s where id = %s",(
                        self.var_atten_attendance.get(),
                        self.var_atten_id.get()

                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("success","Student Detail successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data_from_database()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    #==============================Delete Data============================================================
    def delete_data(self):
        if self.var_atten_id.get()=="" or self.var_atten_date.get()=="":
            messagebox.showerror("Error","Please select the record to delete",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete","Do you want to Delete this attendance record ?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host=self.myhost,username=self.myusername,password=self.mypassword,database=self.mydatabase)
                    my_cursor=conn.cursor()
                    sql = "delete from attendance where id = %s and dateOfPresent = %s"
                    val=(self.var_atten_id.get(),self.var_atten_date.get())
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                messagebox.showinfo("success","Attendance Detail Deleted successfully",parent=self.root)
                conn.commit()
                self.fetch_data_from_database()
                self.reset_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)




    




        




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()        