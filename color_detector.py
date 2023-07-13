import cv2 as cv
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

myColors= []


def findColor(img):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imgHSV, lower, upper)
    cv.imshow("img", mask)
    
    while True:
        success, img = cap.read()
        cv.imshow("Webcam", img)
        
        if cv.waitKey(0) and 0xff==ord("q"):
            break