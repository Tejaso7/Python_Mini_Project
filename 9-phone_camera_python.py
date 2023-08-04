import cv2
import numpy as np
url = "https://[2405:201:1017:e00e:da32:e3ff:fe6c:ccfb]:8080/video"
cp = cv2.VideoCapture(url)
while(True):
    camera, frame = cp.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()