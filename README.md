# gimp_splitimg #
A simple gimp python-fu script to split flat images.

This project assumes that you
1. Are using Linux
2. Have GIMP 2.10+ installed

## A Word of Warning ##
This is a very fragile set of scripts. There is no error checking and it assumes that all the arguments sent to it are valid and exactly what you want. 

# Usage #
```bash
# In the directory in which the splitimg bash script resides
# splitimg <filepath> <sub-image width> <sub-image height> <number of sub-images>
# Example:
splitimg /home/username/Pictures/Foo.png 800 600 5
```
