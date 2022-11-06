from tkinter import *
from functools import partial
import sqlite3

def validateLogin(username,password):
        U = username.get()
        P = password.get()
        rot13 = str.maketrans(
                'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
                'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
        encrypt = P.translate(rot13)
        print("Updated in the sqlite")
        query='''INSERT INTO ROT13 VALUES ("'''+U+'''"'''+''',"'''+encrypt+'''")'''
        cursor_obj.execute(query)

def show():
        statement = '''SELECT * FROM ROT13'''
        cursor_obj.execute(statement)
        output = cursor_obj.fetchall()
        for row in output:
                print(row)

'''sqlite'''
connection_obj = sqlite3.connect('rot13.db')
cursor_obj = connection_obj.cursor()
table = """ CREATE TABLE IF NOT EXISTS ROT13 ( Username VARCHAR(20),
        Encrypted VARCHAR(20)
        ); """
cursor_obj.execute(table)
print("Table is Ready")


'''Window'''
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Password Manager')

'''username label and text entry box'''
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
Password = StringVar()
k= Password
passwordEntry = Entry(tkWindow, textvariable=Password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, Password)
show = partial(show)

#login button
loginButton = Button(tkWindow, text="Add", command=validateLogin).grid(row=4, column=0)
showButton = Button(tkWindow, text="Show", command=show).grid(row=4, column=6)

tkWindow.mainloop()
