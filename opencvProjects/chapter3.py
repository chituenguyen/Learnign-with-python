import cv2

img=cv2.imread("resource/chandung.jpg")
print(img.shape)
imgResize=cv2.resize(img,(400,600))
imgCrop=img[0:200,200:500]

cv2.imshow("image",img)
cv2.imshow("resize",imgResize)
cv2.imshow("image croped",imgCrop)
cv2.waitKey(0)