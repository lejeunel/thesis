import numpy as np
import scipy.misc as scm
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.axes_grid1 import make_axes_locatable


shape = [150, 200]
gazeGaussStd = 0.06 * shape[1]

def gaussian_2D(shape=(3,3), sigma=0.5):
    """
    2D gaussian mask - should give the same result as MATLAB's
    fspecial('gaussian',[shape],[sigma])
    """
    m, n = [(ss - 1.) / 2. for ss in shape]
    y, x = np.ogrid[-m:m + 1, -n:n + 1]
    h = np.exp(-(x * x + y * y) / (2. * sigma * sigma))
    h[h < np.finfo(h.dtype).eps * h.max()] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h


kernel_size = np.ceil(gazeGaussStd * 6) // 2 * 2 + 1
gauss_kernel = gaussian_2D((kernel_size, kernel_size), gazeGaussStd)

gauss_arr = np.zeros(shape)

c_x = round(0.6 * shape[1])
c_y = round(0.4 * shape[0])

edge_x = int(c_x - kernel_size // 2)
edge_y = int(c_y - kernel_size // 2)

v_range1 = slice(max(0, edge_y), max(min(edge_y + gauss_kernel.shape[0], gauss_arr.shape[0]), 0))
h_range1 = slice(max(0, edge_x), max(min(edge_x + gauss_kernel.shape[1], gauss_arr.shape[1]), 0))

v_range2 = slice(max(0, -edge_y), min(-edge_y + gauss_arr.shape[0], gauss_kernel.shape[0]))
h_range2 = slice(max(0, -edge_x), min(-edge_x + gauss_arr.shape[1], gauss_kernel.shape[1]))

gauss_arr[v_range1, h_range1] += gauss_kernel[v_range2, h_range2]

gauss_arr /= np.max(gauss_arr)

plt.figure(figsize=(4, 3))
ax = plt.gca()
im = ax.imshow(gauss_arr, cmap='plasma', vmin=0, vmax=1)

plt.axis('off')

# create an axes on the right side of ax. The width of cax will be 5%
# of ax and the padding between cax and ax will be fixed at 0.05 inch.
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)

plt.colorbar(im, cax=cax, ticks=[0, 0.5, 1])
plt.savefig('prob_map_06.pdf', bbox_inches="tight")
plt.show()

