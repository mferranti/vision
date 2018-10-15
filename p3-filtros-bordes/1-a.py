import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../imagenes/test/boat.png')
newImg = img.copy()

rows = img.shape[0]
cols = img.shape[1]
size = 3
kernel = np.ones((size, size), np.float32)/(size*size)
print(kernel)

cv_image = cv2.filter2D(img,-1,kernel)
#dst = cv2.blur(img,(5,5))

for i in range(0, rows):
  for j in range(0, cols):
    accum = np.zeros(3, dtype=int)
    for k in range(0, size):
      for l in range(0, size):
        if i != 0 and j != 0 and i != rows - 1 and j != cols -1:
          res = np.array([])
          print(img[i][j].dtype)
          print(kernel[k][l].dtype)
          cv2.multiply(img[i][j], kernel[k][l], res)
          accum = cv2.add(accum, res)
    newImg[i][j] = accum

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(cv_image),plt.title('OpenCV')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(cv_image),plt.title('Mi filtro')
plt.xticks([]), plt.yticks([])
plt.show()
