import random
import tkinter
from tkinter import *
from tkinter import messagebox
MAX_KEY_SIZE = random.randrange(1,26)
    
            

# def getMessage():

#      print('Enter your message:')

#      return input()


def getKey():

     key = MAX_KEY_SIZE

     while True:
        if (key >= 1 and key <= MAX_KEY_SIZE):

             return key


def getTranslatedMessage(mode, message, key):

     if mode[0] == 'd':

        key = -key


     translated = ''

     for symbol in message:

         if symbol.isalpha():

             num = ord(symbol)

             num += key 



             if symbol.isupper():

                 if num > ord('Z'):

                     num -= 26

                 elif num < ord('A'):

                     num += 26

             elif symbol.islower():

                 if num > ord('z'):

                     num -= 26

                 elif num < ord('a'):

                     num += 26


             translated += chr(num)

         else:

             translated += symbol

     return translated




def decrypt():
    mode = 'decrypt'    
    message = e1.get()
    key = getKey()
    ans = getTranslatedMessage(mode, message, key)
    output.config(text=ans)


def encrypt():
    mode = 'encrypt'    
    message = e1.get()
    key = getKey()
    ans = getTranslatedMessage(mode, message, key)

    output.config(text=ans)


def reset():
    global MAX_KEY_SIZE 
    e1.delete(0, END)
    MAX_KEY_SIZE = random.randrange(1,26)
    output.config(text='output')







root = tkinter.Tk()
root.geometry("550x600+420+50")
root.title("Encrypt/Decrypt")
root.configure(background = "#000080")




lbl = Label(
    root,
    text = "Enter Your Message Here",
    font = ("Verdana", 18),
    bg = "#ffa500", #eed202
    fg = "#000000",
)
lbl.pack(pady = 30,ipady=10,ipadx=10)



ans1 = StringVar()
e1 = Entry(
    root,
    font = ("Verdana", 16),
    textvariable = ans1,
)
e1.pack(ipady=5,ipadx=5)




btncheck = Button(
    root,
    text = "ENCRYPT",
    font = ("Verdana", 16),
    width = 16,
    bg = "#ffa500",
    fg = "#1d4e89",
    relief = GROOVE,
    command = encrypt,
)
btncheck.pack(pady = 40)

btnreset = Button(
    root,
    text = "DECRYPT",
    font = ("Verdana", 16),
    width = 16,
    bg = "#ffa500",
    fg = "#1d4e89",
    relief = GROOVE,
    command = decrypt,
)
btnreset.pack()

output = Label(
    root,
    text = "Output",
    font = ("Verdana", 18),
    bg = "#000000",
    fg = "#FFFFFF",    
)
output.configure(state="active")
output.pack(pady = 30,ipady=10,ipadx=10)

reset = Button(
    root,
    text = "RESET",
    font = ("Verdana", 16),
    width = 16,
    bg = "#ffa500",
    fg = "#660000",
    relief = GROOVE,
    command = reset,
)
reset.pack()



root.mainloop()
