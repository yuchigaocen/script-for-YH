import cv2
import numpy as np
import game_capture
import os

# 调试信息
print(f"当前工作目录: {os.getcwd()}")


bait = cv2.imread("icon/bait.png")
close = cv2.imread("icon/close.png")
maximize = cv2.imread("icon/maximize.png")
purchase = cv2.imread("icon/purchase.png")
test = cv2.imread("test/fishing_bait.png")

if bait is None:
    raise ValueError("无法读取 bait.png")
#todo 防御措施补全

print(f"成功读取 bait.png，尺寸: {bait.shape}")


#图一为被匹配，图二为匹配
def matching(img1,img2):
    img1_gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY,dstCn=1) #转换为单通道灰度图像，增加运算效率
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY,dstCn=1)

    #匹配图像并返回坐标min_loc
    res=cv2.matchTemplate(img1_gray,img2,cv2.TM_SQDIFF)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)

    #绘制矩形并显示
    h,w=img2.shape
    bottom_right=(min_loc[0] + w, min_loc[1] + h)
    cv2.rectangle(img1, min_loc, bottom_right, (0, 0, 255), 2) 
    cv2.imshow('Detected Range',img1)
    
    return min_loc

cv2.waitKey(0)