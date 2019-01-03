import cv2

coorinates = []
# dont know why he used the status here
# since after this 
# status donesn't change anything
status = False

def lets_crop(event, x, y, flags, params):
	global coordinates, status
	if event == cv2.EVENT_LBUTTONDOWN:
		# status = True
		coordinates = [(x, y)]
	if event == cv2.EVENT_LBUTTONUP:
		# status = False
		coordinates.append((x, y))

		cv2.rectangle(image, coordinates[0], coordinates[1], (255, 0, 0), 3)
		print(coordinates[0])
		print(coordinates[1])
		# cv2.imshow("Crop", image)


image = cv2.imread('2km2km.png')
# create a back up incase we want to redo the process
original_image = image.copy()

cv2.namedWindow('CROP', cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('CROP', lets_crop)

while True:
	cv2.imshow('CROP', image)
	keypress = cv2.waitKey(1)
	if keypress == ord('r'):
		# refresh the image instance from the original image 
		# to redo the crop action
		image = original_image.copy()
	if keypress == ord('y'):
		break

if len(coordinates) == 2:
	# if this way
	# we have to crop starting top-left corner to bottom-right corner
	# cannot do this the other way
	# for example, i fail to crop starting from the top-right corner
	# to bottom-left corner
	# since the x_start and x_end cannot be assigned that way
	# but this is an easy fix, it's okay
	x_start = coordinates[0][1]
	x_end = coordinates[1][1]
	y_start = coordinates[0][0]
	y_end = coordinates[1][0]
	# roi = original_image[x_start:x_end, y_start:y_end]

	roi = image[x_start:x_end, y_start:y_end]
	print(image)
	print(roi)
	height, width = roi.shape[:2]
	cv2.namedWindow('ROI', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('ROI', width, height)
	
	cv2.imshow("ROI", roi)
	cv2.waitKey(0)

cv2.destroyAllWindows()
