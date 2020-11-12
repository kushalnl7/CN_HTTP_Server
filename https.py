import socket
import sys
import os
import datetime
import time
from conf import *
from threading import *
import threading
import concurrent.futures

x = datetime.datetime.now()
x_day = x.strftime("%d")
x_month = x.strftime("%b")
x_nmonth = x.strftime("%m")
x_year = x.strftime("%Y")
x_hour = x.strftime("%H")
x_min = x.strftime("%M")
x_sec = x.strftime("%S")



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
        415: 'Unsupported Media Type'
         }

def response_line(status_code):
    """Returns response line"""
    reason = status_codes[status_code]
    return "HTTP/1.1 %s %s\r\n" % (status_code, reason)

def response_headers(time1, l = None,filename = None, extension = None):
    header = ""
    for h in headers:
        if(h == 'Content-Length'):
            header += "%s: %s\r\n" % (h, l)
        elif(h == 'Date'):
            header += "%s: %s, %s GMT" % (h, time1.strftime("%A")[:3], time.strftime("%d %b %Y %H:%M:%S"))
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
        elif(h == 'Content-Type'):
            if extension == "html":
                header += "%s: %s\r\n" % (h, 'text/html')  
            elif extension == "png":
                header += "%s: %s\r\n" % (h, 'image/png')
            elif extension == "txt":
                header += "%s: %s\r\n" % (h, 'text/plain')
            elif extension == "jpg":
                header += "%s: %s\r\n" % (h, 'image/jpg')
            elif extension == "jpeg":
                header += "%s: %s\r\n" % (h, 'image/jpeg')
            elif extension == "mp3":
                header += "%s: %s\r\n" % (h, 'audio/mpeg')
            elif extension == "mp4":
                header += "%s: %s\r\n" % (h, 'video/mp4')
        else:
            header += "%s: %s\r\n" % (h, headers[h])
    return header



def uri_len(uri):
    l = len(uri)
    print(l)
    if(l > max_uri_len):
        return 1
    else:
        return 0

def getdate(s):
    k = []
    # Wed, 4 Nov 2020 08:48:00 GMT
    p = s.split(" ")
    print(p)
    for i in p:
        print(i)
        i = i.strip(',')
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
        print(k)
    return k

def res_ifs(date, filename):
    N = getdate(date)
    # for h in headers:
    #     if(h == "Last-Modified"):
    #         M = getdate((headers[h])[5:25])
    #         break
    #Wed 4 Nov 2020 08:48:00 GMT
    k = time.ctime(os.path.getmtime(filename))
    s = ""# for h in headers:
    #     if(h == "Last-Modified"):
    #         M = getdate((headers[h])[5:25])
    #         break
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

def logtext(time, filename, st_code, method):
    date = "%s +0530" % (time.strftime("%d/%b/%Y:%H:%M:%S"))
    # print(st_code)
    if(method == "DELETE" and st_code == 200):
        text = '%s - - [%s] "%s %s HTTP/1.1" %s 0 "-" "-" \r\n' % (host, date, method, filename, st_code)
    elif(st_code == 200 or st_code == 201 or st_code == 304 or st_code == 204):
        text = '%s - - [%s] "%s %s HTTP/1.1" %s %s "-" "-" \r\n' % (host, date, method, filename, st_code, (os.stat(filename)).st_size)
    elif(st_code == 404 or st_code == 501 or st_code == 400 or st_code == 501 or st_code == 414 or st_code == 408 or st_code == 411 or st_code == 413 or st_code == 415):
        text = '%s - - [%s] "%s %s HTTP/1.1" %s 0 "-" "-" \r\n' % (host, date, method, filename, st_code)
    with open("access.log", "a") as myfile:
        myfile.write(text)


def HTTP_400_Handler(time):
    global st_code
    responseline = response_line(status_code=400)
    st_code = 400
    response_body = "<html><head><title>400 Bad Request</title></head><body><h1>400 Bad Request></h1><p>Your browser sent a request that this server could not understand.</p><hr><address>My (Ubuntu) Server at 127.0.0.1 Port 12000</address></body></html>\n"
    l = len(response_body)
    responseheaders = response_headers(time, l)
    blank_line = "\r\n"
    return responseline, responseheaders, response_body


def HTTP_408_Handler(time):
    global st_code
    responseline = response_line(status_code=408)
    st_code = 408
    response_body = "<html><head><title>408 Request Timeout</title></head><body><h1>408 Request Timeout></h1><p>Your browser did'nt send a complete request in time.</p><hr><address>My (Ubuntu) Server at 127.0.0.1 Port 12000</address></body></html>\n"
    l = len(response_body)
    responseheaders = response_headers(time,l)
    blank_line = "\r\n"
    return responseline, responseheaders, response_body

