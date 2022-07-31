#!/usr/bin/env python
# coding: utf-8

# In[12]:


from tkinter import *
import random
import base64

root = Tk()

root.geometry('1280x1024')
root.resizable(0,0)
root.title("Encrypt Your Sensitive Data and Passwords")
Tops = Frame(root, width=1600, relief= SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, relief= SUNKEN)
f1.pack(side=LEFT)

lblInfo = Label(Tops, font=("Robot", 40, 'bold'), text="Data Encryption Tool", fg="Black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)


Text = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()


def Encode(key,message):
    enc=[]

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)

def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')
        
# def Results():
#     msg = Msg.get()
#     k = key.get()
#     m = mode.get()
#     if (m=='e'):
#         result.set(encode(k, msg))
#     else:
#         result.set(decode(k, msg))

def Exit():
    root.destroy()
    
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")
    
lblMsg = Label(f1, font=("arial", 16, 'bold'), text = "Message", bd=16, anchor = 'w')
lblMsg.grid(row=1, column=0)      

txtMsg = Entry(f1, font=("arial", 16, 'bold'), textvariable = Text, bd=10, 
               insertwidth=4, bg="powder blue", justify= 'left')
txtMsg.grid(row=1, column=1)

lblkey = Label(f1, font=("arial", 16, 'bold'), text = " Secret Key", bd=16, anchor = 'w')
lblkey.grid(row=2, column=0)

txtkey = Entry(f1, font=("arial", 16, 'bold'), textvariable = key, bd=10, 
               insertwidth=4, bg="powder blue", justify= 'left')
txtkey.grid(row=2, column=1)

lblmode = Label(f1, font=("arial", 16, 'bold'), text = "MODE(e for Encode & d for Decode)", bd=16, anchor = 'w')
lblmode.grid(row=3, column=0)

txtmode = Entry(f1, font=("arial", 16, 'bold'), textvariable = mode, bd=10, 
                insertwidth=4, bg="powder blue", justify= 'left')
txtmode.grid(row=3, column=1)

lblResult = Label(f1, font=("arial", 16, 'bold'), text = "Result", bd=16, anchor = 'w')
lblResult.grid(row=2, column=2)

txtResult = Entry(f1, font=("arial", 16, 'bold'), textvariable  = Result, bd=10, 
                  insertwidth=4, bg="powder blue", justify= 'left')
txtResult.grid(row=2, column=3)

btn1 = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10, 
                  text= "Show Message", bg="powder blue", command=Mode).grid(row=7, column=1)

btn2 = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10, 
                  text= "Reset", bg="powder blue", command=Reset).grid(row=7, column=2)

btn3 = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10, 
                  text= "Exit", bg="powder blue", command=Exit).grid(row=7, column=3)

root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




