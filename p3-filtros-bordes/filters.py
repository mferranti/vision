import cv2
import numpy as np
import math

#convolution
def apply_filter_to_channel(img, filter):
  kernel = cv2.rotate(cv2.rotate(filter, cv2.ROTATE_90_CLOCKWISE), cv2.ROTATE_90_CLOCKWISE)
  new_channel = img.copy()
  rows = img.shape[0]
  cols = img.shape[1]
  rows_border_size = math.floor(kernel.shape[0] / 2)
  cols_border_size = math.floor(kernel.shape[1] / 2)

  for i in range(rows_border_size, rows - rows_border_size):
    for j in range(cols_border_size, cols - cols_border_size):
      row_from = i - rows_border_size
      col_from = j - cols_border_size
      row_to = i + rows_border_size
      col_to = j + cols_border_size

      if (kernel.shape[0] % 2 != 0):
        row_to = row_to + 1
      if (kernel.shape[1] % 2 != 0):
        col_to = col_to + 1
      #print(cols)
      #print (col_to)
      #print(img[row_from : row_to, col_from : col_to])
      matrix_with_filter = cv2.multiply(np.array(img[row_from : row_to, col_from : col_to], dtype='float32'), kernel)
      new_value = cv2.sumElems(matrix_with_filter)[0]
      if (new_value < 0):
        new_value = 0

      new_channel[i][j] = new_value

  return np.array(new_channel, dtype='uint8')


def apply_filter(image, filter):
  new_image = image.copy()
  new_image[:, :, 0] = apply_filter_to_channel(image[:, :, 0], filter)
  new_image[:, :, 1] = apply_filter_to_channel(image[:, :, 1], filter)
  new_image[:, :, 2] = apply_filter_to_channel(image[:, :, 2], filter)

  return new_image