import cvzone
import cv2

#from cvzone.HandTrackingModule import HandDetector
import handtrackingmodule as htm

cap = cv2.VideoCapture(0)
detector = htm.handDetector(maxHands=1,detectionCon=0.5)
#detector = cvzone.HandDetector(maxHands=1,detectionCon=0.5)




while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUp(img)
        print(fingers)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break