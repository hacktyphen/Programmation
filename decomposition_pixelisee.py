#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

f = open("challenge.txt",'r')
lignes  = f.readlines()
f.close()
  
# Utilisation des compteurs pour voir la taille de limage 
hauteur = 0  # type: int


# On traite ligne par ligne l image

for ligne in lignes:

	hauteur += 1
	# On separe les blocs de pixels , soit on construit les colonnes
	blocs = ligne.split("+")
	
	largeur = 0
	for pixels in blocs:
		
		# 0x3 signifie que lon colore 3 blocs de pixels consecutif en blanc, 
		# 0 = FFFFFF = blanc et noir linverse
		#print pixels,
    	#On procede a un split pour savoir le nombre de blocs a colorer en blanc ou en noir
		pixel = pixels.split("x")
		largeur += int(pixel[1])
		
		for i in range(int(pixel[1])) :
		#print pixel,
			if (pixel[0] == "0" ):
				print "x",
			else:
				print " ",
	print " ____"


print "Largeur = " + str(largeur)
print "Hauteur = " + str(hauteur)
print " IL FAUT DEZOOMER POUR VOIR QUE CEST SOLUTION LA SOLUTION DE MERDE !!!!!!!! grrrrrrr "
