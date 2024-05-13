from PIL import Image, ImageOps

image = Image.open("dog.jpg")

# Examples of methods. Find others in Documentation
image_inverted = ImageOps.invert(image)
image_border = ImageOps.expand(image = image, border = 50, fill = (255,255,255))
image_mirrored = ImageOps.mirror(image)
image_scale = ImageOps.scale(image, 0.5) # This one keeps aspect ratio

image.show()
