import h5py
import scipy.misc as scm
import numpy as np
import random

ds = '09'
post = '_gaze_rec_sympadded'
imNbr = 97

featFile = './feat_ds' + ds + post + '.h5'

# initialize hdf5 files
print('read files...')
hdInFile = h5py.File(featFile, 'r')
imFeat = hdInFile['raw_feat'][...]
hdInFile.close()

#imNbr = random.randint(0, imFeat.shape[0] - 1)
outFile = 'activations_ds' + ds + ('_%04i' % imNbr) + post + '.png'
print('image number: %i' % imNbr)

img_shape = [imFeat.shape[1] * 4, imFeat.shape[2] * 4]

nbr_colums = 3
im_array = list()
border_size = img_shape[1] // 15
green_border_size = img_shape[1] // 60
for i, featIdx in enumerate(random.sample(range(imFeat.shape[3]), 12)):
    if i == 0:
        img_norm = scm.imread('ds%s_%04d.png' % (ds, imNbr), mode='RGB')
        img_norm = img_norm.astype('float') / 255
        img_norm = scm.imresize(img_norm, (img_shape[0], img_shape[1]))
        img_norm[...,:green_border_size,1] = 255
        img_norm[...,-green_border_size:,1] = 255
        img_norm[:green_border_size,...,1] = 255
        img_norm[-green_border_size:,...,1] = 255
    else:
        img_norm = np.repeat(imFeat[imNbr,...,featIdx,np.newaxis], 3, axis=-1)
        img_norm = (img_norm - np.min(img_norm)) / (np.max(img_norm) - np.min(img_norm))
        img_norm = scm.imresize(img_norm, (img_shape[0], img_shape[1]))

    print('feat_idx: %i' % featIdx)

    if (i % nbr_colums) == 0:
        im_array.append(img_norm)
    else:
        im_array[i // nbr_colums] = np.concatenate([im_array[i // nbr_colums], np.ones([img_norm.shape[0], border_size, 3]) * 255], axis=1)
        im_array[i // nbr_colums] = np.concatenate([im_array[i // nbr_colums], img_norm], axis=1)

out = im_array[0]
for i in range(1,len(im_array)):
    out = np.concatenate([out, np.ones([border_size, out.shape[1], 3]) * 255], axis=0)
    out = np.concatenate([out, im_array[i]], axis=0)

scm.imsave(outFile, out)

