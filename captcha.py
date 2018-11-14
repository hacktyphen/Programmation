#!/usr/bin/python 

import sys, urllib, base64
import subprocess
import sys
from PIL import Image


if __name__=="__main__":

	page = urllib.urlopen('http://challenge01.root-me.org/programmation/ch8/')
	strpage = page.read()
	print strpage

	contenu = strpage.split("\"")
	#for i in contenu: 
		#print " "
		#print i

	image = contenu[1].split(",")
	img_data = image[1]
	resultat = base64.b64decode(img_data)
	with open("captcha.png", "wb") as fh:
    		fh.write(resultat)
	fh.close()
	
	# ouverture du fichier image

	try:
	  img = Image.open("captcha.png")
	except IOError:
	  print 'Erreur sur ouverture du fichier ' + "captcha.png"
	  sys.exit(1)

	# largeur et hauteur de l'image
	largeur, hauteur = img.size
	img_traiter = Image.new("L",(largeur,hauteur))
	
	#On enleve les points noirs sur l'image 
	for y in range(hauteur): 
		for x in range(largeur):
			p = img.getpixel((x,y))
			#255 = blanc , 0 = noir
			if (p[0] == 0 and p[1] == 0 and p[2] == 0 ) : 
				p = (255,255,255)
			pixel = p 
			img.putpixel((x,y),pixel)
	img.show()
	img.close()

	f = open('captcha.png', 'rb')
    	result = subprocess.Popen(['gocr -f UTF8 -i captcha.png '], shell=True,    stdout=subprocess.PIPE).communicate()[0]
        f.close

	result = result.replace('\n', '')
	result = result.replace(' ', '')
	result = result.replace(',', '')
	result = result.replace('\'', '')
	print result

	fh.close()
		
    	
