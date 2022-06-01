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

    # CREATE TABLE users ( id INT(6) AUTO_INCREMENT PRIMARY KEY null, username VARCHAR(30) NOT NULL UNIQUE, password VARCHAR(30) NOT NULL, email VARCHAR(50) );
    # SELECT MAX(id) FROM users;

    # for x in mycursorObject:
    #  print (x)

    # UPDATE users
    # SET `password` = 2

    # WHERE users.id = ( SELECT MAX(users.id)FROM users);

    # UPDATE users
    # SET `password` = 2

    # WHERE users.id = ( SELECT MAX(users.id)FROM users);

try:
    def All_page():
        my = mysql.connector.connect(  
        host  = "localhost",
        user = "root",
        password = "",
    

    )

        try:
            mycursorObject=my.cursor()
            Querycode = "create database dashboard"
            mycursorObject.execute(Querycode)
            my.commit()

        except mysql.connector.errors.DatabaseError:
            print("database")
        try:
                mycursorObject1=my.cursor()
                Querycode0 = "CREATE TABLE dashboard.users ( id INT(6) AUTO_INCREMENT PRIMARY KEY null, username VARCHAR(30) NOT NULL UNIQUE, password VARCHAR(30) NOT NULL, email VARCHAR(50) , usertype varchar(30) DEFAULT 'false' );"
                Querycode1 = "INSERT INTO dashboard.users(username,password,email,usertype)VALUES('Admin','1','@AdminDashboard','True')"
                mycursorObject.execute(Querycode0)
                mycursorObject.execute(Querycode1)
                my.commit()
        except:
                print("found table")


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
                    Querycode = f"UPDATE dashboard.users SET users.password = '{newpassword}' WHERE dashboard.users.id = ( SELECT MAX(users.id)FROM dashboard.users)"
                    mycursorObject.execute(Querycode)
                    my.commit()

                    m.showinfo("Done","Password successfully changed")
                def deletedata():
                    answer = m.askyesno("Are You Sure ?"," You Want to Delete Your account")
                    if answer == TRUE:
                     mycursorObject=my.cursor()
                     Querycode = "DELETE FROM dashboard.users WHERE users.id = ( SELECT MAX(dashboard.users.id)FROM dashboard.users)"
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
                     Querycode = f"INSERT INTO dashboard.users(username,password,email)VALUES('{username}','{password}','{email}')"
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
            def Home_page(Username):  
                name = Username
                Home = Tk()
                Home.title(string='Home Page')
                Home.geometry('300x400') 
                def Destorypage():
                  Home.destroy()


                def updatedata():
                    New_Email = e1.get()
                    mycursorObject=my.cursor()
                    Querycode = f"UPDATE dashboard.users SET users.email = '{New_Email}' WHERE dashboard.users.username = '{name}'"
                    mycursorObject.execute(Querycode)
                    my.commit()
                    m.showinfo("Done","Password successfully changed")


                def deletedata():
                    answer = m.askyesno("Are You Sure ?"," You Want to Delete Your account")
                    if answer == TRUE:
                     mycursorObject=my.cursor()
                     Querycode = f"DELETE FROM dashboard.users WHERE dashboard.users.username = '{name}'"
                     mycursorObject.execute(Querycode)
                     my.commit()
                     Home.destroy()
                     All_page()
                label1 = Label(Home,text='Change Your Email')
                label1.pack()
                label1.configure(font=("Segoe UI", 10, "italic"))


                e1 = Entry(Home , fg='red')
                e1.pack(pady=5)
                b1 = Button( Home, text='Update' ,width=15 ,height=1,bg='green',fg='white',command=updatedata)
                b1.pack( pady=10)
                b1 = Button( Home, text='Delete My Acc' ,width=15 ,height=1,bg='green',fg='white',command=deletedata)
                b1.pack( pady=10)
                b1 = Button( Home, text='Log_Out' ,width=15 ,height=1,bg='green',fg='white',command=lambda: [Destorypage(), All_page()])
                b1.pack( pady=10)
                Login.destroy()


            def insertdata():
            #   try:
               if(e1.get() =='' or e2.get()==''):
                 m.showwarning("All Data Missing","All Data required")
               else: 
                    mycursorObject=my.cursor()
                    mycursorObject1=my.cursor()
                    mycursor = my.cursor()
                    username =  e1.get()
                    password= e2.get()


                    Querycode ='Select username from dashboard.users'
                    mycursorObject.execute(Querycode)
                    for User in mycursorObject:
                      if User == (f'{username}',):
                         print("yes user")
                         
                    #  else:
                    #      m.showinfo("User Not_Found" ,"This User Is wrong")  
                    Querycode1 ="SELECT password FROM dashboard.users"
                    mycursorObject1.execute(Querycode1)
                    for passw in mycursorObject1:
                      if passw == (f'{password}',):
                         print("yes pass")
                        

                          
                    #   else:
                    #      m.showinfo("Wrong Password" ,"This Password Is wrong")
                    mycursor.execute("SELECT username , password , usertype FROM dashboard.users")

                    myresult = mycursor.fetchall()
                    
                    for User in myresult:
                     if User[0] == username  and User[1]==password and User[2] == 'false':
                           Home_page(username)
                           break
                     elif(User[0] == username  and User[1]==password and User[2] == 'True'):
                         adminboard()
                         Login.destroy()
                         break
                    else:
                       m.showerror('something is wrong ',' User or password Is wrong') 



            def adminboard():
                admin = Tk()
                admin.title(string='Home Page')
                admin.geometry('600x600') 



                l1 = Label(admin , text='Welcome to admin dashboard')
                l1.pack()

                l2 = Label(admin , text='Enter any user_Id')
                l2.pack()

                
                e1 = Entry(admin)
                e1.pack()


                b1 = Button( admin, text='Delete' ,width=15 ,height=1,bg='green',fg='white',command=lambda: [ deletedata()])
                b1.pack(pady=10)
                b3 = Button( admin, text='Back' ,width=15 ,height=1,bg='green',fg='white',command=lambda: [Destorypage(), All_page()])
                b3.pack()
                b1 = Button( admin, text='Show Data' ,width=15 ,height=1,bg='green',fg='white',command=lambda: [ ShowData()])
                b1.pack(side="bottom")


                
                def deletedata():
                    answer = m.askyesno("Are You Sure ?"," You Want to Delete Your account")
                    if answer == TRUE:
                     mycursorObject=my.cursor()
                     Querycode = f"DELETE FROM dashboard.users WHERE users.id = {int(e1.get())}"
                     mycursorObject.execute(Querycode)
                     my.commit()
                     m.showinfo("Done","User Deleted")

                
                def Destorypage():
                 admin.destroy()
                
                
                def ShowData():
                    
                    mycursor = my.cursor()

                    mycursor.execute("SELECT * FROM dashboard.users")

                    myresult = mycursor.fetchall()
                    showddata = ""
                    for i in myresult:
                        # if(i == (1, 'admin', '1', 'admin', 1)):
                        #     continue
                        # else:
                            # print(i)
                            print(i)
                            showddata +='Id is : '+str(i[0])+" "+'User is :' + i[1]+" "+'password is :' + i[2]+" "+'Email iS : ' +i[3]+" "+'Usertype is : '+ str(i[4])+"\n"
                            
                            
                    l1.config(text=showddata)



                
            #         
            #         else:
            #           m.showwarning("Match_Password","write Same Password")
            #   except mysql.connector.errors.IntegrityError:
            #       m.showerror("Not Allow","This UserName Is Used")



            #         else:
            #         else:
            #         else:
            #           m.showwarning("Match_Password","write Same Password")
            #           m.showwarning("Match_Password","write Same Password")
            #           m.showwarning("Match_Password","write Same Password")
            #   except mysql.connector.errors.IntegrityError:
            #   except mysql.connector.errors.IntegrityError:
            #   except mysql.connector.errors.IntegrityError:
            #       m.showerror("Not Allow","This UserName Is Used")
            #       m.showerror("Not Allow","This UserName Is Used")
            #       m.showerror("Not Allow","This UserName Is Used")


            Login = Tk()
            Login.title(string='Register Page')

            Login.geometry('300x500') 

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
            # b2 = Button( Login, text='admin' ,width=15 ,height=1,bg='green',fg='white',command=lambda: [Destorypage(), adminboard()])
            # b2.pack(side="left")


            w.destroy()

        label1 = Label(w,text=' Welcome To Dashboard')
        label1.grid()

        label1.configure(font=("Courier", 16, "italic"))



        b1 = Button( w, text='Login' ,width=20,height=5 ,bg='green',fg='white' , command=Login_page).grid(pady=15)
        b2 = Button( w, text='Register' ,width=20 ,height=5,bg='green',fg='white' ,command=Register_page).grid()

        w.mainloop()
    All_page()
    
    
    
except  mysql.connector.errors.DatabaseError:
     m.showinfo("Xammp Needed","Open Xammp And Start Appache with Database")
