import cv2



def filter_my_contours(image, contours):
	filtered_contours = []
	image_area = image.shape[0] * image.shape[1]
	for ii in contours:
		# criteria for filtering
		area = cv2.contourArea(ii)
		if area >= 0.1 * image_area and area <= 0.9 * image_area:
			filtered_contours.append(ii)

	return filtered_contours



capture = cv2.VideoCapture(0)
cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
while True:
	ret, frame = capture.read()
	blurred = cv2.pyrMeanShiftFiltering(frame, 31, 31)
	# frame_blur = cv2.GaussianBlur(frame, (7, 7), 0)
	gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
	ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	th, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
	filtered_contours = filter_my_contours(threshold, contours)
	cv2.drawContours(gray, filtered_contours, -1, (0, 0, 255), 3)
	for each_contour in filtered_contours:
		top_left_x, top_left_y = min(each_contour[:, 0, 0]), min(each_contour[:, 0, 1])
		bottom_right_x, bottom_right_y = max(each_contour[:, 0, 0]), max(each_contour[:, 0, 1])
		cv2.rectangle(blurred, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255, 0, 0), 3)

	cv2.imshow('Display', gray)
	keypress = cv2.waitKey(1)
	if keypress == ord('q'):
		break


# cv2.imshow('blurred', blurred)
capture.release()
cv2.detroyAllWindows()