def HTTP_414_handler(time):
    global st_code
    responseline = response_line(status_code=414)
    st_code = 414
    blank_line = "\r\n"
    response_body = "<html><head><title>414 REQUEST-URI Too Long</title></head><body><h1>414 REQUEST-URI Too Long</h1><p>The requested URL is too large to process.</p><hr><address>My (Ubuntu) Server at 127.0.0.1 Port 12000</address></body></html>\n"
    l = len(response_body)
    responseheaders = response_headers(time,l)
    return responseline, responseheaders, response_body

def HTTP_411_handler(time):
    global st_code
    responseline = response_line(status_code=411)
    st_code = 411
    blank_line = "\r\n"
    response_body = "<html><head><title>411 Length Required</title></head><body><h1>411 Length Required</h1><p>The request must be chunked or have a content length.</p><hr><address>My (Ubuntu) Server at 127.0.0.1 Port 12000</address></body></html>\n"
    l = len(response_body)
    responseheaders = response_headers(time,l)
    return responseline, responseheaders, response_body

def HTTP_413_handler(time):
    global st_code
    responseline = response_line(status_code=413)
    st_code = 413
    blank_line = "\r\n"
    response_body = "<html><head><title>413 Request Entity Too Large</title></head><body><h1>413 Request Entity Too Large</h1><p>The request entity is too large.</p><hr><address>My (Ubuntu) Server at 127.0.0.1 Port 12000</address></body></html>\n"
    l = len(response_body)
    responseheaders = response_headers(time,l)
    return responseline, responseheaders, response_body

def HTTP_501_handler(time,uri):
    global st_code
    responseline = response_line(status_code=501)
    st_code = 501
    blank_line = "\r\n"
    response_body = "<html><head><title>501 Not Implemented</title></head><body><h1>501 Not Implemented</h1><p>The server is unable to process your request.</p><hr><address>My (Ubuntu) Server at 127.0.0.1 Port 12000</address></body></html>\n"
    l = len(response_body)
    responseheaders = response_headers(time,l)
    return responseline, responseheaders, response_body

def OPTIONS(uri):
    responseline = response_line(200)
    extra_headers = {'Allow': 'OPTIONS, GET'}
    responseheaders = response_headers()
    blank_line = "\r\n"
    return responseline, responseheaders, response_body

def GET(time,uri, data):
    print("Inside get")
    print(uri)
    filename = uri.strip('/')
    k = data.split("\r\n")
    ext_list = filename.split('.')
    if len(ext_list) > 1:
        extension = ext_list[1]
    flag = 0
    if extension == "png" or extension == "jpg" or extension == "jpeg" or extension =="mp4" or extension == "mp3" or extension == "html" or extension == "txt":
        try:
            if extension == "png" or extension == "jpg" or extension == "jpeg" or extension =="mp4" or extension == "mp3":
                flag = 1
        except(UnboundLocalError):
            flag = 0
        p = 0
        global st_code
        for i in k:
            if("If-Modified-Since" in i):
                print(i)
                p = res_ifs(i[24:43], filename)
        if(p):
            if os.path.exists(filename):
                responseline = response_line(304)
                st_code = 304
                response_body = ""
                date = "%s +0530" % (x.strftime("%d/%b/%Y:%H:%M:%S"))
                l = len(response_body)
                responseheaders = response_headers(time,l,filename)
                # logtext = '%s - - [%s] "GET %s HTTP/1.1" 304 %s "-" "-" \r\n' % (host, date, filename, (os.stat(filename)).st_size)
            else:
                responseline = response_line(404)
                st_code = 404
                response_body = "<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1><p>The requested URL was not found on this server.</p><hr><address>My (Ubuntu) Server at 127.0.0.1 Port 12000</address></body></html>\n"
                l = len(response_body)
                date = "%s +0530" % (x.strftime("%d/%b/%Y:%H:%M:%S"))
                # logtext = '%s - - [%s] "GET %s HTTP/1.1" 404 0 "-" "-" \r\n' % (host, date, filename)
                responseheaders = response_headers(time,l)

        else:
            if os.path.exists(filename):
                print("Found file, giving 200")
                if flag == 1:
                    with open(filename, 'rb') as f:
                        response_body = f.read()
                else:
                    with open(filename, 'r') as f:
                        response_body = f.read()
                responseline = response_line(200)
                st_code = 200
                l = len(response_body)
                # logtext = '%s - - [%s] "GET %s HTTP/1.1" 200 %s "-" "-" \r\n' % (host, date, filename, (os.stat(filename)).st_size)
                date = "%s, %s GMT" % (x.strftime("%A")[:3], x.strftime("%d %b %Y %H:%M:%S"))
                responseheaders = response_headers(time,l, filename, extension)
            else:
                responseline = response_line(404)
                st_code = 404
                response_body = "<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1><p>The requested URL was not found on this server.</p><hr><address>My (Ubuntu) Server at 127.0.0.1 Port 12000</address></body></html>\n"
                l = len(response_body)
                date = "%s +0530" % (x.strftime("%d/%b/%Y:%H:%M:%S"))
                # logtext = '%s - - [%s] "GET %s HTTP/1.1" 404 0 "-" "-" \r\n' % (host, date, filename)
                responseheaders = response_headers(time,l)
    else:
        responseline = response_line(415)
        st_code = 415
        response_body = "<html><head><title>415 Unsupported Media Type</title></head><body><h1>415 Unsupported Media Type</h1><p>The server refused the request because the request entity format is not supported by this server.</p><hr><address>My (Ubuntu) Server at 127.0.0.1 Port 12000</address></body></html>\n"
        l = len(response_body)
        date = "%s +0530" % (time.strftime("%d/%b/%Y:%H:%M:%S"))
        responseheaders = response_headers(time,l)
    blank_line = "\r\n"
    return responseline, responseheaders, response_body
    
