import numpy as np
import cv2

img = cv2.imread('players.jpg', 1)

# scale
img_half = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img_stretch = cv2.resize(img, (600, 600))
img_stretch_near = cv2.resize(img, (600, 600), interpolation=cv2.INTER_NEAREST)

cv2.imshow('half', img_half)
cv2.imshow('stretch', img_stretch)
cv2.imshow('strech_near', img_stretch_near)


# rotation
M = cv2.getRotationMatrix2D((img.shape[0]/2, img.shape[1]/2), -45, 1)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow('rotated', rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
