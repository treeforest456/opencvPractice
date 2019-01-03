import cv2

capture = cv2.VideoCapture(0)

while True:
	ret, frame = capture.read()
	frame_blur = cv2.GaussianBlur(frame, (7, 7), 0)
	frame_blur_gray = cv2.cvtColor(frame_blur, cv2.COLOR_BGR2GRAY)
	frame_blur_gray_adap = cv2.adaptiveThreshold(frame_blur_gray,\
							255,\
							cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
							cv2.THRESH_BINARY,\
							3,\
							1)

	cv2.imshow('frame', frame_blur_gray_adap)

	keypress = cv2.waitKey(1)
	if keypress == ord('q'):
		break

capture.release()
cv2.detroyAllWindows()