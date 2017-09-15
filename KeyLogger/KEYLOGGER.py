#coding=utf-8

from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32          = windll.user32
kernel32        = windll.kernel32
psapi           = windll.psapi
current_window = None

def get_current_process():
    #获取前台窗口句柄
    hwnd = user32.GetForegroundWindow()
    
    #获取进程ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd,byref(pid))
    
    #保存当前的进程
    process_id = "%d" % pid.value
    
    #申请内存
    executable = create_string_buffer("\x00" * 512)
    
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)
    
    
    

