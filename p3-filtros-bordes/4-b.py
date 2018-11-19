import cv2
import numpy as np
from matplotlib import pyplot as plt
from filters import sharpen_filter, smooth_filter


img = cv2.cvtColor(cv2.imread('../imagenes/test/lena.png'), cv2.COLOR_BGR2RGB).astype(np.float32)/255.0
#img = cv2.cvtColor(cv2.imread('../imagenes/diegote.jpg'), cv2.COLOR_BGR2RGB).astype(np.float32)/255.0

def add_noise(image):
  rayleigh = np.random.rayleigh(0.000001, image.shape)
  rayleigh = cv2.normalize(rayleigh,  rayleigh, 0, 1, cv2.NORM_MINMAX)
  image = cv2.normalize(image,  image, 0, 1, cv2.NORM_MINMAX)
  noisy = cv2.multiply(image, rayleigh.astype(np.float32))
  #print(noisy)
  return np.array(noisy * 255.0, dtype='uint8')

noise_image = add_noise(img)
#noise_image_2 = add_noise(img)

rayleigh = np.random.rayleigh(1, img.shape[0])
rayleigh = cv2.normalize(rayleigh,  rayleigh, 0, 1, cv2.NORM_MINMAX)
print(rayleigh.mean())
print(np.median(rayleigh))

plt.subplot(231),plt.imshow(noise_image),plt.title('Con ruido')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(smooth_filter(noise_image)),plt.title('Suavizado')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(sharpen_filter(noise_image)),plt.title('Realce de bordes')
plt.xticks([]), plt.yticks([])
"""
plt.subplot(234),plt.imshow(noise_image_02),plt.title('Con ruido σ=0.2')
plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(smooth_filter(noise_image_02)),plt.title('Suavizado')
plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(sharpen_filter(noise_image_02)),plt.title('Realce de bordes')
plt.xticks([]), plt.yticks([])
"""
plt.show()
