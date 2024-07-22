from sre_parse import State
from sre_parse import State
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random,os
import tempfile

class Bill_App:
    def __init__( self , root ):
        self.root=root
        self.root.title("User page")
        
        self.root.geometry("1530x800+0+0")
        
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
        self.medname=StringVar()
        
        
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

        self.ComboProduct=ttk.Entry(Product_Frame,textvariable=self.medname,font=("times new roman",10,"bold"),width=27)
        self.ComboProduct.grid(row=2,column=1,padx=5,pady=2)

        #price
        self.lblPrice=Label(Product_Frame,text="Price",font=("times new roman",10,"bold"),bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Entry(Product_Frame,textvariable=self.price,font=("times new roman",10,"bold"),width=24)
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
        op=self.ComboSubCategory.get()
        q="select * from pharmacy where Ref_no=%s"
        my_curso=conn.cursor()
        my_curso.execute(q,(op,))
        ra=my_curso.fetchall()
        for i in ra:
            self.price.set(i[11])
            self.medname.set(i[3])
            #if(self.ComboSubCategory.get()==i[0]):
              #  self.ComboProduct.config(value=i[3])
              #  self.ComboPrice.config(value=i[11])
              #  self.ComboProduct.current(0)
              #  self.ComboPrice.current(0)                 

                    
        conn.commit()
        conn.close()
                            


#if self.ComboSubCategory.get()=="1212":
#                    self.ComboProduct.config(value=i[1])
























if __name__== "__main__":
    root=Tk()
    obj= Bill_App(root)
    root.mainloop()
