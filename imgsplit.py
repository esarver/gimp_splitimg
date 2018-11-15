#!/usr/bin/python3

import sys

from os import path
from PIL import Image

def process_background():
    raise NotImplementedError  # TODO - Write this

def generate_subimages(full_path: str, sub_image_width: int, 
                       sub_image_height: int, num_images: int = -1, 
                       starting_x: int = 0, starting_y: int = 0):
    '''
    TODO - Write a docstring
    '''
    orig_image = Image.open(full_path)

    orig_width, orig_height = orig_image.size

    count = 0

    for curr_y in range(starting_y, orig_height, sub_image_height):
        for curr_x in range(starting_x, orig_width, sub_image_width):
            if num_images > -1 and count >= num_images:
                return
            if (curr_x + sub_image_width) > orig_width:
                break
                
            select_box = (curr_x, curr_y, (curr_x + sub_image_width), 
                         (curr_y + sub_image_height))

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
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='The file to process')

    parser.add_argument('width', type=int,
                        help='The width of the sub-images')

    parser.add_argument('height', type=int,
                        help='The height of the sub-images')

    parser.add_argument('-x', type=int, help='The starting x-coordinate.',
                        default=0)

    parser.add_argument('-y', type=int, help='The starting y-coordinate.',
                        default=0)

    parser.add_argument('-n', '--num_images', type=int,
                        help='The number of sub-images that should be output.',
                        default=-1)

    args = parser.parse_args()

    x = args.x if args.x >= 0 else None
    y = args.y if args.y >= 0 else None
    width = args.width if args.width >= 1 else None
    height = args.height if args.height >= 1 else None

    if x is None or y is None:
        print('The arguments for \'x\' and \'y\' must be positive integers.')
        exit(1)
    
    if width is None or height is None:
        print('The arguments for \'width\' and \'height\' must be positive integers greater or equal to one.')
        exit(1)

    if args.num_images is not None and args.num_images <= 0:
        print('The argument for \'num_images\', when specified, must be greater than zero.')
        exit(1)

    import imghdr
    if not path.isfile(args.input_file) or imghdr.what(args.input_file) is None:
        print(f'The file \'{args.input_file}\' does not exist or is not an image file.')
        exit(1)

    generate_subimages(args.input_file, width, height, 
                       num_images = args.num_images, starting_x = x, 
                       starting_y = y)
