import cv2
import numpy as np
from matplotlib import pyplot as plt
from filters import sharpen_filter, smooth_filter

img = cv2.imread('../imagenes/test/lena.png', 0)

def add_noise_rayleigh(image, sigma):
  # rayleighCDF = 1 - exp(-x.^2 / (2*sigma^2));
  rayleigh = np.random.rayleigh(sigma, image.shape)
  return np.uint8(np.multiply(image, rayleigh))
 
noise_image_1 = add_noise_rayleigh(img, 1)
noise_image_05 = add_noise_rayleigh(img, 0.5)
noise_image_5 = add_noise_rayleigh(img, 5)

"""
cv2.imwrite('ruido-rayleigh-1.jpg', noise_image_1)
cv2.imwrite('ruido-rayleigh-1-suavizado.jpg', smooth_filter(noise_image_1))
cv2.imwrite('ruido-rayleigh-1-realce.jpg', sharpen_filter(noise_image_1))

cv2.imwrite('ruido-rayleigh-05.jpg', noise_image_05)
cv2.imwrite('ruido-rayleigh-05-suavizado.jpg', smooth_filter(noise_image_05))
cv2.imwrite('ruido-rayleigh-05-realce.jpg', sharpen_filter(noise_image_05))

cv2.imwrite('ruido-rayleigh-5.jpg', noise_image_5)
cv2.imwrite('ruido-rayleigh-5-suavizado.jpg', smooth_filter(noise_image_5))
cv2.imwrite('ruido-rayleigh-5-realce.jpg', sharpen_filter(noise_image_5))
"""

plt.subplot(231),plt.imshow(noise_image_1),plt.title('Con ruido σ=1')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(smooth_filter(noise_image_1)),plt.title('Suavizado')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(sharpen_filter(noise_image_1)),plt.title('Realce de bordes')
plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(noise_image_05),plt.title('Con ruido σ=0.5')
plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(smooth_filter(noise_image_05)),plt.title('Suavizado')
plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(sharpen_filter(noise_image_05)),plt.title('Realce de bordes')
plt.xticks([]), plt.yticks([])
plt.show()