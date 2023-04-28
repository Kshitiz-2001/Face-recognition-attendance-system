import imp
from tkinter import*
from tkinter import ttk
import cv2
from time import strftime
from datetime import datetime
from turtle import bgcolor
from PIL import Image,ImageTk
from cv2 import IMREAD_REDUCED_GRAYSCALE_2
from tkinter import messagebox
import mysql.connector
from tkcalendar import DateEntry
import os
import numpy as np
from student import Student
from train import Train
from face_recognition import Face_Recognition
from developer import About_Developer
from support import Support
from attendance import Attendance


class Face_recognition_system:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("Face Recognition System")


        #Upper Image
                img=Image.open(r"logo and bg\face.jpg")
                img=img.resize((1600,200),Image.ANTIALIAS)
                self.photoimg=ImageTk.PhotoImage(img)

                f_lbl=Label(self.root,image=self.photoimg)
                f_lbl.place(x=0,y=0,width=1600,height=200)

        #Lower Image
                img1=Image.open(r"logo and bg\bg1.jpg")
                img1=img1.resize((1600,600),Image.ANTIALIAS)
                self.photoimg0=ImageTk.PhotoImage(img1)

                bg_img=Label(self.root,image=self.photoimg0)
                bg_img.place(x=0,y=200,width=1600,height=600)

        #main tile
                title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman",35,"bold"),bg="white", fg="red")
                title_lbl.place(x=0,y=0,width=1535,height=35)

        #student button
                b1=Image.open(r"logo and bg\b1.png")
                b1=b1.resize((220,220),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(b1)

                b1=Button(bg_img, image=self.photoimg1, command=self.Student_details, cursor="hand2")
                b1.place(x=497,y=320,width=220,height=220)

                b1_1=Button(bg_img, text="Student Details",  command=self.Student_details, font=("times new roman",15,"bold"),bg="white", fg="red", cursor="hand2")
                b1_1.place(x=497,y=540,width=220,height=20)

        #face recognition
                b2=Image.open(r"logo and bg\b2.png")
                b2=b2.resize((220,220),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(b2)

                b2=Button(bg_img, image=self.photoimg2,command=self.face_recognition, cursor="hand2")
                b2.place(x=170,y=80,width=220,height=220)

                b2_1=Button(bg_img, text="Face Recognition",command=self.face_recognition,font=("times new roman",15,"bold"),bg="white", fg="red", cursor="hand2")
                b2_1.place(x=170,y=300,width=220,height=20)

        #Attendance button
                b3=Image.open(r"logo and bg\b3.jpeg")
                b3=b3.resize((220,220),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(b3)

                b3=Button(bg_img, image=self.photoimg3,command=self.attendance, cursor="hand2")
                b3.place(x=1150,y=80,width=220,height=220)

                b3_1=Button(bg_img, text="Attendance Details",command=self.attendance,font=("times new roman",15,"bold"),bg="white", fg="red", cursor="hand2")
                b3_1.place(x=1150,y=300,width=220,height=20)

        #Train Data Button
                b4=Image.open(r"logo and bg\b4.jpg")
                b4=b4.resize((220,220),Image.ANTIALIAS)
                self.photoimg4=ImageTk.PhotoImage(b4)

                b4=Button(bg_img, image=self.photoimg4,command=self.train_data, cursor="hand2")
                b4.place(x=824,y=320,width=220,height=220)

                b4_1=Button(bg_img, text="Train Data",command=self.train_data,font=("times new roman",15,"bold"),bg="white", fg="red", cursor="hand2")
                b4_1.place(x=824,y=540,width=220,height=20)

        #About Developer
                b6=Image.open(r"logo and bg\b6.jpg")
                b6=b6.resize((50,50),Image.ANTIALIAS)
                self.photoimg6=ImageTk.PhotoImage(b6)

                b6=Button(bg_img, image=self.photoimg6,command=self.developer, cursor="hand2")
                b6.place(x=1450,y=400,width=50,height=50)

        #Helpdesk
                b7=Image.open(r"logo and bg\b7.jpg")
                b7=b7.resize((50,50),Image.ANTIALIAS)
                self.photoimg7=ImageTk.PhotoImage(b7)

                b7=Button(bg_img, image=self.photoimg7,command=self.support, cursor="hand2")
                b7.place(x=1450,y=450,width=50,height=50)

        #Exit
                b8=Image.open(r"logo and bg\b8.jpg")
                b8=b8.resize((50,50),Image.ANTIALIAS)
                self.photoimg8=ImageTk.PhotoImage(b8)

                b8=Button(bg_img, image=self.photoimg8,command=self.Exit, cursor="hand2")
                b8.place(x=1450,y=500,width=50,height=50)
        
        #=============Functions===============

        def Student_details(self):
                self.new_window=Toplevel(self.root)
                self.app=Student(self.new_window)
                
        
        #Train Data Button function

        def train_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Train(self.new_window)


        #Face Recognition button function   
        def face_recognition(self):
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition(self.new_window)

        #attendance details button function   
        def attendance(self):
                self.new_window=Toplevel(self.root)
                self.app=Attendance(self.new_window)

        #About Developer button function
        def developer(self):
                self.new_window=Toplevel(self.root)
                self.app=About_Developer(self.new_window)

        #Support button function
        def support(self):
                self.new_window=Toplevel(self.root)
                self.app=Support(self.new_window)
        
        
        #Exit button function
        def Exit(self):
                self.Exit=messagebox.askyesno("Exit Window","Are you sure, you want to exit",parent=self.root)
                if self.Exit >0:
                        self.root.destroy()
                else:
                        return 



        


if __name__== "__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()
