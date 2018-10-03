import os
import shutil
import hashlib


def get_zip_files():
  for root, _, files in os.walk('/Users/gabe/Documents/'):
    for local_file in files:
      file_path = root + '/' + local_file
      if '.zip' in local_file:
        print(file_path)
        move_zip_files(file_path, local_file)

def move_zip_files(file_path, local_file):
  file_source_hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
  remote_file =  '/Users/gabe/Documents/SDA/' + local_file
  shutil.copy2(file_path, remote_file)
  file_remote_hash = hashlib.md5(open(remote_file, 'rb').read()).hexdigest()
  if file_source_hash == file_remote_hash:
    print(file_remote_hash)
    os.remove(file_path)

get_zip_files()
