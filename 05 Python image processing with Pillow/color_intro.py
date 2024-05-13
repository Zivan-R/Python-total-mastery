from PIL import Image

image = Image.open('checkerboard.png')

# get one pixel
# print(image.getpixel((0, 0)))

# grayscale images (Puts only one value to the 2 others)
# red_grayscale_image = image.getchannel('R')
# blue_grayscale_image = image.getchannel('B')

# change pixel color (pos, color)
# image.putpixel((0,0), (255,0,0))

# Exercise: change all black pixels to red on checkerboard

for x in range(image.size[0]):
    for y in range(image.size[1]):
        if image.getpixel((x, y))[0] == 0:
            image.putpixel((x, y), (200, 20, 20))

image.show()