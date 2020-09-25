import win32api
import win32con
import time
import sys
import os
from datetime import datetime

KEYCODE = {
    'F1':0x70,
    'F2':0x71,
    'F3':0x72,
    'F4':0x73,
    'F5':0x74,
    'F6':0x75,
    'F7':0x76,
    'F8':0x77,
    'F9':0x78,
    'F10':0x79,
    'F11':0x7A,
    'F12':0x7B,
    'F13':0x7C,
    'F14':0x7D,
    'F15':0x7E,
    'F16':0x7F,
    'F17':0x80,
    'F18':0x81,
    'F19':0x82,
    'F20':0x83,
    'F21':0x84,
    'F22':0x85,
    'F23':0x86,
    'F24':0x87,
}

def Keybd_Event(VK_CODE): #VK_CODE為鍵盤編碼
    # @Keyboard
    # input
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    VK_CODE = int(VK_CODE)
    win32api.keybd_event(VK_CODE, 0, 0, 0)
    win32api.keybd_event(VK_CODE, 0, win32con.KEYEVENTF_KEYUP, 0)

    print ("[",current_time, "] - press", str(VK_CODE), "successfully!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        inputParam = sys.argv[1]
    else:
        inputParam = "F10"

    while(True):
        Keybd_Event(KEYCODE[inputParam])
        time.sleep(60*60)