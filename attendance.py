from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk     
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import numpy as np
from tkinter import filedialog
import csv


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

#==================Variables=================
        self.var_ID=StringVar()
        self.var_Roll=StringVar()
        self.var_Name=StringVar() 
        self.var_Department=StringVar()
        self.var_Time=StringVar() 
        self.var_Date=StringVar() 
        self.var_Attendance=StringVar()
  
         #first image
        img_1=Image.open(r"logo and bg\a2.jpg")
        img_1=img_1.resize((800,250),Image.ANTIALIAS) 
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        f_lbl=Label(self.root,image=self.photoimg_1)
        f_lbl.place(x=0,y=0,width=760,height=250)
         

         #second image
        img_2=Image.open(r"logo and bg\a4.jpg")
        img_2=img_2.resize((800,250),Image.ANTIALIAS) 
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        

        f_lbl=Label(self.root,image=self.photoimg_2)
        f_lbl.place(x=760,y=0,width=800,height=250)

         #bg image
        img3=Image.open(r"logo and bg\s2.jpg")
        img3=img3.resize((1545,730),Image.ANTIALIAS) 
        self.photoimg3=ImageTk.PhotoImage(img3)
        

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=-5,y=220,width=1545,height=710)

        title_lbl=Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1540,height=45)


        frame=Frame(f_lbl,bd=2,bg="white")
        frame.place(x=20,y=20,width=1490,height=520)
         

         #left label frame
        left_frame=LabelFrame(frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",13,"bold"),fg="black")
        left_frame.place(x=10,y=10,width=730,height=500)

        img_left=Image.open(r"logo and bg\a1.jpg")
        img_left=img_left.resize((730,500),Image.ANTIALIAS) 
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=730,height=500)

        #Student ID
        id_label=Label(left_frame,text='Student ID:',font=("times new roman",14,"bold"),bg="white")
        id_label.grid(row=1,column=0,padx=10,pady=25,sticky=W)

        id_entry=ttk.Entry(left_frame,textvariable=self.var_ID,width="17",font=("times new roman",14))
        id_entry.grid(row=1,column=1,padx=10,pady=25,sticky=W)

        #student Roll
        roll_label=Label(left_frame,text='Student Roll:',font=("times new roman",14,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,pady=25,sticky=W)

        roll_entry=ttk.Entry(left_frame,textvariable=self.var_Roll,width="17",font=("times new roman",14))
        roll_entry.grid(row=1,column=3,padx=10,pady=25,sticky=W)

        #Name
        name_label=Label(left_frame,text='Name:',font=("times new roman",14,"bold"),bg="white")
        name_label.grid(row=3,column=0,padx=10,pady=25,sticky=W)

        name_entry=ttk.Entry(left_frame,textvariable=self.var_Name,width="17",font=("times new roman",14))
        name_entry.grid(row=3,column=1,padx=10,pady=25,sticky=W)

        #department
        dep_label=Label(left_frame,text='Department:',font=("times new roman",14,"bold"),bg="white")
        dep_label.grid(row=3,column=2,padx=10,pady=25,sticky=W)

        dep_entry=ttk.Entry(left_frame,textvariable=self.var_Department,width="17",font=("times new roman",14,))
        dep_entry.grid(row=3,column=3,padx=10,pady=25,sticky=W)

        #Time
        time_label=Label(left_frame,text='Time:',font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=5,column=0,padx=10,pady=25,sticky=W)

        time_entry=ttk.Entry(left_frame,textvariable=self.var_Time,width="17",font=("times new roman",12,))
        time_entry.grid(row=5,column=1,padx=10,pady=25,sticky=W)

        #Date
        date_label=Label(left_frame,text='Date:',font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=5,column=2,padx=10,pady=25,sticky=W)

        date_entry=ttk.Entry(left_frame,textvariable=self.var_Date,width="17",font=("times new roman",12,))
        date_entry.grid(row=5,column=3,padx=10,pady=25,sticky=W)

        #Attendance Status
        status_label=Label(left_frame,text='Status:',font=("times new roman",12,"bold"),bg="white")
        status_label.grid(row=7,column=0,padx=10,pady=25,sticky=W)
        
        status_entry=ttk.Entry(left_frame,textvariable=self.var_Attendance,width="17",font=("times new roman",12,))
        status_entry.grid(row=7,column=1,padx=10,pady=25,sticky=W)

        #buttonframe1
        b_frame=Frame(left_frame,bd=2,relief=RIDGE)
        b_frame.place(x=90,y=350,width=537,height=45)

        #Import CSV
        import_btn=Button(b_frame,command=self.importCsv,text="Import csv",width=14,font=("times new roman",16,"bold"),bg="orange",fg="Black")
        import_btn.grid(row=0,column=0)

        #Export CSV
        export_btn=Button(b_frame,command=self.exportCsv,text="Export csv",width=14,font=("times new roman",16,"bold"),bg="orange",fg="Black")
        export_btn.grid(row=0,column=1)


        #reset
        reset_btn=Button(b_frame,command=self.reset_data,text="Reset",width=14,font=("times new roman",16,"bold"),bg="orange",fg="Black")
        reset_btn.grid(row=0,column=2)



        #rightframe
        right_frame=LabelFrame(frame,text="Attendance Details",bd=2,relief=RIDGE,font=("times new roman",12,"bold"),bg="white")
        right_frame.place(x=740,y=10,width=730,height=500)

      
        #Table frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=720,height=470) 

        #scrollbars
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("ID","Roll","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("ID",text="Student ID")
        self.AttendanceReportTable.heading("Roll",text="Roll No")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance Status")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("ID",width=100)
        self.AttendanceReportTable.column("Roll",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=150)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)



#=======================Fetch Data Function============

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    
    #import csv function
    def importCsv(self):
        global mydata
        mydata.clear()
        file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(file_name) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
        img_4=Image.open(r"logo and bg\a3.jpg")
        img_4=img_4.resize((800,250),Image.ANTIALIAS) 
        self.photoimg_4=ImageTk.PhotoImage(img_4)
        

        f_lbl=Label(self.root,image=self.photoimg_4)
        f_lbl.place(x=760,y=45,width=800,height=175)


    #export csv function
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False

            file_name=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(file_name,mode="w",newline="") as myfile:
                export_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export_write.writerow(i)
                messagebox.showinfo("Success","Your Data is exported to" +os.path.basename(file_name)+ "successfully",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root)


        
    #=======Get cursor============
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_ID.set(rows[0])   
        self.var_Roll.set(rows[1])  
        self.var_Name.set(rows[2])  
        self.var_Department.set(rows[3])  
        self.var_Time.set(rows[4])  
        self.var_Date.set(rows[5])  
        self.var_Attendance.set(rows[6]) 


    #reset function
    def reset_data(self):
        self.var_ID.set("")   
        self.var_Roll.set("")  
        self.var_Name.set("")  
        self.var_Department.set("")  
        self.var_Time.set("")  
        self.var_Date.set("")  
        self.var_Attendance.set("")
         
         


if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
