import cv2
import numpy as py
import win32gui
import game_capture
import Match


hwnd=game_capture.find_window("异环")

#执行一次截图标注
#img=game_capture.capture_game(hwnd)
#Match.matching(Match.test,Match.judge)
for frame in game_capture.frame_generator(hwnd):
    result=Match.matching(frame,Match.judge)
    
    if cv2.waitKey(1) & 0xFF in (ord('q'), 27):
        break

cv2.waitKey(0)