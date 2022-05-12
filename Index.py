from tkinter import *
import tkinter.messagebox as m


w = Tk()
w.title(string='Dashboard')
w.geometry('300x400')

def Register_page():
    Regist = Tk()
    Regist.title(string='Register Page')
    Regist.geometry('300x400')


    label1 = Label(Regist,text='Enter Your UserName')
    label1.pack()
    label1.configure(font=("Segoe UI", 10, "italic"))
    
    e1 = Entry(Regist , fg='red')
    e1.pack(pady=5)

    label2 = Label(Regist,text='Enter Your Password')
    label2.pack()
    label2.configure(font=("Segoe UI", 10, "italic"))
    e2 = Entry(Regist , fg='red', show="*")
    e2.pack(pady=5)
    label3 = Label(Regist,text='Enter Con_Password')
    label3.pack()
    label3.configure(font=("Segoe UI", 10, "italic"))
    e2 = Entry(Regist , fg='red', show="*")
    e2.pack(pady=5)

    label4 = Label(Regist,text='Enter Your E-mail')
    label4.pack()
    label4.configure(font=("Segoe UI", 10, "italic"))
    e3 = Entry(Regist , fg='red')
    e3.pack(pady=5)

    b1 = Button( Regist, text='Submit' ,width=15 ,height=1,bg='green',fg='white' ,command=Home_page)
    b1.pack( pady=10)
    b2 = Button( Regist, text='Back' ,width=15 ,height=1,bg='green',fg='white')
    b2.pack(pady=60)
    w.destroy()
    


def Login_page():
    Login = Tk()
    Login.title(string='Register Page')
    Login.geometry('300x400') 

    label1 = Label(Login,text='Enter Your UserName')
    label1.pack()
    label1.configure(font=("Segoe UI", 10, "italic"))
    
    e1 = Entry(Login , fg='red')
    e1.pack(pady=5)

    label2 = Label(Login,text='Enter Your Password')
    label2.pack()
    label2.configure(font=("Segoe UI", 10, "italic"))
    e2 = Entry(Login , fg='red', show="*")
    e2.pack(pady=5)
    b1 = Button( Login, text='Submit' ,width=15 ,height=1,bg='green',fg='white' ,command=Home_page)
    b1.pack( pady=10)
    b2 = Button( Login, text='Back' ,width=15 ,height=1,bg='green',fg='white')
    b2.pack(pady=110)

    w.destroy()


def Home_page():
    Home = Tk()
    Home.title(string='Home Page')
    Home.geometry('300x400') 
    
    label1 = Label(Home,text='Change Your UserName')
    label1.pack()
    label1.configure(font=("Segoe UI", 10, "italic"))
    
    e1 = Entry(Home , fg='red')
    e1.pack(pady=5)
    b1 = Button( Home, text='Update' ,width=15 ,height=1,bg='green',fg='white')
    b1.pack( pady=10)
    b1 = Button( Home, text='Delete My Acc' ,width=15 ,height=1,bg='green',fg='white')
    b1.pack( pady=10)
    b1 = Button( Home, text='Log_Out' ,width=15 ,height=1,bg='green',fg='white')
    b1.pack( pady=10)
    
    


label1 = Label(w,text=' Welcome To Dashboard')
label1.grid()

label1.configure(font=("Courier", 16, "italic"))



b1 = Button( w, text='Login' ,width=20,height=5 ,bg='green',fg='white' , command=Login_page).grid(pady=15)
b2 = Button( w, text='Register' ,width=20 ,height=5,bg='green',fg='white' ,command=Register_page).grid()

w.mainloop()