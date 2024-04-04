import cv2
from cv2 import aruco
import numpy as np

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_250)
cap = cv2.VideoCapture(1)
param_markers = aruco.DetectorParameters()

cv2.namedWindow("main", cv2.WINDOW_NORMAL)
cv2.resizeWindow("main", 1100, 800)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detector = aruco.ArucoDetector(aruco_dict, param_markers)
    marker_corners, markerIds, rejected = detector.detectMarkers(gray_frame)

    newFrame = aruco.drawDetectedMarkers(frame, marker_corners, markerIds)

    
    cv2.imshow('main', newFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
         break


cap.release()
cv2.destroyAllWindows()