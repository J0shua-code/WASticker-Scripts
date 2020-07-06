from PIL import Image
import sys
import os

files = os.listdir("input/")

def make_square(im):
	# set the size of image 
	basewidth = 512
	new_im = Image.new('RGBA', (basewidth, basewidth))
	if(im.size[0] > im.size[1]):
		wpercent = (basewidth/float(im.size[0]))
		hsize = int((float(im.size[1])*float(wpercent)))
		im = im.resize((basewidth,hsize), Image.ANTIALIAS)
	else:
		hpercent = (basewidth/float(im.size[1]))
		wsize = int((float(im.size[0])*float(hpercent)))
		im = im.resize((wsize,basewidth), Image.ANTIALIAS)

    
	new_im.paste(im)
	return new_im

for x in files:
	
	if(x[-3:] == "png"):
		temp = Image.open("input/"+x)
		temp1 = make_square(temp)
		temp1.save("output/"+x)