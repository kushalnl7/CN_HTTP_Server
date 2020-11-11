import sys
from socket import *
from _thread import *
from threading import Thread
import requests
import threading
import time
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

# r = requests.get('http://127.0.0.1:12000/index.html')
# print(r)  
# print(r.content)

# for _ in range(10):
start = time.time()

# def conn():

# for i in range(5):
#     print(i)
#     r = requests.get('http://127.0.0.1:12000/index.html')    

threads = []
uri = 'http://127.0.0.1:12000/index.html'
# t1 = Thread(target=, args=())
for _ in range(5):
    t = Thread(target=requests.get, args=(uri,))
    t.setDaemon(True)
    t.start()
    print("No. of active connections : ", threading.active_count())
    print(t)
    threads.append(t)
# print(threads)
for i in threads:
    i.join()    
end = time.time()
print(end - start)

# s_th = Thread(target=sendt)
# s_th.start()

# r_th = Thread(target=receive)
# r_th.start()	