import cv2
image = cv2.imread('2km2km.png')
# image = cv2.imread('road.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray_image', gray)

gray = cv2.GaussianBlur(gray, (31, 31), 0)

cv2.imshow('gray_image_blurred', gray)

ret, th1 = cv2.threshold(gray, 122, 255, cv2.THRESH_BINARY_INV)

th2 = cv2.adaptiveThreshold(gray,\
							255,\
							cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
							cv2.THRESH_BINARY,\
							41,\
							1)

cv2.imshow('Original', image)
cv2.imshow('thresholded_manual', th1)
cv2.imshow('thresholded_adaptive', th2)

cv2.waitKey(0)