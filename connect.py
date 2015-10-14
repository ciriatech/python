#import mysql.connector
#from MySQLDb import *
# import MySQLdb
# import string
import sys, os,__future__
# class Connect:
#     host = "localhost"
#     dbname="test"
#     user = "root"
#     password = " "

#     def __init(self,host,dbname,user,password):
#         # tester l'existance
#         if host != " ":
#             self.host = host
#         if dbname != "":
#             self.dbname = dbname
#         if user != " ":
#             self.user = user
#         if password != " ":
#             self.password = password
#     #creation de la connection
#     def connected(self):
#         try:
#             conn = MySQLDb.connect(host=host,user=user,password=password,database=dbname)
#             return conn
#         except:
#             print("Equation")
#             conn.close()
#     #creation de la deconnexion
#     def logout(self,conn):
#         conn.close()


class Connect:
    username = password = filename=""
    diction = dict()
    def __init__(self,username,password):
        #initialisation des elements
        self.password = password
        self.username = username

    def login(self,filename=None):
        if filename == None:
            self.filename = "members.txt"
        else:
            self.filename = filename
        f = open(self.filename)
        try:
            for line in f:
                user,passed =  line.split()
                if self.username == user and self.password == passed :
                    from window import *

        except:
            f.close()
            print "error"
        f.close()
        root = Tk()
        data = self.getStream()
        app = Application(data,master=root)
        app.mainloop()
        root.destroy()

#lorque cette methode est appeler, filename contient deja le nom du fichier,
#c'est pour cela qu'on ne le passe plus en parametre de la function pour recupeere
#son flux
    def getStream(self):
        f = open(self.filename)
        try:
            for line in f:
                user,passed =  line.split()
                self.diction[user] = passed
            return self.diction
        except:
            f.close()
            print "Stream error"
        f.close()





