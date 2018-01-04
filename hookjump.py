#coding=utf-8
from ctypes import *
import pythoncom
import pyHook
import win32api
import win32con
import math
import time
bIsStart = True
#等待时间系数
wait = 0.28
x = []
y = []
def KeyStroke(event):
    #检测按键是否为Q键
    global x
    global y
    global bIsStart
    if event.Ascii ==81:
        if bIsStart == True:
            x = win32api.GetCursorPos()
            print("你输入了起点")
            bIsStart = False
        else:
            y = win32api.GetCursorPos()
            print("你输入了终点")
            d = math.sqrt((x[0]-y[0])*(x[0]-y[0]) + (x[1]-y[1])*(x[1]-y[1]))
            waittime = wait * d
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
            #按下时间
            time.sleep(waittime/100)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)    
            print("我跳起来啦！")
            bIsStart = True
    #返回直到下一个钩子事件触发
    return True
#创建和注册钩子函数管理器
kl = pyHook.HookManager()
kl.KeyDown = KeyStroke
#注册侧键盘记录的钩子，然后永久执行
kl.HookKeyboard()
pythoncom.PumpMessages()