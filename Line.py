import numpy as np
import cv2

canvas= np.zeros((300,300,3),dtype="uint8")
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

color=(255,0,0)
cv2.line(canvas,(0,0),(300,300),color,4)

cv2.imshow("Line",canvas)
cv2.waitKey(0)

color2=(220,180,90)
cv2.line(canvas,(300,0),(0,300),color2,5)
cv2.imshow("Line",canvas)
cv2.waitKey(0)