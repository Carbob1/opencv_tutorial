import cv2 as cv

img = cv.imread("Resources/Photos/cats.jpg")

cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

canny = cv.Canny(img, 124, 175)
cv.imshow("Canny", canny)

# we need edges
contours, hierarchies = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# mods
# RETR_TREE -> all hierarchical contours,
# RETR_EXTERNAL -> external,
# RETR_LIST -> all contours
cv.waitKey(0)