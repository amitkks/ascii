from PIL import Image
import math

#Character array in decreasing level of grayscale
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,. "[::-1]
chararray = list(chars)
charlen = len(chararray)
interval = charlen/256

#priting the ascii characters in the text file
text_file = open("output.txt", "w")

#importing the image to be converted into ascii art
im = Image.open("porche_taycan.jpg")
print(im.format, im.size, im.mode)

#function to link each pixel with character in the list
def getChar(inputInt):
    return chararray[math.floor(inputInt * interval)]


#getting the width and height of the image
width, height = im.size
#scaling factor
ScaleFactor = 0.2

#resizing the image
im = im.resize((int(ScaleFactor*width),int(ScaleFactor*height*8/18)), Image.NEAREST)


width, height = im.size
#Loading the pixel array
pixels = im.load()
#looping through each pixel in the array
for i in range(height):
    for j in range(width):
        r, g, b = pixels[j, i]
        h = int(r/3 + g/3 + b/3)
        pixels[j, i] = (h, h, h)
        text_file.write(getChar(h))
    text_file.write('\n')
