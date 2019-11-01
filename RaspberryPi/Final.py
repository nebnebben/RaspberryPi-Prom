#Final
import PIL.Image
import PIL.ImageFilter
import PIL.ImageDraw
import numpy
import math
import os
import time
import csv
import datetime
from constants import *

start = time.time()
os.system("fswebcam -r 240x120 --no-banner image.jpg")

end = time.time()
print(end-start, "taken image")


end = time.time()
print(end-start, "ppm")


os.system("date")

im = PIL.Image.open("image.jpg")

picarray = numpy.array(im)

end = time.time()
print(end-start, "import array")

pix1 = 0
pix2 = 0
pix3 = 0

centrex = 0
centrey = 0
num = 0

for x in range(picarray.shape[0]/5):
   for y in range(picarray.shape[1]/5):
       red, green, blue = picarray[x*5,y*5]
       if (red < green) and (red < blue) and (green > blue) and (red<50):
	   centrex += x*5
	   centrey += y*5
	   num += 1

end = time.time()

end = time.time()
print(end-start, "post main loop")
print(num)

if (num > 20):
	centrex = centrex/(num) #div by zero, no green pixels recognised!
	centrey = centrey/(num)


	radius = math.sqrt(num/3.1415)*7
	rtop = centrey + radius
	rbottom = centrey - radius
	rleft = centrex - radius
	rright = centrex + radius 

	altim = PIL.Image.fromarray(picarray)
	end = time.time()
	print(end-start, "image from array")

	draw = PIL.ImageDraw.Draw(altim)
	draw.rectangle([(rbottom, rright ), (rtop, rleft)],fill = None, outline = (255,0,0))
	end = time.time()
	altim.save('altim.jpg')

	print(end-start, "draw rectangle")

	os.system("date")
	momentofcapture = datetime.datetime.now()
	print(momentofcapture)

	end = time.time()
	print(end-start)

	with open('test.csv', 'a') as csvfile:
	    spamwriter = csv.writer(csvfile, delimiter=' ',
		                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    spamwriter.writerow([momentofcapture, 'Image'])
	
	
	os.system("convert altim.jpg -compress none image.ppm")
	print("Image: Cockroach Detected")
else:
	print("Nothing found")