def POST(time,uri, data):
    global st_code
    lines = data.split('\r\n')
    filename = uri.strip('/')
    k = data.split("\r\n")
    ext_list = filename.split('.')
    if len(ext_list) > 1:
        extension = ext_list[1]
    if extension == "png" or extension == "jpg" or extension == "jpeg" or extension =="mp4" or extension == "mp3" or extension == "html" or extension == "txt":
        if os.path.exists(filename):
            responseline = response_line(200)
            st_code = 200
            l = len(lines[-1])
            print('\n')
            print(lines[-1])
            print('\n')
            if(l > max_payload):
                responseline, responseheaders, response_body = HTTP_413_handler(time)
                date = "%s +0530" % (time.strftime("%d/%b/%Y:%H:%M:%S"))
                logtext = '%s - - [%s] "POST %s HTTP/1.1" 413 %s "-" "-"\r\n' % (host, date, filename, (os.stat(filename)).st_size)
                with open("access.log", "a") as myfile:
                    myfile.write(logtext)
                return responseline, responseheaders, response_body
            responseheaders = response_headers(time,l+1)
            blank_line = "\r\n"
            response_body = lines[-1]
            date = "%s +0530" % (time.strftime("%d/%b/%Y:%H:%M:%S"))
            logtext = '%s - - [%s] "POST %s HTTP/1.1" 200 %s "-" "-" %s\r\n' % (host, date, filename, (os.stat(filename)).st_size, lines[-1])
            
        else:
            responseline = response_line(404)
            st_code = 404
            response_body = "<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1><p>The requested URL was not found on this server.</p><hr><address>My (Ubuntu) Server at 127.0.0.1 Port 12000</address></body></html>\n"
            l = len(response_body)
            date = "%s +0530" % (time.strftime("%d/%b/%Y:%H:%M:%S"))
            # logtext = '%s - - [%s] "GET %s HTTP/1.1" 404 0 "-" "-" \r\n' % (host, date, filename)
            responseheaders = response_headers(time,l)
            logtext = '%s - - [%s] "POST %s HTTP/1.1" 404 0 "-" "-"\r\n' % (host, date, filename)
    else:
        responseline = response_line(415)
        st_code = 415
        response_body = "<html><head><title>415 Unsupported Media Type</title></head><body><h1>415 Unsupported Media Type</h1><p>The server refused the request because the request entity format is not supported by this server.</p><hr><address>My (Ubuntu) Server at 127.0.0.1 Port 12000</address></body></html>\n"
        l = len(response_body)
        date = "%s +0530" % (time.strftime("%d/%b/%Y:%H:%M:%S"))
        responseheaders = response_headers(time,l)
        logtext = '%s - - [%s] "POST %s HTTP/1.1" 415 0 "-" "-"\r\n' % (host, date, filename)

    with open("access.log", "a") as myfile:
        myfile.write(logtext)
    return responseline, responseheaders, response_body
    
