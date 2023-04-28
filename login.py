from cProfile import label
from email import message
from logging import root
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk                #pip install pillow
from tkinter import messagebox
from main import Face_recognition_system
import mysql.connector

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1530x790+0+0")


 #background image

        bgimg=Image.open(r"logo and bg\login1.jpeg")
        bgimg=bgimg.resize((1540,800), Image.ANTIALIAS)
        self.photobgimg=ImageTk.PhotoImage(bgimg)

        f_lbl=Label(self.root,image=self.photobgimg)
        f_lbl.place(x=0,y=0,width=1540,height=800)

#Frame
        frame=Frame(self.root,bg="white",bd=3,relief=RIDGE)
        frame.place(x=600,y=150,width=350,height=500)

        img1=Image.open(r"logo and bg\login logo.jpeg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        img1_lbl=Label(frame,image=self.photoimg1,bg="white",borderwidth=0)
        img1_lbl.place(x=125,y=2)

        text=Label(frame, text="Application Login",font=("freestyle script",30,"bold"),bg="white")
        text.place(x=80,y=110,width=200)

#Labels
        #Username
        user_lbl=Label(frame,text="Username:",font=("Monaco",18,"bold"),bg="white")
        user_lbl.place(x=70,y=180)

        self.txtuser=ttk.Entry(frame,width="22",font=("times new roman",16,"bold"))
        self.txtuser.place(x=40,y=210)

        
        #Passwod
        pass_lbl=Label(frame,text="Password:",font=("Monaco",18,"bold"),bg="white")
        pass_lbl.place(x=70,y=255)

        self.txtpass=ttk.Entry(frame,width="22",font=("times new roman",16,"bold"))
        self.txtpass.place(x=40,y=285)

#=============Icon Images==============
        #user
        icon1=Image.open(r"logo and bg\user.jpeg")
        icon1=icon1.resize((35,35),Image.ANTIALIAS)
        self.photoicon1=ImageTk.PhotoImage(icon1)

        icon1_lbl=Label(frame,image=self.photoicon1,bg="white",borderwidth=0)
        icon1_lbl.place(x=38,y=175)

        #password
        icon2=Image.open(r"logo and bg\pass.jpeg")
        icon2=icon2.resize((35,35),Image.ANTIALIAS)
        self.photoicon2=ImageTk.PhotoImage(icon2)

        icon1_lbl=Label(frame,image=self.photoicon2,bg="white",borderwidth=0)
        icon1_lbl.place(x=38,y=250)

#============button===========

        #login
        loginbtn=Button(frame,command=self.login,text="Log In",font=("calibri",18,"bold"),bd=2,relief=RIDGE,fg="snow",bg="red",activeforeground="snow",activebackground="red",cursor="hand2")
        loginbtn.place(x=40,y=330,width=245,height=40) 

        text1=Label(frame, text="----------------- OR -----------------",font=("times new roman",14,"bold"),bg="white")
        text1.place(x=40,y=375,width=245)     
    
        #registerbutton
        registerbtn=Button(frame,command=self.new_register,text="New User Register",font=("calibri",16),bg="white",bd=0,fg="black",activebackground="white",cursor="hand2")
        registerbtn.place(x=60,y=400,width=230) 

        #Forget Password
        forgetbtn=Button(frame,command=self.forgot_password_window,text="Forgot Password?",font=("calibri",12),bg="white",bd=0,fg="black",activebackground="white",cursor="hand2")
        forgetbtn.place(x=55,y=440,width=230) 

#New User Register button function
    def new_register(self):
            self.new_window=Toplevel(self.root)
            self.app=Register(self.new_window)

#================Login FUNCTION================
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mansi@12345",database="student")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                             
                                                                                        ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password",parent=self.root)
            else:
                self.new_window=Toplevel(self.root)
                self.app=Face_recognition_system(self.new_window)
                
            conn.commit()
            conn.close()

#================Reset Password==========

    def reset_pass(self):
        if self.sq_combo.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root2)
        elif self.saa.get()=="":
            messagebox.showerror("Error", "Please enter the answer",parent=self.root2)
        elif self.txt.get()=="":
            messagebox.showerror("Error","Please Enter the New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mansi@12345",database="student")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.sq_combo.get(),self.saa.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s  where email=%s")
                value=(self.txt.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Your password has been reset",parent=self.root2)
                self.root2.destroy()




#=============Forgot password function============    
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mansi@12345",database="student")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter the valid username",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Fogot Password")  
                self.root2.geometry("340x400+475+140")

                #bgimg
                bgimg1=Image.open(r"logo and bg\s2.jpg")
                bgimg1=bgimg1.resize((350,400), Image.ANTIALIAS)
                self.photobgimg1=ImageTk.PhotoImage(bgimg1)

                f_lbl=Label(self.root2,image=self.photobgimg1)
                f_lbl.place(x=0,y=0,width=350,height=400)

               

                l=Label(self.root2,text="Reset Password: ",font=("freestyle script",30,"bold"),bg="azure1",fg="Purple") 
                l.place(x=20,y=10) 


                #Security Question
                sq_lbl=Label(self.root2,text="Select Security Question:",font=("calibri",16,"bold"),bg="azure1",fg="Black")
                sq_lbl.place(x=40,y=80)

                self.sq_combo=ttk.Combobox(self.root2,font=("times new roman",14,"bold"),state="readonly",width=20)
                self.sq_combo["values"]=("Select","Your Birth Place","Your Pet Name","Your Favorite City name","Your first School name")
                self.sq_combo.current(0)
                self.sq_combo.place(x=40,y=110)

                #Security Answer
                sa_lbl=Label(self.root2,text="Security Answer:",font=("calibri",16,"bold"),bg="azure1",fg="Black")
                sa_lbl.place(x=40,y=150)

                self.saa=ttk.Entry(self.root2,width="20",font=("times new roman",14,"bold"))
                self.saa.place(x=40,y=180)

                #New Password
                newpass_lbl=Label(self.root2,text="New Password:",font=("calibri",16,"bold"),bg="azure1",fg="Black")
                newpass_lbl.place(x=40,y=220)

                self.txt=ttk.Entry(self.root2,width="20",font=("times new roman",14,"bold"))
                self.txt.place(x=40,y=250)

                btn=Button(self.root2,command=self.reset_pass,text="Reset",font=("calibri",16,"bold"),bg="green",fg="black",activebackground="green")
                btn.place(x=70,y=310,width=150)



   





#====================Register Class==============
class Register:
        def __init__(self,root):
                self.root=root
                self.root.title("Register Window")
                self.root.geometry("600x500+480+150")

#================variables============
                self.var_fname=StringVar()
                self.var_lname=StringVar()
                self.var_contact=StringVar()
                self.var_email=StringVar()
                self.var_securityQ=StringVar()
                self.var_securityA=StringVar()
                self.var_pass=StringVar()
                self.var_confpass=StringVar()


#Main Frame
                frame=Frame(self.root,bg="white",bd=3,relief=RIDGE)
                frame.place(x=0,y=0,width=600,height=500)

                #bg img
                img1=Image.open(r"logo and bg\reg.jpeg")
                img1=img1.resize((620,500), Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                f_lbl=Label(frame,image=self.photoimg1)
                f_lbl.place(x=-5,y=0,width=620,height=500)

                # register text
                register_lbl=Label(frame,text="Register Here",font=("freestyle script",30,"bold"),bg="white",fg="Darkgreen")
                register_lbl.place(x=20,y=10)

                

        #===============labels and entry==============

                #first name
                fname_lbl=Label(frame,text="First Name:",font=("calibri",16,"bold"),bg="white",fg="Black")
                fname_lbl.place(x=40,y=70)

                self.fname=ttk.Entry(frame,textvariable=self.var_fname,width="20",font=("times new roman",14,"bold"))
                self.fname.place(x=40,y=100)

                #lastname
                lname_lbl=Label(frame,text="Last Name:",font=("calibri",16,"bold"),bg="white",fg="Black")
                lname_lbl.place(x=320,y=70)

                self.lname=ttk.Entry(frame,textvariable=self.var_lname,width="20",font=("times new roman",14,"bold"))
                self.lname.place(x=320,y=100)

                #Contact No.
                contact_lbl=Label(frame,text="Contact No:",font=("calibri",16,"bold"),bg="white",fg="Black")
                contact_lbl.place(x=40,y=140)

                self.cno=ttk.Entry(frame,textvariable=self.var_contact,width="20",font=("times new roman",14,"bold"))
                self.cno.place(x=40,y=170)

                #Email
                Email_lbl=Label(frame,text="Email:",font=("calibri",16,"bold"),bg="white",fg="Black")
                Email_lbl.place(x=320,y=140)

                self.email=ttk.Entry(frame,textvariable=self.var_email,width="20",font=("times new roman",14,"bold"))
                self.email.place(x=320,y=170)

                #Security Question
                sq_lbl=Label(frame,text="Select Security Question:",font=("calibri",16,"bold"),bg="white",fg="Black")
                sq_lbl.place(x=40,y=210)

                sq_combo=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",14,"bold"),state="readonly",width=20)
                sq_combo["values"]=("Select","Your Birth Place","Your Pet Name","Your Favorite City name","Your first School name")
                sq_combo.current(0)
                sq_combo.place(x=40,y=240)

                #Security Answer
                sa_lbl=Label(frame,text="Security Answer:",font=("calibri",16,"bold"),bg="white",fg="Black")
                sa_lbl.place(x=320,y=210)

                self.saa=ttk.Entry(frame,textvariable=self.var_securityA,width="20",font=("times new roman",14,"bold"))
                self.saa.place(x=320,y=240)

                #Password
                pass_lbl=Label(frame,text="Password:",font=("calibri",16,"bold"),bg="white",fg="Black")
                pass_lbl.place(x=40,y=280)

                self.pas=ttk.Entry(frame,textvariable=self.var_pass,width="20",font=("times new roman",14,"bold"))
                self.pas.place(x=40,y=310)

                #Confirm Password
                cpass_lbl=Label(frame,text="Confirm Password:",font=("calibri",16,"bold"),bg="white",fg="Black")
                cpass_lbl.place(x=320,y=280)

                self.cpass=ttk.Entry(frame,textvariable=self.var_confpass,width="20",font=("times new roman",14,"bold"))
                self.cpass.place(x=320,y=310)

        #===============Check button=========
                self.var_check=IntVar()
                checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("calibri",12),bg="white",activebackground="white",onvalue=1,offvalue=0)
                checkbtn.place(x=40,y=340)

        #==============Buttons=============
                #Register
                icon=Image.open(r"logo and bg\reg1.png")
                icon=icon.resize((170,80),Image.ANTIALIAS)
                self.photoicon=ImageTk.PhotoImage(icon)

                b1=Button(frame,image=self.photoicon,command=self.register_data,borderwidth=0,cursor="hand2",bg="black",activebackground="white")
                b1.place(x=50,y=380)

                #Login
                icon2=Image.open(r"logo and bg\reg2.jpg")
                icon2=icon2.resize((190,80),Image.ANTIALIAS)
                self.photoicon2=ImageTk.PhotoImage(icon2)

                b1=Button(frame,command=self.return_login,image=self.photoicon2,borderwidth=0,cursor="hand2",bg="black",activebackground="white")
                b1.place(x=330,y=380)


#======================Function declaration================

        def register_data(self):
                if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_pass.get()=="":
                    messagebox.showerror("Error", "All Fields are required",parent=self.root)

                elif self.var_pass.get()!=self.var_confpass.get():
                        messagebox.showerror("Error","Password does not match!",parent=self.root)
                elif self.var_check.get()==0:
                        messagebox.showerror("Error", "Please agree our Terms & Conditions",parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Mansi@12345",database="student")
                        my_cursor=conn.cursor()
                        query=("select * from register where email=%s")
                        value=(self.var_email.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()
                        if row!=None:
                                messagebox.showerror("Error","User Already exist, Please try another Email!",parent=self.root)
                        else:
                                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_fname.get(),
                                                                                                        self.var_lname.get(),
                                                                                                        self.var_contact.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_securityQ.get(),
                                                                                                        self.var_securityA.get(),
                                                                                                        self.var_pass.get()

                                                                                                        ))         
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success","Registered Successfully",parent=self.root)

        def return_login(self):
            self.root.destroy()



if __name__=="__main__":
    main()
    