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
      x = min(round(i / size), height - 1)
      y = min(round(j / size), width - 1)
      np_new_inter[i, j] = np_new[x,y]

  return np_new_inter.astype(np.uint8)


img_new_inter = Image.fromarray(bi_inter(np_new, size))

plt.imshow(img, cmap='gray')
plt.show()

plt.imshow(img_new, cmap='gray')
plt.show()

plt.imshow(img_new_inter, cmap='gray')
plt.show()