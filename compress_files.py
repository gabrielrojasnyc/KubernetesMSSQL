import os
import zipfile
import time


def compress_file(file_path, file):
  compress_file = file_path + '.zip'
  zip = zipfile.ZipFile(compress_file, 'w')
  zip.write(file_path, file)
  zip.close()


current_time = time.time()
print(current_time)
for root, _, files in os.walk('/Users/gabe/Documents/'):
  for file in files:
    file_path = root + '/' + file
    if '.pdf' in file:
      time_created = os.path.getctime(file_path)
      time_difference = current_time - time_created
      if time_difference < 3600:
        compress_file(file_path, file)
      