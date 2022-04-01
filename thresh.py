import cv2 as cv

img = cv.imread("Resources/Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Simple Thresholding
# threshold is thresh value, thresh is image, set pixels above thresh to 255, rest to 0
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Thresh", thresh)

# Inverse Thresholding
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresh Inverse", thresh_inv)

# Adaptive Thresholding
# block size is like kernel
# method for finding thresh -> mean or gaussian
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 13, 9)
cv.imshow("Adaptive Thresholding", adaptive_thresh)

cv.waitKey(0)