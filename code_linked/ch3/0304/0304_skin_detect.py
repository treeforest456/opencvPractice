import cv2
import numpy as np

img = cv2.imread('faces.jpeg', 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# hue values
h = hsv[:, :, 0]
# saturation values
s = hsv[:, :, 1]
# intensity values
v = hsv[:, :, 2]

hsv_split = np.concatenate((h, s, v), axis=1)
hsv_split = cv2.resize(hsv_split, (0, 0), fx=0.1, fy=0.1)

ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
min_sat = cv2.resize(min_sat, (0, 0), fx=0.1, fy=0.1)
cv2.imshow('sat filter', min_sat)

ret, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)
max_hue = cv2.resize(max_hue, (0, 0), fx=0.1, fy=0.1)
cv2.imshow('hue filter', max_hue)

final = cv2.bitwise_and(min_sat, max_hue)
# final = cv2.resize(final, (0, 0), fx=0.1, fy=0.1)
cv2.imshow('final', final)


# cv2.imshow('split hsv', hsv_split)

cv2.waitKey(0)
cv2.destroyAllWindows()