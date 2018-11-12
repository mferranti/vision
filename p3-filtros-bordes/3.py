import cv2
import numpy as np
from matplotlib import pyplot as plt
from filters import apply_filter

#
# FALTA APLICAR PASABAJOS Y PASAALTOS. EL PUNTO 2 YA ESTA
#

smooth_filter = np.matrix('1 2 1; 2 4 2; 1 2 1', dtype=np.float32)/16
sharp_filter = np.matrix('1 1 1; 1 -8 1; 1 1 1', dtype=np.float32)

image = cv2.cvtColor(cv2.imread('../imagenes/test/lena.png'), cv2.COLOR_BGR2RGB)
#image = cv2.cvtColor(cv2.imread('../imagenes/diegote.jpg'), cv2.COLOR_BGR2RGB)

new_image = apply_filter(image, smooth_filter)
sharpen_image = apply_filter(image, sharp_filter)

#cv_image = cv2.filter2D(image, -1, cv2.rotate(filter, cv2.ROTATE_90_CLOCKWISE))

plt.subplot(131),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(new_image),plt.title('Suavizado')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(sharpen_image),plt.title('Realce de bordes')
plt.xticks([]), plt.yticks([])
plt.show()