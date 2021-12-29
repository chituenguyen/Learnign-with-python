import cv2
import numpy as np
width,height=250,350
img=cv2.imread("resource/chandung.jpg")
pts1=np.float32([[73,73],[246,46],[116,208],[464,165]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOut=cv2.warpPerspective(img,matrix,(width,height))
for x in range(0,4):
    cv2.circle(img,(pts1[x][0],pts1[x][1]),5,(255,0,0),cv2.FILLED)
cv2.imshow("image",imgOut)
cv2.imshow("old",img)
cv2.waitKey(0)
