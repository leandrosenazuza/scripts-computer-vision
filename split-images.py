from split_image import split_image

first_image_index = 20
last_image_index = 162
#Here, you put you base path to your images
#original resolution, resolution: 6000x4000
name_photo = r"C:\Mestrado\FotosPortoVelho\PortoVelho\mission1\IMG_0"

for i in range(first_image_index,last_image_index+1):
    if(i < 100): index = "0" + str(i)
    if (i >= 100): index = "" + str(i)
    print(index)
    #Here, it's split each image to 8 pieces
    split_image(name_photo + index +'.JPG', 8, 8, False, False, False, str(r'C:\Mestrado\FotosPortoVelho\PortoVelho\mission1\splitedMission1'))