# detection - detects presence of a face
# recognition - whose face is this
# classifier - algorithm that decides whether a given image is positive or negative
# whether a face is present or not
# classifiers needs to be trained on thousands of images, OpenCV has a pretrained ones

import cv2 as cv

img = cv.imread("irface_sub016_seq02_frm00297.jpg_lfb.png")
cv.imshow("Person", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

haar_cascade = cv.CascadeClassifier("haar_eyes.xml")
# how to reduce sensitivity to noise -> change minNeighbours
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f"Number of faces found = {len(faces_rect)}")

for (x, y, w, h) in faces_rect[2::]:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

print(faces_rect[1])
cv.imshow("Detected faces", img)


# haar are popular and easy but not the most effective
# haar smile - detects eyes and nose (infrared)
# default face -> face
cv.waitKey(0)
