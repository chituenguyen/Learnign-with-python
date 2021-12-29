import datetime

from PIL import ImageGrab
import numpy as np
import cv2


width = 1366
height = 768
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

webcam = cv2.VideoCapture(1)

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Secret Capture', img_final)

    # cv2.imshow('webcam', frame)

    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break