import dxcam
import cv2
import win32gui
import time
import os
import Match

def find_window(title_keyword):
    result = []
    
    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            if title_keyword.lower() in win32gui.GetWindowText(hwnd).lower():
                result.append(hwnd)

    win32gui.EnumWindows(callback, None)
    if not result:
        raise ValueError(f"未找到包含 '{title_keyword}' 的窗口")

    print(f"找到窗口，句柄: {result[0]}")
    return result[0]

def capture_game(hwnd):
    # 获取客户区窗口的相对坐标
    left, top, right, bottom = win32gui.GetClientRect(hwnd)
    # ClientToScreen 将客户区左上角(0,0)转换为屏幕坐标
    left, top = win32gui.ClientToScreen(hwnd, (left, top))
    right, bottom = win32gui.ClientToScreen(hwnd, (right, bottom))
    # 创建DXCam相机，指定输出格式为BGR(OpenCV默认格式)
    camera = dxcam.create(output_color="BGR")

    # 截取指定区域
    frame = camera.grab(region=(left, top, right, bottom))

    if frame is None:
        raise ValueError("截图失败，可能是最小化或程序被关闭")

    return frame

def img_save(img):
    os.makedirs("screenshots", exist_ok=True)  #创建文件夹，如果已存在也不报错
    path = f"screenshots/game_{time.strftime('%Y%m%d_%H%M%S')}.png"
    cv2.imwrite(path, img)
    print(f"已保存: {path}")
    
def realtime_capture(hwnd,template):
    left, top, right, bottom = win32gui.GetClientRect(hwnd)
    # ClientToScreen 将客户区左上角(0,0)转换为屏幕坐标
    left, top = win32gui.ClientToScreen(hwnd, (left, top))
    right, bottom = win32gui.ClientToScreen(hwnd, (right, bottom))
    region = (left,top,right,bottom)
    
    # 创建相机并启动连续捕获
    camera = dxcam.create(output_color="BGR")
    camera.start(region=region, target_fps=60)
    
    print("开始实时识别，按 q/Esc 退出")
    
    while True:
        frame=camera.get_latest_frame()
        
        
        if template is None:
            print("警告: 未找到模板图片，跳过匹配")
            cv2.imshow("press q/Esc quit", frame)
        else:
            Match.matching(frame,template)
            
        
        # 按 q 或 Esc 退出
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:
            break