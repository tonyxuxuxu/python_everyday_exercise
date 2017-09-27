"""

第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

"""

from PIL import Image
import os

def modify_size(dirpath, size_x, size_y):
    file_list = os.listdir(dirpath)
    for file in file_list:
        if os.path.splitext(file)[1] == ".jpg":
            image = Image.open(file)
            image.thumbnail((size_x, size_y))
            image.save(file)
            print(file)

if __name__ == "__main__":
    modify_size("./", 1136, 640)



