from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
from dashboard import *



def start(root):
    root.title("phrama")
    root.geometry("1550x800+0+0") 
    #root=Tk()
#def __init__( self , root ):
#self.root=root
    #root.title("Login System")
    #root.geometry("1550x800+0+0")
        
    img1=Image.open("wl.jpg")
    img1=img1.resize((1550,800),Image.ANTIALIAS)
    Photoimg1=ImageTk.PhotoImage(img1)

    lbl_img1=Label(root,image=Photoimg1)
    lbl_img1.place(x=0,y=103,width=1550,height=800)

    lbltitle=Label(root,text="PHARMACY MANAGEMENT SYSTEM",bd=10,relief=RIDGE,fg='red',bg="white",
    font=("times new roman",50,"bold"),padx=2,pady=4)
    lbltitle.pack(side=TOP,fill=X)


    img2=Image.open("log2.png")
    img2=img2.resize((750,500),Image.ANTIALIAS)
    Photoimg2=ImageTk.PhotoImage(img2)
    lbl_img2=Label(root,image=Photoimg2)
    lbl_img2.place(x=400,y=200,width=750,height=500)

    Label(root,text="Username",font=("Arial", 15),bg="lightblue").place(x=606,y=470)
    Label(root,text="Password",font=("Arial", 15),bg="lightblue").place(x=606,y=520)


    e1=Entry(root,font=("Arial", 15),bd=0)
    e1.place(x=750,y=470)

    e2=Entry(root,font=("Arial", 15),bd=0)
    e2.place(x=750,y=520)
    e2.config(show="*")

    Button(root,text="Login",command=loginpage,height=1,width=10,font=("Arial", 15),bg="lightblue").place(x=720,y=560)
    Button(root,text="Next",width=20,command=lambda : change(root)).place(x=820,y=660)

def loginpage():
    uname=e1.get()
    password=e2.get()

    if(uname=="" and password==""):
            messagebox.showinfo("","Blank not allowed")
    
    elif(uname=="Admin" and password=="Admin@123"):
            messagebox.showinfo("","Login Successful")
            root.destroy()

    else:
            messagebox.showinfo("","Invalid login credentials")


def change(root):
    root.destroy()
    fun()
def call():
    root=Tk()
    start(root)
    root.mainloop()
call()
    
