from cProfile import label
from cgitb import text
from curses.panel import bottom_panel
from email.mime import image
from lib2to3.pgen2.pgen import generate_grammar
from pickle import FRAME
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from numpy import place
from tkcalendar import DateEntry
from tkinter import messagebox
import cv2
import pandas as pd
import json
import csv
import mysql.connector


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #============variables============
        self.var_Department=StringVar()
        self.var_Year=StringVar()
        self.var_Sem=StringVar()
        self.var_ID=StringVar()
        self.var_Name=StringVar()
        self.var_Section=StringVar()
        self.var_Roll=StringVar()
        self.var_Gender=StringVar()
        self.var_DOB=StringVar()
        self.var_Email=StringVar()
        self.var_Phone=StringVar()
        self.var_Address=StringVar()
        self.var_Teacher=StringVar()




        #top image
        img=Image.open(r"logo and bg\st1.jpg")
        img=img.resize((1600,165),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        img0=Label(self.root,image=self.photoimg)
        img0.place(x=0,y=38,width=1600,height=165)

        #bg img
        img1=Image.open(r"logo and bg\st2.jpg")
        img1=img1.resize((1600,660),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        img01=Label(self.root,image=self.photoimg1)
        img01.place(x=0,y=200,width=1600,height=660)

        #Title
        title_lbl=Label(self.root,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="azure", fg="green")
        title_lbl.place(x=0,y=-1,width=1600,height=39)

        #main frame
        main_frame=Frame(self.root,bd=2,bg="azure")
        main_frame.place(x=10,y=200,width=1510,height=580)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="azure",relief=RIDGE,text="Student Details", font=("calibri",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=550)

        img_left=Image.open(r"logo and bg\st3.jpg")
        img_left=img_left.resize((720,110),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img_left)

        img1=Label(Left_frame,image=self.photoimg1)
        img1.place(x=5,y=0,width=720,height=110)


        # current course 
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="azure",relief=RIDGE,text="Current Course information", font=("calibri",12,"bold"))
        current_course_frame.place(x=5,y=110,width=720,height=95)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("calibri",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Department,font=("calibri",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","CSE","IT","ECE","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("calibri",12,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Year,font=("calibri",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","1st","2nd","3rd","4th")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #Semester
        Sem_label=Label(current_course_frame,text="Semester",font=("calibri",12,"bold"))
        Sem_label.grid(row=1,column=2,padx=10,sticky=W)

        Sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Sem,font=("calibri",12,"bold"),width=17,state="readonly")
        Sem_combo["values"]=("Select Semester","Odd","Even")
        Sem_combo.current(0)
        Sem_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)




        #Student Info 
        student_frame=LabelFrame(Left_frame,bd=2,bg="azure",relief=RIDGE,text="Student information", font=("calibri",12,"bold"))
        student_frame.place(x=5,y=212,width=720,height=350)

        #Student ID
        StudentId_label=Label(student_frame,text="Student ID:",font=("calibri",12,"bold"))
        StudentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        StudentId_entry=ttk.Entry(student_frame,width=20,textvariable=self.var_ID,font=("calibri",12,"bold"))
        StudentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        #Student Name
        StudentName_label=Label(student_frame,text="Student Name:",font=("calibri",12,"bold"))
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        StudentName_entry=ttk.Entry(student_frame,width=20,textvariable=self.var_Name,font=("calibri",12,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,sticky=W)

        #Section
        StudentSection_label=Label(student_frame,text="Section:",font=("calibri",12,"bold"))
        StudentSection_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Section_combo=ttk.Combobox(student_frame,textvariable=self.var_Section,font=("calibri",12,"bold"),width=18,state="readonly")
        Section_combo["values"]=("Select Section","A","B","C","D")
        Section_combo.current(0)
        Section_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll Number
        StudentRoll_label=Label(student_frame,text="Roll Number:",font=("calibri",12,"bold"))
        StudentRoll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        StudentRoll_entry=ttk.Entry(student_frame,width=20,textvariable=self.var_Roll,font=("calibri",12,"bold"))
        StudentRoll_entry.grid(row=1,column=3,padx=10,sticky=W)

        #Phone
        Phone_label=Label(student_frame,text="Phone Number:",font=("calibri",12,"bold"))
        Phone_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Phone_entry=ttk.Entry(student_frame,width=20,textvariable=self.var_Phone,font=("calibri",12,"bold"))
        Phone_entry.grid(row=3,column=1,padx=10,sticky=W)

        #Email
        Email_label=Label(student_frame,text="Email:",font=("calibri",12,"bold"))
        Email_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        Email_entry=ttk.Entry(student_frame,width=20,textvariable=self.var_Email,font=("calibri",12,"bold"))
        Email_entry.grid(row=3,column=3,padx=10,sticky=W)

        #DOB
        DOB_label=Label(student_frame,text="Date of birth:",font=("calibri",12,"bold"))
        DOB_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        DOB_combo=DateEntry(student_frame,textvariable=self.var_DOB, width=22, year=2022, month=5, day=26, background='darkblue', foreground='white', borderwidth=2)
        DOB_combo.grid(row=2,column=1,padx=0, pady=5)     
        

        #Gender
        Gender_label=Label(student_frame,text="Gender:",font=("calibri",12,"bold"))
        Gender_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Gender_combo=ttk.Combobox(student_frame,textvariable=self.var_Gender,font=("calibri",12,"bold"),width=18,state="readonly")
        Gender_combo["values"]=("Select Gender","Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Address
        Address_label=Label(student_frame,text="Address:",font=("calibri",12,"bold"))
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Address_entry=ttk.Entry(student_frame,width=20,textvariable=self.var_Address,font=("calibri",12,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,sticky=W)

        #Class Coordinator
        CC_label=Label(student_frame,text="Class Coordinator:",font=("calibri",12,"bold"))
        CC_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        CC_entry=ttk.Entry(student_frame,width=20,textvariable=self.var_Teacher,font=("calibri",12,"bold"))
        CC_entry.grid(row=4,column=3,padx=10,sticky=W)


        #Radio Buttons
        self.var_radio1=StringVar()
        r1=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        r1.grid(row=6,column=0)

        r2=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        r2.grid(row=6,column=1)

        #buttons frame
        btn_frame=Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=720,height=43)

        #save button
        save_btn=Button(btn_frame,width=17,command=self.add_data,text="Save",font=("calibri",14,"bold"),bg="yellow",fg="black")
        save_btn.grid(row=0,column=0)

        #update button
        update_btn=Button(btn_frame,width=17,command=self.update_data,text="Update",font=("calibri",14,"bold"),bg="yellow",fg="black")
        update_btn.grid(row=0,column=1)

        #delete button
        delete_btn=Button(btn_frame,width=17,command=self.delete_data,text="Delete",font=("calibri",14,"bold"),bg="yellow",fg="black")
        delete_btn.grid(row=0,column=2)

        #reset button
        reset_btn=Button(btn_frame,width=17,text="Reset",command=self.reset_data,font=("calibri",14,"bold"),bg="yellow",fg="black")
        reset_btn.grid(row=0,column=3)

        #button frame 2
        btn_frame2=Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=0,y=253,width=720,height=43)

        #Take_photo button
        Take_photo_btn=Button(btn_frame2,width=35,command=self.generate_dataset,text="Take Photo Sample",font=("calibri",14,"bold"),bg="yellow",fg="black")
        Take_photo_btn.grid(row=1,column=0)

        #update_photo button
        update_photo_btn=Button(btn_frame2,width=35,text="Update Photo Sample",font=("calibri",14,"bold"),bg="yellow",fg="black")
        update_photo_btn.grid(row=1,column=1)



        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="azure",relief=RIDGE,text="Student Details", font=("calibri",12,"bold"))
        Right_frame.place(x=760,y=10,width=730,height=550)

        #img_Right=Image.open(r"D:\project\facial_recognition_project\logo and bg\s2.jpg")
        #img_Right=img_Right.resize((720,550),Image.ANTIALIAS)
        #self.photoimg2=ImageTk.PhotoImage(img_Right)

        #img2=Label(Right_frame,image=self.photoimg2)
        #img2.place(x=5,y=0,width=720,height=375)
        
        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="azure",relief=RIDGE)
        table_frame.place(x=0,y=0,width=726,height=527)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Department","Year","Sem","ID","Name","Section","Roll","DOB","Gender","Phone","Email","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Roll",text="Roll No.")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Phone",text="Phone No.")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="Photo")

        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)
        


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        
#============================Function Declaration============================

