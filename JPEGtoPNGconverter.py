import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if output folder exists, if not create one
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through the image folder
# convert images to png
# save it to the output folder
for pictures in os.listdir(image_folder):
    clean_name = os.path.splitext(pictures)[0]
    img = Image.open(f'{image_folder}/{pictures}')
    img.save(f'{output_folder}/{clean_name}.png', 'png')
    print('all done!')
