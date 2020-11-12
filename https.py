import socket
import sys
import os
import datetime
import time
from conf import *
from threading import *
import threading
import concurrent.futures
"""
HTTP/1.1 200 OK
Date: Mon, 12 Oct 2020 06:35:24 GMT
Server: Apache/2.4.41 (Ubuntu)
Last-Modified: Tue, 06 Oct 2020 13:33:34 GMT
ETag: "2aa6-5b100a5427dfe"
Accept-Ranges: bytes
Content-Length: 10918
Vary: Accept-Encoding
Content-Type: text/html
"""

x = datetime.datetime.now()
# date = "%s +0530" % (x.strftime("%d/%b/%Y:%H:%M:%S"))
x_day = x.strftime("%d")
x_month = x.strftime("%b")
x_nmonth = x.strftime("%m")
x_year = x.strftime("%Y")
x_hour = x.strftime("%H")
x_min = x.strftime("%M")
x_sec = x.strftime("%S")
# response = "Hello, I am Kushal\r\n"



headers = {
        'Date': "%s, %s GMT" % (x.strftime("%A")[:3], x.strftime("%d %b %Y %H:%M:%S")),
        'Server': 'CrudeServer',
        'Last-Modified': 'Tue, 06 Oct 2020 13:33:34 GMT',
        'ETag': "2aa6-5b100a5427dfe",
        'Accept-Ranges': 'bytes',
        'Content-Length': '10918',
        'Vary': 'Accept-Encoding',
        'Content-Type': 'text/html',
        'Set-Cookie': 'yummy_cookie=choco',
          }
status_codes = {
        200: 'OK',
        404: 'Not Found',
        501: 'Not Implemented',
        400: 'Bad Request',
        201: 'Created',
        202: 'Accepted',
        304: 'Not Modified',
        414: 'URI Too Long',
        408: 'Request Timeout',
        411: 'Length Required',
        413: 'Payload Too Large',
        204: 'No Content',
         }

def response_line(status_code):
    """Returns response line"""
    reason = status_codes[status_code]
    return "HTTP/1.1 %s %s\r\n" % (status_code, reason)

def response_headers(l = None,filename = None):
    header = ""
    for h in headers:
        if(h == 'Content-Length'):
            header += "%s: %s\r\n" % (h, l)
        elif(h == 'Last-Modified'):
            if(filename != None):
                k = time.ctime(os.path.getmtime(filename))
                s = ""
                if(int(k[9]) < 10):
                    s += "0" + k[9]
                else:
                    s += k[9]
                header += "%s: %s, %s %s %s %s GMT\r\n" % (h, k[0:3], s, k[4:7], k[20:24], k[11:19])
            # header += "%s: %s\r\n" % (h, time.ctime(os.path.getmtime(filename)))
        elif(h == 'Set-Cokkie'):
            for k in cokkies:
                header += "%s: %s=%s\r\n" % (h, k, cokkies[k])
        else:
            header += "%s: %s\r\n" % (h, headers[h])
    return header

def uri_len(uri):
    l = len(uri)
    if(l > max_uri_len):
        return 1
    else:
        return 0

def getdate(s):
    k = []
    p = s.split(" ")
    for i in p:
        if(len(i) == 3):
            datetime_object = datetime.datetime.strptime(i, "%b")
            m_num = datetime_object.month
            k.append(int(m_num))
        elif(len(i) == 8):
            p1 = i.split(":")
            k.append(int(p1[0]))
            k.append(int(p1[1]))
            k.append(int(p1[2]))
        else:
            k.append(int(i))
    return k

def res_ifs(date, filename):
    N = getdate(date)
    # for h in headers:
    #     if(h == "Last-Modified"):
    #         M = getdate((headers[h])[5:25])
    #         break
    k = time.ctime(os.path.getmtime(filename))
    s = ""
    if(int(k[9]) < 10):
        s += "0" + k[9]
    else:
        s += k[9]
    datetime_object = datetime.datetime.strptime(k[4:7], "%b")
    m_num = datetime_object.month
    b = datetime.datetime(int(k[20:24]), int(m_num), int(s), int(k[11:13]), int(k[14:16]), int(k[17:19]))
    a = datetime.datetime(N[2], N[1], N[0], N[3], N[4], N[5])
    # b = datetime.datetime(M[2], M[1], M[0], M[3], M[4], M[5])
    return a>b

