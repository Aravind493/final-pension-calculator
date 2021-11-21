from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def main():
    win=Tk()
    app=login_panel(win)
    win.mainloop()
    

class login_panel:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1550x800+0+0")

        frame=Frame(self.root,bg="red")
        frame.place(x=240,y=200,width=800,height=200)
        get_str=Label(frame,text="Login\nHere!\n",font=("times new roman",32,"bold"),bg="black",fg="white")
        get_str.place(x=30,y=45)

        #labels
        username=Label(frame,text="USERNAME",font=("times new roman",18,"italic"),bg="black",fg="white")
        username.place(x=150,y=45)
        self.txtuser=ttk.Entry(frame,font=("times new roman",18,"bold"))
        self.txtuser.place(x=300,y=45)

        password=Label(frame,text="PASSWORD",font=("times new roman",18,"italic"),bg="black",fg="white")
        password.place(x=150,y=100)
        self.txtpass=ttk.Entry(frame,font=("times new roman",18,"bold"))
        self.txtpass.place(x=300,y=100)

        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",18,"bold"),bd=3,relief=RIDGE,fg="white",bg="black")
        loginbtn.place(x=600,y=65,width=150,height=40)

        #registerbutton
        regbtn=Button(frame,text="Create a new account",command=self.register_window,font=("times new roman",12,"bold"),bd=2,relief=RIDGE,fg="white",bg="black")
        regbtn.place(x=600,y=130,width=150,height=40)

       
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window)

        
        

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are mandatory")
        elif self.txtuser.get()=="Aravind@lpu.in" and self.txtpass.get()=="Aravind@123":
            messagebox.showinfo("Successful","Logged In Successfully!")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Aravind@123",database="sys")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and pswd=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()

                                                                                      ))
           
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=calculator(self.new_window)
                else:
                    if not open_main :
                        return
                
      
                    
                 

            
