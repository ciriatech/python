from Tkinter import *
master = Tk()
master.title("Login Prompt")
master.resizable(0,0)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
username = password = " "

def login():
    Label(master, text="First Name").grid(row=0)
    Label(master, text="Last Name").grid(row=1)
    Label(master,text="Filename").grid(row=2)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)

    Button(master,text="Se Connecter",command=getData).grid(row=3,column=0)
    #Button(master,text="Quitter",command=master.quit).grid(row=3,column=1)
    mainloop( )

def getData():
    username = e1.get()
    password = e2.get()
    from connect import *
    connecte = Connect(username,password)
    connecte.login(e3.get())


