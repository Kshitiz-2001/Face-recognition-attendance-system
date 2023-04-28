from tkinter import*
from tkinter import ttk
import cv2
from time import strftime
from datetime import datetime
from turtle import bgcolor
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkcalendar import DateEntry
import webbrowser



class About_Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("600x400+450+200")
        self.root.title("About Developer")


#bg img
        img1=Image.open(r"C:\Users\kshitiz\Pictures\Predator\Predator_3840x2160.jpg")
        img1=img1.resize((600,400),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=600,height=400)


#main tile
        title_lbl=Label(self.root,text="ABOUT DEVELOPER",font=("calibri",35,"bold"),bg="azure",fg="red")
        title_lbl.place(x=0,y=0,width=600,height=35)

#text
        title_lbl1=Label(self.root,text="My name is Mansi Rao.", font=("times new roman",14,"bold"))
        title_lbl1.place(x=0,y=50,height=20)
        title_lbl2=Label(self.root,text="currently pursuing Bachelor of Technology in Information Technology", font=("times new roman",14,"bold"))
        title_lbl2.place(x=0,y=70,height=20)
        title_lbl3=Label(self.root,text="from ABES Engineering College, Ghaziabad", font=("times new roman",14,"bold"))
        title_lbl3.place(x=0,y=90,height=20)


#callbak function
        def callback(url):
                webbrowser.open_new(url)

#mail to function
        def mailto():
                webbrowser.open("mailto:?to=raomansi126@gmail.com&subject=support", new=1)


#contact
        link1=Label(self.root,text="Insta:", font=("times new roman",14,"bold"))
        link1.place(x=0,y=150,height=20)

        link1_1 = Label(root, text="mansi____rao", fg="blue", cursor="hand2")
        link1_1.pack()
        link1_1.bind("<Button-1>", lambda e: callback("https://instagram.com/mansi____rao?igshid=YmMyMTA2M2Y="))
        link1_1.place(x=100,y=150,height=20)


        link2=Label(self.root,text="Email me:", font=("times new roman",14,"bold"))
        link2.place(x=0,y=180,height=20)

        link2_1 = Label(root, text="Email me", fg="blue", cursor="hand2")
        link2_1.pack()
        link2_1.bind("<Button-1>", lambda e: mailto())
        link2_1.place(x=100,y=180,height=20)


#exit
        B8=Image.open(r"logo and bg\b8.jpg")
        B8=B8.resize((50,50), Image.ANTIALIAS)
        self.photoB8=ImageTk.PhotoImage(B8)

        b8=Button(self.root,command=self.iExit,image=self.photoB8,cursor="hand2",bg="black")
        b8.place(x=500,y=300,width=50,height=50)

    def iExit(self):
                self.iExit=messagebox.askyesno("Exit Window","Are you sure, you want to exit",parent=self.root)
                if self.iExit >0:
                        self.root.destroy()
                else:
                        return  



if __name__== "__main__":
    root=Tk()
    obj=About_Developer(root)
    root.mainloop()