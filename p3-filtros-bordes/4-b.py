import cv2
import numpy as np
from filters import sharpen_filter, smooth_filter

img = cv2.imread('../imagenes/test/lena.png', 0)

def add_noise_rayleigh(image, sigma):
  # rayleighCDF = 1 - exp(-x.^2 / (2*sigma^2));
  rayleigh = np.random.rayleigh(sigma, image.shape)
  return np.uint8(np.multiply(image, rayleigh))
 
noise_image_1 = add_noise_rayleigh(img, 1)
noise_image_05 = add_noise_rayleigh(img, 0.5)
noise_image_5 = add_noise_rayleigh(img, 5)

cv2.imwrite('ruido-rayleigh-1.jpg', noise_image_1)
cv2.imwrite('ruido-rayleigh-1-suavizado.jpg', smooth_filter(noise_image_1))
cv2.imwrite('ruido-rayleigh-1-realce.jpg', sharpen_filter(noise_image_1))

cv2.imwrite('ruido-rayleigh-05.jpg', noise_image_05)
cv2.imwrite('ruido-rayleigh-05-suavizado.jpg', smooth_filter(noise_image_05))
cv2.imwrite('ruido-rayleigh-05-realce.jpg', sharpen_filter(noise_image_05))

cv2.imwrite('ruido-rayleigh-5.jpg', noise_image_5)
cv2.imwrite('ruido-rayleigh-5-suavizado.jpg', smooth_filter(noise_image_5))
cv2.imwrite('ruido-rayleigh-5-realce.jpg', sharpen_filter(noise_image_5))

