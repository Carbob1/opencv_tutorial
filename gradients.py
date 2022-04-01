# https://www.techtarget.com/searchenterpriseai/definition/face-detection
# https://www.semanticscholar.org/paper/A-fully-annotated-thermal-face-database-and-its-for-Kopaczka-Kolk/fd809ee36fa6832dda57a0a2403b4b52c207549d
# https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8409768&tag=1
# https://www.researchgate.net/publication/3193340_Detecting_Faces_in_Images_A_Survey
# https://towardsdatascience.com/face-detection-for-beginners-e58e8f21aad9

import cv2 as cv

img = cv.imread("Resources/Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Laplacian
cv.waitKey(0)
