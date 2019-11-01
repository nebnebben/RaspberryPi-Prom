import PIL.Image
import PIL.ImageFilter
import PIL.ImageDraw
import numpy
import math
import os
import time
import csv
import datetime

def mdetect(camroach):
	start = time.time()

	#os.system("fswebcam -r 640x480 --no-banner image.jpg")-uncomment this
	im = PIL.Image.open("brokenimage.jpg")
	picarray = numpy.array(im)
	pix1 = 0
	pix2 = 0
	pix3 = 0

	centrex = 0
	centrey = 0
	num = 0

	#old = 49,65,5
	#new = 25,13,5

	#quad = numpy.zeros((13,25,5))

	quad = numpy.zeros((49,65,5))


	quadx = 0
	quady = 0

	print(picarray.shape)
	for x in range(picarray.shape[0]):
	   quady = 0
	   if (x % 10) == 0:
	       quadx += 1
	   for y in range(picarray.shape[1]):
	       if (y % 10) == 0:
		  quady += 1
	       red, green, blue = picarray[x,y]
	       if (green > blue > red) or ((green < 100) and (red < 100) and (blue < 100)):
		   quad[quadx][quady][0] += 1
		   quad[quadx][quady][1] += x 
		   quad[quadx][quady][2] += y
		   num += 1

	numsquare = 0

	for x in range(quadx):
	   for y in range(quady):
	      if (quad[x][y][0] > 80):
		 quad[x][y][3] = 1
		 quad[x][y][1] = quad[x][y][1]/quad[x][y][0]
		 quad[x][y][2] = quad[x][y][2]/quad[x][y][0]
		 numsquare += 1
		 centrex += quad[x][y][1]
		 centrey += quad[x][y][2]

	no = 1

	def checkbounds(x,y):
	   if (quad[x][y][3] == 1) and (quad[x][y][4] == 0):
		quad[x][y][4] = no
		numli[no-1] += 1
		xli[no-1] += x
		yli[no-1] += y
		if y < 64 and (quad[x][y+1][4] == 0):
		   checkbounds(x,y+1)
		if x < 64 and (quad[x+1][y][4] == 0):
		   checkbounds(x+1,y)	
		if y > 0 and (quad[x][y-1][4] == 0):
		   checkbounds(x,y-1)	   
		if x > 0 and (quad[x-1][y][4] == 0):
		   checkbounds(x-1,y)

	numli = []
	xli = []
	yli = []
	for x in range(quadx):
	   for y in range(quady):
		if (quad[x][y][3] == 1) and (quad[x][y][4] == 0):
		   numli.append(1)
		   xli.append(0)
		   yli.append(0)
		   checkbounds(x,y)
		   no +=1	


#	print(numli)
	
	try:	
		c = 0
		while c < len(numli):
		   if numli[c] < 30:
			del numli[c]
			del xli[c]
			del yli[c]
			c = c - 1
		   c += 1		
	except IndexError:
		print("IndexError")

#	print(numli)

	if len(numli) == 0:
		print("No bug here")
		return camroach, picarray
	else:
		print("The number of bugs found is ", len(numli))
		altim = PIL.Image.fromarray(picarray)

		for i in range(0,len(numli)):	
		   radius = math.sqrt(numli[i]/3.1415)*10
		   centrex = (xli[i]/numli[i])*10
		   centrey = (yli[i]/numli[i])*10
		   rtop = centrey + radius
		   rbottom = centrey - radius
		   rleft = centrex - radius
		   rright = centrex + radius 
		   draw = PIL.ImageDraw.Draw(altim)
		   draw.rectangle([(rbottom, rright ), (rtop, rleft)],fill = None, outline = (255,0,0))
		altim.save('altim.jpg')
#		print(no)
#		print(numsquare)
#		print(num)
		os.system("date")
		momentofcapture = datetime.datetime.now()
		momentofcapture = momentofcapture.strftime('%Y_%m_%d_%H:%M:%S')
		print(momentofcapture)
		os.system("convert altim.jpg -compress none image{}.ppm".format(momentofcapture))

		with open('test.csv', 'a') as csvfile:
		    spamwriter = csv.writer(csvfile, delimiter=' ',
				            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		    spamwriter.writerow([momentofcapture, 'ImageMult'])
		camroach += len(numli)
		return camroach, picarray

#im.show()
#imedges.show()

#rgb
#cropimage = 27.6599773426 89.8834762907 75.3515941091
#cropimage4 = 83.2177533087 114.568656433 105.684916739
#if red < green and red < blue
#if green > red and green > blue
#if blue > red and blue < green

#maybe check if a pixel is within a boundary in terms of colours

#give each pixel a value depending on the ones around it as well?

#some function in terms of distance and location?
#Have centre + edges fSystem Core Requirements

#each new pixel changes values slightly


#change to lower resolution for faster results



