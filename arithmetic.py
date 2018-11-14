#!/usr/bin/python

import sys, os , requests 
from bs4 import BeautifulSoup

# Scraping de donnee 
# Consiste a recuperer automatiquement du contenu dune page Web

client = requests.Session()
requete = client.get("http://challenge01.root-me.org/programmation/ch1/")
page = requete.content
soup = BeautifulSoup(page,'xml')

body = soup.find("body")
#on supprime les balises <sub>
filtre = str(body).replace("<sub>"," ")
#on supprime les balises </sub>
res = filtre.replace("</sub>"," ")
lignes = res.split("\n")


ligne0 = lignes[0].split("=")
ligne1 = lignes[1].split("=")
ligne2 = lignes[2].split(" ")

equation = ligne0[10].split("<br")
equation = equation[0]
U0 = ligne1[1]
U1 = ligne2[4]

conditions = equation.split(" ")

res = int(U0)
for i in range(0,int(U1)):
	if((conditions[3] == "+") and (conditions[8]=="+")):
		res =  ( int(conditions[2]) + res ) + ( i * int(conditions[12]) )
	else:
		res =  ( int(conditions[2]) + res ) - ( i * int(conditions[12]) )
	
print "Equation : " + equation + " Solution = " + str(res)
print "U0=" + U0
print "Un+1= " + U1

url = "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result="+str(res)
print url
resultat = client.get(url)
page_res = resultat.content
print page_res

