import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('d2Image1.png',cv.IMREAD_COLOR)
# image = cv.cvtColor(image,cv.COLOR_BGR2RGB)



def colorThresholding(img):
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    lower = np.array([0,0,180])
    upper = np.array([179,30,255])
    mask = cv.inRange(hsv,lower,upper)
    return mask

white_color_mask = colorThresholding(image)

plt.subplot(121)
plt.imshow(cv.cvtColor(image,cv.COLOR_BGR2RGB))

plt.subplot(122)
plt.imshow(white_color_mask,cmap='gray')
plt.show()

