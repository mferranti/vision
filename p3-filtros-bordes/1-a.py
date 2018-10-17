import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.cvtColor(cv2.imread('../imagenes/test/boat.png'), cv2.COLOR_BGR2RGB)
#img = cv2.imread('../imagenes/messi.jpg')
#img = cv2.cvtColor(cv2.imread('../imagenes/diegote.jpg'), cv2.COLOR_BGR2RGB)
new_img = img.copy()

rows = img.shape[0]
cols = img.shape[1]
size = 3
kernel = np.ones((size, size), np.float32)/(size*size)

cv_image = cv2.filter2D(img,-1,kernel)
#dst = cv2.blur(img,(5,5))

print(img[99:102, 99:102])

for i in range(0, rows):
  for j in range(0, cols):
    accum = np.zeros(3, dtype=float)
    for k in range(0, size):
      for l in range(0, size):
        if i != 0 and j != 0 and i != rows - 1 and j != cols -1:
          res = img[i + (k - 1)][j + (l - 1)].astype(float) * kernel[k][l]
          accum = np.add(accum, res)
    new_img[i][j] = accum

print(img[150][150])

print(cv_image[150][150])
print(new_img[150][150])

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
#plt.subplot(121),plt.imshow(cv_image),plt.title('OpenCV')
#plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(new_img),plt.title('Mi filtro')
plt.xticks([]), plt.yticks([])
plt.show()
