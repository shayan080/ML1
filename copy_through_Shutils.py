import glob
import shutil
import os


src_folder = "D:\myfile" 
destination_folder = "D:\otherfile"  


for folder in ['images', 'txt', 'json']:
    os.makedirs(os.path.join(destination_folder, folder), exist_ok=True)


for image_file in glob.glob(os.path.join(src_folder, '*.jpg')) + \
                  glob.glob(os.path.join(src_folder, '*.png')) + \
                  glob.glob(os.path.join(src_folder, '*.jpeg')):
    shutil.copy(image_file, os.path.join(destination_folder, 'images'))

for txt in glob.glob(os.path.join(src_folder, '*.txt')):
    shutil.copy(txt, os.path.join(destination_folder, 'txt'))


for json in glob.glob(os.path.join(src_folder, '*.json')):
    shutil.copy(json, os.path.join(destination_folder, 'json'))

print("Files moved successfully!")