#==========Add Function=================
    def add_data(self):
            if self.var_Department.get()=="Select Department" or self.var_Name.get()=="" or self.var_ID.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Mansi@12345",database="student")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_Department.get(),
                                                                                                        self.var_Year.get(),
                                                                                                        self.var_Sem.get(),
                                                                                                        self.var_ID.get(),
                                                                                                        self.var_Name.get(),
                                                                                                        self.var_Section.get(),
                                                                                                        self.var_Roll.get(),
                                                                                                        self.var_DOB.get(),
                                                                                                        self.var_Gender.get(),
                                                                                                        self.var_Phone.get(),
                                                                                                        self.var_Email.get(),
                                                                                                        self.var_Address.get(),
                                                                                                        self.var_Teacher.get(),
                                                                                                        self.var_radio1.get()
                                                                                                        ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)

                except Exception as es:
                    messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root)


#============fetch function============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mansi@12345",database="student")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()





#=====================Get Cursor=====================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Department.set(data[0]),
        self.var_Year.set(data[1]),
        self.var_Sem.set(data[2]),
        self.var_ID.set(data[3]),
        self.var_Name.set(data[4]),
        self.var_Section.set(data[5]),
        self.var_Roll.set(data[6]),
        self.var_DOB.set(data[7]),
        self.var_Gender.set(data[8]),
        self.var_Phone.set(data[9]),
        self.var_Email.set(data[10]),
        self.var_Address.set(data[11]),
        self.var_Teacher.set(data[12]),
        self.var_radio1.set(data[13])


