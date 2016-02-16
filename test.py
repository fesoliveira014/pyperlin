from pyperlin import *
from PIL import Image

W = 255
H = 255

def col( a ):
	return int(round((128-(128*a))))

def col2( a ):
	return int(round((32-(32*a))))        

if __name__ == '__main__':
	noise = PerlinNoise(0.5, 1.0/32.0, 5)
	image = Image.new('L', (255,255))

	for j in range(H):
		for i in range(W):
			noise_value = noise.get_height(float(i),float(j))
			pixel = col(noise_value)
			image.putpixel((i,j), pixel)

	image.show()
	image.save("output.bmp", format="bmp")

