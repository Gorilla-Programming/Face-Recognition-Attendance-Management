from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow 
from tkinter import messagebox 
import mysql.connector
from register import Register

    

class Login_Window:

    flag = 0
    user = "Student"
    
    myhost="localhost"
    myusername="root"
    mypassword="admin"
    mydatabase="face_recognizer"
    

    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+00+0")

        self.var_email=StringVar()
        self.var_pass=StringVar()

        #self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\Desktop\login_form\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1") 
        #lbl_bg=Label(self.root,image=self.bg)
        #lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        #background Image
        bgimg=Image.open(r"assets\Images\college_images\logibgbg.png")
        bgimg = bgimg.resize((1530,790),Image.LANCZOS)
        self.bgimg1 = ImageTk.PhotoImage(bgimg)

        bgimg_label=Label(self.root,image=self.bgimg1)
        bgimg_label.place(x=0,y=0,width=1530,height=790)
        
        #Frame
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=150,width=340,height=500)
        
        
        img1=Image.open(r"assets\Images\college_images\LoginIconAppl.png") 
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0) 
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started", font=("times new roman",20,"bold"),fg="white",bg="black") 
        get_str.place(x=95,y=130)

        #Label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black") 
        username.place(x=70,y=175)
        
        self.txtuser=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold")) 
        self.txtuser.place(x=40,y=200, width=270)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black") 
        password.place(x=70,y=245)

        self.txtpass=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"), show='*') 
        self.txtpass.place(x=40,y=270,width=270)

    #======Icon Images============
        
        img2=Image.open(r"assets\Images\college_images\LoginIconAppl.png") 
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0) 
        lblimg1.place(x=650,y=323,width=25,height=25)

        
        img3=Image.open(r"assets\Images\college_images\lock-512.png")
        img3=img3.resize((25,25),Image.LANCZOS) 
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0) 
        lblimg1.place(x=650,y=395,width=25,height=25)

    # LoginButton 
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red") 
        loginbtn.place(x=110,y=320,width=120,height=35)

    # registerbutton

        registerbtn=Button(frame,command=self.register_window,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black") 
        registerbtn.place(x=15,y=370,width=160)




    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fiels required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Sucess","welcome")
        else:
            conn=mysql.connector.connect(host=self.myhost,username=self.myusername,password=self.mypassword,database=self.mydatabase)
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.var_email.get(),
                self.var_pass.get()

            ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                #open_main=messagebox.askyesno("YesNo","Access only admin")
                #if open_main>0:
                    #self.new_window=Toplevel(self.new_window)
                self.flag=1
                my_cursor.execute("select USERTYPE from register where email=%s and password=%s",(self.var_email.get(),self.var_pass.get()))
                row=my_cursor.fetchone()
                self.user=row[0]
                print("before return ",self.flag)
                self.root.destroy()

            






if __name__== "__main__":
    win=Tk()
    app=Login_Window(win)
    win.mainloop()