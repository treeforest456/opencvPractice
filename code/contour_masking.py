import cv2
import numpy as np


original_image = cv2.imread('chess.jpg')
gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

masked_image = cv2.bitwise_and(original_image, original_image, mask=threshold)


cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
cv2.imshow('Display', masked_image)
cv2.waitKey(0)