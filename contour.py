import cv2
import numpy as np

image = cv2.imread('pedes.jpg')
blurred = cv2.pyrMeanShiftFiltering(image, 101, 201)
cv2.imshow('blurred', blurred)

gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
th, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(len(contours))

cv2.drawContours(image, contours, -1, (0, 0, 255), 3)

cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
cv2.imshow('Display', image)
cv2.waitKey(0)