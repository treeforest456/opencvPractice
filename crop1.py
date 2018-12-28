import cv2

coorinates = []
status = False

def lets_crop(event, x, y, flags, params):
	global coordinates, status
	if event == cv2.EVENT_LBUTTONDOWN:
		status = True
		coordinates = [(x, y)]
	if event == cv2.EVENT_LBUTTONUP:
		status = False
		coordinates.append((x, y))

		cv2.rectangle(image, coordinates[0], coordinates[1], (255, 0, 0), 3)
		# cv2.imshow("Crop", image)


image = cv2.imread('2km2km.png')
copied_image = image.copy()

cv2.namedWindow('CROP', cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('CROP', lets_crop)

while True:
	cv2.imshow('CROP', image)
	keypress = cv2.waitKey(1)
	if keypress == ord('r'):
		image = copied_image.copy()
	if keypress == ord('c'):
		break

if len(coordinates) == 2:
	x_start = coordinates[0][1]
	x_end = coordinates[1][1]
	y_start = coordinates[0][0]
	y_end = coordinates[1][0]
	roi = copied_image[x_start:x_end, y_start:y_end]
	height, width = roi.shape[:2]
	cv2.namedWindow('ROI', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('ROI', width, height)
	cv2.imshow("ROI", roi)
	cv2.waitKey(0)

cv2.destroyAllWindows()