def logtext(filename, st_code, method):
    date = "%s +0530" % (x.strftime("%d/%b/%Y:%H:%M:%S"))
    # print(st_code)
    if(st_code == 200 or st_code == 201 or st_code == 304 or st_code == 204):
        text = '%s - - [%s] "%s %s HTTP/1.1" %s %s "-" "-" \r\n' % (host, date, method, filename, st_code, (os.stat(filename)).st_size)
    elif(st_code == 404 or st_code == 501 or st_code == 400 or st_code == 501 or st_code == 414 or st_code == 408 or st_code == 411 or st_code == 413):
        text = '%s - - [%s] "%s %s HTTP/1.1" %s 0 "-" "-" \r\n' % (host, date, method, filename, st_code)
    with open("access.log", "a") as myfile:
        myfile.write(text)


def HTTP_400_Handler():
    global st_code
    responseline = response_line(status_code=400)
    st_code = 400
    response_body = "<h1>400 Bad Request</h1>\n"
    l = len(response_body)
    responseheaders = response_headers(l)
    blank_line = "\r\n"
    
    return "%s%s%s%s" % (
        # blank_line,
        responseline,
        responseheaders,
        blank_line,
        response_body
    )


def HTTP_408_Handler():
    global st_code
    responseline = response_line(status_code=408)
    st_code = 408
    response_body = "<h1>408 Request Timeout</h1>\n"
    l = len(response_body)
    responseheaders = response_headers(l)
    blank_line = "\r\n"
    
    return "%s%s%s%s" % (
        # blank_line,
        responseline,
        responseheaders,
        blank_line,
        response_body
    )

def HTTP_414_handler():
    global st_code
    responseline = response_line(status_code=414)
    st_code = 414
    blank_line = "\r\n"
    response_body = "<h1>411 Uri Too Long</h1>\n"
    l = len(response_body)
    responseheaders = response_headers(l)
    return "%s%s%s%s" % (
            # blank_line,
            responseline, 
            responseheaders, 
            blank_line, 
            response_body
        )

def HTTP_411_handler():
    global st_code
    responseline = response_line(status_code=411)
    st_code = 411
    blank_line = "\r\n"
    response_body = "<h1>411 Length Required</h1>\n"
    l = len(response_body)
    responseheaders = response_headers(l)
    return "%s%s%s%s" % (
            # blank_line,
            responseline, 
            responseheaders, 
            blank_line, 
            response_body
        )

def HTTP_413_handler():
    global st_code
    responseline = response_line(status_code=413)
    st_code = 413
    blank_line = "\r\n"
    response_body = "<h1>413 Payload Too Large</h1>\n"
    l = len(response_body)
    responseheaders = response_headers(l)
    return "%s%s%s%s" % (
            # blank_line,
            responseline, 
            responseheaders, 
            blank_line, 
            response_body
        )

def HTTP_501_handler(uri):
    global st_code
    responseline = response_line(status_code=501)
    st_code = 501
    blank_line = "\r\n"
    response_body = "<h1>501 Not Implemented</h1>\n"
    l = len(response_body)
    responseheaders = response_headers(l)
    return "%s%s%s%s" % (
            # blank_line,
            responseline, 
            responseheaders, 
            blank_line, 
            response_body
        )

def OPTIONS(uri):
    responseline = response_line(200)
    extra_headers = {'Allow': 'OPTIONS, GET'}
    responseheaders = response_headers()
    blank_line = "\r\n"
    return "%s%s%s" % (
            # blank_line,
            responseline, 
            responseheaders,
            blank_line
        )

