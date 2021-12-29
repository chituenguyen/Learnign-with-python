import cv2
import numpy as np

kernel=np.ones((5,5),np.uint8)

img=cv2.imread("resource/chandung.jpg")

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(5,7),0)
imgCanny=cv2.Canny(img,100,100)
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1) #tang trang
imgEroded=cv2.erode(imgDialation,kernel,iterations=1) # tang den
cv2.imshow("display",imgGray)
cv2.imshow('blur',imgBlur)
cv2.imshow('canny',imgCanny)
cv2.imshow('dialte',imgDialation)
cv2.imshow('erorded',imgEroded)
cv2.waitKey(0)
