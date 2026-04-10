import numpy as np
import matplotlib.pyplot as plt
from itertools import product  # to replace domainIterator

def geometric_forward_transform(f, phi):
    #  get image size
    fdomain = f.shape[:2]  # (height, width)

    #  creates a copy of our original image with same shape.
    g = np.zeros_like(f)

    # domainIterator - iterates through all pixel positions in the image
    # so, for each pixel position in original image
    for y, x in product(range(fdomain[0]), range(fdomain[1])):
        p = np.array([y, x])

        #  clamps the rotated co-ords to integers
        q = phi(p)
        q = np.rint(q).astype(int)

        # if transformed pixel position is between 0 and width, height of image, we fill position, else skip.
        if 0 <= q[0] < fdomain[0] and 0 <= q[1] < fdomain[1]:
            g[q[0], q[1]] = f[y, x]
    return g


def rotator(angle):
    ca = np.cos(angle)
    sa = np.sin(angle)

    #  2D rotation matrix - this matrix multiplied by the vector rep of the pixel co-ords
    # gives you the new co-ordinates of the pixel after rotation.
    R = np.array([[ca, -sa],
                  [sa, ca]])

    # define and return the function that rotates a pixel
    def rotate(t):
        # the matrix multiplication that produces the rotated pixel co-ordinates
        # [cosθ sinθ, −sinθ cosθ] * [y, x] = [cosθ*y - sinθ*x, sinθ*y + cosθ*x]
        return R @ t

    return rotate


a = plt.imread("bright.png")
plt.subplot(131)
plt.imshow(a)

#  np.pi/6) means π/6 radians, rotate the image by 30 degrees
b = geometric_forward_transform(a, rotator(np.pi / 6))
plt.subplot(132)
plt.imshow(b)
plt.subplot(133)
plt.imshow(b[:64, :64])
plt.show()