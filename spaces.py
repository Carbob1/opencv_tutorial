import cv2 as cv
import matplotlib.pyplot as plt

# in opencv we have BGR, normally we use RGB
img = cv.imread("Resources/Photos/park.jpg")
cv.imshow('Park', img)

# matplotlib displays it as RGB, even if its BGR picture, so it looks odd
# plt.imshow(img)
# plt.show()  # code stops until you close this window

# color space - RGB, grayscale, HSV etc.

# BGR to Grayscale (pixel intensity)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# BGR to HSV (how humans sees color)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# BGR to LAB -> L * a * b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

# you can't converse Grayscale to HSV directly
# you need to converse GRAY2BGR and then BGR2HSV

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV --> BGR", hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("LAB --> BGR", lab_bgr)


plt.imshow(rgb)
plt.show()

cv.waitKey(0)
