import cv2
import numpy as np
import os

# 调试信息
print(f"当前工作目录: {os.getcwd()}")


bait = cv2.imread("icon/bait.png")
close = cv2.imread("icon/close.png")
maximize = cv2.imread("icon/maximize.png")
purchase = cv2.imread("icon/purchase.png")
test = cv2.imread("test/test.png")
judge = cv2.imread("icon/judge.png")
needle = cv2.imread("icon/needle.png")
closetip = cv2.imread("icon/closetip.png")

if closetip is None:
    raise ValueError("无法读取 closetip.png")
if judge is None:
    raise ValueError("无法读取 judge.png")
if needle is None:
    raise ValueError("无法读取 needle.png")

print(f"成功读取 closetip.png，尺寸: {closetip.shape}")
print(f"成功读取 judge.png，尺寸: {judge.shape}")
print(f"成功读取 needle.png，尺寸: {needle.shape}")

# 预计算模板灰度图，避免每帧重复转换
_judge_gray = cv2.cvtColor(judge, cv2.COLOR_BGR2GRAY)
_needle_gray = cv2.cvtColor(needle, cv2.COLOR_BGR2GRAY)

#图一为被匹配，图二为匹配
def matching(img1,img2,confident_aim=0.9):
    img1_gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY,dstCn=1)
    # 模板是固定图片，用预计算的灰度图
    if img2 is judge:
        img2_gray = _judge_gray
    elif img2 is needle:
        img2_gray = _needle_gray
    else:
        img2_gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY,dstCn=1)

    #匹配图像并返回坐标min_loc
    res=cv2.matchTemplate(img1_gray,img2_gray,cv2.TM_SQDIFF_NORMED)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
    confident = 1.0 - min_val

    if confident>confident_aim:
        return min_loc,confident
    else:
        #低置信度不采用
        return None,None

def draw_match(img,loc,template,confident):
    """在图像上绘制匹配结果"""
    if loc is None:
        return None
    h,w=template.shape[:2]
    bottom_right=(loc[0] + w, loc[1] + h)
    cv2.rectangle(img, loc, bottom_right, (0, 0, 255), 2)
    cv2.putText(img, f"{confident:.2f}", loc, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3, cv2.LINE_AA)
        

def save_screenshot(img):
    """保存截图到 screenshots 文件夹

    Args:
        img: cv2 图片数组
    """
    import time
    os.makedirs("screenshots", exist_ok=True)
    path = f"screenshots/screenshot_{time.strftime('%Y%m%d_%H%M%S')}.png"
    cv2.imwrite(path, img)
    print(f"已保存: {path}")
    return path

