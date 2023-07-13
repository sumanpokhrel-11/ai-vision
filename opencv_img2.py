import cv2 as cv

img = cv.imread("photos/1.jpg")


imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGrey,(7,7),0)
imgCanny = cv.Canny(img, 100, 100)


cv.imshow("Grey Image", imgGrey)
cv.imshow("Blur Image", imgBlur)
cv.imshow("Canny Image", imgCanny)

cv.waitKey(0)