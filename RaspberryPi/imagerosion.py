import PIL.Image
import PIL.ImageFilter
import PIL.ImageDraw
import numpy
import math
import os
import time
import csv
import datetime

start = time.time()

im = PIL.Image.open("image.jpg")
picarray = numpy.array(im)

for x in range(picarray.shape[0]):
   for y in range(picarray.shape[1]):
       red, green, blue = picarray[x,y]
       redl, greenl, bluel = picarray[x-1,y]
       redr, greenr, bluer = picarray[x+1,y]
       redu, greenu, blueu = picarray[x,y+1]
       redd, greend, blued = picarray[x,y-1]
       if (green > blue > red) and (red<50) and (greenr > bluer > redr) and (redr<50) and (greenl > bluel > redl) and (redl<50) and (greenu > blueu > redu) and (redu<50) and (greend > blued > redd) and (redd<50):
	   centrex += x
	   centrey += x
	   num += 1

end = time.time()

end = time.time()
print(end-start, "post main loop")
print(num)
centrex = centrex/(num)
centrey = centrey/(num)


radius = math.sqrt(num/3.1415)*6
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
altim.show()

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


#check pixel above, below, left and right
