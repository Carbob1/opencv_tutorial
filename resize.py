import cv2 as cv


# rescale -> do zmniejszyć ilość informacji itd.
# nie ma takiej funkcji, trzeba samemu napisać


def rescale_frame(frame, scale=0.75):  # for old files
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_res(capture, width, height):  # for live images, videos
    capture.set(3, width)  # 3 is property id of width
    capture.set(4, height)


image = cv.imread("Resources/Photos/cat.jpg")
image_resized = rescale_frame(image)

cv.imshow("cat", image)
cv.imshow("cat resized", image_resized)

cv.waitKey(0)
