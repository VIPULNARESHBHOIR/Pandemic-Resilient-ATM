import cv2
import numpy as np
import Hand_trace as htm
import time
import autopy

wCam,hCam = 640,480
wScr,hScr= autopy.screen.size() #screen size
frameR=100 #frame reduction
smoothening=5

pTime=0
plocX,plocY=0,0
clocX,clocY=0,0

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
detector=htm.handDetector(maxHands=1)

while True:
    #findind the hand landmarks
    success,img=cap.read()
    img=detector.findHands(img)
    lmList,bbox=detector.findPosition(img)
    #print(lmList)

    #get the tip of the index and middle finger
    if len(lmList)!=0:
        x1,y1=lmList[8][1:]
        x2,y2=lmList[12][1:]
        #print(x1,y1,x2,y2)

    #check Up fingers
    fingures=detector.fingersUp()
    #print(fingures,"\n")

    cv2.rectangle(img,(frameR,frameR),(wCam-frameR,hCam-frameR),
    (255,0,255),2)
    if len(fingures)!=0:
        #only index fingure in moving position
        if fingures[1]==1 and fingures[2]==0:
            #converting coordinates for perfect movment of hands
            x3=np.interp(x1,(0,wCam),(0,wScr))
            y3=np.interp(y1,(0,hCam),(0,hScr))

            #setting to mmouse curser properly over the screen (smothening)
            clocX=plocX+(x3-plocX)/smoothening
            clocY=plocY+(y3-plocY)/smoothening
            #movment of mouse over the screen
            autopy.mouse.move(wScr-clocX,clocY)
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            
            plocX,plocY=clocX,clocY
        
        #when index and middle fingure are up then click
        if fingures[1]==1 and fingures[2]==1:
            #find distance between fingures
            dis,img,line_info=detector.findDistance(8,12,img)
            

            if dis<25:
                cv2.circle(img,(line_info[4],line_info[5]),15,(0,255,0),cv2.FILLED)
                autopy.mouse.click()
                time.sleep(0.1)
                #print(dis)

    #framerate
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    cv2.imshow('myimage',img)
    cv2.waitKey(1)