class register:
    #calling constructor
    def __init__(self,root):
        self.root=root
        self.root.title("Create New Account")
        self.root.geometry("1600x900+0+0")

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_sq=StringVar()
        self.var_sa=StringVar()
        self.var_pswd=StringVar()
        self.var_cnfpswd=StringVar()
        self.var_checkbtn=IntVar()

        frame=Frame(self.root,bg="black")
        frame.place(x=250,y=100,width=800,height=800)

        reglbl=Label(frame,text="CREATE YOUR ACCOUNT!",font=("times new roman",28,"bold"),fg="yellow",bg="black")
        reglbl.place(x=140,y=20)

        #labels and entry fields
        fname=Label(frame,text="First Name",font=("times new roman",16,"bold"),fg="white",bg="black")
        fname.place(x=100,y=100)

        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.txt_fname.place(x=100,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",16,"bold"),fg="white",bg="black")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact Number",font=("times new roman",16,"bold"),fg="white",bg="black")
        contact.place(x=100,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=100,y=200,width=250)

        email=Label(frame,text="E-mail ID",font=("times new roman",16,"bold"),fg="white",bg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        sq=Label(frame,text="Select security question", font=("times new roman",16,"bold"),fg="white",bg="black")
        sq.place(x=100,y=240)

        self.combo_sq=ttk.Combobox(frame,textvariable=self.var_sq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_sq["values"]=("Select","Your birth place","your mom name","your pet name","Your favourite game")
        self.combo_sq.place(x=100,y=270,width=250)
        self.combo_sq.current(0)

        sa=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="white",bg="black")
        sa.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        pswd=Label(frame,text="Password",font=("times new roman",16,"bold"),fg="white",bg="black")
        pswd.place(x=100,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pswd,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=100,y=340,width=250)

        cnfpswd=Label(frame,text="Confirm Password",font=("times new roman",16,"bold"),fg="white",bg="black")
        cnfpswd.place(x=370,y=310)

        self.txt_cnfpswd=ttk.Entry(frame,textvariable=self.var_cnfpswd,font=("times new roman",15,"bold"))
        self.txt_cnfpswd.place(x=370,y=340,width=250)

        checkbtn=Checkbutton(frame,variable=self.var_checkbtn,text="I agree with all terms & conditions",font=("times new roman",8,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=100,y=380)

        b1=Button(frame,command=self.register_data,text="Register",font=("times new roman",12,"bold"),bd=2,relief=RIDGE,fg="black",bg="red",activebackground="red",activeforeground="black")
        b1.place(x=100,y=420,width=100)


    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="" or self.var_sq.get()=="Select" or self.var_sa.get()=="Select":
            messagebox.showerror("Error","All fields are mandatory",parent=self.root)
        elif self.var_pswd.get()!=self.var_cnfpswd.get():
            messagebox.showerror("Error","Password and Confirm Password must be same.",parent=self.root)
        elif self.var_checkbtn.get()==0:
            messagebox.showerror("Error","Please check the box after you read terms and conditions",parent=self.root)
        else:
           conn=mysql.connector.connect(host="localhost",user="root",password="Aravind@123",database="sys")
           my_cursor=conn.cursor()
           query=("select * from register where email=%s")
           value=(self.var_email.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
           if row!=None:
               messagebox.showerror("Error","User Already Exist,Please Try Another Email",parent=self.root)
           else:
                   my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_sq.get(),
                                                                                    self.var_sa.get(),
                                                                                    self.var_pswd.get()
                                                                                          ))
                   conn.commit()
                   conn.close()
                   messagebox.showinfo("success","Register Successfully")


class calculator:

    def Calculate(self):
        frame=Frame(self.root)
        base=int(self.var_bp.get())
        service=int(self.var_ser.get())
        total = (base * service * 12 * (70 / 3000))
        commute = (base * service * 12 * (70 / 3000)) * (0.3)
        Label(text=f"{total}",font="bold 10").place(x=500, y=630)
        Label(text=f"{commute}",font="bold 10").place(x=900, y=630)
    

    
    #calling constructor
    def __init__(self,root):
        self.root=root
        self.root.title("Calculator")
        self.root.geometry("1600x900+0+0")

  

        #variables
        self.var_name=StringVar()
        self.var_age=IntVar()
        self.var_ser=IntVar()
        self.var_bp=IntVar()
        self.var_contact=IntVar()
        

        frame=Frame(self.root,bg="black")
        frame.place(x=250,y=100,width=800,height=800)

        reglbl=Label(frame,text="Pension Calculator",font=("times new roman",28,"bold"),fg="red",bg="black")
        reglbl.place(x=250,y=20)

        #labels and entry fields
        fname=Label(frame,text="Name",font=("times new roman",16,"bold"),fg="white",bg="black")
        fname.place(x=280,y=100)

        self.txt_name=ttk.Entry(frame,textvariable=self.var_name,font=("times new roman",15))
        self.txt_name.place(x=280,y=130,width=250)


        age=Label(frame,text="Enter Age",font=("times new roman",16,"bold"),fg="white",bg="black")
        age.place(x=280,y=170)

        self.txt_age=ttk.Entry(frame,textvariable=self.var_age,font=("times new roman",15))
        self.txt_age.place(x=280,y=200,width=250)

        ser=Label(frame,text="Service years",font=("times new roman",16,"bold"),fg="white",bg="black")
        ser.place(x=280,y=240)

        self.txt_ser=ttk.Entry(frame,textvariable=self.var_ser,font=("times new roman",15))
        self.txt_ser.place(x=280,y=270,width=250)

        bp=Label(frame,text="Enter Basic Pay",font=("times new roman",16,"bold"),fg="white",bg="black")
        bp.place(x=280,y=310)

        self.txt_bp=ttk.Entry(frame,textvariable=self.var_bp,font=("times new roman",15,"bold"))
        self.txt_bp.place(x=280,y=340,width=250)

        contact=Label(frame,text="Contact Number",font=("times new roman",16,"bold"),fg="white",bg="black")
        contact.place(x=280,y=380)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=280,y=410,width=250)

        reglbl=Label(frame,text="Please validate before clicking calculate ",font=("times new roman",18,"bold"),fg="red",bg="black")
        reglbl.place(x=60,y=460)
 

        b1=Button(frame,command=self.calculator_data,text="Validate",font=("times new roman",12,"bold"),bd=2,relief=RIDGE,fg="black",bg="red")
        b1.place(x=120,y=500,width=100)

        b2=Button(frame,command=self.Calculate,text="Calculate",font=("times new roman",12,"bold"),bd=2,relief=RIDGE,fg="black",bg="red")
        b2.place(x=320,y=500,width=100)

        b3=Button(frame,text="Log out",command=self.return_login,font=("times new roman",12,"bold"),bd=2,relief=RIDGE,fg="black",bg="red")
        b3.place(x=530,y=500,width=100)


        pension=Label(frame,text="Total Pension :",font="bold 10")
        pension.place(x=100, y=560)

        commute=Label(frame,text="Total Commutation :",font="bold 10")
        commute.place(x=500, y=560)

        


    def calculator_data(self):
        if self.var_name.get()=="" or self.var_age.get()=="" or self.var_ser.get()=="" or self.var_bp.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error","All fields are mandatory",parent=self.root)
        elif self.var_age.get() < 50:
            messagebox.showerror("Error","Age should be above 50",parent=self.root)
        elif self.var_age.get() > 80:
            messagebox.showerror("Error","Age should be below 80",parent=self.root)
        elif self.var_ser.get() > 30:
            messagebox.showerror("Error","service years should be below 31 years",parent=self.root)
        else:
           conn=mysql.connector.connect(host="localhost",user="root",password="Aravind@123",database="sys")
           my_cursor=conn.cursor()
           query=("select * from calculate where contact=%s")
           value=(self.var_contact.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
           if row!=None:
               messagebox.showerror("Error","User Already Exist,Please Try Another contact",parent=self.root)
           else:
               my_cursor.execute("insert into calculate values(%s,%s,%s,%s,%s)",(self.var_name.get(),
                                                                                          self.var_age.get(),
                                                                                          self.var_ser.get(),
                                                                                          self.var_bp.get(),
                                                                                          self.var_contact.get()
                                                                                          ))
           conn.commit()
           conn.close()

    def return_login(self):
        self.root.destroy()
                   

if __name__ == '__main__':
    main()
    
