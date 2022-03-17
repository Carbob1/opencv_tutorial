import cv2 as cv
import numpy as np
# turned off pixel is 0, turned on is 1

blank = np.zeros((400, 400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)  # color is white because its binary image
circle = cv.circle(blank.copy(), (200, 200), 200, (255, 255, 255), -1)  # copy so it won't affect original blank
# for example color white (255, 255, 255) can be written as 255

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# bitwise AND (intersection)
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("AND", bitwise_and)

# bitwise OR (sum of images -> intersection plus rest)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("OR", bitwise_or)

cv.waitKey(0)
