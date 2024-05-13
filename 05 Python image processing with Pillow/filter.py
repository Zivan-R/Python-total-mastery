from PIL import Image, ImageFilter

image = Image.open('dog.jpg')

# apply basic filter
image_blur = image.filter(ImageFilter.BLUR)
image_contour = image.filter(ImageFilter.CONTOUR)
image_emboss = image.filter(ImageFilter.EMBOSS)
image_edge = image.filter(ImageFilter.FIND_EDGES)

# apply advanced filter
image_boxblur = image.filter(ImageFilter.BoxBlur(radius = 20))
image_gaussianblur = image.filter(ImageFilter.GaussianBlur(radius = 20))
image_unsharp = image.filter(ImageFilter.UnsharpMask(radius = 20))

image_unsharp.show()