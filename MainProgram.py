import cv2
import numpy as py
import win32gui
import game_capture
import Match


hwnd=game_capture.find_window("异环")
#执行一次截图标注
img=game_capture.capture_game(hwnd)
Match.matching(img,Match.bait)


cv2.waitKey(0)