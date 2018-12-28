import cv2

km2km = cv2.imread('2km2km.png')
road = cv2.imread('road.jpg')
km2km_re = cv2.resize(km2km, (450, 650), interpolation=cv2.INTER_CUBIC)
road_re = cv2.resize(road, (450, 650), interpolation=cv2.INTER_CUBIC)

dst = cv2.addWeighted(km2km_re, 0.8, road_re, 0.8, 0)

resize = cv2.resize(dst, (450, 650), interpolation=cv2.INTER_CUBIC)

cv2.imshow('super impose', resize)

cv2.waitKey(0)