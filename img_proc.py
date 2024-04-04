import numpy as np
import matplotlib.pylab as plt
import cv2

# read image using matplotlib
image_mpl = plt.imread('car.jpg')

# creates a 3x3 array of 1s, then divide by 10, so array of 0.1s
blurring_kernel = np.ones((3, 3), np.float32) / 10

blurred = cv2.filter2D(image_mpl, -1, blurring_kernel)

fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(blurred)
ax.axis('off')
ax.set_title('blurred')

plt.show()
