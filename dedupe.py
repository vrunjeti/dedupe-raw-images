import os
import sys

# the following are specific to jpgs and dngs only
def is_image(filename):
  file_type = filename[-3:]
  return file_type == 'jpg' or file_type == 'dng'

def get_image_name(filename):
  return filename[:-4]


if len(sys.argv) > 1:
  path = sys.argv[1]
else:
  path = '.'

images = [file for file in os.listdir(path) if is_image(file)]
filename_hash = {}

for image in images:
  image_name = get_image_name(image)
  if image_name not in filename_hash:
    filename_hash[image_name] = 1
  else:
    filename_hash[image_name] += 1

images_to_remove = []
for image_name, occurrences in filename_hash.items():
  if occurrences > 1:
    images_to_remove.append(image_name)

images_to_remove = [filename + '.jpg' for filename in images_to_remove]

for image in images_to_remove:
  os.remove(os.path.join(path, image))
