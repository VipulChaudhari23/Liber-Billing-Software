from os import TMP_MAX
from tkinter import * 
from tkinter import ttk
from typing import AsyncContextManager
from PIL import Image,ImageTk  #pip install pillow
import random,os
from tkinter import messagebox
import tempfile
from time import strftime
from datetime import datetime

class Billing:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Liber Billing Software")
        root.iconbitmap('icon.ico')

        ################ Variables ##############
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(999,99999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        self.prod_id=StringVar()
        # self.timedate=StringVar()

        #Product categories
        self.Category=["Select Category","Fashion","Shoes","Electronics"]

        #product subCategory
        #1.fashion
        self.subcatfashion=["T-Shirt","Jeans","Shirt"]
        
        self.T_shirt=["Tommy Hilfiger","Roadstar","Polo","Arrow"]
        self.price_Tommy_hilfiger=1800
        self.price_Roadstar=400
        self.price_Polo=1000
        self.price_Arrow=1200
        self.ProductID_Tommy_hilfiger="ft1"
        self.ProductID_Roadstar="ft2"
        self.ProductID_Polo="ft3"
        self.ProductID_Arrow="ft4"

        self.Jeans=["CottonJeans","PlainJeans","Joger"]
        self.price_CottonJeans=1200
        self.price_PlainJeans=900
        self.price_Joger=1800
        self.ProductID_CottonJeans="fj1"
        self.ProductID_PlainJeans="fj2"
        self.ProductID_Joger="fj3"

        self.shirt=["Levis","AllenSoly","Linen"]
        self.price_Levis=1200
        self.price_AllenSoly=1500
        self.price_Linen=1800
        self.ProductID_Levis="fs1"
        self.ProductID_AllenSoly="fs2"
        self.ProductID_Linen="fs3"

        #2.Shoes
        self.subcatShoes=["Chaple","Sneakers"]
        
        self.Chaple=["Dr.Chaple","NormarChaple","Sleeplers"]
        self.price_DrChaple=400
        self.price_NormarChaple=250
        self.price_Sleeplers=300
        self.ProductID_DrChaple="sc1"
        self.ProductID_NormarChaple="sc2"
        self.ProductID_Sleeplers="sc3"

        self.Sneakers=["Adidas","polo","RedChief"]
        self.price_Adidas=2000
        self.price_polo=900
        self.price_RedChief=2500
        self.ProductID_Adidas="sa1"
        self.ProductID_polo="sp2"
        self.ProductID_RedChief="sr3"

        #3.Electronics
        self.subcatelectronics=["Mobile","TV","AC","Laptop"]
        
        self.Mobile=["Samsung","Nokia","Apple"]
        self.price_Samsung=30000
        self.price_Nokia=20000
        self.price_Apple=80000
        self.ProductID_Samsung="em1"
        self.ProductID_Nokia="em2"
        self.ProductID_Apple="em3"

        self.TV=["LG","SamsungTV","MI"]
        self.price_LG=27000
        self.price_tvSamsung=30000
        self.price_MI=25000
        self.ProductID_LG="et1"
        self.ProductID_tvSamsung="et2"
        self.ProductID_MI="et3"

        self.AC=["Blue Star","voltas","Haier"]
        self.price_BlueStar=35000
        self.price_voltas=32000
        self.price_Haier=30000
        self.ProductID_BlueStar="ea1"
        self.ProductID_voltas="ea2"
        self.ProductID_Haier="ea3"

        self.Laptop=["HP","Lenovo","Dell"]
        self.price_HP=50000
        self.price_Lenovo=65000
        self.price_Dell=60000
        self.ProductID_HP="el1"
        self.ProductID_Lenovo="el2"
        self.ProductID_Dell="el3"



        # # Background Image
        # img=Image.open("image/B4.jpg")
        # img=img.resize((1530,800),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

        # bg_img=Label(self.root,image=self.photoimg)
        # bg_img.place(x=0,y=0,width=1510,height=800)
        
        # Image 1
        img1=Image.open("image/Logo.jpg")
        img1=img1.resize((1530,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        part_img1=Label(self.root,image=self.photoimg1)
        part_img1.place(x=0,y=0,width=1530,height=100)

        # # Image 2
        # img2=Image.open("image/B4.jpg")
        # img2=img2.resize((1530,800),Image.ANTIALIAS)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # part_img2=Label(self.root,image=self.photoimg2)
        # part_img2.place(x=0,y=0,width=1530,height=800)

        # # Title
        # title=Label(self.root,text="Billing Software",font=("times new roman",35,"bold"),fg="red") #bg= "white"
        # title.place(x=0,y=200,width=1530,height=50)

        # Main Frame
        Main_Frame=Frame(self.root,bd=5,relief=RIDGE,bg="black")
        Main_Frame.place(x=0,y=100,width=1400,height=643)
        # load = Image.open("image/B1.jpg")
        # render = ImageTk.PhotoImage(load)
        # img = Label(Main_Frame, image=render)
        # img.image = render
        # img.place(x=0, y=100,width=1530,height=630)
        #root.attributes('-alpha',0.5)...... make GUI transprant
        
        # Customer Frame
        cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("Roboto",12,"bold"),fg="red",bg="snow") #bg= "white"
        cust_Frame.place(x=2,y=5,width=400,height=147)

        # enter compartments in Customer Frame
        # 1. mobile number
        self.mobile=Label(cust_Frame,text="Mobile No.",font=("Roboto",12,"bold")) # by default fg color is black
        self.mobile.grid(row=0,column=0,sticky=W,padx=5,pady=5)

        self.entry_mobno=ttk.Entry(cust_Frame,font=("Roboto",10,"bold"),textvariable=self.c_phone,width=33)
        self.entry_mobno.grid(row=0,column=1)

        # 2. Name
        self.name=Label(cust_Frame,text="Customer Name",font=("Roboto",12,"bold"),bd=4) # by default fg color is black
        self.name.grid(row=1,column=0,sticky=W,padx=5,pady=5)

        self.txtname=ttk.Entry(cust_Frame,font=("Roboto",10,"bold"),textvariable=self.c_name,width=33)
        self.txtname.grid(row=1,column=1,sticky=W,padx=5,pady=5)

        # 3. Email
        self.email=Label(cust_Frame,text="Customer Email",font=("Roboto",12,"bold"),bd=4) # by default fg color is black
        self.email.grid(row=2,column=0,sticky=W,padx=5,pady=5)

        self.txtemail=ttk.Entry(cust_Frame,font=("times new roman",10,"bold"),textvariable=self.c_email,width=33)
        self.txtemail.grid(row=2,column=1,sticky=W,padx=5,pady=5)

        # product Frame
        prod_Frame=LabelFrame(Main_Frame,text="Product",font=("Roboto",12,"bold"),fg="red",bg="snow") #bg= "white"
        prod_Frame.place(x=400,y=5,width=639,height=147)

        # enter compartments in product Frame
        # 1. Categories
        self.lblCategories=Label(prod_Frame,text="Categories",font=("Roboto",12,"bold"),bd=4) # by default fg color is black
        self.lblCategories.grid(row=0,column=0,sticky=W,padx=5,pady=5)

        self.combo_Categories=ttk.Combobox(prod_Frame,font=("Roboto",10,"bold"),value=self.Category,width=24,state="readonly")
        self.combo_Categories.current(0)
        self.combo_Categories.grid(row=0,column=1,sticky=W,padx=5,pady=5)
        self.combo_Categories.bind("<<ComboboxSelected>>",self.subcategories)

        # 2. SubCategories
        self.lblSubCategories=Label(prod_Frame,text="Sub Categories",font=("Roboto",12,"bold"),bd=4) # by default fg color is black
        self.lblSubCategories.grid(row=1,column=0,sticky=W,padx=5,pady=5)

        self.combo_SubCategories=ttk.Combobox(prod_Frame,font=("Roboto",10,"bold"),value=[""],width=24,state="readonly")
        self.combo_SubCategories.grid(row=1,column=1,sticky=W,padx=5,pady=5)
        self.combo_SubCategories.bind("<<ComboboxSelected>>",self.Product_add)

        # 3. Product_Name
        self.Product_Name=Label(prod_Frame,text="Product Name",font=("Roboto",12,"bold"),bd=4) # by default fg color is black
        self.Product_Name.grid(row=2,column=0,sticky=W,padx=5,pady=5)

        self.combo_Product_Name=ttk.Combobox(prod_Frame,font=("Roboto",10,"bold"),textvariable=self.product,width=24,state="readonly")
        self.combo_Product_Name.grid(row=2,column=1,sticky=W,padx=5,pady=5)
        self.combo_Product_Name.bind("<<ComboboxSelected>>",self.price)
        #self.combo_Product_Name.bind("<<ComboboxSelected>>",self.P_ID)
        
        # # 4. Product_Id
        # self.Product_id=Label(prod_Frame,text="Product ID",font=("times new roman",12,"bold"),bd=4) # by default fg color is black
        # self.Product_id.grid(row=3,column=0,sticky=W,padx=5,pady=5)

        # self.combo_Product_id=ttk.Combobox(prod_Frame,font=("times new roman",10,"bold"),textvariable=self.prod_id,width=24,state="readonly")
        # self.combo_Product_id.grid(row=3,column=1,sticky=W,padx=5,pady=5)

        # 5. Price
        self.lblPrice=Label(prod_Frame,text="Price",font=("Roboto",12,"bold"),bd=4) # by default fg color is black
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=5)

        self.combo_Price=ttk.Combobox(prod_Frame,font=("Roboto",10,"bold"),textvariable=self.prices,width=24,state="readonly")
        self.combo_Price.grid(row=0,column=3,sticky=W,padx=5,pady=5)

        # 6. Qty
        self.Qty=Label(prod_Frame,text="Qty",font=("Roboto",12,"bold"),bd=4) # by default fg color is black
        self.Qty.grid(row=1,column=2,sticky=W,padx=5,pady=5)

        self.Qty=ttk.Entry(prod_Frame,font=("Roboto",10,"bold"),textvariable=self.qty,width=27)
        self.Qty.grid(row=1,column=3,sticky=W,padx=5,pady=5)

        # search
        search_Frame=Frame(Main_Frame,bg="snow",bd=2)
        search_Frame.place(x=1040,y=5,width=320,height=147)

        self.bill=Label(search_Frame,text="Bill Number",font=("Roboto",12,"bold"),bg="red",fg="white",width=33) # by default fg color is black
        self.bill.grid(row=1,column=0,sticky=W,padx=5,pady=5)

        self.txt_search=ttk.Entry(search_Frame,font=("Roboto",10,"bold"),textvariable=self.search_bill,width=42)
        self.txt_search.grid(row=2,column=0,sticky=W,padx=5,pady=5)

        self.btnsearch=Button(search_Frame,command=self.find_bill,text="Search",font=("Roboto",10,"bold"),bg="#1C1C1C",fg="white",width=20,cursor="hand2",height=2)        
        self.btnsearch.grid(row=3,column=0,sticky=W,padx=5,pady=5)

        # Frame Bill Area
        billarea=LabelFrame(Main_Frame,text="Bill Area",font=("Roboto",12,"bold"),bg="snow",fg="red")
        billarea.place(x=2,y=153,width=850,height=476)

        # Scroll bar in RightFrame Bill Area
        scroll_bar=Scrollbar(billarea,orient=VERTICAL)
        self.textarea=Text(billarea,yscrollcommand=scroll_bar.set,bg="white",fg="black",font=("Roboto",12,"bold"))
        scroll_bar.pack(side=RIGHT,fill=Y)
        scroll_bar.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)        

        # Bill Counter
        Counter_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("Roboto",12,"bold"),fg="red",bg="snow") #bg= "white"
        Counter_Frame.place(x=852,y=153,width=507,height=476)

        # subtotal
        self.Subtotal=Label(Counter_Frame,text="Subtotal",font=("Roboto",12,"bold"),bd=4) # by default fg color is black
        self.Subtotal.grid(row=0,column=0,sticky=W,padx=5,pady=5)

        self.Subtotal=ttk.Entry(Counter_Frame,font=("Roboto",10,"bold"),textvariable=self.sub_total,width=48)
        self.Subtotal.grid(row=0,column=1,sticky=W,padx=5,pady=5)        

        # tax
        self.tax=Label(Counter_Frame,text="Tax",font=("Roboto",12,"bold"),bd=4) # by default fg color is black
        self.tax.grid(row=1,column=0,sticky=W,padx=5,pady=5)

        self.tax=ttk.Entry(Counter_Frame,font=("Roboto",10,"bold"),textvariable=self.tax_input,width=48)
        self.tax.grid(row=1,column=1,sticky=W,padx=5,pady=5) 

        # total amount
        self.totalamount=Label(Counter_Frame,text="Total Amount",font=("Roboto",12,"bold"),bd=4) # by default fg color is black
        self.totalamount.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.totalamount=ttk.Entry(Counter_Frame,font=("Roboto",10,"bold"),textvariable=self.total,width=48)
        self.totalamount.grid(row=2,column=1,sticky=W,padx=5,pady=5) 

        # Display Current time
        def time():
            string = datetime.now()
            lbl.config(text = string)
            lbl.after(1000, time)
        lbl = Label(Counter_Frame, font = ('Roboto',16,'bold'), background= 'white',foreground='black')
        lbl.place(x=10,y=370,width=300,height=50)
        time()

        # Button Frame
        btn_Frame=Frame(Counter_Frame,bg="white",bd=2)
        btn_Frame.place(x=20,y=130)

        self.btnaddtocart=Button(btn_Frame,text="Add To Cart",command=self.AddItem,font=("Roboto",15,"bold"),bg="#1C1C1C",fg="white",height=2,width=13,cursor="hand2")        
        self.btnaddtocart.grid(row=3,column=0,sticky=W,padx=15,pady=8)

        self.btngeneratebill=Button(btn_Frame,text="Generate Bill",command=self.gen_bill,font=("Roboto",15,"bold"),bg="#1C1C1C",fg="white",height=2,width=13,cursor="hand2")        
        self.btngeneratebill.grid(row=3,column=1,sticky=W,padx=15,pady=8)

        self.btnsave=Button(btn_Frame,text="Save Bill",command=self.save_bill,font=("Roboto",15,"bold"),bg="#1C1C1C",fg="white",height=2,width=13,cursor="hand2")        
        self.btnsave.grid(row=4,column=0,sticky=W,padx=15,pady=8)

        self.btnPrint=Button(btn_Frame,text="Print",command=self.print_bill,font=("Roboto",15,"bold"),bg="#1C1C1C",fg="white",height=2,width=13,cursor="hand2")        
        self.btnPrint.grid(row=4,column=1,sticky=W,padx=15,pady=8)

        self.btnclear=Button(btn_Frame,text="Clear",command=self.clear,font=("Roboto",15,"bold"),bg="#1C1C1C",fg="white",height=2,width=13,cursor="hand2")        
        self.btnclear.grid(row=5,column=0,sticky=W,padx=15,pady=8)

        self.btnexit=Button(btn_Frame,text="Exit",command=self.root.destroy,font=("Roboto",15,"bold"),bg="#1C1C1C",fg="white",height=2,width=13,cursor="hand2")        
        self.btnexit.grid(row=5,column=1,sticky=W,padx=15,pady=5)

        # self.btnexit=Button(btn_Frame,text="in",command=self.root.destroy,font=("Roboto",15,"bold"),bg="#1C1C1C",fg="white",height=0,width=5,cursor="hand2")        
        # self.btnexit.grid(x=10,y=370)

        # self.btnexit=Button(btn_Frame,text="fb",command=self.root.destroy,font=("Roboto",15,"bold"),bg="#1C1C1C",fg="white",height=0,width=5,cursor="hand2")        
        # self.btnexit.grid(x=10,y=370)

        # self.btnexit=Button(btn_Frame,text="insta",command=self.root.destroy,font=("Roboto",15,"bold"),bg="#1C1C1C",fg="white",height=0,width=5,cursor="hand2")        
        # self.btnexit.grid(x=10,y=370)

        self.welcom()  # call welcome function
        self.l=[] 

