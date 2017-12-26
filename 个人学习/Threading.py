#coding=utf-8
import threading
import time

class timer(threading.Thread):
    def __init__(self,num,interval):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval = interval
        self.thread_stop = False
        
    def run(self):
        while not self.thread_stop:
            print('Thread Object(%d),Time:%s\n' % (self.thread_num,time.ctime()))
            time.sleep(self.interval)
            
    def stop(self):
        self.thread_stop = True


if __name__=='__main__':
    thread1 = timer(1, 1)  
    thread2 = timer(2, 2)  
    thread1.start()  
    thread2.start()  
    time.sleep(10)  
    thread1.stop()  
    thread2.stop()  