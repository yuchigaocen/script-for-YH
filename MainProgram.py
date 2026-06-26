import cv2
import game_capture
import pyautogui
import input

start = False
tofish = False

hwnd=game_capture.find_window("异环")

#钓鱼模块调用视频捕获
for frame in game_capture.frame_generator(hwnd):
    if start == False:
        input.click(hwnd, input.start)
        start = True

    if tofish == False:
        tofish = input.tofish(hwnd, frame)


    if tofish == True:
        tofish = input.fishing(hwnd, frame)

    cv2.imshow('press q/Esc quit', frame)
    if cv2.waitKey(1) & 0xFF in (ord('q'), 27):
        if input.current_dir:
            pyautogui.keyUp(input.current_dir)
        break

cv2.waitKey(0)