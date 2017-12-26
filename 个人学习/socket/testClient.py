#coding=utf-8
from socket import *
from time import ctime

DEFAULTHOST = 'localhost'
DEFAULTPORT = 21567
BUFSIZE = 1024
#ADDR = (HOST,PORT)

def get_addr():
    HOST = input("请输入IP")
    PORT = input("请输入端口号")
    if not HOST:
        HOST = DEFAULTHOST
    if not PORT:
        PORT = DEFAULTPORT
    return HOST,PORT

HOST, PORT = get_addr()
ADDR = (HOST,PORT)


tcpsocket = socket(AF_INET,SOCK_STREAM)
tcpsocket.connect(ADDR)

while True:
    data = input("> ")
    if not data:
        break
    tcpsocket.send(data.encode())
    data= tcpsocket.recv(BUFSIZE)
    if not data:
        break
    print(data)
tcpsocket.close()