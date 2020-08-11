import scipy.misc as scm
import skimage.segmentation as sks
import skimage.morphology as skm
import numpy as np

img_file = 'ds13_img.png'
gt_file = 'ds13_gt.png'
out_file = 'ds13_boundary.png'

dilation_size = 3

img = scm.imread(img_file, mode='RGB')
gt = scm.imread(gt_file, mode='L') > 0
gt = skm.opening(gt, skm.square(5)).astype(np.uint8)

zero_array = np.zeros(img.shape, dtype='uint8')[...,0]

mask = sks.mark_boundaries(zero_array, gt > 0, color=(1,0,0), mode='inner')[...,0]

out = skm.dilation(mask, skm.square(dilation_size))

out_green = np.concatenate((zero_array[..., np.newaxis], out[..., np.newaxis], zero_array[..., np.newaxis]), axis=-1).astype('uint8') * 255

clear_mask = np.repeat(out[..., np.newaxis], 3, axis=-1)

print(img.shape, clear_mask.shape)

img[clear_mask > 0] = 0

img = img.astype('uint8')

img += out_green

# scm.imshow(img)

print(img.shape, type(img))

scm.imsave(out_file, img)


