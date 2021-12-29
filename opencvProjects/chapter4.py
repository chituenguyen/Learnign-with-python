import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8) #2^8 bits BGR
print(img.shape)
# img[100:200,100:200]=255,0,0
cv2.line(img,(0,0),(200,500),(155,255,100),4) # starting point,ending point,color,thickness
cv2.rectangle(img,(0,0),(400,200),(0,0,200),cv2.FILLED) # instead thickness
cv2.circle(img,(400,200),40,(100,100,100),2)
cv2.putText(img,"hello world",(100,100),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,150,0),1)
cv2.imshow("Image",img)
cv2.waitKey(0)