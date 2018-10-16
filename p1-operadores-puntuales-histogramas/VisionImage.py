import cv2
import numpy as np

class VisionImage:
  def __init__(self, img):
    self.img = np.uint8(img)

  def add(self, other): # without saturation
    return VisionImage(self.img + other.img)
  
  def substract(self, other):
    return VisionImage(self.img - other.img)

  def multiply(self, other):
    return VisionImage(np.multiply(self.img, other.img))

  def scalar(self, n):
    return VisionImage(self.img * n)

  def compress(self):
    r = np.max(self.img)
    c = 255 / np.log(r+1);
    compressed = c * np.log(self.img + 1)
    return VisionImage(compressed)

  def negative(self):
    white = VisionImage(np.full(self.img.shape, 255))
    return white.substract(self)

  def threshold(self, p):
    return VisionImage(np.where(self.img < p, 0, 255))

  def save(self, filename):
    cv2.imwrite(filename, self.img)

  def show(self):
    cv2.imshow('Image', self.img)
    cv2.waitKey(0)