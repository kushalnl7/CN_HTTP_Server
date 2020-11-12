import sys
from socket import *
from _thread import *
from threading import Thread
import requests
import threading
import time
serverName = '127.0.0.1'
serverPort = int(sys.argv[1])

filecontent = "Hello, I am Kushal from Pune.\r\nI am from COEP\r\nI stay at V N Lahoti Hostel\r\nI am basically from Akola"
myobj = {'username' : 'kushalnl_7', 'email' : 'lahotikn18.comp@coep.ac.in'}
# requests.get("http://localhost:" + serverPort + "/index.html")
# requests.head("http://localhost:" + serverPort + "/index.html")
# a = requests.put("http://localhost:" + str(serverPort) + "/newfile.txt", data=filecontent)
# requests.delete("http://localhost:" + serverPort + "/newfile.txt")
# a = requests.post("http://localhost:" + str(serverPort) + "/form.html", data = myobj)
# print(a)

def GET():
    #200
    a = requests.get("http://localhost:" + str(serverPort) + "/index.html") 
    print(a)
    #404
    a = requests.get("http://localhost:" + str(serverPort) + "/indx.html") 
    print(a)
    # requests.get("http://localhost:" + str(serverPort) + "/index.htmlaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") #414
# GET()

myobj_pl = {'username' : 'kushalnl_7kushalnl_7kushalnl_7kushalnl_7kushalnl_7kushalnl_7kushalnl_7', 'email' : 'lahotikn18.comp@coep.ac.inlahotikn18.comp@coep.ac.inlahotikn18.comp@coep.ac.inlahotikn18.comp@coep.ac.inlahotikn18.comp@coep.ac.inlahotikn18.comp@coep.ac.in'}
def POST():
    #200
    a = requests.post("http://localhost:" + str(serverPort) + "/form.html", data = myobj)
    print(a)
    #404
    a = requests.post("http://localhost:" + str(serverPort) + "/for.html", data = myobj)
    print(a)
    #413
    a = requests.post("http://localhost:" + str(serverPort) + "/form.html", data = myobj_pl)
    print(a)

POST()