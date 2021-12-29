import cv2
import numpy as np


def empty(a):
    pass


cv2.namedWindow("TrackBars", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("TrackBars", 440, 240)
cv2.createTrackbar("Hue min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sta min", "TrackBars", 19, 255, empty)
cv2.createTrackbar("Sta max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val min", "TrackBars", 64, 255, empty)
cv2.createTrackbar("Val max", "TrackBars", 255, 255, empty)
img = cv2.imread("resource/chandung.jpg")

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while True:
    h_min = cv2.getTrackbarPos("Hue min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sta min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sta max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val max", "TrackBars")

    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imageResult=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("orginal", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("mask",mask)
    cv2.imshow("imageResult",imageResult)
    cv2.waitKey(1)
