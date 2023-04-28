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


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
         
         #top photo
        img_top=Image.open(r"logo and bg\t1.jpg")
        img_top=img_top.resize((1530,790),Image.ANTIALIAS) 
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=790)
        

        #button
        b1=Label(self.root,text="Click the button below to train data set.",font=("times new roman",16,"bold"),bg="black",fg="white")
        b1.place(x=590,y=340,height=30)
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",45,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        b1_1.place(x=0,y=370,width=1530,height=80)
    

        #exit button
        b8=Image.open(r"logo and bg\b8.jpg")
        b8=b8.resize((50,50),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(b8)

        b8=Button(self.root, image=self.photoimg8,command=self.Exit, cursor="hand2")
        b8.place(x=1450,y=700,width=50,height=50)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        
        faces=[]
        ids=[]
        

        for image in path:
            img=Image.open(image).convert('L')  #grey scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

        # train the classifier and save

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!",parent=self.root)

        
    #exit
    
        
    def Exit(self):
                self.Exit=messagebox.askyesno("Exit Window","Are you sure, you want to exit",parent=self.root)
                if self.Exit >0:
                        self.root.destroy()
                else:
                        return 


if __name__== "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()