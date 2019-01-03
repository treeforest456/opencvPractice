import cv2
import numpy as np
image_2km = cv2.imread('2km2km.png')


'''
# my way of doing the RGB thing
print(type(image_2km))
print(image_2km.shape)
test_r = cv2.imread('2km2km.png')
test_r[:, :, 0] = np.zeros((test_r.shape[0], test_r.shape[1]))
cv2.imshow('test_r', test_r)
cv2.waitKey(0)


test_g = cv2.imread('2km2km.png')
test_g[:, :, 1] = np.zeros((test_g.shape[0], test_g.shape[1]))
cv2.imshow('test_g', test_g)
cv2.waitKey(0)



test_b = cv2.imread('2km2km.png')
test_b[:, :, 2] = np.zeros((test_b.shape[0], test_b.shape[1]))
cv2.imshow('test_b', test_b)
cv2.waitKey(0)
'''

# split the image to 3 channels
# blue
(b, g, r) = cv2.split(image_2km)
cv2.imshow('b', b)
cv2.waitKey(0)

# green
cv2.imshow('g', g)
cv2.waitKey(0)

# red
cv2.imshow('r', r)
cv2.waitKey(0)

# merge them together to see they are really the 3 components
merged_image = cv2.merge((b,g,r))
cv2.imshow('merged image', merged_image)
cv2.waitKey(0)





cv2.imshow("2km2km", image_2km)
cv2.waitKey(0)

gray_2km = cv2.cvtColor(image_2km, cv2.COLOR_BGR2GRAY)
cv2.imshow("2km_gray", gray_2km)
cv2.waitKey(0)
cv2.imwrite('gray_2km.jpg', gray_2km)