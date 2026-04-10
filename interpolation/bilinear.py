# for a 2d matrix image
import cv2
import numpy as np

image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

scale = 2
width = image.shape[1]
height = image.shape[0]

new_height = int(height * scale)
new_width = int(width * scale)
output_image = np.zeros((new_height, new_width))

# for each i we look at the j's
# for each y we look at the x's
# for each row we look at the cols
for i in range(new_height):
    for j in range(new_width):

        # scale down on vertical and horizontal axis
        old_y = i / scale
        old_x = j / scale

        # Vertical neighbours (rows)
        top = int(np.floor(old_y))
        bottom = min(height - 1, top + 1)

        # Horizontal neighbours (columns)
        left = int(np.floor(old_x))
        right = min(width - 1, left + 1)

        ty = old_y - top
        tx = old_x - left

        # 4 surrounding pixels
        top_left     = image[top, left]
        top_right    = image[top, right]
        bottom_left  = image[bottom, left]
        bottom_right = image[bottom, right]

        # Interpolate horizontally
        top_interp    = (1 - tx) * top_left + tx * top_right
        bottom_interp = (1 - tx) * bottom_left + tx * bottom_right

        # Interpolate vertically
        output_image[i, j] = (1 - ty) * top_interp + ty * bottom_interp


print("output_image =", output_image)
