import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/cats 2.jpg")
cv.imshow("Cats", img)

# dimensions of mask must be equal to size of an image
blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank", blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2 + 45), 100, 255, -1)
mask = cv.rectangle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), (img.shape[1] - 10, img.shape[0] - 10), 255, -1)
cv.imshow("Mask", mask)

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)  # color is white because its binary image
cv.imshow("Rectangle", rectangle)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("Weird shape", weird_shape)

masked_image = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow("Masked image", masked_image)

cv.waitKey(0)
