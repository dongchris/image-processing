import sys
from PIL import Image

# define your flip function here
def flip(img):
	width, height = img.size

	imgdup = img.copy()

	m = img.load()
	m2 = imgdup.load()

	for x in range(width):
		for y in range(height):
			m2[x,y] = m[width-x-1,y]
	return imgdup


if len(sys.argv)<=1:
	print "missing image filename"
	sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

# call your flip function here
flip(img).show()
