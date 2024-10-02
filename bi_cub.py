from PIL import Image
from urllib.request import urlopen
import matplotlib.pyplot as plt
import numpy as np

img = Image.open(urlopen('https://i.ibb.co/9G57VHk/image.jpg'))
img = img.convert('L')
img_new = img.crop((200, 100, 400, 300))

np_new = np.asarray(img_new, dtype=int)

size = 3 #поменять размер зума

def cub_inter_main(p0,p1,p2,p3,t):
  I = p1 + 0.5 * t * (p2 - p0 + t * (2 * p0 - 5 * p1 + 4 * p2 - p3 + t * (3 * (p1 - p2) + p3 - p0)))

  return I

def cub_inter(np_new, size):
  height, width = np_new.shape
  new_height, new_width = height * size, width * size

  np_new_inter = np.zeros((new_height, new_width))

  for i in range(new_height):
    for j in range(new_width):
      x, y  = i / size, j / size
      xi, yi = int(np.floor(x)), int(np.floor(y))
      dx, dy = x - xi, y - yi

      x0, x1, x2, x3 = max(0,xi - 1), xi, min(height - 1, xi + 1), min(height - 1, xi + 2)
      y0, y1, y2, y3 = max(0,yi - 1), yi, min(width - 1, yi + 1), min(width - 1, yi + 2)

      I1, I2 = cub_inter_main(np_new[x0,y0], np_new[x1,y0], np_new[x2,y0], np_new[x3,y0], dx), cub_inter_main(np_new[x0,y1], np_new[x1,y1], np_new[x2,y1], np_new[x3,y1], dx)
      I3, I4 = cub_inter_main(np_new[x0,y2], np_new[x1,y2], np_new[x2,y2], np_new[x3,y2], dx), cub_inter_main(np_new[x0,y3], np_new[x1,y3], np_new[x2,y3], np_new[x3,y3], dx)

      I5 = cub_inter_main(I1, I2, I3, I4, dy)

      np_new_inter[i, j] = I5

  return np_new_inter.astype(np.uint8)

img_new_inter = Image.fromarray(cub_inter(np_new, size))

plt.imshow(img, cmap='gray')
plt.show()

plt.imshow(img_new, cmap='gray')
plt.show()

plt.imshow(img_new_inter, cmap='gray')
plt.show()