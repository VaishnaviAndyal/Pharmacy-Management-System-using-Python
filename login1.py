from tkinter import*;
import tkinter.messagebox
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
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="powder blue")
        self.frame=Frame(self.root,bg="sky blue")
        self.frame.pack()
        self.Username = StringVar()
        self.Password = StringVar()
        

       
        self.LabelTitle =Label(self.frame,text="Online Medical Store", font=('arial',50,'bold'),bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        #load1=Image.open('Loginlbl.png')
        #render=ImageTk.PhotoImage(load1)
        #img1= Label (self.master, image = render,bd=0,bg="lightblue")
        #img.place (x = 300, y = 200)


        self.Loginframe1=LabelFrame(self.frame, width=1350,height=600,bd=20,relief="ridge",bg="cadet blue")

        self.Loginframe1.grid(row=1,column=0)


        self.Loginframe2=LabelFrame(self.frame, width=1000,height=600,bd=20,relief="ridge",bg="cadet blue")

        self.Loginframe2.grid(row=2,column=0)

        self.LoginFrame3=Frame(self.frame, width=1010,height=400,bd=20,relief="ridge")
        self.LoginFrame3.grid(row=3,column=0,pady=2)

        
        
        #==================================Lable And entry=========================================
        self.lblUsername=Label(self.Loginframe1,text="Username",font=('arial',20,'bold'),bd=22,bg="cadet blue",fg="Cornsilk")
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername=Entry(self.Loginframe1,font=('arial',20,'bold'),textvariable=self.Username)
        self.txtUsername.grid(row=0,column=1)

        self.lblPassword=Label(self.Loginframe1,text="Password",font=('arial',20,'bold'),bd=22,bg="cadet blue",fg="Cornsilk")
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword=Entry(self.Loginframe1,font=('arial',20,'bold'),show="*",textvariable=self.Password)
        self.txtPassword.grid(row=1,column=1)


        
        #===================================Buttons========================================
        self.btnLogin = Button(self.Loginframe2, text="Login",width=17,font=('arial',20,'bold'),
                                         command=self.Login_System ,pady=2,padx=8)
        self.btnLogin.grid(row=3, column=0)

        self.btnReset = Button(self.Loginframe2, text="Reset",width=17,font=('arial',20,'bold'),
                                           command=self.Reset,pady=2,padx=8)
        self.btnReset.grid(row=3, column=1)

        self.btnExit = Button(self.Loginframe2, text="Exit",width=17,font=('arial',20,'bold'),
                                           command=self.iExit,pady=2,padx=8)
        self.btnExit.grid(row=3, column=2)


        self.btnUserRegistration=Button(self.LoginFrame3, text="User Registration",
                                        state=DISABLED,command=self.User_Registration_Window,font=('arial',20,'bold'))
        self.btnUserRegistration.grid(row=0, column=0)

        self.btnAdminRegistration=Button(self.LoginFrame3, text="Admin Registration",
                                        state=DISABLED,command=self.Admin_Registration_Window,font=('arial',20,'bold'))
        self.btnAdminRegistration.grid(row=0, column=1)

        #===================================Buttons========================================

    def Login_System(self):
        user=(self.Username.get())
        pas=(self.Password.get())
        if(user==str(1234) and pas==str(2345)):
           self.btnUserRegistration.config(state=NORMAL)
           self.btnAdminRegistration.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("Login System","too Bad,Invaild login detail")
            self.btnUserRegistration.config(state=DISABLED)
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
            
    def User_Registration_Window(self):
        self.newWindow = Toplevel(self.root)
        self.app = Window2(self.newWindow)


    def Admin_Registration_Window(self):
        self.newWindow = Toplevel(self.root)
        self.app = Window3(self.newWindow)
        



class Window2:
    def __init__(self, root):
        self.root=root
        self.root.title("User Registration")
        self.root.geometry("1550x800+0+0")
        self.frame=Frame(self.root)
        self.frame.pack()
        #===================================================================================
      #=========================AddMed Variable=========================
        self.addmed_var =StringVar()
        self.refMed_var =StringVar()

        #=========================main variable============================
        self.ref_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medname_var=StringVar()
        self.lot_var=StringVar()
        self.issuedata_var=StringVar()
        self.uses_var=StringVar()
        self.expdata_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()
        
        
        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,fg='red',bg="white",
        font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("logo.jpg")
        img1=img1.resize((90,75),Image.ANTIALIAS)
        self.Photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.Photoimg1,borderwidth=0)
        b1.place(x=70,y=20)
        #============================================================DataFrame======================================================
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20,)#bg="green")
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg='darkgreen',font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
       # DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",fg='darkgreen',font=("arial",12,"bold"))
       # DataFrameRight.place(x=910,y=5,width=550,height=350)
        #============================================================ButtonFrame======================================================
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)
        #============================================================Main Button======================================================
        btnAddData=Button(ButtonFrame, command=self.add_data,text="Medicine Add",font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)

        btnUpdatMed=Button(ButtonFrame,command=self.Update,text="UPDATE",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnUpdatMed.grid(row=0,column=1)

        btnDeleteMed=Button(ButtonFrame,command=self.delete,text="DELETE",font=("arial",13,"bold"),width=14,bg="red",fg="white")
        btnDeleteMed.grid(row=0,column=2)

        btnResetMed=Button(ButtonFrame,command=self.reset,text="RESET",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnResetMed.grid(row=0,column=3)

        btnExitMed=Button(ButtonFrame,text="EXIT",font=("arial",13,"bold"),width=14,bg="red",fg="white")
        btnExitMed.grid(row=0,column=4)
        #============================================================Search By======================================================
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)
        
        #variables
        self.search_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",17,"bold"),state="readonly")
        search_combo["values"]=("Ref_no","medname","Lot")
        search_combo.grid(row=0,column=6)
        #search_combo.current(0)

        self.searchTxt_var=StringVar()
        txtsearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtsearch.grid(row=0,column=7)

        searchBtn=Button(ButtonFrame,command=self.search_data,text="SEARCH",font=("arial",13,"bold"),width=13,bg="darkgreen",fg="white")
        searchBtn.grid(row=0,column=8)

        showAll=Button(ButtonFrame,command=self.fetch_data,text="SHOW ALL",font=("arial",13,"bold"),width=13,bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)
        #=====================================================label and entry=======================================
        Framedeatils=Frame(self.root,bd=15,padx=20,relief=RIDGE)
        Framedeatils.place(x=0,y=590,width=1530,height=210)

        conn=mysql.connector.connect(host="localhost",username="root",passwd="Vaishnavi@123",database="mydata",port=3306)
        my_cursor=conn.cursor()
        my_cursor.execute("select Ref from pharma")
        r=my_cursor.fetchall()

        lblrefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No :",padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)
        
        comrefno=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,width=20,font=("arial",12,"bold"),state="readonly")
        comrefno["values"]=r
        comrefno.current(0)
        comrefno.grid(row=0,column=1)

        lblCompanyName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name :",padx=2,pady=6)
        lblCompanyName.grid(row=1,column=0,sticky=W)
        txtCompanyName=Entry(DataFrameLeft,textvariable=self.cmpName_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=22)
        txtCompanyName.grid(row=1,column=1)

        lblTypeofMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type of Medicine :",padx=2,pady=6)
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)

        comTypeofMedicine_combo=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,width=20,font=("arial",12,"bold"),)
        comTypeofMedicine_combo["values"]=("Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhales","Injection")
        comTypeofMedicine_combo.current(0)
        comTypeofMedicine_combo.grid(row=2,column=1)
        #==============================================AddMedicine===========================================
        conn=mysql.connector.connect(host="localhost",username="root",passwd="Vaishnavi@123",database="mydata",port=3306)
        my_cursor=conn.cursor()
        my_cursor.execute("select MedName from pharma")
        med=my_cursor.fetchall()

        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name :",padx=2,pady=4)
        lblMedicineName.grid(row=3,column=0,sticky=W)
        comMedicineName_combo=ttk.Combobox(DataFrameLeft,textvariable=self.medname_var,width=20,font=("arial",12,"bold"),state="readonly")
        comMedicineName_combo["values"]=med
        comMedicineName_combo.current(0)
        comMedicineName_combo.grid(row=3,column=1)

        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No :",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=22)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date :",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedata_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=22)
        txtIssueDate.grid(row=5,column=1)

        lblExdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date :",padx=2,pady=6)
        lblExdate.grid(row=6,column=0,sticky=W)
        txtExdate=Entry(DataFrameLeft,textvariable=self.expdata_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=22)
        txtExdate.grid(row=6,column=1)

        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses :",padx=2,pady=6)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=22)
        txtUses.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect :",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=22)
        txtSideEffect.grid(row=8,column=1)

        lblPrecWarning=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prec&Warning : ",padx=15,pady=6)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        txtPrecWarning=Entry(DataFrameLeft,textvariable=self.warning_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=22)
        txtPrecWarning.grid(row=0,column=3)

        lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage :",padx=15,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=22)
        txtDosage.grid(row=1,column=3)

        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Price : ",padx=15,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=22)
        txtPrice.grid(row=2,column=3)

        lblProductQt=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product&Qt : ",padx=15,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt=Entry(DataFrameLeft,textvariable=self.product_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=22)
        txtProductQt.grid(row=3,column=3)

        #===============================================images====================================================
        lblhome=Label(DataFrameLeft,font=("arial",15,"bold"),text="Stay Home Stay Safe",padx=15,pady=6,bg="white",fg="red",width=30)
        lblhome.place(x=410,y=140)

        """img2=Image.open("tab.jpg")
        img2=img2.resize((150,135),Image.ANTIALIAS)
        Self.Photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(Self.root,image=Self.Photoimg2,borderwidth=0)
        b1.place(x=750,y=330)"""

        img3=Image.open("eng.jpg")
        img3=img3.resize((350,135),Image.ANTIALIAS)
        self.Photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.Photoimg3,borderwidth=0)
        b1.place(x=495,y=345)

        """img4=Image.open("lab.jpg")
        img4=img4.resize((150,135),Image.ANTIALIAS)
        Self.Photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(Self.root,image=Self.Photoimg4,borderwidth=0)
        b1.place(x=475,y=330)"""

        #===================================DataFrameRight=================================
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",fg='darkgreen',font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=550,height=350)
        
        img5=Image.open("tab.jpg")
        img5=img5.resize((200,75),Image.ANTIALIAS)
        self.Photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.Photoimg5,borderwidth=0)
        b1.place(x=960,y=160)

        img6=Image.open("tablet.jpg")
        img6=img6.resize((200,75),Image.ANTIALIAS)
        self.Photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(self.root,image=self.Photoimg6,borderwidth=0)
        b1.place(x=1160,y=160)

        img7=Image.open("tab1.jpg")
        img7=img7.resize((200,145),Image.ANTIALIAS)
        self.Photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(self.root,image=self.Photoimg7,borderwidth=0)
        b1.place(x=1270,y=160)

        lblrefno=Label(DataFrameRight,font=("arial",12,"bold"),text="Reference No : ")
        lblrefno.place(x=0,y=80)
        txtrefno=Entry(DataFrameRight,textvariable=self.refMed_var,font=("arial",15,"bold"),bg="white",bd=2,relief=RIDGE,width=14)
        txtrefno.place(x=135,y=80)

        lblmedName=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Name : ")
        lblmedName.place(x=0,y=110)
        txtmedName=Entry(DataFrameRight,textvariable=self.addmed_var,font=("arial",15,"bold"),bg="white",bd=2,relief=RIDGE,width=14)
        txtmedName.place(x=135,y=110)

        #=====================================side Frame=========================================================
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=290,height=160)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)

        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)


        #=================================================Medicine Add Button====================================
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="yellow")
        down_frame.place(x=330,y=150,width=135,height=160)

        btnAddmed=Button(down_frame, command=self.AddMed,text="Add",font=("arial",12,"bold"),width=12,bg="purple",fg="white",pady=4,)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame, command=self.UpdateMed,text="UPDATE ",font=("arial",12,"bold"),width=12,bg="green",fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,command=self.DeleteMed,text="DELETE",font=("arial",12,"bold"),width=12,bg="red",fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)

        btnClearmed=Button(down_frame,command=self.ClearMed,text="CLEAR",font=("arial",12,"bold"),width=12,bg="orange",fg="white",pady=4)
        btnClearmed.grid(row=3,column=0)

        #==================================================Frame Details===================================================
        Framedeatils=Frame(self.root,bd=15,relief=RIDGE)
        Framedeatils.place(x=0,y=580,width=1530,height=210)

        #==================================================Main Table & Scrollbar============================================

        Table_frame=Frame(Framedeatils,bd=15,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=1,width=1500,height=180)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame,column=("reg","companyname","type","tabletname","lotno","issuedate","expdate","uses","sideeffect","warning","dosage","price","productqt"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("reg",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product Qt")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)


        #====================================================Add Medicine Functionality Declaration==================================

    def AddMed(self):
           conn=mysql.connector.connect(host="localhost",username="root",passwd="Vaishnavi@123",database="mydata",port=3306)
           my_cursor=conn.cursor()
           my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(
                                                                                self.refMed_var.get(),
                                                                                self.addmed_var.get()

                                                                            ))
           conn.commit()
           self.fetch_dataMed()
           self.Medget_cursor()
           conn.close()
           messagebox.showinfo("Success","Medicine Added")

    def fetch_dataMed(self): 
        conn=mysql.connector.connect(host="localhost",username="root",passwd="Vaishnavi@123",database="mydata",port=3306)
        my_cursor=conn.cursor()
        my_cursor.execute  ("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                  self.medicine_table.delete(*self.medicine_table.get_children())
                  for i in rows:
                       self.medicine_table.insert("",END,values=i)
                  conn.commit()
        conn.close()

    #============================================MadGetcursor==============
    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row) 
        row=content["values"]
        self.refMed_var.set(row[0])
        self.addmed_var.set(row[1])    

    def UpdateMed(self):
        if self.refMed_var.get()=="" or self.addmed_var.get()=="" :  
            messagebox.showerror("Error","All Field are Requried") 
        else:
             conn=mysql.connector.connect(host="localhost",username="root",passwd="Vaishnavi@123",database="mydata",port=3306)
             my_cursor=conn.cursor()
             my_cursor.execute("Update pharma set MedName=%s where Ref=%s",(
                                                                                self.addmed_var.get(),
                                                                                self.refMed_var.get(),
                                                                           ))
             conn.commit()
             self.fetch_dataMed()
             conn.close()

             messagebox.showinfo("Success","Medicine has be updated")
    
    def DeleteMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="Vaishnavi@123",database="mydata",port=3306)
        my_cursor=conn.cursor()

        sql="delete from pharma where Ref=%s"
        val=(self.refMed_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_dataMed()
        conn.close()
        messagebox.showinfo("Success","Medicine has be Deleted")
        
    def ClearMed(self):
        self.refMed_var.set("")
        self.addmed_var.set("")


        #================================================Main table=================================================

    def add_data(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",passwd="Vaishnavi@123",database="mydata",port=3306)
            my_cursor=conn.cursor()
            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.ref_var.get(),
                                                                                                        self.cmpName_var.get(),
                                                                                                        self.typeMed_var.get(),
                                                                                                        self.medname_var.get(),
                                                                                                        self.lot_var.get(),
                                                                                                        self.issuedata_var.get(),
                                                                                                        self.expdata_var.get(),
                                                                                                        self.uses_var.get(),
                                                                                                        self.sideEffect_var.get(),
                                                                                                        self.warning_var.get(),
                                                                                                        self.dosage_var.get(),
                                                                                                        self.price_var.get(),
                                                                                                        self.product_var.get()
                                                                                                    ))
            
            conn.commit()
            self.fetch_data()
            #self.get_cursor()
            conn.close()
            messagebox.showinfo("Success","data has be inserted")

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="Vaishnavi@123",database="mydata",port=3306)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        row=my_cursor.fetchall()
        if len(row)!=0:
                  self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                  for i in row:
                       self.pharmacy_table.insert("",END,values=i)
                  conn.commit()
        conn.close()


    def get_cursor(self,ev=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]
        
        self.ref_var.set(row[0]),
        self.cmpName_var.set(row[1]),
        self.typeMed_var.set(row[2]),   
        self.medname_var.set(row[3]),
        self.lot_var.set(row[4]),
        self.issuedata_var.set(row[5]),
        self.expdata_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideEffect_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.dosage_var.set(row[10]),
        self.price_var.set(row[11]),
        self.product_var.set(row[12])
    def Update(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="" :
            messagebox.showerror("Error","All fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",passwd="Vaishnavi@123",database="mydata",port=3306)
            my_cursor=conn.cursor()
            my_cursor.execute("Update pharmacy set CmpName=%s,TypeMed=%s,LotNo=%s,Issuedate=%s,Expdate=%s,uses=%s,Sideeffect=%s,warning=%s,dosage=%s,Price=%s,product=%s,medname=%s where Ref_no=%s",(      
                                                                                  
                                                                                                                                                                                                                         self.cmpName_var.get(),
                                                                                                                                                                                                                         self.typeMed_var.get(),
                                                                                                                                                                                                                         self.lot_var.get(),
                                                                                                                                                                                                                         self.issuedata_var.get(),
                                                                                                                                                                                                                         self.expdata_var.get(),
                                                                                                                                                                                                                         self.uses_var.get(),
                                                                                                                                                                                                                         self.sideEffect_var.get(),
                                                                                                                                                                                                                         self.warning_var.get(),
                                                                                                                                                                                                                         self.dosage_var.get(),
                                                                                                                                                                                                                         self.price_var.get(),
                                                                                                                                                                                                                         self.product_var.get(),
                                                                                                                                                                                                                         self.medname_var.get(),
                                                                                                                                                                                                                         self.ref_var.get()                                                                                                                     
                                                                                                                                                                                                                         ))                                                                                                           

                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                           
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("UPDATE","Records has be Updated Successfully")  

    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="Vaishnavi@123",database="mydata",port=3306)
        my_cursor=conn.cursor()
        sql="delete from pharmacy where ref_no=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete","Info deleted successfully")

    def reset(self):
        #self.ref_var.get(""),
        self.cmpName_var.set(""),
        #self.typeMed_var.get(""),
        #self.medName_var.get(""),
        self.lot_var.set(""),
        self.issuedata_var.set(""),
        self.expdata_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.warning_var.set(""),
        self.dosage_var.set(r""),
        self.price_var.set(r""),
        self.product_var.set(r"")

    def search_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="Vaishnavi@123",database="mydata",port=3306)
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from pharmacy where"+str(self.search_var.get())+"LIKE %"+str(self.searchTxt_var.get())+"%")
        rows=my_cursor.fatchall()
        if len(rows)!=0:    
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        #===================================================================================

