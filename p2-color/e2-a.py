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

hue_small_c = img_hsv.copy()
hue_big_c = img_hsv.copy()

small_c = 10
big_c = 80

for i in range(0, rows):
  for j in range(0, cols):
    cv2.add(img_hsv[i][j], np.array([small_c, 0, 0], dtype='uint8'), hue_small_c[i][j])
    cv2.add(img_hsv[i][j], np.array([big_c, 0, 0], dtype='uint8'), hue_big_c[i][j])

hue_small_c = cv2.cvtColor(hue_small_c, cv2.COLOR_HSV2RGB)
hue_big_c = cv2.cvtColor(hue_big_c, cv2.COLOR_HSV2RGB)

plt.subplot(131),plt.imshow(hue_small_c),plt.title('C chico = ' + str(small_c))
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(hue_big_c),plt.title('C grande = ' + str(big_c))
plt.xticks([]), plt.yticks([])
plt.show()
