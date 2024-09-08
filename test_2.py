from PIL import Image
import numpy as np
import os


def bilinear_interpolation_expand(image, new_width, new_height):
    old_width, old_height = image.size
    old_pixels = np.array(image)

    # Создаем пустое изображение с новым размером
    new_pixels = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Коэффициенты масштабирования
    x_ratio = old_width / new_width
    y_ratio = old_height / new_height

    for y in range(new_height):
        for x in range(new_width):
            # Определяем координаты в старом изображении
            old_x = x * x_ratio
            old_y = y * y_ratio

            # Индексы ближайших пикселей
            x1 = int(old_x)
            y1 = int(old_y)
            x2 = min(x1 + 1, old_width - 1)
            y2 = min(y1 + 1, old_height - 1)

            # Дробные части
            dx = old_x - x1
            dy = old_y - y1

            # Интерполяция
            pixel = (
                    (1 - dx) * (1 - dy) * old_pixels[y1, x1] +
                    dx * (1 - dy) * old_pixels[y1, x2] +
                    (1 - dx) * dy * old_pixels[y2, x1] +
                    dx * dy * old_pixels[y2, x2]
            )

            new_pixels[y, x] = pixel

    return Image.fromarray(new_pixels)


def expand_image(image_path, output_path, new_width, new_height):
    image = Image.open(image_path)
    new_image = bilinear_interpolation_expand(image, new_width, new_height)
    new_image.save(output_path)


# Путь к исходному изображению
source_image_path = '/Users/dmitrij/Desktop/2.jpg'
# Путь к новому изображению на рабочем столе
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "3.jpg")

# Новые размеры
new_width = 4000
new_height = 3000

expand_image(source_image_path, desktop_path, new_width, new_height)

print(f"Изображение сохранено на рабочий стол как 'expanded_image.jpg'")
