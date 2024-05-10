from PIL import Image

# create an image via import
image = Image.open('cat1.jpg')

# analyze the image
print(image.size)
print(image.filename)
print(image.format)

# flip the image
#image = image.transpose(Image.Transpose.ROTATE_90)

# show image
# image.rotate(30).save("cat1_rotated.png")
# image.rotate(30).show()

# Exercice

cat_rotated = image.rotate(30)
cat_rotated.save('cat1_rotated.png', 'png')