class Window3:
    def __init__(self, root):
        self.root=root
        self.root.title("Admin Registration")
        self.root.geometry("1550x800+0+0")
        self.frame=Frame(self.root)
        self.frame.pack()
        #==================================================================================
        self.c_name_var=StringVar()
        self.c_phon_var=StringVar()
        self.c_mail_var=StringVar()
        self.bill_no_var=StringVar()
        z=random.randint(1000,9999)
        self.bill_no_var.set(z)
        self.search_bill=StringVar()
        self.product=StringVar()
        self.price=StringVar()
        self.Qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        
        
        #product category list
        ta=[]
        li=[]
        cap=[]
        to=[]
        dr=[]
        inh=[]
        inj=[]
        
        self.category=["Select options","Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhales","Injection"]
        #sub category
        conn=mysql.connector.connect(host="localhost",username="root",passwd="Vaishnavi@123",database="mydata",port=3306)
        my_cursor=conn.cursor()
        my_cursor.execute("select TypeMed,Ref_no from pharmacy")
        r=my_cursor.fetchall()
        self.SubCategoryTab=r
        a=0
        for i in r:
            if(i[0]=="Liquid"):
                li.append(i[1])
               
            if(i[0]=="Tablet"):
                ta.append(i[1])
                
            if(i[0]=="Capsules"):
                cap.append(i[1])
                
            if(i[0]=="Topical Medicines"):
                to.append(i[1])
                
            if(i[0]=="Inhales"):
                inh.append(i[1])
                
            if(i[0]=="Drops"):
                dr.append(i[1])
                
            if(i[0]=="Injection"):
                inj.append(i[1])
               
        
        self.SubCategoryliq=li
        self.SubCategoryTab=ta
        self.SubCategorycap=cap
        self.SubCategoryTom=to
        self.SubCategorydro=dr
        self.SubCategoryInh=inh
        self.SubCategoryInj=inj
        
      #Product
        """conn=mysql.connector.connect(host="localhost",username="root",passwd="Vaishnavi@123",database="mydata",port=3306)
        my_cursor=conn.cursor()
        my_cursor.execute("select medname from pharmacy")
        p=my_cursor.fetchall()
        self.Product=p
        a=0
        for i in p:
            if(i[0]=="Liquid"):
                li.append(i[1])

        self.Product=li
      #Price
        conn=mysql.connector.connect(host="localhost",username="root",passwd="Vaishnavi@123",database="mydata",port=3306)
        my_cursor=conn.cursor()
        my_cursor.execute("select Price from pharmacy")
        P=my_cursor.fetchall()
        self.Price=P
        a=0
        for i in P:
            if(i[0]=="Liquid"):
                li.append(i[1])

        self.Price=li
     """
       # conn.commit()
       # conn.close()

