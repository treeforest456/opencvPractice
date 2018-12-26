import cv2

coorinates = []
status = False

def lets_crop(event, x, y, flags, params):
	global coordinates, status
	if event == cv2.EVENT_LBUTTONDOWN:
		status = True


image = cv2.imread('')
copied_image = image.copy()

cv2.nameWindow('CROP')
cv2.setMouseCallback('CROP', lets_crop)
