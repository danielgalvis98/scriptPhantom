import threading
import os
from PIL import Image
import numpy as np
import sys
import time

MU_X = 800
MU_Y = 450
SIGMA_X = 134.63975
SIGMA_Y = 61.00864
URL_IMAGES = './defaced/'
URL_REPRESENTATIVE = './representativeDefaced/'


def crop(image_path, coords, saved_location):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        print('Error: Format = scriptRepresentativeImage.py directorySourcePath directoryDestinationPath')
    else:
        source = args[1]
        destination = args[2]
        i = 0
        isFile = os.path.isfile(source + str(i) + '.png')
        while isFile:
            while threading.active_count() == 50:
                time.sleep(2)
            image = source + str(i) + '.png'
            center_x = -1
            while center_x < 80 or center_x > 1520:
                center_x = np.random.normal(MU_X, SIGMA_X, 1)

            center_y = -1
            while center_y < 80 or center_y > 820:
                center_y = np.random.normal(MU_Y, SIGMA_Y, 1)

            x1 = center_x[0] - 80
            x2 = center_x[0] + 80

            y1 = center_y[0] - 80
            y2 = center_y[0] + 80

            threading.Thread(target=crop, args=(image, (x1, y1, x2, y2), destination + str(i) + '.png',)).start()
            i += 1
            isFile = os.path.isfile(source + str(i) + '.png')
