"""
Script to generate train and test text files for yolo
Copied from:
https://medium.com/geekculture/train-a-custom-yolov4-object-detector-on-linux-49b9114b9dc8
with link to git: https://github.com/techzizou/yolov4-custom-training_LOCAL/blob/main/yolov4/process.py
"""

import glob, os
import random

# Current directory
current_dir = 'data/obj/'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('data/train.txt', 'w')
file_test = open('data/test.txt', 'w')

# Populate train.txt and test.txt
image_list = glob.glob(os.path.join(current_dir, "*.JPG"))

# shuffle image list
random.seed(42)
random.shuffle(image_list)

index_test = round(len(image_list)*(100-percentage_test)/100)
print(index_test)

for i, image in enumerate(image_list):
    if i < index_test:
        file_train.write(image + "\n")
    else:
        file_test.write(image + "\n")

file_train.close()
file_test.close()