#root=Tk()
#root.title("")
        
        img=Image.open("bg3.jpg")
        img=img.resize((1530,130),Image.ANTIALIAS)
        self.Photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.Photoimg)
        lbl_img.place(x=0,y=0,width=1530,height=130)

        #img1=Image.open("tab.jpg")
        #img1=img1.resize((500,130),Image.ANTIALIAS)
        #self.Photoimg1=ImageTk.PhotoImage(img1)

        #lbl_img1=Label(self.root,image=self.Photoimg1)
        #lbl_img1.place(x=500,y=0,width=500,height=130)

        #img2=Image.open("tablet.jpg")
        #img2=img2.resize((525,130),Image.ANTIALIAS)
        #self.Photoimg2=ImageTk.PhotoImage(img2)

        #lbl_img2=Label(self.root,image=self.Photoimg2)
        #lbl_img2.place(x=1000,y=0,width=525,height=130)

        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=8,relief=RIDGE,fg='red',bg="white",
                        font=("times new roman",35,"bold"),padx=2,pady=4)
        lbltitle.place(x=0,y=130,width=1530,height=60)

        #img1=Image.open("logo.jpg")
        #img1=img1.resize((90,75),Image.ANTIALIAS)
        #self.Photoimg1=ImageTk.PhotoImage(img1)
        #b1=Button(self.root,image=self.Photoimg1,borderwidth=0)
        #b1.place(x=70,y=20)

