import cv2
import numpy as np
image = cv2.imread('2km2km.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
row, col = np.shape(gray)
threshold = 122

for ii in range(row):
	for jj in range(col):
		if gray[ii][jj] >= threshold:
			gray[ii][jj] = 255
		else:
			gray[ii][jj] = 0

cv2.imshow('Threshold', gray)
cv2.waitKey(0)