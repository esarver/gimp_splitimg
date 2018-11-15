#!/usr/bin/python3

import sys

from os import path
from PIL import Image

def process_background():
    raise NotImplementedError  # TODO - Write this

def crop(full_path, sub_image_width, sub_image_height, num_images = None, starting_x = 0, starting_y = 0):
    orig_image = Image.open(full_path)

    orig_width, orig_height = orig_image.size

    count = 0

    for curr_y in range(starting_y, orig_height, sub_image_height):
        for curr_x in range(starting_x, orig_width, sub_image_width):
            if num_images is not None and count > num_images:
                return
            if (curr_x + sub_image_width) > orig_width:
                break
            select_box = (curr_x, curr_y, curr_x + sub_image_width, curr_y + sub_image_height)
            selection = orig_image.crop(select_box)
            try:
                file_path, new_name = path.split(full_path)
                new_name, ext = path.splitext(new_name)
                new_name = f'{new_name}_{count:03}{ext}'
                selection.save(path.join(file_path, new_name))
            except:
                raise
            count += 1
        if (curr_y + sub_image_height) > orig_height:
            break

if __name__ == '__main__':
    if len(sys.argv) == 4:
        crop(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    elif len(sys.argv) == 5:
        crop(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif len(sys.argv) == 7:
        crop(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
    else:
        print(f'Usage: {sys.argv[0]} file sub-image-width sub-image-height [number-sub-images] [starting-x starting-y]')
        exit(1)
