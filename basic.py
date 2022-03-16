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

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=3)
cv.imshow("Eroded", eroded)

# Resize    (ignores aspect ratio - for ex 16:9 (width to height))
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)  # INTER_AREA (or default) useful for shrinking
# INTER_LINEAR or INTER_CUBIC for enlarging images, CUBIC is the slower but gives better quality
cv.imshow("Resized", resize)

# Cropping (images are arrays, so we can crop them like arrays)
cropped = img[200:300, 300:500]
cv.imshow("Cropped", cropped)

cv.waitKey(0)

