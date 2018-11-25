import cv2
import median
import random
from filters import median_filter

random.seed(42)

img = cv2.imread('../imagenes/test/flinstones.png', 0)

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


noised_image = apply_salt_and_pepper(img, 0.3)
denoised_image = median_filter(noised_image, 5)

cv2.imshow('image',noised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('median', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


