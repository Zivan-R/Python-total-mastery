from PIL import Image

image = Image.open('cat3.jpg')

# get one pixel
print(image.getpixel((0, 0)))