#coding=utf-8

from socketserver import (TCPServer as TCP, StreamRequestHandler as SHR)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST,PORT)

class MyRequestHIandler(SHR):
    def handle(self):
        print('...connected from:', self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(),self.rfile.readline())).encode())
        
tcpServ = TCP(ADDR,MyRequestHIandler)
print('waiting for connection...')
tcpServ.serve_forever()