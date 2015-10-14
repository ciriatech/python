from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self,data):

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})


        self.message = Message(self)
        self.message['text'] = data
        self.message.pack({"side":"left"})




    def __init__(self,data, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets(data)
