import sys
from socket import *
from _thread import *
from threading import Thread
import requests

# serverName = '127.0.0.1'
# serverPort = int(sys.argv[1])
# clientSocket = socket(AF_INET, SOCK_STREAM)
# clientSocket.connect((serverName,serverPort))

def sendt():
    clientSocket.send(username.encode())
    while(True):
        r = requests.get('http://127.0.0.1:12000/index.html')
        print(r)  
        print(r.content)
        clientSocket.send(sentence.encode())	
    clientSocket.close()
    
def receive():
    while(True):
        sentence = clientSocket.recv(1024).decode()
        print(sentence)
        clientSocket.close()

r = requests.get('http://127.0.0.1:12000/index.html')
print(r)  
print(r.content)

# s_th = Thread(target=sendt)
# s_th.start()

# r_th = Thread(target=receive)
# r_th.start()	