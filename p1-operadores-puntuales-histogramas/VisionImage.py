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

  def hist(self):
    h = np.zeros(256);
    n, m = self.img.shape;
    for i in range(0, n - 1):
      for j in range(0, m - 1):
        h[self.img[i,j]] += 1
    return h

  def contrast(self, p, e):
    return VisionImage(np.where(self.img > p, self.img * e, self.img / e))

  def ecualize(self):
    n, m = self.img.shape;
    res = np.zeros((n, m));
    probOrig = self.hist() / (m * n);
    acumOrig = np.cumsum(probOrig);
    acumEq = np.cumsum(np.full(256, 1)) / 256;
    transform = np.zeros(256);
    for k in range(0, 255):
      for i in range(0, 255):
        diff = acumEq[255 - i] - acumOrig[k]
        if (diff > 0):
          transform[k] = 255 - i;
    for i in range(0, m):
      for j in range(0, n):
        res[i, j] = transform[self.img[i, j]];

    return VisionImage(res);

  def bitPlane(self, p):
    n, m = self.img.shape;
    res = np.zeros((n, m));
    for i in range(0, m):
      for j in range(0, n):
        res[i, j] = np.uint8(np.binary_repr(self.img[i, j], 8)[p]);
    return VisionImage(res).threshold(1)

  def save(self, filename):
    cv2.imwrite(filename, self.img)

  def show(self):
    cv2.imshow('Image', self.img)
    cv2.waitKey(0)
