import cv2 
import numpy as np

img = cv2.imread("C:/Users/jayap/DIP/images/BW.jpeg" , 0)

img = 255 - img
cv2.imshow("Output", img)
cv2.waitKey(0)
