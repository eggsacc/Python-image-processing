import numpy as np
import matplotlib.pylab as plt
import time

start = time.time()

# read image as array
img_arr = plt.imread('download.jpg')

# split rgb channels into 3 seperate arrays
img_r = img_arr[:, :, 0]
img_g = img_arr[:, :, 1]
img_b = img_arr[:, :, 2]

kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])

output_r = np.empty(0, dtype=int)
output_g = np.empty(0, dtype=int)
output_b = np.empty(0, dtype=int)

img_height = img_arr.shape[0]
img_width = img_arr.shape[1]
k_width = kernel.shape[0]
k_height = kernel.shape[1]

# iterating through all pixels
for row in range(img_height - k_height + 1):
    for clmn in range(img_width - k_width + 1):
        sum = 0
        for k_row in range(k_height):
            for k_clmn in range(k_width):
                multiple = img_r[row + k_row][clmn + k_clmn] * kernel[k_row][k_clmn]
                sum += int(multiple)
        output_r = np.append(output_r, sum)

for row in range(img_height - k_height + 1):
    for clmn in range(img_width - k_width + 1):
        sum = 0
        for k_row in range(k_height):
            for k_clmn in range(k_width):
                multiple = img_g[row + k_row][clmn + k_clmn] * kernel[k_row][k_clmn]
                sum += int(multiple)           
        output_g = np.append(output_g, sum)

for row in range(img_height - k_height + 1):
    for clmn in range(img_width - k_width + 1):
        sum = 0
        for k_row in range(k_height):
            for k_clmn in range(k_width):
                multiple = img_b[row + k_row][clmn + k_clmn] * kernel[k_row][k_clmn]
                sum += int(multiple)
        output_b = np.append(output_b, sum)

# reshape output to 2D, then stack along the 3rd dimension to reform 3D array
rgb_arr_3d = np.dstack((output_r.reshape(img_height - k_height + 1, img_width - k_width + 1),
                        output_g.reshape(img_height - k_height + 1, img_width - k_width + 1),
                        output_b.reshape(img_height - k_height + 1, img_width - k_width + 1)))

fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(rgb_arr_3d)
ax.axis('off')
ax.set_title('blurred')

plt.show()

end = time.time()

print(f"time taken: {end - start} seconds")
