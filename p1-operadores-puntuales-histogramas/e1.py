import cv2
from VisionImage import VisionImage

img = VisionImage(cv2.imread('../imagenes/messi.jpg', 0))
img2 = VisionImage(cv2.imread('../imagenes/china.jpg', 0))
img3 = VisionImage(cv2.imread('../imagenes/histograma/Fig10.jpg', 0))
img4 = VisionImage(cv2.imread('../imagenes/histograma/Fig15.jpg', 0))

res = img.add(img)
res.save('1-a-suma.jpg')

res = img.substract(img2)
res.save('1-a-resta.jpg')

res = img.multiply(img)
res.save('1-a-prod.jpg')

res = img.scalar(0.3)
res.save('1-b-escalar.jpg')

res = img4.compress()
res.save('1-c-compresion.jpg')

res = img.negative();
res.save('2-negativo.jpg')

res = img.negative().threshold(170)
res.save('3-umbral.jpg')

for i in range(0, 7):
  res = img3.bitPlane(i)
  res.save('4-bitplane-' + str(i) + '.jpg')

res = img3.contrast(110, 1.5)
res.save('4-contraste.jpg')

res = img3.ecualize()
res.save('7-ecualizacion.jpg')

res = img3.ecualize().ecualize()
res.save('8-ecualizacion-x2.jpg')
