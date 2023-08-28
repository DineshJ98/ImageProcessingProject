import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

original_image = cv.imread('d2Image1.png',cv.IMREAD_COLOR)

blur = cv.medianBlur(original_image,3)
gray_image = cv.cvtColor(blur,cv.COLOR_BGR2GRAY)

hieght = 135
width = 65

refference_empty_space = gray_image[50:50+hieght,168:168+width]

space_1_upperrow = gray_image[50:50+hieght,100:100+width]
space_2_upperrow = gray_image[50:50+hieght,168:168+width]
space_3_upperrow = gray_image[50:50+hieght,233:233+width]
space_4_upperrow = gray_image[50:50+hieght,300:300+width]
space_5_upperrow = gray_image[50:50+hieght,365:365+width]
space_6_upperrow = gray_image[50:50+hieght,430:430+width]
space_7_upperrow = gray_image[50:50+hieght,496:496+width]

space_1_lowerrow = gray_image[205:205+hieght,100:100+width]
space_2_lowerrow = gray_image[205:205+hieght,168:168+width]
space_3_lowerrow = gray_image[205:205+hieght,233:233+width]
space_4_lowerrow = gray_image[205:205+hieght,300:300+width]
space_5_lowerrow = gray_image[205:205+hieght,365:365+width]
space_6_lowerrow = gray_image[205:205+hieght,430:430+width]
space_7_lowerrow = gray_image[205:205+hieght,496:496+width]

arr = [space_1_lowerrow,space_2_lowerrow,space_3_lowerrow,space_4_lowerrow,space_5_lowerrow,space_6_lowerrow,space_7_lowerrow,
       space_1_upperrow,space_2_upperrow,space_3_upperrow,space_4_upperrow,space_5_upperrow,space_6_upperrow,space_7_upperrow]

cv.imshow('name',cv.divide(space_3_upperrow,refference_empty_space))
cv.waitKey(0)

def findEmpty(img):
    subtracted = cv.divide(img,refference_empty_space)
    # ret,thresh =  cv.threshold(subtacted,0,255,cv.THRESH_BINARY)
    # cv.imshow('name',subtracted)
    # cv.waitKey(0)
    count = np.sum(subtracted == 255)
    if count > (img.shape[0]*img.shape[1])*0.1:
        return True
    else:
        return False

# print(findEmpty(space_3_upperrow))
temp = space_1_lowerrow.copy()

def findEmptySpaces(arr):
    count = 0
    j = -1
    for item in arr:
        if findEmpty(item) == True:
            count += 1
            # cv.imshow('name',item)
            # cv.waitKey(0)
    return count

print(findEmptySpaces(arr))

# i = 0
# for item in arr:
#     i +=1
#     plt.subplot(7,7,i)
#     plt.imshow(item,cmap='gray')
# plt.show()

plt.subplot(231)
plt.imshow(cv.cvtColor(refference_empty_space,cv.COLOR_BGR2RGB))

plt.subplot(2,3,2)
plt.imshow(cv.cvtColor(space_3_upperrow,cv.COLOR_BGR2RGB))

plt.subplot(2,3,3)
plt.imshow(cv.divide(space_3_upperrow,refference_empty_space),cmap='gray')

plt.subplot(234)
plt.imshow(cv.cvtColor(refference_empty_space,cv.COLOR_BGR2RGB))

plt.subplot(2,3,5)
plt.imshow(cv.cvtColor(temp,cv.COLOR_BGR2RGB))

plt.subplot(2,3,6)
plt.imshow(cv.divide(space_2_lowerrow,refference_empty_space),cmap='gray')
plt.show()
