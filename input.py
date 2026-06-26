import pyautogui
import time
import win32gui
import Match
import calculate
current_dir = None
havesave = 0
closetip_count = 0

close = (1225,65)
start = (1080,625)
tofish = (1185,650)

def fishing(hwnd, frame):
    global current_dir, havesave, closetip_count
    loc,confident=Match.matching(frame,Match.judge,0.97)
    loc2,confident2=Match.matching(frame,Match.needle,0.97)
    loc3,confident3=Match.matching(frame,Match.closetip,0.90)

    if loc and loc2:
        needle_center = calculate.center(loc2,Match.needle)
        judge_center = calculate.center(loc,Match.judge)
        #指针偏右
        if needle_center[0] > judge_center[0]:
            new_dir = 'a'
        elif needle_center[0] < judge_center[0]:
            new_dir = 'd'
        else:
            new_dir = None

        #方向变化时才发键盘事件
        if new_dir != current_dir:
            if current_dir:
                pyautogui.keyUp(current_dir)
            if new_dir:
                pyautogui.keyDown(new_dir)
            current_dir = new_dir

    #保存未标记图标
    if confident is None and confident2 is not None and havesave == 0:
        Match.save_screenshot(frame)
        havesave = 1 #防重复标记
        print("已保存未标记图标")

    Match.draw_match(frame,loc3,Match.closetip,confident3)
    Match.draw_match(frame,loc,Match.judge,confident)
    Match.draw_match(frame,loc2,Match.needle,confident2)

    #loc3 连续出现5帧后才点击，防止误触
    if loc3:
        closetip_count += 1
        if closetip_count >= 30:
            click(hwnd, (650,650))
            closetip_count = 0
            return False
    else:
        closetip_count = 0

    return True

#点击，coord是客户区坐标
def click(hwnd, coord):
    screen_x, screen_y = win32gui.ClientToScreen(hwnd, (int(coord[0]), int(coord[1])))
    pyautogui.click(screen_x, screen_y)
    
    
    
def shutdown(hwnd):
    click(hwnd, close)
    click(hwnd, start)

def tofish(hwnd, frame):
    pyautogui.press("f")
    loc,_=Match.matching(frame,Match.judge,0.97)
    loc2,_=Match.matching(frame,Match.needle,0.97)
    if loc and loc2:
        return True
    if loc is None and loc2:
        shutdown(hwnd)
        return False

    return False
    