from PIL import Image
import numpy as np

img = Image.open('/Users/dmitrij/Desktop/image_2.jpg').convert('L')
size = 1.01 #поменять размер зума
def bi_inter(image, size):
  image = image.convert('L')
  height, width = image.size
  img_new = image.crop((height / 3, width / 3, 2 / 3 * height, 2 / 3 * width))
  img_new = image
  np_new = np.asarray(img_new, dtype=int)

  height, width = np_new.shape
  new_height, new_width = int(height * size), int(width * size)

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

img_new_inter = Image.fromarray(bi_inter(img, size))
img_new_inter.save('/Users/dmitrij/Desktop/image_2_1.01.jpg')

