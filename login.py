from tkinter import*;
from tkinter import messagebox
from tkinter import ttk;
from PIL import Image,ImageTk
import random;
import time;
import datetime;
import mysql.connector
def main():
      root=Tk()
      app=Window1(root)


class Window1:
    def __init__(self, root):
        self.root=root
        self.root.title("Online Medical Store")
        self.root.geometry("1550x800+0+0")
        #self.root.config(bg="powder blue")
        #self.frame=Frame(self.root,bg="sky blue")
        #self.frame.pack()
        self.Username = StringVar()
        self.Password = StringVar()

        img2=Image.open("wl.png")
        img2=img2.resize((1550,800),Image.ANTIALIAS)
        self.Photoimg2=ImageTk.PhotoImage(img2)

        lbl_img2=Label(self.root,image=self.Photoimg2)
        lbl_img2.place(x=0,y=0,width=1550,height=800)

        
        lbltitle=Label(self.root,text=" Welcome To Admin Login",bd=8,relief=RIDGE,fg='red',bg="white",
                        font=("times new roman",35,"bold"),padx=2,pady=4)
        lbltitle.place(x=100,y=0,width=1330,height=100)



        self.Loginframe1=LabelFrame(self.root, width=1350,height=600,bd=15,relief="ridge",bg="sky blue")

        self.Loginframe1.place(x=480,y=150,width=560,height=190)

        self.Loginframe2=LabelFrame(self.root, width=1000,height=600,bd=15,relief="ridge",bg="sky blue")

        self.Loginframe2.place(x=300,y=380,width=970,height=90)

        self.LoginFrame3=Frame(self.root, width=1010,height=400,bd=15,relief="ridge",bg="sky blue")
        self.LoginFrame3.place(x=600,y=500,width=310,height=87)

        
        


       
        
        #load1=Image.open('Loginlbl.png')
        #render=ImageTk.PhotoImage(load1)
        #img1= Label (self.master, image = render,bd=0,bg="lightblue")
        #img.place (x = 300, y = 200)


        
        
        #==================================Lable And entry=========================================
        self.lblUsername=Label(self.Loginframe1,text="Username",font=('arial',20,'bold'),bd=22,bg="sky blue",fg="Cornsilk")
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername=Entry(self.Loginframe1,font=('arial',20,'bold'),textvariable=self.Username)
        self.txtUsername.grid(row=0,column=1)

        self.lblPassword=Label(self.Loginframe1,text="Password",font=('arial',20,'bold'),bd=22,bg="sky blue",fg="Cornsilk")
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword=Entry(self.Loginframe1,font=('arial',20,'bold'),show="*",textvariable=self.Password)
        self.txtPassword.grid(row=1,column=1)

        #self.lblUsername=Label(root,text="Username",font=("Arial", 15),bg="lightblue").place(x=606,y=470)
        #self.txtUsername=Entry(root,font=("Arial", 15),bd=0,textvariable=self.Username,)
        #self.txtUsername.place(x=750,y=470)
        #self.lblPassword=Label(root,text="Password",font=("Arial", 15),bg="lightblue").place(x=606,y=520)
        #self.lblPassword=Entry(root,font=("Arial", 15),bd=0,textvariable=self.Password)
        #self.lblPassword.place(x=750,y=520)
        #self.lblPassword.config(show="*")
   


        
        #===================================Buttons========================================
        #self.btnLogin =Button(root,text="Login",command=self.Login_System,height=1,width=10,font=("Arial", 15),bg="lightblue").place(x=720,y=560)
        
        self.btnLogin = Button(self.Loginframe2, text="Login",width=17,font=('arial',20,'bold'),
                                         command=self.Login_System ,pady=2,padx=8)
        self.btnLogin.grid(row=3, column=0)

        self.btnReset = Button(self.Loginframe2, text="Reset",width=17,font=('arial',20,'bold'),
                                           command=self.Reset,pady=2,padx=8)
        self.btnReset.grid(row=3, column=1)

        self.btnExit = Button(self.Loginframe2, text="Exit",width=17,font=('arial',20,'bold'),
                                           command=self.iExit,pady=2,padx=8)
        self.btnExit.grid(row=3, column=2)


        #self.btnUserRegistration=Button(self.LoginFrame3, text="User Registration",
                                        #state=DISABLED,command=self.User_Registration_Window,font=('arial',20,'bold'))
        #self.btnUserRegistration.grid(row=0, column=1)

        self.btnAdminRegistration=Button(self.LoginFrame3, text="Admin Registration",
                                        state=DISABLED,command=self.Admin_Registration_Window,font=('arial',20,'bold'))
        self.btnAdminRegistration.grid(row=0, column=1)

        #===================================Buttons========================================

    def Login_System(self):
        user=(self.Username.get())
        pas=(self.Password.get())
        if(user==str(1234) and pas==str(2345)):
           #self.btnUserRegistration.config(state=NORMAL)
           self.btnAdminRegistration.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("Login System","too Bad,Invaild login detail")
            #self.btnUserRegistration.config(state=DISABLED)
            self.btnAdminRegistration.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

        
       
    def Reset(self):
         self.Username.set("")
         self.Password.set("")
         self.txtUsername.focus()
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Login System","confirm if you want to exit")
        if self.iExit>0:
            self.root.destroy()
        else:
            comand=self.new_window
            return
            
    #def Admin_Registration_Window(self):
        #self.newWindow = Toplevel(self.root)
        #self.app = Window3(self.newWindow)


   # def User_Registration_Window(self):
        #self.newWindow = Toplevel(self.root)
        #self.app = Window4(self.newWindow)

if __name__ == "__main__":
    main()

        

