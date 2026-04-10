import numpy as np
import matplotlib.pyplot as plt
import cv2

f = cv2.imread('dim.png')  # or 'dim.jpeg' or 'images/peppers.png'
if f is None:
    raise FileNotFoundError("Image not found")
gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)

plt.figure(1)
plt.imshow(f)

hist, bin_edges = np.histogram(gray.ravel(), bins=256, range=(0, 256))
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

plt.figure(2)
plt.bar(bin_centers, hist, width=1.0, color='gray', edgecolor='none')
plt.xlabel('Pixel intensity')
plt.ylabel('Count')
plt.title('Grayscale histogram')

plt.show()