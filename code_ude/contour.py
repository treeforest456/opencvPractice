import cv2
import numpy as np

def filter_my_contours(image, contours):
	filtered_contours = []
	image_area = image.shape[0] * image.shape[1]
	for ii in contours:
		# criteria for filtering
		area = cv2.contourArea(ii)
		if area >= 0.1 * image_area and area <= 0.9 * image_area:
			filtered_contours.append(ii)

	return filtered_contours


image = cv2.imread('chess.jpg')
# how this function work
# need to understand
# try different values of the two numbers we can get different results
# play with it
blurred = cv2.pyrMeanShiftFiltering(image, 51, 51)
# cv2.imshow('blurred', blurred)

gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('thres', threshold)
th, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(len(contours))

filtered_contours = filter_my_contours(threshold, contours)
print(len(filtered_contours))

cv2.drawContours(blurred, filtered_contours, -1, (0, 0, 255), 3)

cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
cv2.imshow('Display', blurred)
cv2.waitKey(0)