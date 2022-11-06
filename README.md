# Password Manager
Password Manager is a small project for python beginners which includes encryption algorithm called rot 13 and also tkinter is used.
## Description
Password Manager is a Graphical User Interface program which asks a username and password from the user and it encrypts the password using the algorithm ROT13. This project is completely based on Python version 3.
## TKinter
Tkinter is the most commonly used library for developing GUI (Graphical User Interface) in Python. It is a standard Python interface to the Tk GUI toolkit shipped with Python. As Tk and Tkinter are available on most of the Unix platforms as well as on the Windows system, developing GUI applications with Tkinter becomes the fastest and easiest.
## ROT13 Algorithm
**ROT13** (a variant of the Caesar method) is a very simple text encryption algorithm. As its name suggests, it involves shifting each letter of the text to be encrypted by 13 characters.**The drawback of this encryption is that if it takes care of letters, it does not take care of numbers, symbols, and punctuation**.

n The Julius Caesar Encryption where the encryption key is N (13th letter of the alphabet), this encryption is called ROT13 (the number 13, half of 26, was chosen to be able to easily encrypt and decrypt text messages).

Example for ROT13 Algorithm : Suppose, an user enter a password i.e., **Helloworld**, It will encrypt the password as **Uryybjbeyq**.

## Implementation
There are two programs , one is a GUI program which is used create the login window, which consisting of two textboxes and a login button. First text box is used to enter the username. Second text box is used to enter the password. The password will not be seen. It will be seen in a set of * character only.  The image of the login window is shown below:

![image](https://user-images.githubusercontent.com/72243394/200178520-5f6cd067-1cf5-4de6-ba9c-cf93259d61a7.png)

The second program consisting of a function which implements ROT13 encryption algorithm which accepts password from the login window, then it encrypts the password and show username and encrypted password within the console.

The Output will be:

![image](https://user-images.githubusercontent.com/72243394/200178776-1e4dabe4-6209-4869-b46e-05c56f81c08c.png)

## Conclusion