def HEAD(time,uri, data):
    global st_code
    print("Inside Head")
    filename = uri.strip('/')
    k = data.split("\r\n")
    ext_list = filename.split('.')
    if len(ext_list) > 1:
        extension = ext_list[1]
    if extension == "png" or extension == "jpg" or extension == "jpeg" or extension =="mp4" or extension == "mp3" or extension == "html" or extension == "txt":
        if os.path.exists(filename):
            print("File exists")
            responseline = response_line(200)
            st_code = 200
            with open(filename) as f:
                response_body = f.read()
            l = len(response_body)
            date = "%s +0530" % (x.strftime("%d/%b/%Y:%H:%M:%S"))
            # logtext = '%s - - [%s] "HEAD %s HTTP/1.1" 200 %s "-" "-" \r\n' % (host, date, filename, (os.stat(filename)).st_size)
            date = "%s, %s GMT" % (x.strftime("%A")[:3], x.strftime("%d %b %Y %H:%M:%S"))
            responseheaders = response_headers(time,l)
            
        else:
            print("File does not exist")
            responseline = response_line(404)
            st_code = 404
            response_body = "<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1><p>The requested URL was not found on this server.</p><hr><address>My (Ubuntu) Server at 127.0.0.1 Port 12000</address></body></html>\n"
            l = len(response_body)
            date = "%s +0530" % (x.strftime("%d/%b/%Y:%H:%M:%S"))
            # logtext = '%s - - [%s] "HEAD %s HTTP/1.1" 404 0 "-" "-" \r\n' % (host, date, filename)
            responseheaders = response_headers(time,l)
    else:
        responseline = response_line(415)
        st_code = 415
        response_body = "<html><head><title>415 Unsupported Media Type</title></head><body><h1>415 Unsupported Media Type</h1><p>The server refused the request because the request entity format is not supported by this server.</p><hr><address>My (Ubuntu) Server at 127.0.0.1 Port 12000</address></body></html>\n"
        l = len(response_body)
        date = "%s +0530" % (time.strftime("%d/%b/%Y:%H:%M:%S"))
        responseheaders = response_headers(time,l)
    blank_line = "\r\n"
    return responseline, responseheaders, response_body

def PUT(time,uri, data):
    global st_code
    data1 = data.split('\r\n')
    filename = uri.strip('/')
    k = data.split("\r\n")
    ext_list = filename.split('.')
    if len(ext_list) > 1:
        extension = ext_list[1]
    k = 0
    if extension == "png" or extension == "jpg" or extension == "jpeg" or extension =="mp4" or extension == "mp3" or extension == "html" or extension == "txt":
        for i in data1:
            if("Content-Length" in i):
                k += 1
                break
        if(k == 1):
            data = data.split('\r\n')
            print(data)
            i = 0
            while(data[i] != '' and i < len(data)):
                if(i < len(data) - 2 and data[i+1] == '' and data[i+2] == ''):
                    i += 3
                    break
                i += 1
            if(i < len(data) and data[i] == ''):
                i += 1
            str = ""
            while(i < len(data)):
                str += data[i]
                if(i != len(data) - 1):
                    str += '\r\n'
                i += 1
            print(len(str))
            if(len(str) > max_payload):
                responseline, responseheaders, response_body = HTTP_413_handler(time)
                return responseline, responseheaders, response_body
            else:
                filename = uri.strip('/')
                if(os.path.isfile(filename) == False):
                    f = open(filename,"w+")
                    f.write(str)
                    response_body = ""
                    if(f):
                        response_body += "<h1>The file was created.</h1>\n"
                    responseline = response_line(201)
                    st_code = 201
                    responseheaders = response_headers(time,len(response_body))
                elif(len(data) == 0):
                    f = open(filename,"w+")
                    f.write(str)
                    responseline = response_line(204)
                    st_code = 204
                    response_body = ""
                    l = len(response_body)
                    responseheaders = response_headers(time,l)
                else:
                    f = open(filename,"w+")
                    f.write(str)
                    responseline = response_line(200)
                    st_code = 200
                    response_body = ""
                    responseheaders = response_headers(time,len(response_body))

            """ 204 No Content Status Code Pending """
            blank_line = "\r\n"
            return responseline, responseheaders, response_body
        else:
            responseline, responseheaders, response_body = HTTP_411_handler(time)
            return responseline, responseheaders, response_body
    else:
        responseline = response_line(415)
        st_code = 415
        response_body = "<html><head><title>415 Unsupported Media Type</title></head><body><h1>415 Unsupported Media Type</h1><p>The server refused the request because the request entity format is not supported by this server.</p><hr><address>My (Ubuntu) Server at 127.0.0.1 Port 12000</address></body></html>\n"
        l = len(response_body)
        date = "%s +0530" % (time.strftime("%d/%b/%Y:%H:%M:%S"))
        responseheaders = response_headers(time,l)
        return responseline, responseheaders, response_body

