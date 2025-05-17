from PIL import Image
import numpy as np

def grayscale(filename, resultAverFilename):
    with Image.open(filename) as img:
        width, height = img.size
        greyAverImg = Image.new('L', (width, height))
        pix = img.load()
        greyAverPix = greyAverImg.load()

        for x in range(width):
            for y in range(height):
                R, G, B = pix[x, y]
                greyAverPix[x, y] = int((R + G + B) / 3)

        greyAverImg.save(resultAverFilename)
        print(f"The image {filename.split('/')[2]} is converted to grayscale...")


def singh(filename, resultFilename, k=0.1, R=128):
    with Image.open(filename) as img:
        windowSize = 3
        width, height = img.size
        pix = np.array(img)

        binaryPix = np.zeros((height, width), dtype=np.uint8)
        offset = windowSize // 2

        for x in range(offset, width - offset):
            for y in range(offset, height - offset):
                window = pix[y - offset:y + offset + 1, x - offset:x + offset + 1]

                # Вычисляем среднее и стандартное отклонение в окне
                mean = np.mean(window)
                std = np.std(window)

                threshold = mean * (1 + k * ((std / R) - 1))

                # Применяем пороговую обработку
                if pix[y, x] > threshold:
                    binaryPix[y, x] = 255  # Белый
                else:
                    binaryPix[y, x] = 0  # Черный

        binaryImg = Image.fromarray(binaryPix, mode='L')
        binaryImg.save(resultFilename)

        print(f"Adaptive binarization of Singh image {filename.split('/')[-1]} is completed...\n")