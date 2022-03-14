import cv2 as cv
from resize import rescale_frame

# reading images
# img = cv.imread("Resources/Photos/cat_large.jpg")
#
# cv.imshow('Cat', img)
# cv.waitKey(0)  # wait infinite amount of time for click (0)

# reading videos
capture = cv.VideoCapture("Resources/Videos/dog.mp4")  # argument = 0/1/2/3 (for computer camera or path
# we display videos frame by frame
while True:
    isTrue, frame = capture.read()  # we get boolean saying if frame was successfully read and individual frame

    # rescale
    frame_resized = rescale_frame(frame, .1)    # .3 == 0.3

    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)

    # if cv.waitKey(20) & 0xFF == ord('d'):   # waitKey - jak długo pokazuje się jedna klatka.
    # waitKey zwraca wartość wciśniętego przycisku w bitach, stąd 0xFF i & (przeprowadza operacje and na bitach)
    if cv.waitKey(20) == ord('q'):  # łatwiej napisane a działa tak samo
        # ord zwraca wartość ASCII znaku
        # 0xFF -> ostatnie 8 bitów
        break   # zabezpieczenie przed nieskończoną pętlą

# capture.release() # zwalnia wybrane urządzenie
# cv.destroyAllWindows()    # zamknij okna, bo po co

# -215 Assertion failed -> prawdopodobnie zła ścieżka do pliku/skończyły się klatki
