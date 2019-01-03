import cv2
import numpy as np

image = cv2.imread('chess.jpg')
blurred = cv2.pyrMeanShiftFiltering(image, 5, 5)


def filter_my_contours(image, contours):
	filtered_contours = []
	image_area = image.shape[0] * image.shape[1]
	for ii in contours:
		# criteria for filtering
		area = cv2.contourArea(ii)
		if area >= 0.1 * image_area and area <= 0.9 * image_area:
			filtered_contours.append(ii)

	return filtered_contours


gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('thres', threshold)
th, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

print(len(contours))

filtered_contours = filter_my_contours(threshold, contours)
print(len(filtered_contours))
print(filtered_contours[0].shape)

cv2.drawContours(blurred, filtered_contours, -1, (0, 0, 255), 3)

# bonding box
for each_contour in filtered_contours:
	top_left_x, top_left_y = min(each_contour[:, 0, 0]), min(each_contour[:, 0, 1])
	bottom_right_x, bottom_right_y = max(each_contour[:, 0, 0]), max(each_contour[:, 0, 1])
	cv2.rectangle(blurred, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255, 0, 0), 3)

cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
cv2.imshow('Display', blurred)
cv2.waitKey(0)