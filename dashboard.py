from tkinter import*
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
#from phrama import *
#from billing import *
#from loginpage import *


class Dashboard:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy System")
        self.root.geometry("1550x800+0+0")


        img1=Image.open("logo.jpg")
        img1=img1.resize((90,75),Image.ANTIALIAS)
        self.Photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.Photoimg1,borderwidth=0)
        b1.place(x=70,y=20)

        img2=Image.open("bg2.png")
        img2=img2.resize((1550,800),Image.ANTIALIAS)
        self.Photoimg2=ImageTk.PhotoImage(img2)

        lbl_img2=Label(self.root,image=self.Photoimg2)
        lbl_img2.place(x=0,y=0,width=1550,height=800)

        
        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,fg='red',bg="white",
        font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)

        
        #img2=Image.open("bg2.png")
        #img2=img2.resize((1550,700),Image.ANTIALIAS)
        #self.Photoimg2=ImageTk.PhotoImage(img2)
        #b1=Button(self.root,image=self.Photoimg2,borderwidth=0)
        #b1.place(x=0,y=115)

        img3=Image.open("button1.png")
        img3=img3.resize((150,135),Image.ANTIALIAS)
        self.Photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.Photoimg3,borderwidth=0)
        b1.place(x=100,y=150)
       # def parma():
            

        img4=Image.open("button2.png")
        img4=img4.resize((150,135),Image.ANTIALIAS)
        self.Photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.Photoimg4,borderwidth=0)
        b1.place(x=100,y=350)

        img5=Image.open("button3.png")
        img5=img5.resize((150,135),Image.ANTIALIAS)
        self.Photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.Photoimg5,borderwidth=0)
        b1.place(x=100,y=550)

        img6=Image.open("final3.png")
        img6=img6.resize((1000,600),Image.ANTIALIAS)
        self.Photoimg6=ImageTk.PhotoImage(img6)
        
        lbl_img6=Label(self.root,image=self.Photoimg6)
        lbl_img6.place(x=400,y=150,width=1000,height=600)





if __name__== "__main__":
    root=Tk()
    obj=Dashboard(root)
    root.mainloop()
    
