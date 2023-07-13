import cv2 as cv

cap = cv.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 640)
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv.imshow("Webcam", img)
    
    if cv.waitKey(1) & 0xff == ord('q'):
        break