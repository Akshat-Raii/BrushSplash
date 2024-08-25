import cv2 as cv
import numpy as np
import os
import handTrackingModule as htm


brushThickness=50
eraserThickness=50

folderPath="Images"
myList=os.listdir(folderPath)
headerList=[]

for imPath in myList:
    image=cv.imread(f"{folderPath}/{imPath}")
    headerList.append(image)

header=headerList[0]
color=(255,0,0)

cap=cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector=htm.handDetector(detectionCon=0.85)

xp,yp=0,0
imgCanvas=np.zeros((720,1280,3),np.uint8)

while True:
    success,img=cap.read()
    img=cv.flip(img,1)

    img=detector.findHands(img,draw=False)
    lmList=detector.findPosition(img,draw=False)

    if len(lmList)!=0:

        x1,y1=lmList[8][1:]
        x2,y2=lmList[12][1:]

        fingers=detector.fingersUp()
        
    #4.If Selection mode - Two fingers are up
        if fingers[1] and fingers[2]:
            xp,yp=0,0
            
            # Checking for the choice of color
            if y1<125:
                if 250<x1<450:
                    header=headerList[0]
                    color=(255,0,0)
                elif 550<x1<750:
                    header=headerList[1]
                    color=(0,0,255)
                elif 800<x1<950:
                    header=headerList[2]
                    color=(0,255,0)
                elif 1050<x1<1200:
                    header=headerList[3]
                    color=(0,0,0)
            cv.rectangle(img,(x1,y1-25),(x2,y2+25),color,cv.FILLED)

    #5.If Drawing mode - Index finger is up
        if fingers[1] and fingers[2]==False:
            cv.circle(img,(x1,y1),15,(0,0,0),cv.FILLED)
            
            if xp==0 and yp==0:
                xp,yp=x1,y1
            
            if color==(0,0,0):
                cv.line(img,(xp,yp),(x1,y1),color,eraserThickness)
                cv.line(imgCanvas,(xp,yp),(x1,y1),color,eraserThickness)
            else:
                cv.line(img,(xp,yp),(x1,y1),color,brushThickness)
                cv.line(imgCanvas,(xp,yp),(x1,y1),color,eraserThickness)
            xp,yp=x1,y1


    imgGray=cv.cvtColor(imgCanvas,cv.COLOR_BGR2GRAY)
    _,binInv=cv.threshold(imgGray,50,255,cv.THRESH_BINARY_INV)
    binInv=cv.cvtColor(binInv,cv.COLOR_GRAY2BGR)
    img=cv.bitwise_and(img,binInv)
    img=cv.bitwise_or(img,imgCanvas)

    img[0:125,0:1280]=header
    cv.imshow("Brush Splash",img)
    if cv.waitKey(1) & 0xFF == ord('q'):  # Exit loop if 'q' is pressed
            break
cap.release()
cv.destroyAllWindows()
