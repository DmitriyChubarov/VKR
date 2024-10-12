from PIL import Image
from urllib.request import urlopen
import numpy as np

img_1 = Image.open(urlopen('https://i.ibb.co/6ZK2BZj/pc-1.jpg'))
img_1 = img_1.convert('L')
img_2 = Image.open(urlopen('https://i.ibb.co/WyWPPNt/pc-2.jpg'))
img_2 = img_2.convert('L')
img_3 = Image.open(urlopen('https://i.ibb.co/8dp99kR/200-200-1.jpg'))
img_3 = img_3.convert('L')

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
def cor(x, y):

    ux = np.mean(x)
    uy = np.mean(y)

    numerator = np.sum((x - ux) * (y - uy))
    denominator = np.sqrt(np.sum((x - ux) ** 2)) * np.sqrt(np.sum((y - uy) ** 2))

    return ((numerator / denominator) + 1) / 2

img_1_new, img_3_new = size(img_1, img_3)
print(cor(img_1_new, img_3_new))




