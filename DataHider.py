from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os 
from stegano import lsb

root=Tk()
root.title("Steganography - Hide a Secret in an Image")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

def show_image():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File', 
                                        filetype=(("PNG file", "*.png"),("JPG file", "*.jpg"), ("All file", "*.txt")))
    img= Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image=img

def hide_data():
    global secret
    message= text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)


def show_data():
    clear_message = lsb.reveal(filename)
    text1.delete=(1.0, END)
    text1.insert(END,clear_message)

def save_image():
    secret.save("hidden.png")

#icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="lock.png")
Label(root,image=logo,bg="#2f4155").place(x=10, y=10)

Label(root,text="Elbaz Cyber Co.",bg="#2d4155", fg="white", font="arial 25 bold").place(x=70, y=12.5)

#First Frame
frame1= Frame(root,bd=3, bg="black", width=340, height= 280, relief=GROOVE)
frame1.place(x=10,y=80)

lbl= Label(frame1, bg="black")
lbl.place(x=40, y =10)

#Second Frame
frame2 = Frame(root, bd=3, width=340, height=280,bg="white",relief=GROOVE)
frame2.place(x=320,y=80)

text1=Text(frame2, font="Robote 20" , bg="white", fg="black", relief=GROOVE, wrap= WORD)
text1.place(x=0, y=0, width=319.8, height=280)

scrollbar1= Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#Third Frame
frame3= Frame(root,bd=3,bg="#2f4155", width= 310, height=100,relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3,text="Open Image", width=10,height=2, font= "arial 14 bold", command=show_image).place(x=15, y=28.5)
Button(frame3,text="Save Image", width=10,height=2, font= "arial 14 bold",command=save_image).place(x=165, y=28.5)
Label(frame3,text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=10, y= 2 )


#Fourth Frame
frame4= Frame(root,bd=3,bg="#2f4155", width= 310, height=100,relief=GROOVE)
frame4.place(x=320, y=370)

Button(frame4,text="Hide Data", width=10,height=2, font= "arial 14 bold",command=hide_data).place(x=15, y=28.5)
Button(frame4,text="Show Data", width=10,height=2, font= "arial 14 bold",command=show_data).place(x=165, y=28.5)
Label(frame4,text="Steganography", bg="#2f4155", fg="yellow").place(x=10, y= 2 )






root.mainloop()