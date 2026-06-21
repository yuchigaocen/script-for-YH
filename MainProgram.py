import cv2
import numpy as py

import win32gui


#hwnd= Handle to a Window
#hwnd=986274 | class=UnrealWindow | title='异环  '  

hwnd = win32gui.FindWindow('UnrealWindow',u'异环  ')
if hwnd == 0:
    print('窗口未找到')

hwnd_dc = win32gui.GetWindowDC(hwnd)
mfc_dc =  win32ui.CreateDCFromHandle(hwnd_dc)
save_dc = mfc_dc.CreateCompatibleDC()
