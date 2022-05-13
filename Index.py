from pickle import GLOBAL
from tkinter import *
import tkinter.messagebox as m
import mysql.connector


# CREATE TABLE users ( id INT(6) AUTO_INCREMENT PRIMARY KEY null, username VARCHAR(30) NOT NULL UNIQUE, password VARCHAR(30) NOT NULL, email VARCHAR(50) );
# SELECT MAX(id) FROM users;

# for x in mycursorObject:
#  print (x)

# UPDATE users
# SET `password` = 2

# WHERE users.id = ( SELECT MAX(users.id)FROM users);


def All_page():
    my = mysql.connector.connect(  
    host  = "localhost",
    user = "root",
    password = "",
    database = "dashboard"

)

    w = Tk()
    w.title(string='Dashboard')
    w.geometry('300x400')

    def Register_page():
        def Home_page():     
            Home = Tk()
            Home.title(string='Home Page')
            Home.geometry('300x400') 

            def Destorypage():
              Home.destroy()

            def updatedata():
                newpassword = e1.get()
                mycursorObject=my.cursor()
                Querycode = f"UPDATE users SET users.password = '{newpassword}' WHERE users.id = ( SELECT MAX(users.id)FROM users)"
                mycursorObject.execute(Querycode)
                my.commit()

                m.showinfo("Done","Password successfully changed")
            def deletedata():
                answer = m.askyesno("Are You Sure ?"," You Want to Delete Your account")
                if answer == TRUE:
                 mycursorObject=my.cursor()
                 Querycode = "DELETE FROM users WHERE users.id = ( SELECT MAX(users.id)FROM users)"
                 mycursorObject.execute(Querycode)
                 my.commit()

                 Home.destroy()
                 All_page()
            label1 = Label(Home,text='Change Your Password')
            label1.pack()
            label1.configure(font=("Segoe UI", 10, "italic"))

            e1 = Entry(Home , fg='red')
            e1.pack(pady=5)
            b1 = Button( Home, text='Update' ,width=15 ,height=1,bg='green',fg='white',command=updatedata)
            b1.pack( pady=10)
            b1 = Button( Home, text='Delete My Acc' ,width=15 ,height=1,bg='green',fg='white' ,command=deletedata)
            b1.pack( pady=10)
            b1 = Button( Home, text='Log_Out' ,width=15 ,height=1,bg='green',fg='white', command=lambda: [Destorypage(), All_page()])
            b1.pack( pady=10)
            Regist.destroy()
            

        

             
        def insertdata():
          try:
           if(e1.get() =='' or e2.get()==''or e4.get()==''):
             m.showwarning("All Data Requerid","Enter All Data")
           else: 
                mycursorObject=my.cursor()
                username =  e1.get()
                password= e2.get()
                confrimpassword = e3.get()
                email = e4.get()

                if(password == confrimpassword):    
                 Querycode = f"INSERT INTO users(username,password,email)VALUES('{username}','{password}','{email}')"
                 mycursorObject.execute(Querycode)

                 my.commit()
                 Home_page()
                else:
                  m.showwarning("Match_Password","write Same Password")
          except mysql.connector.errors.IntegrityError:
              m.showerror("Not Allow","This UserName Is Used")


        Regist = Tk()
        Regist.title(string='Register Page')
        Regist.geometry('300x400')
        def Destorypage():
            Regist.destroy()

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
        e3 = Entry(Regist , fg='red', show="*")
        e3.pack(pady=5)

        label4 = Label(Regist,text='Enter Your E-mail')
     
        label4.pack()
        label4.configure(font=("Segoe UI", 10, "italic"))
        e4 = Entry(Regist , fg='red')
        e4.pack(pady=5)
        b1 = Button( Regist, text='Submit' ,width=15 ,height=1,bg='green',fg='white' ,command=lambda: [insertdata()])
        b1.pack( pady=10)
        b2 = Button( Regist, text='Back' ,width=15 ,height=1,bg='green',fg='white',command=lambda: [Destorypage(), All_page()])
        b2.pack(pady=60)
        w.destroy()
        



    def Login_page():
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
            Login.destroy()
      
        def insertdata():
        #   try:
           if(e1.get() =='' or e2.get()==''):
             m.showwarning("All Data Missing","All Data required")
           else: 
                mycursorObject=my.cursor()
                mycursorObject1=my.cursor()
                username =  e1.get()
                password= e2.get()

                Querycode ='Select username from users'
                mycursorObject.execute(Querycode)
                for User in mycursorObject:
                 if User == (f'{username}',):
                     print("yes user")
                Querycode1 ='Select password from users'
                mycursorObject1.execute(Querycode1)
                for passw in mycursorObject1:
                 if passw == (f'{password}',):
                     print("yes pass")
                     Home_page()
                     break 
                    
        #         
        #         else:
        #           m.showwarning("Match_Password","write Same Password")
        #   except mysql.connector.errors.IntegrityError:
        #       m.showerror("Not Allow","This UserName Is Used")


        Login = Tk()
        Login.title(string='Register Page')
     
        Login.geometry('300x400') 
     
        def Destorypage():
            Login.destroy()

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
        b1 = Button( Login, text='Submit' ,width=15 ,height=1,bg='green',fg='white' ,command=insertdata)
        
        b1.pack( pady=10)
        b2 = Button( Login, text='Back' ,width=15 ,height=1,bg='green',fg='white',command=lambda: [Destorypage(), All_page()])
        
        b2.pack(pady=110)

        w.destroy()

    label1 = Label(w,text=' Welcome To Dashboard')
    label1.grid()

    label1.configure(font=("Courier", 16, "italic"))



    b1 = Button( w, text='Login' ,width=20,height=5 ,bg='green',fg='white' , command=Login_page).grid(pady=15)
    b2 = Button( w, text='Register' ,width=20 ,height=5,bg='green',fg='white' ,command=Register_page).grid()

    w.mainloop()
All_page()
