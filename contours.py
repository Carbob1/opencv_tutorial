import numpy as np
import cv2 as cv

img = cv.imread("Resources/Photos/cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# blur = cv2.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)
#
# canny = cv.Canny(blur, 124, 175)
# cv.imshow("Canny", canny)

# other method for finding contours
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)
# pixel < 125 -> 0/black and pixel > 125 -> 255/white
# BINARY -> making image binary

# we need edges
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)  # -1 -> all contours
cv.imshow("Contours", blank)

# mods
# RETR_TREE -> all hierarchical contours,
# RETR_EXTERNAL -> external,
# RETR_LIST -> all contours

# approximation method
# NONE -> does nothing, gives all the points
# SIMPLE -> compresses all points of line to 2 endpoints

print(f"Numbers of found contours: {len(contours)}")
# 2700 contours is huge number, by blurring we can get 380
# image with colors gives more contours

# first edge cascades with canny and then findContours

cv.waitKey(0)
