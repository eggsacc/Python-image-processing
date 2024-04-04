import cv2
from cv2 import aruco

marker_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_250)

marker_size = 300

for id in range(4):
    marker_image = aruco.generateImageMarker(marker_dict, id, marker_size)
    cv2.imshow("img", marker_image)
    cv2.imwrite(f"markers/marker_{id}.png", marker_image)


