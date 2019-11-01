import PIL.Image
import PIL.ImageFilter
import numpy


#im = PIL.Image.open("image.jpg")
#picarray = numpy.array(im)
#im.show()
def mfilter(picarray):
	print("mean filter")
	for x in range(2, picarray.shape[0]-2):
		for y in range(2, picarray.shape[1]-2):
		    avgred = 0
		    avggreen = 0
		    avgblue = 0
		    for i in range(-2,3):
		        for j in range(-2,3):
		            avgred += int(picarray[x+i][y+j][0])
		            avggreen += int(picarray[x + i][y + j][1])
		            avgblue += int(picarray[x + i][y + j][2])
		    avgblue = avgblue/25
		    avgred = avgred/25
		    avggreen = avggreen/25
		    picarray[x][y][0] = avgred
		    picarray[x][y][1] = avggreen
		    picarray[x][y][2] = avgblue
	return picarray

#	im = PIL.Image.fromarray(picarray)
#	im.show()
