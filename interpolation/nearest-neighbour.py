
import cv2
import numpy as np

image = cv2.imread("mandy-moore.jpg")  # BGR image
if image is None:
    raise RuntimeError("Could not load image")

height, width, channels = image.shape
print("input H,W =", height, width)

# args
scale = 2.0
new_height = int(height * scale)
new_width = int(width * scale)

print("new_height, new_width =", new_height, new_width)

sy = height / new_height
sx = width / new_width

print("sy, sx =", sy, sx)

# this checks the number of dimensions in the image
# color returns 3 (height, width, channel)
# grayscale returns 2 (height, width)
# we use it to know if its a grayscale or color image
if image.ndim == 3:
    out = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)
else:
    out = np.zeros((new_height, new_width), dtype=image.dtype)

for v in range(new_height):
    for u in range(new_width):
        # map output (u, v) back to input coordinates
        y = (v ) * sy 
        x = (u ) * sx 

        iy = int(round(y))
        ix = int(round(x))

        # ensure we get min position for values that exceed the image boundaries
        iy = min(height - 1, iy)
        ix = min(width - 1, ix)

        # get value at position in input image
        out[v, u] = image[iy, ix]


# print("output H,W =", resized.shape[:2])

cv2.imwrite("nearest-neighbour.png", out)