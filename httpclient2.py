import requests
from threading import *
import sys
from socket import *

myobj = {'username' : 'kushalnl_7', 'email' : 'lahotikn18.comp@coep.ac.in'}
filecontent = "Hello"
maxfilecontent = "The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007"
port = sys.argv[1]
serverName = '127.0.0.1'
serverPort = int(sys.argv[1])
def stage1():
    a = requests.get("http://localhost:" + port + "/index.html")
    requests.head("http://localhost:" + port + "/index.html")
    requests.put("http://localhost:" + port + "/newfile.txt", data=filecontent)
    requests.delete("http://localhost:" + port + "/newfile.txt")
    requests.post("http://localhost:" + port + "/form.html", data = myobj)

def stage2():
    #GET status codes
    a = requests.get("http://localhost:" + port + "/index.html")                                
    a = requests.get("http://localhost:" + port + "/index.html", headers = {'If-Modified-Since': 'Wed, 4 Nov 2020 08:48:00 GMT'})
    a = requests.get("http://localhost:" + port + "/fdjgk.html")
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    data = ""
    data += "GETT /index.html HTTP/1.1\r\nContent-Type: text/plain\r\nAccept: /\r\nHost: 127.0.0.1:12000\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nContent-Length: 13\r\nCookie: yummy_cookie=choco\r\nUser-Agent: My testing file\r\n\r\n"
    clientSocket.send(data.encode())
    modifiedSentence = clientSocket.recv(10000)
    # print('From Server: ', modifiedSentence.decode())
    clientSocket.close()
    requests.get("http://127.0.0.1:" + port + "/fdsajlfjdfjhajkhfkjdahfjkahjfkdhakjfdhkajhfjkahfdjhakjfhajdfjkajkfdhakjfasfasjfdsjfalfdjaofklfajldsdfjalkjlaksjflkasjfjalfjsjfsakjfdsdjflkasjdfljskdfjlsadfjlsdakjflksdajfldsajflkdjsafljsalfjalfjalkfjlasjfldsjaflkjsdlfkjklrajfdifarennrelajlktjwtljrltjlrejltjlrejtlrjtlkwaijrf4lrgljreltjlrtjdfjlkjf.html")
    requests.get("http://127.0.0.1:" + port + "/index.asd")
    #POST Status codes
    requests.post("http://localhost:" + port + "/form.html", data = myobj)
    requests.post("http://localhost:" + port + "/form2.html", data = myobj)

    #HEAD Status codes
    requests.head("http://localhost:" + port + "/index.html")
    requests.head("http://localhost:" + port + "/index.html", headers = {'If-Modified-Since': 'Wed 4 Nov 2020 08:48:00 GMT'})
    requests.head("http://localhost:" + port + "/form.html")
    requests.head("http://127.0.0.1:" + port + "/fdsajlfjdfjhajkhfkjdahfjkahjfkdhakjfdhkajhfjkahfdjhakjfhajdfjkajkfdhakjfasfasjfdsjfalfdjaofklfajldsdfjalkjlaksjflkasjfjalfjsjfsakjfdsdjflkasjdfljskdfjlsadfjlsdakjflksdajfldsajflkdjsafljsalfjalfjalkfjlasjfldsjaflkjsdlfkjklrajfdifarennrelajlktjwtljrltjlrejltjlrejtlrjtlkwaijrf4lrgljreltjlrtjdfjlkjf.html")
    requests.head("http://127.0.0.1:" + port + "/index.asd")

    #PUT Status Codes
    requests.put("http://localhost:" + port + "/newfile.txt", data=filecontent)
    requests.put("http://localhost:" + port + "/newfile.txt", data=filecontent)
 

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    data = ""
    data += "PUT /newfile.txt HTTP/1.1\r\nContent-Type: text/plain\r\nAccept: /\r\nHost: 127.0.0.1:12000\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nContent-Type: text/html\r\nCookie: yummy_cookie=choco\r\nUser-Agent: My testing file\r\n\r\n"
    clientSocket.send(data.encode())
    modifiedSentence = clientSocket.recv(10000)
    # print('From Server: ', modifiedSentence.decode())
    clientSocket.close()
    
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    data = ""
    data += "PUT /newfile.txt HTTP/1.1\r\nContent-Type: text/plain\r\nAccept: /\r\nHost: 127.0.0.1:12000\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nContent-Type: text/html\r\nCookie: yummy_cookie=choco\r\nUser-Agent: My testing file\r\n\r\nThe most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007The most viewed pages of Wikipedia before 2007 remain unknown, though the multiyear ranking of most viewed pages gives views for top 100 pages since 2007\r\n"
    clientSocket.send(data.encode())
    modifiedSentence = clientSocket.recv(10000)
    # print('From Server: ', modifiedSentence.decode())
    clientSocket.close()
    requests.put("http://127.0.0.1:" + port + "/fdsajlfjdfjhajkhfkjdahfjkahjfkdhakjfdhkajhfjkahfdjhakjfhajdfjkajkfdhakjfasfasjfdsjfalfdjaofklfajldsdfjalkjlaksjflkasjfjalfjsjfsakjfdsdjflkasjdfljskdfjlsadfjlsdakjflksdajfldsajflkdjsafljsalfjalfjalkfjlasjfldsjaflkjsdlfkjklrajfdifarennrelajlktjwtljrltjlrejltjlrejtlrjtlkwaijrf4lrgljreltjlrtjdfjlkjf.html", data = filecontent)
    requests.put("http://127.0.0.1:" + port + "/index.asd", data = filecontent)

    #DELETE Status Codes
    # requests.delete("http://localhost:" + port + "/newfile.txt")
    requests.delete("http://localhost:" + port + "/fdk.txt")


    



def stage3():
    pass

# stage1()
# stage2()
threads = []
for _ in range(1):
    t = Thread(target=stage1)
    t.setDaemon(True)
    t.start()
    threads.append(t)
for _ in range(1):
    t = Thread(target=stage2)
    t.setDaemon(True)
    t.start()
    threads.append(t)
for i in threads:
    i.join()    