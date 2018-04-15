import sys
from PIL import Image

# define function region3x3
def region3x3(img, x, y):
	me = getpixel(img, x, y)
	N = getpixel(img, x, y-1)
	S = getpixel(img, x, y+1)
	E = getpixel(img, x + 1, y)
	W = getpixel(img, x-1, y)
	NW = getpixel(img, x-1, y-1)
	NE = getpixel(img, x+1, y-1)
	SE = getpixel(img, x+1, y+1)
	SW = getpixel(img, x-1, y+1)

	return list([me,N,E,S,W,NW,NE,SE,SW])

def getpixel(img, x, y):

	width, height = img.size

	imgdup = img.copy()

	pixels = imgdup.load()

	if x < 0: x = 0

	if x >= width: x = x-1

	if y < 0: y = 0

	if y >= height: y = y-1

	return pixels[x,y]

def open(argv):
    if len(argv)<=1:
        print "missing image filename"
        sys.exit(1)
    img = Image.open(argv[1])
    img = img.convert("L") #make greyscale if not already (luminance)
    return img

def filter(img, f):
    width, height = img.size

    imgdup = img.copy()

    pixels = imgdup.load()

    for x in range(width):
        for y in range(height):
            r = region3x3(img, x, y)
            pixels[x, y] = f(r)

    return imgdup
