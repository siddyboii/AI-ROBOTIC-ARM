import cvzone
import cv2

#from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject
import testing1 as tt

cap = cv2.VideoCapture(0)
detector = tt.handDetector(maxHands=1,detectionCon=0.7)
mySerial = SerialObject("COM5", 9600, 1)
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUp()
        #print(fingers)
        mySerial.sendData(fingers)


    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

