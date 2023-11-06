from split_image import split_image

first_image_index = 20
last_image_index = 162
#Here, you put you base path to your images
#original resolution, resolution: 6000x4000
#info photo: 6000x4000 12.4MB 72dpi 24 bit
name_photo = r"C:\Mestrado\FotosPortoVelho\PortoVelho\mission1\IMG_0"

for i in range(first_image_index,last_image_index+1):
    if(i < 100): index = "0" + str(i)
    if (i >= 100): index = "" + str(i)
    print(index)
    #Here, it's split each image to 8 pieces
    #info photo: 750x500 63kb 96 dpi 24 bit
    split_image(name_photo + index +'.JPG', 8, 8, False, False, False, str(r'C:\Mestrado\FotosPortoVelho\PortoVelho\mission1\splitedMission1'))
