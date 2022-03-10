import cv2 as cv

img = cv.imread("Resources/Photos/cat.jpg")

cv.imshow('Car', img)

cv.waitKey(0) # wait infinite amount of time for click (0)
