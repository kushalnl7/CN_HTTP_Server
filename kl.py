# import os
# import pathlib
# print(os.path.getmtime("CN/Project/access.log"))
# print(pathlib.Path.stat("access.log"))

# import os.path, time
# k = time.ctime(os.path.getmtime("CN/Project/access.log"))
# print(k[0:3], k[4:7], k[9], k[11:19], k[20:24])

data = ""
data += "GET /index.html HTTP/1.1\r\nContent-Type: text/plain\r\nAccept: */*\r\nHost: 127.0.0.1:12000\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nContent-Length: 13\r\nCookie: yummy_cookie=choco"

print(data)
print(data.encode())

data1 = ""
data1 += "GET /index.html HTTP/1.1\n"
data1 += "Content-Type: text/plain\n"
data1 += "Accept: */*\n"
data1 += "Host: 127.0.0.1:12000\n"
data1 += "Accept-Encoding: gzip, deflate, br\n"
data1 += "Connection: keep-alive\n"
data1 += "Content-Length: 13\n"
data1 += "Cookie: yummy_cookie=choco"

print(data)
print(data.encode())