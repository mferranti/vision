import numpy as np
import cv2
from matplotlib import pyplot as plt

#img = cv2.cvtColor(cv2.imread('../imagenes/test/boat.png'), cv2.COLOR_BGR2RGB)
#img = cv2.cvtColor(cv2.imread('../imagenes/color/1906ax.png'), cv2.COLOR_BGR2RGB)
#img = cv2.cvtColor(cv2.imread('../imagenes/color/1901xx.png'), cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(cv2.imread('../imagenes/messi.jpg'), cv2.COLOR_BGR2RGB)

img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

hue = img_hsv[..., 0]
saturation = img_hsv[..., 1]
lightness = img_hsv[..., 2]

plt.subplot(131),plt.imshow(hue, cmap='gray'),plt.title('Tono (H)')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(saturation, cmap='gray'),plt.title('Saturacion (S)')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(lightness, cmap='gray'),plt.title('Brillo (L)')
plt.xticks([]), plt.yticks([])
plt.show()

# en el canal de saturacion es mas distinguible el granulado
# en el canal de tono son mas distinguibles los bordes
# en el canal de saturacion afectan mas los bordes difuminados
