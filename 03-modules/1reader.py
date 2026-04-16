import glob
import os

for file in glob.glob("./materials/**"):

    file_name = file.strip("./materials/")
    dir_name = file_name[0]

    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    os.rename(file, f'{dir_name}/{file_name}')

    print(f'file_name: {file_name}, dir_name = {dir_name}')