################### BackEnd ##############################
    ''' Function Declaration '''  

    # Bill Format
    def welcom(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t\t\t WELCOME To MEGA MART")
        self.textarea.insert(END,"\n\t\t\t\t BOT, Jalgaon Road, Jamner,")
        self.textarea.insert(END,"\n\t\t\t\t Maharashtra  - 424206")
        self.textarea.insert(END,"\n\t\t\t\t Contact No.: 7066759941")

        self.textarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number: {self.c_phone.get()}")
        self.textarea.insert(END,f"\n Mail ID: {self.c_email.get()}")

        self.textarea.insert(END,f"\n===========================================================================================")
        self.textarea.insert(END,f"\n Products\t\t\tPrice\t\t\tQTY\t\t\tTotal")
        self.textarea.insert(END,f"\n===========================================================================================\n")

    # Button Backend
    def AddItem(self):
        Tax=1
        self.o=self.prices.get()
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error!","Please Select the Product Name")
        else:
            self.textarea.insert(END,f"\n{self.product.get()}\t\t\t{self.o}\t\t\t{self.qty.get()}\t\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))
    
    # Generate Bill Button
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error!","Please Add Product To Cart")
        else:
            text = self.textarea.get(13.0,(13.0+float(len(self.l))))
            self.welcom()
            self.textarea.insert(END,text)
            self.textarea.insert(END,f"\n===========================================================================================")
            self.textarea.insert(END,f"\n Sub Amount: \t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount: \t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount: \t\t\t{self.total.get()}")
            self.textarea.insert(END,f"\n===========================================================================================")
            self.textarea.insert(END,f"\n\t\t\t\t THANK YOU !! VISIT AGAIN !!")

    # Save Bill Button
    def save_bill(self):
        openb=messagebox.askyesno("Save Bill","Do You to Save Bill")
        if openb>0:
            self.bill_data=self.textarea.get(1.0,END)
            o1=open('Bills_Details/'+str(self.bill_no.get())+".txt",'w')
            o1.write(self.bill_data)
            openb=messagebox.showinfo("Saved",f"Bill No.: {self.bill_no.get()} Bill Saved Successfully ")
            o1.close()
    
    # Print Bill Button
    def print_bill(self):
        vip=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(vip)
        os.startfile(filename,"Print")

    # search Bill Button
    def find_bill(self):
        found="no"
        for i in os.listdir("Bills_Details/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"Bills_Details/{i}","r")
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="Yes"
        if found=="no":
            messagebox.showinfo("Error!","Invalid Bill Number")
                
    # clear Bill Button
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        X=random.randint(999,99999)
        self.bill_no.set(X)
        self.c_email.set("")
        self.search_bill.set("")
        self.product.set("")
        self.prices.set("")
        self.qty.set(0)
        self.l=(0)
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.welcom()

    def subcategories(self,event=""):
        if self.combo_Categories.get()=="Fashion":
            self.combo_SubCategories.config(value=self.subcatfashion)
            self.combo_SubCategories.current(0)

        if self.combo_Categories.get()=="Shoes":
            self.combo_SubCategories.config(value=self.subcatShoes)
            self.combo_SubCategories.current(0)

        if self.combo_Categories.get()=="Electronics":
            self.combo_SubCategories.config(value=self.subcatelectronics)
            self.combo_SubCategories.current(0)

    def Product_add(self,event=""):
        # fashion
        if self.combo_SubCategories.get()=="T-Shirt":
            self.combo_Product_Name.config(value=self.T_shirt)
            self.combo_Product_Name.current(0)

        if self.combo_SubCategories.get()=="Jeans":
            self.combo_Product_Name.config(value=self.Jeans)
            self.combo_Product_Name.current(0)

        if self.combo_SubCategories.get()=="Shirt":
            self.combo_Product_Name.config(value=self.shirt)
            self.combo_Product_Name.current(0)

        # Shoes
        if self.combo_SubCategories.get()=="Chaple":
            self.combo_Product_Name.config(value=self.Chaple)
            self.combo_Product_Name.current(0)

        if self.combo_SubCategories.get()=="Sneakers":
            self.combo_Product_Name.config(value=self.Sneakers)
            self.combo_Product_Name.current(0)

        # Electronics
        if self.combo_SubCategories.get()=="Mobile":
            self.combo_Product_Name.config(value=self.Mobile)
            self.combo_Product_Name.current(0)

        if self.combo_SubCategories.get()=="TV":
            self.combo_Product_Name.config(value=self.TV)
            self.combo_Product_Name.current(0)

        if self.combo_SubCategories.get()=="AC":
            self.combo_Product_Name.config(value=self.AC)
            self.combo_Product_Name.current(0)

        if self.combo_SubCategories.get()=="Laptop":
            self.combo_Product_Name.config(value=self.Laptop)
            self.combo_Product_Name.current(0) 
        ''' 
        self.T_shirt=["Tommy Hilfiger","Roadstar","Polo","Arrow"]
        self.ProductID_Tommy_hilfiger="ft1"
        self.ProductID_Roadstar="ft2"
        self.ProductID_Polo="ft3"
        self.ProductID_Arrow="ft4"

        self.Jeans=["CottonJeans","PlainJeans","Joger"]
        self.ProductID_CottonJeans="fj1"
        self.ProductID_PlainJeans="fj2"
        self.ProductID_Joger="fj3"

        self.shirt=["Levis","AllenSoly","Linen"]
        self.ProductID_Levis="fs1"
        self.ProductID_AllenSoly="fs2"
        self.ProductID_Linen="fs3"
 '''       
    def price(self,event=""):
        # T-Shirt 
        if self.combo_Product_Name.get()=="Tommy Hilfiger":
            self.combo_Price.config(value=self.price_Tommy_hilfiger)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="Roadstar":
            self.combo_Price.config(value=self.price_Roadstar)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="Polo":
            self.combo_Price.config(value=self.price_Polo)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="Arrow":
            self.combo_Price.config(value=self.price_Arrow)
            self.combo_Price.current(0)
            self.qty.set(1)
        
        # Jeans
        if self.combo_Product_Name.get()=="CottonJeans":
            self.combo_Price.config(value=self.price_CottonJeans)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="PlainJeans":
            self.combo_Price.config(value=self.price_PlainJeans)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="Joger":
            self.combo_Price.config(value=self.price_Joger)
            self.combo_Price.current(0)
            self.qty.set(1)
    
        # Shirt
        if self.combo_Product_Name.get()=="Levis":
            self.combo_Price.config(value=self.price_Levis)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="AllenSoly":
            self.combo_Price.config(value=self.price_AllenSoly)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="Linen":
            self.combo_Price.config(value=self.price_Linen)
            self.combo_Price.current(0)
            self.qty.set(1)

        ''' 
        self.subcatShoes=["Chaple","Sneakers"]
        
        self.Chaple=["Dr.Chaple","NormarChaple","Sleeplers"]
        self.ProductID_DrChaple="sc1"
        self.ProductID_NormarChaple="sc2"
        self.ProductID_Sleeplers="sc3"

        self.Sneakers=["Adidas","polo","RedChief"]
        self.ProductID_Adidas="sa1"
        self.ProductID_polo="sp2"
        self.ProductID_RedChief="sr3"
        '''    
        #Chaple
        if self.combo_Product_Name.get()=="Dr.Chaple":
            self.combo_Price.config(value=self.price_DrChaple)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="NormarChaple":
            self.combo_Price.config(value=self.price_NormarChaple)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="Sleeplers":
            self.combo_Price.config(value=self.price_Sleeplers)
            self.combo_Price.current(0)
            self.qty.set(1)

        #sneakers
        if self.combo_Product_Name.get()=="Adidas":
            self.combo_Price.config(value=self.price_Adidas)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="polo":
            self.combo_Price.config(value=self.price_polo)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="RedChief":
            self.combo_Price.config(value=self.price_RedChief)
            self.combo_Price.current(0)
            self.qty.set(1)

        '''
        self.subcatelectronics=["Mobile","TV","AC","Laptop"]
        
        self.Mobile=["Samsung","Nokia","Apple"]
        self.ProductID_Samsung="em1"
        self.ProductID_Nokia="em2"
        self.ProductID_Apple="em3"

        self.TV=["LG","SamsungTV","MI"]
        self.ProductID_LG="et1"
        self.ProductID_tvSamsung="et2"
        self.ProductID_MI="et3"

        self.AC=["Blue Star","voltas","Haier"]
        self.ProductID_BlueStar="ea1"
        self.ProductID_voltas="ea2"
        self.ProductID_Haier="ea3"

        self.Laptop=["HP","Lenovo","Dell"]
        self.ProductID_HP="el1"
        self.ProductID_Lenovo="el2"
        self.ProductID_Dell="el3"
        '''

        #Mobile
        if self.combo_Product_Name.get()=="Samsung":
            self.combo_Price.config(value=self.price_Samsung)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="Nokia":
            self.combo_Price.config(value=self.price_Nokia)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="Apple":
            self.combo_Price.config(value=self.price_Apple)
            self.combo_Price.current(0)
            self.qty.set(1)  


        #TV
        if self.combo_Product_Name.get()=="LG":
            self.combo_Price.config(value=self.price_LG)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="SamsungTV":
            self.combo_Price.config(value=self.price_tvSamsung)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="MI":
            self.combo_Price.config(value=self.price_MI)
            self.combo_Price.current(0)
            self.qty.set(1) 

        #AC
        if self.combo_Product_Name.get()=="Blue Star":
            self.combo_Price.config(value=self.price_BlueStar)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="voltas":
            self.combo_Price.config(value=self.price_voltas)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="Haier":
            self.combo_Price.config(value=self.price_Haier)
            self.combo_Price.current(0)
            self.qty.set(1) 

        #Laptop
        if self.combo_Product_Name.get()=="HP":
            self.combo_Price.config(value=self.price_HP)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="Lenovo":
            self.combo_Price.config(value=self.price_Lenovo)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product_Name.get()=="Dell":
            self.combo_Price.config(value=self.price_Dell)
            self.combo_Price.current(0)
            self.qty.set(1)
    
    # def P_ID(self,event=""):
    #      # T-Shirt 
    #     if self.combo_Product_Name.get()=="Tommy Hilfiger":
    #         self.Product_id.config(value=self.ProductID_Tommy_hilfiger)
    #         self.Product_id.current(0)

    #     if self.combo_Product_Name.get()=="Roadstar":
    #         self.Product_id.config(value=self.ProductID_Roadstar)
    #         self.Product_id.current(0)

    #     if self.combo_Product_Name.get()=="Polo":
    #         self.Product_id.config(value=self.ProductID_Polo)
    #         self.Product_id.current(0)

    #     if self.combo_Product_Name.get()=="Arrow":
    #         self.Product_id.config(value=self.ProductID_Arrow)
    #         self.Product_id.current(0)

if __name__ == '__main__':
    root=Tk()
    obj=Billing(root)  
    root.mainloop()


