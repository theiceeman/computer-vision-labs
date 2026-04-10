import numpy as np
import matplotlib.pyplot as plt
from itertools import product


def geometric_backward_transform(f, invphi):
    # generate blank output image canvas with same shape as input image
    g = np.zeros_like(f)

    # get its shape(width & height) or possible domain
    gdomain = g.shape[:2]

    # loop through all pixel positions in the output image - for each y(col) in x(row)
    for y, x in product(range(gdomain[0]), range(gdomain[1])):

        # matrix multiplication to get the new rotated pixel co-ordinates, requires a vector,
        # so we rep. each pixel co-ord as a vector
        q = np.array([y, x])

        # this our transformation function that does the inverse of the forward transform.
        p = invphi(q)
        # we clamp the rotated co-ords possibly decimals to integers
        p = np.rint(p).astype(int)
        # replacement for p.isin(gdomain)
        if 0 <= p[0] < gdomain[0] and 0 <= p[1] < gdomain[1]:
            g[y, x] = f[p[0], p[1]]
    return g


"""our transformation function that rotates a pixel by a given angle."""
def rotator(angle):
    ca = np.cos(angle)
    sa = np.sin(angle)

    #  2D rotation matrix - this matrix multiplied by the vector rep of the pixel co-ords
    # gives you the new co-ordinates of the pixel after rotation.
    R = np.array([[ca, -sa], [sa, ca]])

    # define and return the function that rotates a pixel
    def rotate(t):
        # the matrix multiplication that produces the rotated pixel co-ordinates
        # [cosθ sinθ, −sinθ cosθ] * [y, x] = [cosθ*y - sinθ*x, sinθ*y + cosθ*x]
        return R @ t

    return rotate

a = plt.imread("bright.png")

plt.subplot(131)
plt.imshow(a)

# -π/6 means -30 degrees undos the rotation of the image by 30 degrees
b = geometric_backward_transform(a, rotator(-np.pi / 6))

plt.subplot(132)
plt.imshow(b)
plt.subplot(133)
plt.imshow(b[:64, :64])
plt.show()
