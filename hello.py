import win32gui,win32api,win32con
import pyautogui
import re

hwnd_title = dict()
def get_all_hwnd(hwnd,mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})
win32gui.EnumWindows(get_all_hwnd, 0)

for h,t in hwnd_title.items():
    if re.match('QQ飞车',t):
        hwnd=h
win32gui.SetForegroundWindow(hwnd)
