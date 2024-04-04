import cv2
import numpy as np
from PIL import Image

# color to track: BGR colorspace
dark_red = [0, 255, 0]

def getLimits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_RGB2HSV)

    lower_limit = hsvC[0][0][0] - 10, 100, 100
    upper_limit = hsvC[0][0][0] + 10, 255, 255

    lower_limit = np.array(lower_limit, dtype=np.uint8)
    
    upper_limit = np.array(upper_limit, dtype=np.uint8)

    return lower_limit, upper_limit


cap = cv2.VideoCapture(0)
 
while True:
    ret, frame = cap.read()

    # convert the images to HSV colorspace such that a 'range' of colors could be defined.
    # convert frames to HSV format;
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = getLimits(dark_red)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)


    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
