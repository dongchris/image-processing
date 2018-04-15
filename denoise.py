import sys
from PIL import Image

# define your denoise function here
def denoise(img):

	width, height = img.size

	imgdup = img.copy()

	pixels = imgdup.load()

	for x in range(width):
		for y in range(height):
			r = region3x3(img, x, y)
			pixels[x,y] = median(r)

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

def median(data):

	data = sorted(data)

	index = len(data)/2

	return data[index]

if len(sys.argv)<=1:
	print "missing image filename"
	sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

# call your denoise function here
denoise(img).show()
img.save(%s-%s.png % (sys.argv[1][:-4], sys.argv[0][:-3]))
