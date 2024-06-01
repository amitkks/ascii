from PIL import Image
import math


chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,. "[::-1]
chararray = list(chars)
charlen = len(chararray)
interval = charlen/256


text_file = open("output.txt", "w")


im = Image.open("porche_taycan.jpg")
print(im.format, im.size, im.mode)


def getChar(inputInt):
    return chararray[math.floor(inputInt * interval)]


#
width, height = im.size

ScaleFactor = 0.2

im = im.resize((int(ScaleFactor*width),int(ScaleFactor*height*8/18)), Image.NEAREST)


width, height = im.size

pixels = im.load()

for i in range(height):
    for j in range(width):
        r, g, b = pixels[j, i]
        h = int(r/3 + g/3 + b/3)
        pixels[j, i] = (h, h, h)
        text_file.write(getChar(h))
    text_file.write('\n')
