# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:18:52 2020

@author: miquel.sarrias.ext
"""

import xarray
import numpy as np
import cv2
import matplotlib.pyplot as plt


dsx = xarray.open_dataset(r'd:/Users/miquel.sarrias.ext/Desktop/GoSafe/datasets/pertipus/merged.nc')
np_arr = np.array(dsx['Band1'])

for i in range(np_arr.shape[0]-1):
    for j in range(np_arr.shape[1]-1):
        if np.isnan(np_arr[i][j]):
            np_arr[i][j] = max([np_arr[i][j+1],np_arr[i+1][j+1],np_arr[i+1][j],np_arr[i][j]])

maxval = 0
minval = 100
for i in range(np_arr.shape[0]-1):
    for j in range(np_arr.shape[1]-1):
        if np_arr[i][j] > maxval:
            maxval = np_arr[i][j]
        if np_arr[i][j] < minval:
            minval = np_arr[i][j]

np_arr = np_arr / (maxval+0.001) * 254
np_arr = np_arr.astype(np.uint8)

for i in range(np_arr.shape[0]-1):
    for j in range(np_arr.shape[1]-1):
        if np_arr[i][j] < 1:
            np_arr[i][j] = max([np_arr[i][j+1],np_arr[i+1][j+1],np_arr[i+1][j],np_arr[i][j]])

b = np.zeros([np_arr.shape[0],np_arr.shape[1],3])
b[:,:,0] = np_arr
b[:,:,1] = np_arr
b[:,:,2] = np_arr
cv2.imwrite('color_img.png', b)

img = cv2.imread('color_img.png')
img = cv2.flip(img, 0)

## LOAD AND APPLY COLOR RAMP
lut = cv2.imread('colormap.png',cv2.IMREAD_COLOR)
#im_color = cv2.LUT(img, lut)
im_color = cv2.LUT(img, lut)
cv2.imwrite('color_img.png', im_color)


## MASK IMAGE (JUST BARCELONA AREA)
b = np.zeros([np_arr.shape[0],np_arr.shape[1],3])
b[:,:,0] = np.zeros([np_arr.shape[0],np_arr.shape[1]])
b[:,:,1] = np.ones([np_arr.shape[0],np_arr.shape[1]])*100
b[:,:,2] = np.zeros([np_arr.shape[0],np_arr.shape[1]])
cv2.imwrite('mask_fullalpha.png', b)
alpha = cv2.imread('mask_fullalpha.png')

dsx = xarray.open_dataset(r'd:/Users/miquel.sarrias.ext/Desktop/GoSafe/datasets/pertipus/side_mask.nc')
mask = np.array(dsx['Band1'])
mask = mask.astype(np.uint8)
mask = cv2.flip(mask, 0)

res = cv2.bitwise_and(im_color,im_color,mask = mask)


## TRANSPARENT BACKGROUND
tmp = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
_,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
b, g, r = cv2.split(res)
rgba = [b,g,r, alpha]
dst = cv2.merge(rgba,4)


## SAVE IMAGE
cv2.imwrite('out.png',dst)

#pix = img2.flatten()
#plt.hist(pix, bins=10)
