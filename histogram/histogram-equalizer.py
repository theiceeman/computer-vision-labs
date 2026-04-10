import cv2
import numpy as np


def histogramEqualization(f, bins=100):
    his, be = np.histogram(f.ravel(), bins=bins, range=(0, 256))
    his = his.astype(float) / his.sum()
    cdf_at_edges = np.hstack((np.zeros(1), np.cumsum(his)))
    out = np.interp(f.ravel(), be, cdf_at_edges)
    return out.reshape(f.shape)


img = cv2.imread("dim.png")
if img is None:
    raise FileNotFoundError("Image not found")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float64)  # or float32

# Equalize: input intensities -> equalized btw 0 & 1 [0, 1]
equalized_01 = histogramEqualization(gray, bins=256)

# Convert to 0-255 uint8 for display/save
equalized = (np.clip(equalized_01, 0, 1) * 255).round().astype(np.uint8)
cv2.imwrite("equalized.png", equalized) 

# Optional: show or save
cv2.imshow("Equalized", equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