def GET(uri, data):
    print("Inside get")
    print(uri)
    filename = uri.strip('/')
    k = data.split("\r\n")
    p = 0
    global st_code
    for i in k:
        if("If-Modified-Since" in i):
            p = res_ifs(i[24:44], filename)
    if(p):
        if os.path.exists(filename):
            responseline = response_line(304)
            st_code = 304
            response_body = ""
            date = "%s +0530" % (x.strftime("%d/%b/%Y:%H:%M:%S"))
            l = len(response_body)
            responseheaders = response_headers(l,filename)
            # logtext = '%s - - [%s] "GET %s HTTP/1.1" 304 %s "-" "-" \r\n' % (host, date, filename, (os.stat(filename)).st_size)
        else:
            responseline = response_line(404)
            st_code = 404
            response_body = "<h1>404 Not Found</h1>\n"
            l = len(response_body)
            date = "%s +0530" % (x.strftime("%d/%b/%Y:%H:%M:%S"))
            # logtext = '%s - - [%s] "GET %s HTTP/1.1" 404 0 "-" "-" \r\n' % (host, date, filename)
            responseheaders = response_headers(l)

    else:
        if os.path.exists(filename):
            print("Found file, giving 200")
            responseline = response_line(200)
            st_code = 200
            with open(filename) as f:
                response_body = f.read()
            l = len(response_body)
            # logtext = '%s - - [%s] "GET %s HTTP/1.1" 200 %s "-" "-" \r\n' % (host, date, filename, (os.stat(filename)).st_size)
            date = "%s, %s GMT" % (x.strftime("%A")[:3], x.strftime("%d %b %Y %H:%M:%S"))
            responseheaders = response_headers(l, filename)
        else:
            responseline = response_line(404)
            st_code = 404
            response_body = "<h1>404 Not Found</h1>\r\n"
            l = len(response_body)
            date = "%s +0530" % (x.strftime("%d/%b/%Y:%H:%M:%S"))
            # logtext = '%s - - [%s] "GET %s HTTP/1.1" 404 0 "-" "-" \r\n' % (host, date, filename)
            responseheaders = response_headers(l)

    blank_line = "\r\n"
    # with open("access.log", "a") as myfile:
    #     myfile.write(logtext)
    return "%s%s%s%s" % (
            # blank_line,
            responseline, 
            responseheaders, 
            blank_line, 
            response_body
        )
    
def POST(uri, data):
    global st_code
    lines = data.split('\r\n')
    filename = uri.strip('/')
    responseline = response_line(200)
    st_code = 200
    l = len(lines[-1])
    print('\n')
    print(lines[-1])
    print('\n')
    if(l > max_payload):
        response = HTTP_413_handler()
        return response
    responseheaders = response_headers(l+1)
    blank_line = "\r\n"
    k = lines[-1].split('&')
    response_body = ""
    for i in k:
        response_body += str(i) + "\r\n"
    date = "%s +0530" % (x.strftime("%d/%b/%Y:%H:%M:%S"))
    logtext = '%s - - [%s] "POST %s HTTP/1.1" 200 %s "-" "-" %s\r\n' % (host, date, filename, (os.stat(filename)).st_size, lines[-1])
    with open("access.log", "a") as myfile:
        myfile.write(logtext)
    return "%s%s%s%s" % (
            # blank_line,
            responseline, 
            responseheaders, 
            blank_line, 
            response_body
        )
    
def HEAD(uri, data):
    global st_code
    filename = uri.strip('/') # remove the slash from URI
    if os.path.exists(filename):
        responseline = response_line(200)
        st_code = 200
        with open(filename) as f:
            response_body = f.read()
        l = len(response_body)
        date = "%s +0530" % (x.strftime("%d/%b/%Y:%H:%M:%S"))
        # logtext = '%s - - [%s] "HEAD %s HTTP/1.1" 200 %s "-" "-" \r\n' % (host, date, filename, (os.stat(filename)).st_size)
        date = "%s, %s GMT" % (x.strftime("%A")[:3], x.strftime("%d %b %Y %H:%M:%S"))
        responseheaders = response_headers(l)
        
    else:
        responseline = response_line(404)
        response_body = "<h1>404 Not Found</h1>\n"
        l = len(response_body)
        date = "%s +0530" % (x.strftime("%d/%b/%Y:%H:%M:%S"))
        # logtext = '%s - - [%s] "HEAD %s HTTP/1.1" 404 0 "-" "-" \r\n' % (host, date, filename)
        responseheaders = response_headers(l)
    blank_line = "\r\n"

    # with open("access.log", "a") as myfile:
    #     myfile.write(logtext)
    return "%s%s%s" % (
            # blank_line,
            responseline, 
            responseheaders, 
            blank_line, 
        )

