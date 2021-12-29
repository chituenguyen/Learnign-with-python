import cv2
import numpy as np






frameWidth=640
frameHeight=480
cap=cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)
def getCoutours(img):
    contours,hierar=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>500:
            # cv2.drawContours(imageResult,cnt,-1,(255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
    return x+w//2,y
def findColor(img):
    count=0
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = 3
    h_max = 32
    s_min = 81
    s_max = 255
    v_min = 138
    v_max = 255
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    x,y=getCoutours(mask)
    cv2.circle(imageResult,(x,y),10,(255,0,0),cv2.FILLED)
    count+=1
def draw():

while True:
    success, img = cap.read()
    imageResult=img.copy()
    findColor(img)
    cv2.imshow("orginal", imageResult)
    cv2.waitKey(1)