from PIL import Image, ImageEnhance

# importe image
image = Image.open('cat4.jpg')

# create an enhancer
vibrance_enhancer = ImageEnhance.Color(image)
contrast_enhancer = ImageEnhance.Contrast(image)
brightness_enhancer = ImageEnhance.Brightness(image)
sharpness_enhancer = ImageEnhance.Sharpness(image)

# apply the enhancer 0 == black and white
enhanced_image = vibrance_enhancer.enhance(1.5)

image.show()
enhanced_image.show()