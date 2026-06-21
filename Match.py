import cv2
import numpy as py

img_store1=cv2.imread('Fishing_bait3.png')
purchase=cv2.imread('purchase.png')
close=cv2.imread('close.png')
bait=cv2.imread('bait.png')
maximize=cv2.imread('maximize.png')


def matching(img1,img2):
    img1_gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY,dstCn=1) #转换为单通道灰度图像
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY,dstCn=1)

    h,w=img2.shape
    res=cv2.matchTemplate(img1_gray,img2,cv2.TM_SQDIFF)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)

    bottom_right=(min_loc[0] + w, min_loc[1] + h)
    cv2.rectangle(img1, min_loc, bottom_right, (0, 0, 255), 3)
    cv2.imshow('Detected Range',img1)

matching(img_store1,purchase)
matching(img_store1,close)
matching(img_store1,bait)
matching(img_store1,maximize)

cv2.waitKey(0)