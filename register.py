from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow 
from tkinter import messagebox 
import mysql.connector

class Register:
    
    myhost="localhost"
    myusername="root"
    mypassword="admin"
    mydatabase="face_recognizer"

    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+00+0")


        #background Image
        bgimg=Image.open(r"assets\Images\college_images\logibgbg.png")
        bgimg = bgimg.resize((1530,790),Image.LANCZOS)
        self.bgimg1 = ImageTk.PhotoImage(bgimg)

        bgimg_label=Label(self.root,image=self.bgimg1)
        bgimg_label.place(x=0,y=0,width=1530,height=790)

#===========variables================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_userType=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_dep=StringVar()


#=============bg inage=================
        #self.bg=ImageTk.PhotoImage(file=r"assets\Images\college_images\studentbg.png")
        #bg_lbl=Label(self.root,image=self.bg)
        #bg_lbl.place(x=0, y=0,relwidth=1,relheight=1)



#=============left image=================
        self.bg1=ImageTk.PhotoImage(file=r"assets\Images\college_images\face_detector1.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=150, y=100,width=470,height=550)

#=============main frame=================    

        frame=Frame(self.root,bg="white")
        frame.place(x=620,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen", bg="white")
        register_lbl.place(x=20,y=20)

#=============label and entry=======

    ############# row 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black") 
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman",15)) 
        self.txt_lname.place(x=370,y=130, width=250)

    ##########-row2

        contact=Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black") 
        contact.place(x=50,y=178)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15)) 
        self.txt_contact.place(x=50,y=200, width=250)

        email=Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black") 
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15)) 
        self.txt_email.place(x=370,y=200,width=250)

    ########## - row 3

        userType=Label(frame,text="Select User Type",font=("times new roman", 15, "bold"), bg="white", fg="black")
        userType.place(x=50,y=240)

        self.combo_userType=ttk.Combobox(frame,textvariable=self.var_userType,font=("times new roman", 15, "bold"),state="readonly")
        self.combo_userType["values"]=("Select","Faculty","Administrator" )
        self.combo_userType.place(x=50,y=270,width=250)
        self.combo_userType.current(0)

        dep=Label(frame, text="Department", font=("times new roman", 15, "bold"), bg="white", fg="black") 
        dep.place(x=370,y=248)

        self.txt_dep=ttk.Entry(frame, textvariable=self.var_dep,font=("times new roman",15)) 
        self.txt_dep.place(x=370,y=270,width=250)


    ########## - row 4

        pswd=Label(frame,text="Password",font=("times new roman", 15, "bold"), bg="white", fg="black") 
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman", 15), show='*')
        self.txt_pswd.place(x=50,y=348, width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman", 15, "bold"), bg="white", fg="black") 
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15), show='*') 
        self.txt_confirm_pswd.place(x=370,y=340,width=250)


    ########### chewck button ###########3
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms And Condition",font=("times new roman", 12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

    
    ########### button ###########3
        img=Image.open(r"assets\Images\college_images\register-now-button1.jpg")
        img=img.resize((200,55),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data, borderwidth=0,cursor="hand2",font=("times new roman", 15, "bold"), fg="white")
        b1.place(x=10,y=420,width=200)
        
        
        img1=Image.open(r"assets\Images\college_images\loginpng.png")
        img1=img1.resize((200,45),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1, command=self.moveToLogin,borderwidth=0,cursor="hand2",font=("times new roman", 15, "bold"),fg="white")
        b1.place(x=330,y=420, width=200) 

    ###########function declaration #############
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()==""  or self.var_userType.get()=="Select": 
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error", "password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error", "Plaese agree our terms ane condition")
        else:
            conn=mysql.connector.connect(host=self.myhost,username=self.myusername,password=self.mypassword,database=self.mydatabase)
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error", "User already exist, plaese try another email")
            else:
                my_cursor.execute("insert into register values (%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_pass.get(),
                    self.var_userType.get(),
                    self.var_dep.get()
                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sucess","Register Successfully")

    def moveToLogin(self):
        self.root.destroy()

if __name__== "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()