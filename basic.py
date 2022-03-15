import cv2 as cv

img = cv.imread("irface_sub001_seq02_frm00336.jpg_lfb.png")     # BGR image

# cv.imshow("Boston", img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# Blur (Kernel size must be odd)
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
# for example (15, 1) is like blur from motion
cv.imshow("Blur", blur)

# Edge Cascade
# how to reduce edges: pass in slightly blurred image
canny = cv.Canny(blur, 50, 70)
cv.imshow("Canny Edge", canny)

# Dilating image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("Dilated", dilated)

cv.waitKey(0)
