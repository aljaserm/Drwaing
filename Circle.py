import numpy as np
import cv2 as cv

canvas= np.zeros((300,300,3),dtype="uint8")
cv.imshow("canvas", canvas)
cv.waitKey(0)

(centerX,centerY)=(canvas.shape[1]//2,canvas.shape[0]//2)
color=(255,0,0)
cv.circle(canvas,(centerX,centerY),30,color)
cv.imshow("circle",canvas)
cv.waitKey(0)

for r in range(0,175,25):
    cv.circle(canvas,(centerX,centerY),r,color)
cv.imshow("circle2",canvas)
cv.waitKey(0)