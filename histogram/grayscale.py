import cv2

img = cv2.imread("dim.jpeg")  # or path to bright.jpg, dim.jpeg, etc.
if img is None:
    raise FileNotFoundError("Image not found")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("grayscale.png", gray)