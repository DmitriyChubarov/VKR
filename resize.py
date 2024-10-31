from PIL import Image
from urllib.request import urlopen
import numpy as np

# img_1 = Image.open(urlopen('https://i.ibb.co/xXT9zLT/1.png'))
# img_1 = img_1.convert('L')
# img_3 = Image.open(urlopen('https://i.ibb.co/Gkcp1T0/2.png'))
# img_3 = img_3.convert('L')

img_1 = Image.open('/Users/dmitrij/Desktop/image_1.jpg').convert('L')
img_2 = Image.open('/Users/dmitrij/Desktop/image_2_1.01.jpg').convert('L')

def size(x,y):
    w1, h1 = x.size
    w2, h2 = y.size

    if w1 * h1 == w2 * h2:
        return x, y
    elif w1 * h1 > w2 * h2:
        a, b = w1 - w2, h1 - h2
        if a % 2 != 0:
            c = a // 2 + 1
        else:
            c = a / 2
        if b % 2 != 0:
            d = b // 2 + 1
        else:
            d = b / 2

        y = y.crop((- (a // 2), - (b // 2), w2 + c, h2 + d))
    else:
        a, b = w2 - w1, h2 - h1
        if a % 2 != 0:
            c = a // 2 + 1
        else:
            c = a / 2

        if b % 2 != 0:
            d = b // 2 + 1
        else:
            d = b / 2

        x = x.crop((- (a // 2), - (b // 2), w1 + c, h1 + d))

    return x, y

img_1_new, img_2_new = (size(img_1, img_2))


img_2_new.save('/Users/dmitrij/Desktop/image_2_1.01_r.jpg')

# img_1_new.show()
# img_2_new.show()