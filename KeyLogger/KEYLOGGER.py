from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32          = windll.user32
kernel32        = windll.kernel32
psapi           = windll.psapi
current_window = None

#def get_current_process():
    #
hwnd = user32.GetForegroundWindow()

