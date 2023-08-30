import cv2 as cv
import pickle
import numpy as np
import cvzone as cvz

width,heigth = 102,46

cap = cv.VideoCapture('carPark.mp4')


with open('carParkPos','rb') as f:
    posList = pickle.load(f)

def checkParkingSpace(imageProcessed):
    i = []
    mindist = 1000
    minIndex = 0
    spaceCounter = 0
    for j,pos in enumerate(posList):
        x,y,distance= pos
        cropped = imageProcessed[y:y+heigth,x:x+width]
        # cv.imshow(str(x*y),cropped)            
        bitCount = cv.countNonZero(cropped)
        text = str(round(distance,1))+'/'+str(bitCount)
        cvz.putTextRect(image,text,(x,y+heigth-4),scale=0.8,thickness=2,offset=0)

        if bitCount < 900:
                color = (35,220,240)
                thickness = 3
                i.append(j)
                spaceCounter += 1
        else:
                color = (0,0,255)
                thickness = 2

        cv.rectangle(image,(pos[0],pos[1]),(pos[0]+width,pos[1]+heigth),color,thickness)

    cvz.putTextRect(image,'Entrence',(335,20),scale=1,thickness=2,offset=0,colorR=(0,255,0))
    cvz.putTextRect(image,str(len(posList))+'/'+str(spaceCounter),(0,50),colorR=(0,255,0))
        
    for k in i:
         _,_,dist = posList[k]
         if dist < mindist:
              mindist = dist
              minIndex = k
    minPos = posList[minIndex]
    cvz.putTextRect(image,'park here',(minPos[0],minPos[1]+10),scale=1,thickness=2,colorR=(0,255,0),offset=0)
    cv.rectangle(image,(minPos[0],minPos[1]),(minPos[0]+width,minPos[1]+heigth),(0,255,0),2)



try:
    while True:

        if cap.get(cv.CAP_PROP_POS_FRAMES) == cap.get(cv.CAP_PROP_FRAME_COUNT):
            cap.set(cv.CAP_PROP_POS_FRAMES,0)

        success,image = cap.read()
        grayImage = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
        blurImage = cv.GaussianBlur(grayImage,(3,3),1)
        threshImage = cv.adaptiveThreshold(blurImage,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,25,16)
        medianBlurImage = cv.medianBlur(threshImage,5)
        kernel = np.ones((3,3),np.uint8)
        dilateImage = cv.dilate(medianBlurImage,kernel,iterations= 1)

        checkParkingSpace(dilateImage)
        
        cv.imshow('image',image)
        # cv.imshow('blurImage',blurImage)
        # cv.imshow('threshImage',threshImage)
        # cv.imshow('finalImage',dilateImage)
        cv.waitKey(10)

except:
    print("video has ended!")