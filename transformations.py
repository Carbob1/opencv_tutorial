import numpy as np
import cv2 as cv

img = cv.imread("Resources/Photos/park.jpg")

cv.imshow("Park", img)


# translation (shift image by value)
def translate(img, x, y):   # x, y ->  number of pixels on x, y
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimensions)

# -x -> left
# -y -> up
# x -> right
# y -> down


translated = translate(img, -100, 100)
cv.imshow("Translated", translated)


# Rotation
def rotate(img, angle, rot_point=None):
    (height, width) = img.shape[:2]  # first two values [y, x]

    if rot_point is None:
        rot_point = (width // 2, height // 2)

    rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rot_mat, dimensions)


rotated = rotate(img, 45)   # +45 -> counterclockwise, -45 -> clockwise
cv.imshow("Rotated", rotated)

rotated_rotated = rotate(rotated, 45)
cv.imshow("Rotated v2", rotated_rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resized)

# Flipping
flip = cv.flip(img, -1)
# flipped code
# 0 -> vertically/over x axis
# 1 -> horizontally/over y axis
# -1 -> both

cv.imshow("Flipped", flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
