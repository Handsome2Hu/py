#coding=utf-8
from socket import *
from time import ctime
import os
import re

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)
tcpsocket = socket(AF_INET,SOCK_STREAM)
tcpsocket.bind(ADDR)
tcpsocket.listen(5)

while True:
    print("waiting for connection...")
    tcpCliSock,addr = tcpsocket.accept()
    print("...connected from:",addr)
    
    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        if data.decode() == "date":
            tcpCliSock.send(('[%s] %s' % (ctime(),data.decode())).encode())
        elif data.decode() == "os":
            tcpCliSock.send(('[%s] %s' % (os.name,data.decode())).encode())
    tcpCliSock.close()
tcpsocket.close()