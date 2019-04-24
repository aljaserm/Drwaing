import numpy as np
import cv2 as cv

canvas= np.zeros((300,300,3),dtype="uint8")
cv.imshow("Rectangle", canvas)
cv.waitKey(0)
color=(255,0,0)
cv.rectangle(canvas,(10,10),(60,60),color,5)
cv.imshow("Rectangle",canvas)
cv.waitKey(0)

color=(255,255,0)
cv.rectangle(canvas,(60,60),(200,200),color,-1)
cv.imshow("Rectangle",canvas)
cv.waitKey(0)