#========Update Function=========
    def update_data(self):
        if self.var_Department.get()=="Select Department" or self.var_Name.get()=="" or self.var_ID.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details.",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Mansi@12345",database="student")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Department=%s,Year=%s,Sem=%s,Name=%s,Section=%s,Roll=%s,DOB=%s,Gender=%s,Phone=%s,Email=%s,Address=%s,Teacher=%s,Photo=%s where ID=%s",(
                                                                                                                                                                                    self.var_Department.get(),
                                                                                                                                                                                    self.var_Year.get(),
                                                                                                                                                                                    self.var_Sem.get(),
                                                                                                                                                                                    self.var_Name.get(),
                                                                                                                                                                                    self.var_Section.get(),
                                                                                                                                                                                    self.var_Roll.get(),
                                                                                                                                                                                    self.var_DOB.get(),
                                                                                                                                                                                    self.var_Gender.get(),
                                                                                                                                                                                    self.var_Phone.get(),
                                                                                                                                                                                    self.var_Email.get(),
                                                                                                                                                                                    self.var_Address.get(),
                                                                                                                                                                                    self.var_Teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_ID.get()
                                                                                                                                                                                                            ))
                else:
                    if not Update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details updated successfully, Update Completed",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


#==========Delete Function========
    def delete_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete page","Do you want to delete this Student data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Mansi@12345",database="student")
                    my_cursor=conn.cursor()
                    sql="delete from student where ID=%s"
                    val=(self.var_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data
                conn.close()
                Student(self.root) 
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



#=========Reset Function==========
    def reset_data(self):
        self.var_Department.set("Select Department")
        self.var_Year.set("Select Year")
        self.var_Sem.set("Select Semester")
        self.var_ID.set("")
        self.var_Name.set("")
        self.var_Section.set("Select Section")
        self.var_Roll.set("")
        self.var_Gender.set("Select Gender")
        self.var_DOB.set("29/5/22")
        self.var_Email.set("")
        self.var_Phone.set("")
        self.var_Address.set("")
        self.var_Teacher.set("")
        self.var_radio1.set("")


#=========Take photo sample===========
    def generate_dataset(self):
        if self.var_Department.get()=="Select Department" or self.var_Name.get()=="" or self.var_ID.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Mansi@12345",database="student")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set Department=%s,Year=%s,Sem=%s,Name=%s,Section=%s,Roll=%s,DOB=%s,Gender=%s,Phone=%s,Email=%s,Address=%s,Teacher=%s,Photo=%s where ID=%s",(
                                                                                                                                                                                    self.var_Department.get(),
                                                                                                                                                                                    self.var_Year.get(),
                                                                                                                                                                                    self.var_Sem.get(),
                                                                                                                                                                                    self.var_Name.get(),
                                                                                                                                                                                    self.var_Section.get(),
                                                                                                                                                                                    self.var_Roll.get(),
                                                                                                                                                                                    self.var_DOB.get(),
                                                                                                                                                                                    self.var_Gender.get(),
                                                                                                                                                                                    self.var_Phone.get(),
                                                                                                                                                                                    self.var_Email.get(),
                                                                                                                                                                                    self.var_Address.get(),
                                                                                                                                                                                    self.var_Teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_ID.get()==id+1
                                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                
                #========Load predefined data on frontal face from open cv=========
                face_classifiers=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifiers.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                #Videocapture(0) for inbuilt camera
                #Videocapture(1) for external webcam
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data sets Completed!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)







if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()