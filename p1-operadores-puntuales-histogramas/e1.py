import cv2
from VisionImage import VisionImage

img = VisionImage(cv2.imread('../imagenes/messi.jpg', 0))
img2 = VisionImage(cv2.imread('../imagenes/china.jpg', 0))
img3 = VisionImage(cv2.imread('../imagenes/histograma/Fig10.jpg', 0))
res = img.add(img)
res.save('result.jpg')
# res = img.substract(img2)
# res.save('result2.jpg')
# res = img.multiply(img)
# res.save('result3.jpg')

#res = img.scalar(0.3)
#res.save('res.jpg')
#res2 = img.negative().threshold(170)
#res2 = img3.contrast(110, 1.5)
res2 = img3.ecualize()
res2.save('res.jpg')
res3 = img3.ecualize().ecualize()
res3.save('res2.jpg')
