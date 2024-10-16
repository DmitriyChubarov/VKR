from PIL import Image
from urllib.request import urlopen
import numpy as np

img_1 = Image.open(urlopen('https://i.ibb.co/xXT9zLT/1.png'))
img_1 = img_1.convert('L')
img_2 = Image.open(urlopen('https://i.ibb.co/WyWPPNt/pc-2.jpg'))
img_2 = img_2.convert('L')
img_3 = Image.open(urlopen('https://i.ibb.co/Gkcp1T0/2.png'))
img_3 = img_3.convert('L')

def cor(x, y):

    ux = np.mean(x)
    uy = np.mean(y)

    numerator = np.sum((x - ux) * (y - uy))
    denominator = np.sqrt(np.sum((x - ux) ** 2)) * np.sqrt(np.sum((y - uy) ** 2))

    return ((numerator / denominator) + 1) / 2

print(cor(img_1, img_1))






