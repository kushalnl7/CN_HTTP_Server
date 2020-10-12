#!/usr/bin/python

from socket import *
import sys
import datetime 

serverSocket = socket(AF_INET,SOCK_STREAM)
serverPort = int(sys.argv[1])
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print("Server is ready to receive\n")
while True:
	current_time = datetime.datetime.now() 
	connectionSocket, addr = serverSocket.accept()
	print("New request from: {}".format(addr))
	print("Connection Socket is: {}".format(connectionSocket))
	sentence = connectionSocket.recv(10324).decode()
	words = sentence.split()
	print(words[0],words[1])
	if(words[0] == "GET"):
		string = "HTTP/1.1 200 OK\n"
		string += "Date: {} GMT\n".format(current_time)
		string += "Local HTTP server/0.0.1 (Ubuntu)\n"
		string += "Content-Length: 303\n"
		string += "Connection: close\n"
		string += "Content-Type: text/html: charset=iso-8859-1\n\n"
		f = open("index1.html")
		text = f.read()
		output = string + text
		connectionSocket.send(output.encode())
	connectionSocket.close()
	
