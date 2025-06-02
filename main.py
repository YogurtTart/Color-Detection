import cv2 as cv
from PIL import Image
from util import get_limits


orange = [255, 165, 0]
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImg = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lowerlimit, upperLimit = get_limits(color=orange)

    mask = cv.inRange(hsvImg, lowerlimit, upperLimit)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv.rectangle(frame, (x1, y1), (x2,y2), (0, 255, 0), 5)


    print(bbox)

    cv.imshow('Frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    
cap.release()

cv.destroyAllWindows()