##########################Main Frame#############################
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=190,width=1530,height=620)

#============================customer LabelFrame===========================
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("Times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",10,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entry_mob=ttk.Entry(Cust_Frame,textvariable= self.c_phon_var,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1,padx=5,pady=2)

        self.lblCustName=Label(Cust_Frame,text="Customer Name:",font=("times new roman",10,"bold"),bg="white")
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.txtCustName=ttk.Entry(Cust_Frame,textvariable= self.c_name_var,font=("times new roman",10,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,text="Email",font=("times new roman",10,"bold"),bg="white",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.txtEmail=ttk.Entry(Cust_Frame, textvariable=self.c_mail_var,font=("times new roman",10,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,padx=5,pady=2)

#===============================Product LabelFrame=========================

        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("Times new roman",12,"bold"),bg="white",fg="red",bd=4)
        Product_Frame.place(x=370,y=5,width=620,height=140)
        #category
        self.lblCategory=Label(Product_Frame,text="Type of Medicine",font=("times new roman",10,"bold"),bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.category,font=("times new roman",10,"bold"),width=24)
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.categories)

       #Subcategory
        self.lblSubCategory=Label(Product_Frame,text="Reference No",font=("times new roman",10,"bold"),bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,font=("times new roman",10,"bold"),width=24)
        self.ComboSubCategory.grid(row=1,column=1,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.reftomadn)

        #Product Name
        self.lblproduct=Label(Product_Frame,text="Medicine Name",font=("times new roman",10,"bold"),bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Entry(Product_Frame,font=("times new roman",10,"bold"),width=27)
        self.ComboProduct.grid(row=2,column=1,padx=5,pady=2)

        #price
        self.lblPrice=Label(Product_Frame,text="Price",font=("times new roman",10,"bold"),bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Entry(Product_Frame,font=("times new roman",10,"bold"),width=24)
        self.ComboPrice.grid(row=0,column=3,padx=5,pady=2)

        #Qty
        self.lblQty=Label(Product_Frame,text="Qty",font=("times new roman",10,"bold"),bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)
        self.ComboQty=ttk.Entry(Product_Frame,font=("times new roman",10,"bold"),width=24)
        self.ComboQty.grid(row=1,column=3,padx=5,pady=2)
        
        #middel Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=980,height=340)

        img3=Image.open("tab5.jpg")
        img3=img3.resize((980,340),Image.ANTIALIAS)
        self.Photoimg3=ImageTk.PhotoImage(img3)

        lbl_img3=Label(MiddleFrame,image=self.Photoimg3)
        lbl_img3.place(x=0,y=0,width=980,height=340)

        #img4=Image.open("tablet.jpg")
        #img4=img4.resize((490,340),Image.ANTIALIAS)
        #self.Photoimg4=ImageTk.PhotoImage(img4)

        #lbl_img4=Label(MiddleFrame,image=self.Photoimg4)
        #lbl_img4.place(x=490,y=0,width=490,height=340)


       
       #Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1020,y=10,width=500,height=40)
        
        self.lblBill=Label(Search_Frame,text="Bill Number",font=("times new roman",12,"bold"),fg="white",bg="red")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Serach=ttk.Entry(Search_Frame,textvariable=self.bill_no_var,font=("times new roman",10,"bold"),width=24)
        self.txt_Entry_Serach.grid(row=0,column=1,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,height=2,text="Search",font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)

        
       #RightFrame Bill Area
        RightlabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("Times new roman",12,"bold"),bg="white",fg="red")
        RightlabelFrame.place(x=1000,y=45,width=480,height=440)

        scroll_y=Scrollbar(RightlabelFrame,orient=VERTICAL)
        self.textarea=Text(RightlabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("Times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        self.Welcome()
        
        #Bill Counter
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("Times new roman",12,"bold"),bg="white",fg="red",bd=4)
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)

        self.lblSubTotal=Label(Bottom_Frame,text="Sub Total",font=("times new roman",10,"bold"),bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.EntrySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("times new roman",10,"bold"),width=24)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_tax=Label(Bottom_Frame,text="Gov Tax",font=("times new roman",10,"bold"),bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("times new roman",10,"bold"),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblAmountTotal=Label(Bottom_Frame,text="Total",font=("times new roman",10,"bold"),bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("times new roman",10,"bold"),width=24)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        #Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)
        
        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        


    def Welcome(self):
            self.textarea.delete(1.0,END)
            self.textarea.insert(END," WELCOME TO PHARMACY MANAGEMENT SYSTEM")
            self.textarea.insert(END,f"\n Bill Number:{self.bill_no_var.get()}")
            self.textarea.insert(END,f"\n Customer Name:{self.txtCustName.get()}")
            self.textarea.insert(END,f"\n Phone Number:{self.entry_mob.get()}")
            self.textarea.insert(END,f"\n Customer Email:{self.txtEmail.get()}")

            self.textarea.insert(END,"\n==================================================")
            self.textarea.insert(END,f"\n Products\t\t\tQty\t\tPrice")
            self.textarea.insert(END,"\n=================================================\n")
            self.l=[]
            #================================function declaration===========================
    def AddItem(self):
            self.n=float(self.ComboPrice.get())
            b=int(self.ComboQty.get())
            self.m=b*self.n
            tax=18
            self.l.append(self.m)
            if self.ComboProduct.get()=="":
                messagebox.showerror("Error","please select the product name")
            else:
                self.textarea.insert(END,f"\n{self.ComboProduct.get()}\t\t\t{self.ComboQty.get()}\t\t{self.m}")
                self.sub_total.set(str("Rs.%.2f"%(sum(self.l))))
                self.tax_input.set(str("Rs.%.2f"%((((sum(self.l))-(float(self.ComboPrice.get())))*tax)/100)))                    
                self.tax_input.set(str("Rs.%.2f"%(((sum(self.l))+((((sum(self.l))-(float(self.ComboPrice.get())))*tax)/100)))))



    def gen_bill(self):
        if self.ComboProduct.get()=="":
            messagebox.showerror("Error","please Add to Card product ")
        else:
            text=self.textarea.get(9.0,(10.0+float(len(self.l))))
            self.Welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n=================================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,"\n=================================================")


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open("bills/"+str(self.bill_no_var.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no_var.get()} saved successfully")
            f1.close()
            #+str(self.bill_no_var.get()+

    def iprint(self):
        q=self.textarea.get(1.0,END)
        filename=tempfile.mktemp(".txt")
        open(filename,"w").write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.txt_Entry_Serach.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete(1.0,END)
                for d in f1:
                     self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=="no":
             messagebox.showerror("Error","not found bill no")

    def clear(self):
        self.textarea.delete(1.0,END)
        
        self.c_name_var.set("")
        self.c_phon_var.set("")
        self.c_mail_var.set("") 
        self.bill_no_var=StringVar()
        z=random.randint(1000,9999)
        self.bill_no_var.set(str(z))
        self.search_bill.set("")
       # self.ComboProduct.set("")
       # self.price.set(0)
       # self.ComboQty.set(0)
        self.l=[0]
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.Welcome()
                

    
    
    
        #================================================functions=================================================
    def categories(self,event=""):
            if self.Combo_Category.get()=="Tablet":
                    self.ComboSubCategory.config(value=self.SubCategoryTab)
                    self.ComboSubCategory.current(0)

            if self.Combo_Category.get()=="Liquid":
                    self.ComboSubCategory.config(value=self.SubCategoryliq)
                    self.ComboSubCategory.current(0)

            if self.Combo_Category.get()=="Capsules":
                    self.ComboSubCategory.config(value=self.SubCategorycap)
                    self.ComboSubCategory.current(0)

            if self.Combo_Category.get()=="Topical Medicines":
                    self.ComboSubCategory.config(value=self.SubCategoryTom)
                    self.ComboSubCategory.current(0)

            if self.Combo_Category.get()=="Drops":
                    self.ComboSubCategory.config(value=self.SubCategorydro)
                    self.ComboSubCategory.current(0)

            if self.Combo_Category.get()=="Inhales":
                    self.ComboSubCategory.config(value=self.SubCategoryInh)
                    self.ComboSubCategory.current(0)

            if self.Combo_Category.get()=="Injection":
                    self.ComboSubCategory.config(value=self.SubCategoryInj)
                    self.ComboSubCategory.current(0)
                   

    def reftomadn(self,event=""):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="Vaishnavi@123",database="mydata",port=3306)
        my_curso=conn.cursor()
        my_curso.execute("select * from pharmacy")
        ra=my_curso.fetchall()
        for i in ra:
            if(self.ComboSubCategory.get()==i[0]):
                self.ComboProduct.config(value=i[3])
                self.ComboPrice.config(value=i[11])
                self.ComboProduct.current(0)
                self.ComboPrice.current(0)                 

                    
        conn.commit()
        conn.close()



        #==================================================================================



    



if __name__ == "__main__":
    main()

    
