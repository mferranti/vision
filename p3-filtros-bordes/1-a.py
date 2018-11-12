import cv2
import numpy as np
from matplotlib import pyplot as plt
from filters import apply_filter

#
# FALTA APLICAR PASABAJOS Y PASAALTOS. EL PUNTO 2 YA ESTA
#

def create_filter(rows, columns):
  return np.ones((rows, columns), np.float32)/(columns*rows)

image = cv2.cvtColor(cv2.imread('../imagenes/diegote.jpg'), cv2.COLOR_BGR2RGB)

filter = create_filter(5, 5)

new_image = apply_filter(image, filter)

cv_image = cv2.filter2D(image, -1, cv2.rotate(filter, cv2.ROTATE_90_CLOCKWISE))

plt.subplot(121),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
#plt.subplot(132),plt.imshow(cv_image),plt.title('OpenCV')
#plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(new_image),plt.title('Mi filtro')
plt.xticks([]), plt.yticks([])
plt.show()