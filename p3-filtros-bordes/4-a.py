import cv2
import numpy as np
from matplotlib import pyplot as plt
from filters import sharpen_filter, smooth_filter


img = cv2.cvtColor(cv2.imread('../imagenes/test/lena.png'), cv2.COLOR_BGR2RGB).astype(np.float32)/255.0
#img = cv2.cvtColor(cv2.imread('../imagenes/diegote.jpg'), cv2.COLOR_BGR2RGB).astype(np.float32)/255.0

def add_noise(image, sigma):
  gauss = np.zeros(image.shape, dtype='float32')
  m = np.array([0, 0, 0])
  s = np.array([sigma, sigma, sigma])
  cv2.randn(gauss, m, s)
  return np.array(cv2.add(image, gauss) * 255.0, dtype='uint8')

noise_image = add_noise(img, 0.05)
noise_image_02 = add_noise(img, 0.2)

plt.subplot(231),plt.imshow(noise_image),plt.title('Con ruido σ=0.05')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(smooth_filter(noise_image)),plt.title('Suavizado')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(sharpen_filter(noise_image)),plt.title('Realce de bordes')
plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(noise_image_02),plt.title('Con ruido σ=0.2')
plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(smooth_filter(noise_image_02)),plt.title('Suavizado')
plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(sharpen_filter(noise_image_02)),plt.title('Realce de bordes')
plt.xticks([]), plt.yticks([])
plt.show()