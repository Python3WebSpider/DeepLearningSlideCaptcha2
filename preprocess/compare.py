import cv2
import numpy as np

image1 = cv2.imread('image1.png')
image2 = cv2.imread('image2.png')
sub = image1 - image2
affine_arr = np.float32([[1, 0, 0], [0, 1, 0]])
res = cv2.warpAffine(image2, affine_arr, (image2.shape[1], image2.shape[0]))
cv2.imwrite('sub.png', sub)
