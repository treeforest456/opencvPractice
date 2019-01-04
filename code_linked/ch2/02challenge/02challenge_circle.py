import cv2
import numpy as np

canvas = np.ones([500, 500, 3], 'uint8') * 255
point = None
radius = 2
color = (0, 0, 255)
pressed_flag = False

def click (event, x, y, flags, param):
	global canvas, pressed_flag, point, radius, color
	if event == cv2.EVENT_LBUTTONDOWN:
		print('pressed')
		point = (x, y)
		print(point)
		pressed_flag = True
		cv2.circle(canvas, point, radius, color, 2)
	elif event == cv2.EVENT_MOUSEMOVE and pressed_flag == True:
		point = (x, y)
		cv2.circle(canvas, point, radius, color, 2)
	elif event == cv2.EVENT_LBUTTONUP:
		print('up')
		point = (x, y)
		pressed_flag = False

cv2.namedWindow('canvas')
cv2.setMouseCallback('canvas', click)

while True:
	cv2.imshow('canvas', canvas)
	key_press = cv2.waitKey(1)
	if key_press & 0xFf == ord('r'):
		color = (0, 0, 255)
	if key_press & 0xFF == ord('q'):
		break
	if key_press & 0xFF == ord('c'):
		canvas = np.ones([500, 500, 3]) * 255
	if key_press & 0xFF == ord('b'):
		color = (255, 0, 0)

cv2.destroyAllWindows()
