# Password Manager
Password Manager is a small project for python beginners which implements encryption algorithm called ROT 13.
## Description
Password Manager is a Graphical User Interface program which asks a username and password from the user and it encrypts the password using the encryption algorithm ROT13 and stores username and password in a database . This project is completely based on Python version 3.
## Background Study
### TKinter
Tkinter is the most commonly used library for developing GUI (Graphical User Interface) in Python. It is a standard Python interface to the Tk GUI toolkit shipped with Python. As Tk and Tkinter are available on most of the Unix platforms as well as on the Windows system, developing GUI applications with Tkinter becomes the fastest and easiest.
### ROT13 Algorithm
**ROT13** (a variant of the Caesar method) is a very simple text encryption algorithm. As its name suggests, it involves shifting each letter of the text to be encrypted by 13 characters.**The drawback of this encryption is that if it takes care of letters, it does not take care of numbers, symbols, and punctuation**.

n The Julius Caesar Encryption where the encryption key is N (13th letter of the alphabet), this encryption is called ROT13 (the number 13, half of 26, was chosen to be able to easily encrypt and decrypt text messages).

Example for ROT13 Algorithm : Suppose, an user enter a password i.e., **Helloworld**, It will encrypt the password as **Uryybjbeyq**.

### SQLITE
Python SQLite3 module is used to integrate the SQLite database with Python. It is a standardized Python DBI API 2.0 and provides a straightforward and simple-to-use interface for interacting with SQLite databases. There is no need to install this module separately as it comes along with Python after the 2.5x version.

## Implementation
This is a Graphical User Interface program which collects username and password from the user and it encrypts the password using textboxes. There are two buttons like Add and Show. Add button is used to encrypt the password and stores encrypted password along with username. Show button is used to see encrypted passwords. The image of the window is show below:

![image](https://user-images.githubusercontent.com/72243394/200180454-7d44adfe-f7ac-4afe-b56a-9915ee043be9.png)

### Functions
**ValidateLogin()** - This function is invoked when the Add button is clicked. It encrypts the password using ROT 13 encryption algorithm and stores in a database. 

**show()** - This function is invoked when the show button is clicked. It shows the username and encrypted password.

## Conclusion
Final Output of the project will be storing and viewing encrypted passwords and their username respectively. Sample output is shown below:

![image](https://user-images.githubusercontent.com/72243394/200180929-ff263b22-9002-47f6-816d-82e80e125e3f.png)

©Arjun_S_Prasad

