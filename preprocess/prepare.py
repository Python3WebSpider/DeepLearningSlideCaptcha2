import glob
from sklearn.model_selection import train_test_split

file_paths = glob.glob('captcha/images/*.png')
print('file_paths', file_paths)

train, valid = train_test_split(file_paths, test_size=0.2)

with open('train.txt', 'w', encoding='utf-8') as f:
    for item in train:
        f.write(f'data/{item}\n')

with open('valid.txt', 'w', encoding='utf-8') as f:
    for item in valid:
        f.write(f'data/{item}\n')
