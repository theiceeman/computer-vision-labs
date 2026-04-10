# for a 1d image
import cv2
import numpy as np

image = np.array([1, 2, 3, 4, 5, 6])

scale = 2
width = image.shape[0]

# new_height = int(height * scale)
new_width = int(width * scale)
output_image = np.zeros(new_width)

for i in range(new_width):
    input_pixel_position = i / scale

    left_neighbour = int(np.floor(input_pixel_position))
    right_neighbour = min(width - 1, left_neighbour + 1)

    left_neighbour_value = image[left_neighbour]
    right_neighbour_value = image[right_neighbour]

    left_neighbour_to_mapped_point = input_pixel_position - left_neighbour

    # A + (old_pos - left_index) * (B - A)
    # (1 - t) * A + (t * B)
    output_image[i] = left_neighbour_value + left_neighbour_to_mapped_point * (
        right_neighbour_value - left_neighbour_value
    )


print("output_image =", output_image)