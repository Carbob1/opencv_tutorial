import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/park.jpg")
cv.imshow("Park", img)

# how to display blue as blue channel
blank = np.zeros(img.shape[:2], dtype="uint8")  # sometimes blank need shape with [:2] sometimes not
# whole shape is probably if we need blank with all its channels
# here we need blank as individual channel

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

# img1 = cv.merge([blue, green, red]) doesnt work -> too many color channels
# cv.imshow("Merged merged", img1)

cv.imshow("Blue merged", blue)
cv.imshow("Green merged", green)
cv.imshow("Red merged", red)

cv.imshow("Blue", b)    # represented in grayscale -> lighter -> more pixels of that color
cv.imshow("Green", r)
cv.imshow("Red", r)

print(img.shape)    # shape and dimension, shape of image is 3
print(b.shape)  # shape of b, g, r is 1, that's why it's in grayscale (grayscale shape is one)
print(g.shape)
print(r.shape)


merged = cv.merge([b, g, r])
cv.imshow("Merged", merged)

cv.waitKey(0)
