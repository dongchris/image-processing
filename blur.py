import sys
from PIL import Image

# define your blur function here
def blur(img):

	width, height = img.size

	imgdup = img.copy()

	pixels = imgdup.load()

	for x in range(width):
		for y in range(height):
			r = region3x3(img, x, y)
			pixels[x,y] = avg(r)

	return imgdup

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

def avg(num):
	sum = 0
	count = 0

	for i in num:
		sum = sum + i
		count = count + 1
	return sum/count

if len(sys.argv)<=1:
	print "missing image filename"
	sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

# call your blur function here
blur(img).show()