import numpy as np
import cv2

messi = cv2.imread('../imagenes/messi.jpg', -1)

china = cv2.imread('../imagenes/china.jpg', -1)

#print(china.shape)
wb = np.array([[
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
],
[
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
],
[
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
	[255,255,255,255,255,255],
]])
print(messi.shape, china.shape)
sum = cv2.add(messi, china)
subtract = cv2.subtract(messi, china)
mult = cv2.multiply(messi, china)
escalar = messi * 2 % 255
escalar2 = messi * 10 % 255
escalar3 = messi * 3 % 255
b, g, r = cv2.split(messi)

#zeros = np.zeros((2348, 3570), np.int8)
#multnp = [np.matmul(messi[0], china[0]), np.matmul(messi[:, :, 1], china[1]), np.matmul(messi[2], china[2])]
#for img in [sum, subtract, mult, escalar]:
for img in [messi, sum, subtract, mult, b, g, r]:
	cv2.imshow('Image', img)
	cv2.waitKey(0)
# cv2.imshow('Subtract', subtract)
# cv2.destroyAllWindows()
