import cv2 as cv

img = cv.imread("Resources/Photos/cats.jpg")
cv.imshow("Cats", img)

# we blur images when there are noise (problem with lightning etc.)
# kernel is matrix on part of image, blur is applied on middle pixel (so kernel must be odd)
# blur is result of surrounding pixel
# kernel moves from left to right, then floor down, and again left to right (must go through all the pixels)

# Averaging (average of surrounding pixels' intensities)
average = cv.blur(img, (3, 3))
cv.imshow("Average", average)

# Gaussian Blur(like averaging but each of pixels has its weight, less blur but more natural)
gauss = cv.GaussianBlur(img, (3, 3), 0)  # 3rd parameter -> sigma x -> standard deviation in the x direction
cv.imshow("Gaussian", gauss)

# Median Blur (finds medium of surrounding pixels, more effecting in reducing noise than both methods above)
# Good for salt and pepper noise, pretty popular method even in advanced projects
median = cv.medianBlur(img, 3)  # here kernel must be given as 7, but it's still (7, 7)
cv.imshow("Median", median)
# more effective for smaller kernel, for reducing some noise - part of it (like 3 by 3)

# Bilateral (most effective, in a lot of advanced projects)
# blur image but retains/keeps edges
bilateral = cv.bilateralFilter(img, 10, 35, 25)
# space sigma -> how far can be pixels influencing the center pixel
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)
