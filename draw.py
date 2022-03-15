import cv2 as cv
import numpy as np

# how to create blank/black image
blank = np.zeros((500, 500, 3), dtype='uint8')    # uint8 -> image datatype, 3 -> color channels
# cv.imshow("Blank", blank)
# img = cv.imread("Resources/Photos/cat.jpg")
# cv.imshow('Cat', img)

# 1. Paint the image certain colour
# blank[:] = 0, 255, 0  # [:] all pixels
# blank[:, 200:400] = 0, 0, 255
# # [y, x]
# cv.imshow("Colored blank", blank)

# 2. Draw rectangle (image to draw on, (x, y) left upper corner, right lower corner, colour, thickness, other)
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
# # alternatively
# cv.rectangle(blank, (200, 0), (250, 500), (0, 0, 255), thickness=-1)
# # draw 1/x of image (how to get middle of image)
# cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 0, 255), thickness=-1)
#
# cv.imshow("Rectangle", blank)

# 3. Draw circle
# cv.circle(blank, (250, 250), 40, (0, 255, 255), thickness=-1)
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 20, (0, 0, 255), thickness=2)
#
# cv.imshow("Circle", blank)

# 4. Draw a line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow("Line", blank)

# 5. Write text
cv.putText(blank, "Hello", (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow("Text", blank)

cv.waitKey(0)
