import cv2
import numpy as np
import math
import random
from matplotlib import pyplot as plt
from filters import apply_filter

def apply_salt_and_pepper(img, p):
  new_image = img.copy()
  rows = img.shape[0]
  cols = img.shape[1]

  for i in range(0, rows):
    for j in range(0, cols):
      rand_value = random.random()

      if rand_value < p:
        new_value = 0
      elif rand_value > 1 - p:
        new_value = 255
      else:
        new_value = new_image[i][j]

      new_image[i][j] = new_value

  return new_image

img = cv2.imread('../imagenes/test/lena.png', 0)
#noise_image = apply_salt_and_pepper(img, 0.1)

def add_noise(image, sigma):
  # rayleighCDF = 1 - exp(-x.^2 / (2*sigma^2));
  rayleigh = np.random.rayleigh(sigma, image.shape)
  return np.uint8(np.multiply(image, rayleigh))

#noise_image = add_noise(img, 1)
noise_image = img

roberts = np.matrix('-1 0; 0 1', dtype=np.float32)
sobel = np.matrix('-1 -2 -1; 0 0 0; 1 2 1', dtype=np.float32)
prewitt = np.matrix('-1 -1 -1; 0 0 0; 1 1 1', dtype=np.float32)

plt.subplot(221),plt.imshow(noise_image, cmap='gray'),plt.title('Con ruido')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(apply_filter(noise_image, roberts), cmap='gray'),plt.title('Roberts')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(apply_filter(noise_image, sobel), cmap='gray'),plt.title('Sobel')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(apply_filter(noise_image, prewitt), cmap='gray'),plt.title('Prewitt')
plt.show()