def DELETE(time, uri):
    global st_code
    filename = uri.strip('/')   
    ext_list = filename.split('.')
    if len(ext_list) > 1:
        extension = ext_list[1]
    if(extension == "png" or extension == "jpg" or extension == "jpeg" or extension =="mp4" or extension == "mp3" or extension == "html" or extension == "txt"):
        filename = uri.strip('/')
        if(os.path.isfile(filename) == False):
            """ Not Sure about 202"""
            responseline = response_line(202)
            st_code = 202
            response_body = ""
            responseheaders = response_headers(time,len(response_body))
        else:
            os.remove(filename)
            responseline = response_line(200)
            st_code = 200
            response_body = "<html><body><h1>File deleted.</h1></body></html>"
            responseheaders = response_headers(time,len(response_body))
    
    else:
        responseline = response_line(415)
        st_code = 415
        response_body = "<html><head><title>415 Unsupported Media Type</title></head><body><h1>415 Unsupported Media Type</h1><p>The server refused the request because the request entity format is not supported by this server.</p><hr><address>My (Ubuntu) Server at 127.0.0.1 Port 12000</address></body></html>\n"
        l = len(response_body)
        date = "%s +0530" % (time.strftime("%d/%b/%Y:%H:%M:%S"))
        responseheaders = response_headers(time,l)
    return responseline, responseheaders, response_body

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
    global body
    global st_code
    # time.sleep(10)
    time = datetime.datetime.now()
    method, uri, http_version = HTTPRequest(data)
    print(uri)
    # print(method, uri, http_version)
    if(uri_len(uri.strip('/')) == 1):
        print("Inside this function")
        responseline, responseheaders, response_body = HTTP_414_handler(time)
        print("Inside this function")
    elif(method == 'GET'):
        if(uri is None or http_version != "HTTP/1.1"):
            responseline, responseheaders, response_body = HTTP_400_Handler(time)
        else:
            responseline, responseheaders, response_body = GET(time,uri, data)
        logtext(time, uri.strip('/'), st_code, method)
    elif(method == 'HEAD'):
        if(uri is None or http_version != "HTTP/1.1"):
            responseline, responseheaders, response_body = HTTP_400_Handler(time)
        else:
            responseline, responseheaders, response_body = HEAD(time,uri, data)
        logtext(time, uri.strip('/'), st_code, method)
    elif(method == 'POST'):
        if(uri is None or http_version != "HTTP/1.1"):
            responseline, responseheaders, response_body = HTTP_400_Handler(time)
        else:
            responseline, responseheaders, response_body = POST(time,uri, data)
    elif(method == 'PUT'):
        if(uri is None or http_version != "HTTP/1.1"):
            responseline, responseheaders, response_body = HTTP_400_Handler(time)
        else:    
            responseline, responseheaders, response_body = PUT(time,uri, data)
        logtext(time,uri.strip('/'), st_code, method)
    elif(method == 'DELETE'):
        if(uri is None or http_version != "HTTP/1.1"):
            responseline, responseheaders, response_body = HTTP_400_Handler(time)
        else:
            responseline, responseheaders, response_body = DELETE(time,uri)
        logtext(time, uri.strip('/'), st_code, method)
    else:
        responseline, responseheaders, response_body = HTTP_501_handler(time,uri)
        logtext(time,uri.strip('/'), st_code, method)
    # response_h = response_l + response_h + blank_line
    response = responseline + responseheaders + '\r\n'
    if type(response_body) == str:
        body = bytes(response_body,'utf-8')
    else:
        body = response_body


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
body = None
st_code = None
while True:
    # global conn
    # print("Starting Connection")
    conn, addr = s.accept()
    print("Connected by", addr)
    data = (conn.recv(1024))
    print(data)
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
    while(response is None or body is None):
        continue
    if(end - start < max_time):
        conn.sendall(bytes(response, 'utf-8'))
        conn.sendall(body)
    else:
        response = HTTP_408_Handler()
    response = None
    print("Closing Connection")
    conn.close()
    print("Closed Connection\n")
    

