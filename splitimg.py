!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from os import path
from gimpfu import *

def process(orig_full, sub_img_width, sub_img_height, num_imgs):
    orig_path, orig_filename = path.split(orig_full)

    orig_img = pdb.gimp_file_load(orig_full, orig_full)

    layer = pdb.gimp_image_get_active_layer(orig_img)

    # Cut off the right and bottom space that we won't use
    total_width = layer.width - (layer.width % sub_img_width)
    total_height = layer.height - (layer.height % sub_img_height)

    # Start in the upper-left corner
    x = 0
    y = 0

    count = 0

    # Split left to right, top to bottom
    while y < total_height and count < num_imgs:
        while x < total_width and count < num_imgs:
            new_name, ext = path.splitext(orig_filename)
            pict_num = '{:03d}'.format(count)
            
            # Output name is <inputname>_###.<ext> in the same directory
            # as the original
            new_name = '{0}_{1}{2}'.format(new_name, pict_num, ext)
            pdb.gimp_rect_select(orig_img, x, y, sub_img_width, sub_img_height, 2, 0, 0)

            # Copy the original and paste it as a new image
            pdb.gimp_edit_copy(orig_img.layers[0])
            new_img = pdb.gimp_edit_paste_as_new()

            new_full = orig_path + new_name
            # Save the new image.
            pdb.gimp_file_save(new_img, new_img.layers[0], new_full, new_full)

            # Clean up the image to save RAM
            pdb.gimp_image_delete(new_img)
            count += 1
            x += sub_img_width
        x = 0  # reset to the left side
        y += sub_img_height

    # Clean up the image to save RAM
    pdb.gimp_image_delete(orig_img)

if __name__ == "__main__":
    print "Running as __main__ with args: %s" % sys.argv
