import cv2
import mediapipe as mp
import time 


class handDetector():
    def __init__(self,
                 mode = False,
                 maxHands = 2,
                 modelComplexity = 1,
                 detectionCon = 0.5,
                 trackingCon = 0.5) -> None:
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionCon = detectionCon
        self.trackinCon = trackingCon
        

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.modelComplexity,self.detectionCon,self.trackinCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8,9,0, 12, 16, 20]
        self.lmList = []


    def findHands(self, img, draw = True):



        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img 
    
    

    def findPosition(self, img, HandNo = 0, draw = True):

        lmList = []
        if self.results.multi_hand_landmarks: 
            myHand = self.results.multi_hand_landmarks[HandNo]          
            for id, lm in enumerate(myHand.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx , cy = int(lm.x*w), int(lm.y*h)
                #print(id, cx, cy)
                lmList.append([id, cx, cy])

                """ if draw:
                    cv2.circle(img,(cx,cy),25,(0,0,0),cv2.FILLED) """

        return lmList
    
    def fingersUp(self,lmList):
        fingers = []
        #lmList = []
        # Thumb
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Fingers
        for id in range(1, 5):

            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # totalFingers = fingers.count(1)

        return fingers

    


def  main():
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])

        cv2.imshow("image", img)
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break




if __name__ == "__main__":
    main()
