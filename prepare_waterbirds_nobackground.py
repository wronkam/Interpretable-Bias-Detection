# prepare waterbirds dataset without background

import csv
import os
import numpy as np
from PIL import Image

# dataset directory
root_dir = os.path.join('.', 'data', 'waterbirds')
file_name = os.path.join(root_dir, 'metadata.csv')
split_dir = {0: 'train', 1: 'val', 2: 'test'}

# segmentation masks directory
segmentation_dir = os.path.join('.', 'data', 'segmentations')

# Read the CSV file with its header
with open(file_name, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Get the header row

    # Print the header
    print("Header:")
    print(", ".join(header))
    cls = {}
    splits = {}
    # Print the values
    print("Values:")
    i = 0
    for k,v in split_dir.items():
        os.makedirs(os.path.join(root_dir, v), exist_ok=True) # create test, train, val dir

    for row in csv_reader:
        # read row data
        id, file, y, split, place,place_f = row
        place_f = place_f.split('/')[1]
        classez = int(file[:3])
        dir, image = file.split('/')
        split = int(split)
        print(split_dir[split], split, file)

        # open src image
        img_data = Image.open(os.path.join(root_dir, file))
        img_data = np.asarray(img_data)

        # open segmentation mask
        print(file)
        seg_data = Image.open(os.path.join(segmentation_dir, file.replace('.jpg', '.png')))
        seg_data = np.asarray(seg_data)/255
        if len(seg_data.shape) > 2:
            seg_data = seg_data[:, :, 0]
            # some masks have many layers
        seg_data = np.reshape(seg_data, (seg_data.shape[0], seg_data.shape[1], 1))
        seg_data = np.repeat(seg_data, 3, axis=-1)

        # remove background
        if len(img_data.shape) == 2:  # grayscale
            img_data = np.reshape(img_data, (img_data.shape[0], img_data.shape[1], 1))
            img_data = np.repeat(img_data, 3, axis=-1)
        img_data = img_data * seg_data
        img_data = np.uint8(img_data)
        im = Image.fromarray(img_data)

        dest = os.path.join(root_dir, split_dir[split], dir)
        os.makedirs(dest, exist_ok=True)
        # save image
        im.save(os.path.join(dest, image))
