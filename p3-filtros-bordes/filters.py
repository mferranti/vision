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

def apply_filter_one_channel(image, filter):
  new_image = apply_filter_to_channel(image, filter)

  return new_image

def apply_filter(image, filter):
  new_image = image.copy()
  if (len(new_image.shape) == 3):
    new_image[:, :, 0] = apply_filter_to_channel(image[:, :, 0], filter)
    new_image[:, :, 1] = apply_filter_to_channel(image[:, :, 1], filter)
    new_image[:, :, 2] = apply_filter_to_channel(image[:, :, 2], filter)
  else:
    new_image = apply_filter_to_channel(image, filter)

  return new_image

def smooth_filter(image):
  smooth_image = np.matrix('1 2 1; 2 4 2; 1 2 1', dtype=np.float32)/16
  return apply_filter(image, smooth_image)

def sharpen_filter(image):
  laplacian_filter = np.matrix('1 1 1; 1 -8 1; 1 1 1', dtype=np.float32)
  sharpen_image = apply_filter(smooth_filter(image), laplacian_filter)
  return cv2.subtract(image, sharpen_image)

def median_filter(img, size):
  # res = img.copy()
  res = np.zeros(img.shape)
  rows = img.shape[0]
  cols = img.shape[1]
  border_size = math.floor(size / 2)

  print(border_size)
  for i in range(border_size, rows - border_size):
    for j in range(border_size, cols - border_size):
      submatrix = img[
        border_size - i : border_size + i,
        border_size - j : border_size + j
      ]
      value = np.median(submatrix)
      res[i][j] = value
  return np.uint8(res)

