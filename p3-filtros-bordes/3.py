import cv2
import numpy as np
from matplotlib import pyplot as plt
from filters import smooth_filter, sharpen_filter

img = cv2.cvtColor(cv2.imread('../imagenes/test/lena.png'), cv2.COLOR_BGR2RGB)
#image = cv2.cvtColor(cv2.imread('../imagenes/diegote.jpg'), cv2.COLOR_BGR2RGB)

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(smooth_filter(img)),plt.title('Suavizado')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(sharpen_filter(img)),plt.title('Realce de bordes')
plt.xticks([]), plt.yticks([])
plt.show()