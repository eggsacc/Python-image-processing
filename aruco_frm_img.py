import cv2
from cv2 import aruco
import numpy as np

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_250)
param_markers = aruco.DetectorParameters()

image = cv2.imread("133415_result_rotated_005.png")
detector = aruco.ArucoDetector(aruco_dict, param_markers)
marker_corners, markerIds, rejected = detector.detectMarkers(image)

if len(marker_corners) > 0:
    m1_coords, m2_coords, m3_coords, m4_coords = marker_corners[0], marker_corners[1], marker_corners[2], marker_corners[3]
    


print(f"marker corners: {m1_coords}, {m2_coords}")
print(f"marker id: {markerIds}")

newImage = aruco.drawDetectedMarkers(image, marker_corners, markerIds)
    
cv2.imshow('frame', newImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
