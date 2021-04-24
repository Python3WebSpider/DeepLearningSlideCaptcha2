import os
from PIL import Image
import random
import glob
from loguru import logger

CAPTCHA_WIDTH = 520
CAPTCHA_HEIGHT = 320

image_source = Image.open('block_source.png')
image_target = Image.open('block_target.png')

label_offset_x_base = 260
label_offset_y_base = 120

count = 0
total = 1000
root_dir = 'output'
file_paths = glob.glob(f'{root_dir}/*.png')

while True:
    file_path = random.choice(file_paths)
    
    offset_y = random.randint(-100, 100)
    offset_x = random.randint(-100, 100)
    
    label_offset_x = label_offset_x_base + offset_x
    label_offset_y = label_offset_y_base + offset_y
    
    image_path = os.path.join(file_path)
    image = Image.open(image_path)
    image.paste(image_target, (offset_x, offset_y), image_target)
    image.paste(image_source, (0, offset_y), image_source)
    label = f'0 {label_offset_x / CAPTCHA_WIDTH} {label_offset_y / CAPTCHA_HEIGHT} 0.16596774 0.24170968'
    image.save(f'captcha/images/captcha_{count}.png')
    logger.debug(f'generated captcha file captcha_{count}.png')
    with open(f'captcha/labels/captcha_{count}.txt', 'w') as f:
        f.write(label)
    logger.debug(f'generated label file captcha_{count}.txt')
    count += 1
    if count > total:
        logger.debug('finished')
        break
