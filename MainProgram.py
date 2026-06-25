import cv2
import numpy as py
import win32gui
import game_capture
import Match
import calculate
import pyautogui

#防重复标记
havesave = 0

hwnd=game_capture.find_window("异环")

#执行一次截图标注

#钓鱼模块调用视频捕获
for frame in game_capture.frame_generator(hwnd):
    loc,confident=Match.matching(frame,Match.judge,0.97)
    loc2,confident2=Match.matching(frame,Match.needle,0.97)
    
    if loc and loc2:
        needle_center = calculate.center(loc2,Match.needle)
        judge_center = calculate.center(loc,Match.judge)
        #指针偏右
        if needle_center[0]>judge_center[0]:
            pyautogui.keyUp("d")
            pyautogui.keyDown("a")
        elif needle_center[0]<judge_center[0]:
            pyautogui.keyUp("a")
            pyautogui.keyDown("d")
    
    #保存未标记图标
    if confident is None and confident2 is not None and havesave == 0:
        Match.save_screenshot(frame)
        havesave = 1 #防重复标记
        print("已保存未标记图标")
    
    Match.draw_match(frame,loc,Match.judge,confident)
    Match.draw_match(frame,loc2,Match.needle,confident2)

    cv2.imshow('press q/Esc quit', frame)
    if cv2.waitKey(1) & 0xFF in (ord('q'), 27):
        pyautogui.keyUp("a")
        pyautogui.keyUp("d")
        break

cv2.waitKey(0)