import numpy as np
import cv2
from matplotlib import pyplot as plt

# np.set_printoptions(threshold=np.nan)

# img = cv2.cvtColor(cv2.imread('../imagenes/test/boat.png'), cv2.COLOR_BGR2RGB)
#img = cv2.cvtColor(cv2.imread('../imagenes/color/1906ax.png'), cv2.COLOR_BGR2RGB)
#img = cv2.cvtColor(cv2.imread('../imagenes/color/1901xx.png'), cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(cv2.imread('../imagenes/messi.jpg'), cv2.COLOR_BGR2RGB)

img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

rows = img_hsv.shape[0]
cols = img_hsv.shape[1]

moved = img_hsv.copy()

for i in range(0, rows):
  for j in range(0, cols):
    saturation = 0 if (i <= 50 or j <= 50) else img_hsv[i-50][j-50][1]
    moved[i][j] = np.array([img_hsv[i][j][0], saturation, img_hsv[i][j][2]])

saturation_layer = moved[..., 1]

moved = cv2.cvtColor(moved, cv2.COLOR_HSV2RGB)

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(moved),plt. title('Trasladada')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(saturation_layer, cmap='gray'),plt.title('Capa de saturacion')
plt.xticks([]), plt.yticks([])
plt.show()
