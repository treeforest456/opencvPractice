import cv2
import numpy as np

canvas = np.ones([500, 500, 3], 'uint8') * 255
start = None
moving = None
end = None
pressed_flag = False

def click (event, x, y, flags, param):
	global canvas, pressed_flag, start, moving, end
	if event == cv2.EVENT_LBUTTONDOWN:
		print('pressed')
		start = (x, y)
		print(start)
		pressed_flag = True
	elif event == cv2.EVENT_MOUSEMOVE and pressed_flag == True:
		moving = (x, y)
		cv2.rectangle(canvas, start, moving, (0, 0, 255), 3)
	elif event == cv2.EVENT_LBUTTONUP:
		print('up')
		end = (x, y)
		pressed_flag = False
		canvas = np.ones([500, 500, 3]) * 255
		cv2.rectangle(canvas, start, end, (0,0,255), 3)

cv2.namedWindow('canvas')
cv2.setMouseCallback('canvas', click)

while True:
	cv2.imshow('canvas', canvas)
	key_press = cv2.waitKey(1)
	if key_press & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
