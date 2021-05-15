import cv2
import os
import numpy as np
from loguru import logger

CAPTCHA_WIDTH = 520
CAPTCHA_HEIGHT = 320

for root, dirs, files in os.walk('input'):
    for file in files:
        image_path = os.path.join(root, file)
        logger.debug(f'image path {image_path}')
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        image_height, image_width, image_dim = image.shape
        
        if image_dim == 3:
            b_channel, g_channel, r_channel = cv2.split(image)
            alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255
            image = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
        
        if image_width / image_height > CAPTCHA_WIDTH / CAPTCHA_HEIGHT:
            image = cv2.resize(image, (int(CAPTCHA_HEIGHT * image_width / image_height), CAPTCHA_HEIGHT))
            image_height, image_width, _ = image.shape
            image = image[:, int(image_width / 2 - CAPTCHA_WIDTH / 2): int(image_width / 2 + CAPTCHA_WIDTH / 2)]
        else:
            image = cv2.resize(image, (CAPTCHA_WIDTH, int(CAPTCHA_WIDTH * image_height / image_width)))
            image_height, image_width, _ = image.shape
            image = image[int(image_height / 2 - CAPTCHA_HEIGHT / 2): int(image_height / 2 + CAPTCHA_HEIGHT / 2), :]
            
        cv2.imwrite(f'output/{file}', image)
        logger.debug(f'finish output/{file}')
