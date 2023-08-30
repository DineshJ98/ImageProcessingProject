import cv2 as cv
import pickle
import numpy as np

# entrance coordinates
eX,eY = 335,5
width,heigth = 102,46

try:
    with open('carParkPos','rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        distance = np.sqrt(((eX-x)**2)+((eY-y)**2))
        posList.append((x,y,distance))

    if event == cv.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1,y1,_ = pos
            if x1<x<x1+width and y1<y<y1+heigth:
                posList.pop(i)

while True:
    
    image = cv.imread('carParkImg.png')
    
    for pos in posList:
        cv.rectangle(image,(pos[0],pos[1]),(pos[0]+width,pos[1]+heigth),(255,0,255),2)

    with open('carParkPos','wb') as f:
        pickle.dump(posList,f)

    
    cv.imshow("original image",image)
    cv.setMouseCallback("original image",mouseClick)
    cv.waitKey(1)