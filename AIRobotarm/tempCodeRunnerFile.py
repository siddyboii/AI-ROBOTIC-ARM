lmList = detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUp()
        print(fingers)