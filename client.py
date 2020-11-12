import sys
from socket import *
from _thread import *
from threading import Thread
import requests
import threading
import time
serverName = '127.0.0.1'
serverPort = int(sys.argv[1])
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

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


# def conn():

# for i in range(5):
#     print(i)
#     r = requests.get('http://127.0.0.1:12000/index.html')    
# start = time.time()
# threads = []
# uri = 'http://127.0.0.1:12000/index.html'
# # t1 = Thread(target=, args=())
# for _ in range(5):
#     t = Thread(target=requests.get, args=(uri,))
#     t.setDaemon(True)
#     t.start()
#     print("No. of active connections : ", threading.active_count())
#     print(t)
#     threads.append(t)
# # print(threads)
# for i in threads:
#     i.join()    
# end = time.time()
# print(end - start)

# s_th = Thread(target=sendt)
# s_th.start()

# r_th = Thread(target=receive)
# r_th.start()	
data_GET = ""
data_GET += "GET /index.html HTTP/1.1\r\n"
data_GET += "Content-Type: text/plain\r\n"
data_GET += "Accept: */*\r\n"
data_GET += "Host: 127.0.0.1:12000\r\n"
data_GET += "Accept-Encoding: gzip, deflate, br\r\n"
data_GET += "Connection: keep-alive\r\n"
data_GET += "Content-Length: 13\r\n"
data_GET += "Cookie: yummy_cookie=choco\r\n\r\n"

data_POST = ""
data_POST += "POST /form.html HTTP/1.1\r\n"
data_POST += "Content-Type: text/plain\r\n"
data_POST += "Accept: */*\r\n"
data_POST += "Host: 127.0.0.1:12000\r\n"
data_POST += "Accept-Encoding: gzip, deflate, br\r\n"
data_POST += "Connection: keep-alive\r\n"
data_POST += "Content-Length: 57\r\n"
data_POST += "Cookie: yummy_cookie=choco\r\n"
data_POST += "\r\n\r\nusername=kushalnl_7&email_id=lahotikn18.comp%40coep.ac.in"

data_HEAD = ""
data_HEAD += "HEAD /index.html HTTP/1.1\r\n"
data_HEAD += "Accept: */*\r\n"
data_HEAD += "Host: 127.0.0.1:12000\r\n"
data_HEAD += "Accept-Encoding: gzip, deflate, br\r\n"
data_HEAD += "Connection: keep-alive\r\n"
data_HEAD += "Cookie: yummy_cookie=choco\r\n\r\n"

data_PUT = ""
data_PUT += "PUT /kush.html HTTP/1.1\r\n"
data_PUT += "Content-Type: text/plain\r\n"
data_PUT += "Accept: */*\r\n"
data_PUT += "Host: 127.0.0.1:12000\r\n"
data_PUT += "Accept-Encoding: gzip, deflate, br\r\n"
data_PUT += "Connection: keep-alive\r\n"
data_PUT += "Content-Length: 29\r\n"
data_PUT += "Cookie: yummy_cookie=choco\r\n\r\n"
# data_PUT += "\r\nHello, I am Kushal from Pune.\r\n"
# data_PUT += "I am from COEP\r\n"
# data_PUT += "I stay at V N Lahoti Hostel\r\n"
# data_PUT += "I am basically from Akola"

data_DELETE = ""
data_DELETE += "DELETE /klput.html HTTP/1.1\r\n"
data_DELETE += "Accept: */*\r\n"
data_DELETE += "Host: 127.0.0.1:12000\r\n"
data_DELETE += "Accept-Encoding: gzip, deflate, br\r\n"
data_DELETE += "Connection: keep-alive\r\n"
data_DELETE += "Cookie: yummy_cookie=choco\r\n\r\n"


def sendt1():
    while(True):
        clientSocket.send(data_DELETE.encode())
    clientSocket.close()

def receive1():
    while(True):
        sentence = clientSocket.recv(1024).decode()
        print(sentence)
    clientSocket.close()
        
    

# s_th = Thread(target=sendt1)
# s_th.start()
# r_th = Thread(target=receive1)
# r_th.start()
# s_th.join()
# r_th.join()
# clientSocket.close()
clientSocket.send(data_PUT.encode())
modifiedSentence = clientSocket.recv(1024)
print(modifiedSentence.decode())
clientSocket.close()
# sendt1()
# receive1()