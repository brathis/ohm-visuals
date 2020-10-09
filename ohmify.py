#        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#                    Version 2, December 2004 
#
# Copyright (C) 2020 Mathis Dedial <mathis@dedial.net> 
#
# Everyone is permitted to copy and distribute verbatim or modified 
# copies of this license document, and changing it is allowed as long 
# as the name is changed. 
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

import os
import os.path
from pathlib import Path
import urllib.parse

from PIL import Image

TARGET_SIZE = (526, 526)  # this is the smallest image size in the feed at the time this script was made
MEDIA_DOWNLOAD_DIR = 'cd_masterizzato'
MEDIA_OUT_DIR = 'out'
Path(MEDIA_OUT_DIR).mkdir(parents=False, exist_ok=True)

# create list of local file paths to the first image of each post
first_image_paths = []
with open('urls_first_image.txt', 'r') as urls_file:
    for line in urls_file.readlines():
        path = urllib.parse.urlparse(line).path
        first_image_paths.append(os.path.join(MEDIA_DOWNLOAD_DIR, path.split('/')[-1]))

# resize images and fit them into canvas
canvas = Image.open('canvas.png')
for i, first_image_path in enumerate(first_image_paths):
    image = Image.open(first_image_path)
    image = image.resize(TARGET_SIZE)
    canvas_copy = canvas.copy()
    canvas_copy.paste(image, (round(canvas.width / 2 - image.width / 2), round(canvas.height / 2 - image.height / 2)))
    canvas_copy.save(os.path.join(MEDIA_OUT_DIR, f'{i:04d}.jpg'))
