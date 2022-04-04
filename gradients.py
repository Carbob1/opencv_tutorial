# https://www.techtarget.com/searchenterpriseai/definition/face-detection
# https://www.semanticscholar.org/paper/A-fully-annotated-thermal-face-database-and-its-for-Kopaczka-Kolk/fd809ee36fa6832dda57a0a2403b4b52c207549d
# https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8409768&tag=1
# https://www.researchgate.net/publication/3193340_Detecting_Faces_in_Images_A_Survey
# https://towardsdatascience.com/face-detection-for-beginners-e58e8f21aad9

import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/park.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

# Sobel
# x = 1, y = 0
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobel_x, sobel_y)
# chaos
# sobel_try = cv.Sobel(gray, cv.CV_64F, 1, 1)

cv.imshow("Combined sobel", combined_sobel)
cv.imshow("Sobel x", sobel_x)
cv.imshow("Sobel y", sobel_y)
# cv.imshow("Sobel try", sobel_try)

# canny uses sobel,
# sobel is used in more advanced problems
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)

cv.waitKey(0)
