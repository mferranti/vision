import numpy as np
import cv2
from matplotlib import pyplot as plt

# np.set_printoptions(threshold=np.nan)

# img = cv2.cvtColor(cv2.imread('../imagenes/test/boat.png'), cv2.COLOR_BGR2RGB)
#img = cv2.cvtColor(cv2.imread('../imagenes/color/1906ax.png'), cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(cv2.imread('../imagenes/color/1901xx.png'), cv2.COLOR_BGR2RGB)
#img = cv2.cvtColor(cv2.imread('../imagenes/messi.jpg'), cv2.COLOR_BGR2RGB)

img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

rows = img_hsv.shape[0]
cols = img_hsv.shape[1]

img_less_saturated = img_hsv.copy()
img_more_saturated = img_hsv.copy()

for i in range(0, rows):
  for j in range(0, cols):
    img_less_saturated[i][j] = img_hsv[i][j] * np.array([1, 0.5, 1])

for i in range(0, rows):
  for j in range(0, cols):
    cv2.multiply(img_hsv[i][j], np.array([1, 2, 1], dtype='uint8'), img_more_saturated[i][j])

img_less_saturated = cv2.cvtColor(img_less_saturated, cv2.COLOR_HSV2RGB)
img_more_saturated = cv2.cvtColor(img_more_saturated, cv2.COLOR_HSV2RGB)

plt.subplot(131),plt.imshow(img_less_saturated),plt.title('Menos saturada')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_more_saturated),plt.title('Mas saturada')
plt.xticks([]), plt.yticks([])
plt.show()