def PUT(uri, data):
    global st_code
    data1 = data.split('\r\n')
    k = 0
    for i in data1:
        if("Content-Length" in i):
            k += 1
            break
    if(k == 1):
        data = data.split('\r\n')[-1]
        if(len(data) > max_payload):
            response = HTTP_413_handler()
            return response
        else:
            filename = uri.strip('/')
            if(os.path.isfile(filename) == False):
                f = open(filename,"w+")
                f.write(data)
                response_body = ""
                if(f):
                    response_body += "<h1>The file was created.</h1>\n"
                responseline = response_line(201)
                st_code = 201
                responseheaders = response_headers(len(response_body))
            elif(len(data) == 0):
                f = open(filename,"w+")
                f.write(data)
                responseline = response_line(204)
                st_code = 204
                response_body = ""
                l = len(response_body)
                responseheaders = response_headers(l)
            else:
                f = open(filename,"w+")
                f.write(data)
                responseline = response_line(200)
                st_code = 200
                response_body = ""
                responseheaders = response_headers(len(response_body))

        """ 204 No Content Status Code Pending """
        blank_line = "\r\n"
        return "%s%s%s%s" % (
                # blank_line,
                responseline, 
                responseheaders, 
                blank_line, 
                response_body
            )
    else:
        res = HTTP_411_handler()
        return res

def DELETE(uri):
    global st_code
    filename = uri.strip('/')
    if(os.path.isfile(filename) == False):
        """ Not Sure about 202"""
        responseline = response_line(202)
        st_code = 202
        response_body = ""
        responseheaders = response_headers(len(response_body))
    else:
        os.remove(filename)
        responseline = response_line(200)
        st_code = 200
        response_body = "<html><body><h1>File deleted.</h1></body></html>"
        responseheaders = response_headers(len(response_body))
    blank_line = "\r\n"
    """ 204 No Content Status Code Pending """
    return "%s%s%s%s" % (
            # blank_line,
            responseline, 
            responseheaders, 
            blank_line, 
            response_body
        )

def HTTPRequest(data):
    http_version = '1.1' # default to HTTP/1.1 if request doesn't provide a version
    headers = {} # a dictionary for headers
    lines = data.split('\r\n')
    words = lines[0].split(' ')
    method = words[0]
    try:
        uri = words[1]
    except(IndexError):
        uri = None
    if len(words) > 2:
        http_version = words[2]
    return method, uri, http_version

def handle_request(data):
    print("Handle_request")
    data = data.decode()
    print(data)
    global response
    global st_code
    # time.sleep(10)
    method, uri, http_version = HTTPRequest(data)
    print(method, uri, http_version)
    if(uri_len(uri.strip('/')) == 1):
        response = HTTP_414_handler()
    elif(method == 'GET'):
        if(uri is None or http_version != "HTTP/1.1"):
            response = HTTP_400_Handler()
        else:
            response = GET(uri, data)
        logtext(uri.strip('/'), st_code, method)
    elif(method == 'HEAD'):
        if(uri is None or http_version != "HTTP/1.1"):
            response = HTTP_400_Handler()
        else:
            response = HEAD(uri, data)
        logtext(uri.strip('/'), st_code, method)
    elif(method == 'POST'):
        if(uri is None or http_version != "HTTP/1.1"):
            response = HTTP_400_Handler()
        else:
            response = POST(uri, data)
    elif(method == 'PUT'):
        if(uri is None or http_version != "HTTP/1.1"):
            response = HTTP_400_Handler()
        else:    
            response = PUT(uri, data)
        logtext(uri.strip('/'), st_code, method)
    elif(method == 'DELETE'):
        if(uri is None or http_version != "HTTP/1.1"):
            response = HTTP_400_Handler()
        else:
            response = DELETE(uri)
        logtext(uri.strip('/'), st_code, method)
    else:
        response = HTTP_501_handler(uri)
        logtext(uri.strip('/'), st_code, method)
    

    

def sleep():
    time.sleep(1)

host='127.0.0.1'
try:
    port=int(sys.argv[1])
except(IndexError):
    print("Provide the port number in command line.")
    exit(1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)
print("Listening at", s.getsockname())
response = None
st_code = None
while True:
    # global conn
    # print("Starting Connection")
    conn, addr = s.accept()
    print("Connected by", addr)
    data = (conn.recv(1024))
    # print('\n\n')
    # print(data)
    # print('\n\n')
    start = time.time()
    # handle_request(data)
    t1 = Thread(target=handle_request, args=(data,))
    # t2 = Thread(target=sleep)
    t1.start()
    end = time.time()
    print("No. of active connections : ", threading.active_count())
    while(response is None):
        continue
    if(end - start < max_time):
        conn.sendall(bytes(response, 'utf-8'))
    else:
        response = HTTP_408_Handler()
    response = None
    print("Closing Connection")
    conn.close()
    print("Closed Connection\n")
    

