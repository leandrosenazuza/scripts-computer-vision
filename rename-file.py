#Rename images
import os

first_image_index = 1
last_image_index = 40
#Here, you put you base path to your images
#original resolution, resolution: 6000x4000
#info photo: 6000x4000 12.4MB 72dpi 24 bit
#C:\Mestrado\ImagensMission1\
path_file = r"C:\Mestrado\Missiao1Mavic\IMG ("

for i in range(first_image_index,last_image_index+1):
    if(i < 10): index = "" + str(i)
    if (i >= 10): index = "" + str(i)
    print(index)
    #Here, it's split each image to 8 pieces
    #info photo: 750x500 63kb 96 dpi 24 bit
    os.rename(path_file + index + ").JPG", "IMG_0" + index  +".JPG")