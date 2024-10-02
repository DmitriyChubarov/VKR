from PIL import Image
from urllib.request import urlopen
import matplotlib.pyplot as plt
import numpy as np

img = Image.open(urlopen('https://i.ibb.co/9G57VHk/image.jpg'))
img = img.convert('L')
img_new = img.crop((200, 100, 400, 300))

np_new = np.asarray(img_new, dtype=int)

size = 3 #поменять размер зума

def bi_inter(np_new, size):
  height, width = np_new.shape
  new_height, new_width = height * size, width * size

  np_new_inter = np.zeros((new_height, new_width))

  for i in range(new_height):
    for j in range(new_width):
      x, y = i / size, j / size

      x0, y0 = int(np.floor(x)), int(np.floor(y))
      x1, y1 = min(x0 + 1, height - 1), min(y0 - 1, width - 1)

      dx, dy = (x - x0), (y - y0)

      I0 = np_new[x0, y0] * (1 - dx) + np_new[x1, y0] * dx
      I1 = np_new[x0, y1] * (1 - dx) + np_new[x1, y1] * dx
      I = I0 * (1 - dy) + I1 * dy

      np_new_inter[i, j] = I

  return np_new_inter.astype(np.uint8)

img_new_inter = Image.fromarray(bi_inter(np_new, size))

plt.imshow(img, cmap='gray')
plt.show()

plt.imshow(img_new, cmap='gray')
plt.show()

plt.imshow(img_new_inter, cmap='gray')
plt.show()
