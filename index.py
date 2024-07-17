from tkinter import*
from register import Register
from login import Login_Window
from home import Face_Recognition_System

def login():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
    print("after return", app.flag)
    if app.flag==1:
       app.flag=0
       home(app.user)
    

def reg():
    win=Tk()
    app=Register(win)
    win.mainloop()

def home(user):
    win=Tk()
    print(user)
    app=Face_Recognition_System(win,user)
    win.mainloop()


if __name__== "__main__":
    login()

