# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 10:40:54 2022

@author: laure

"""
from PIL import Image
import random

#création de la clé
def creationDuMasque():
    masque=[]
    for i in range(1000):
        masque.append(random.randint(0,255))
    return masque

#appel de la fonction
masque=creationDuMasque()

#ouverture image
im = Image.open("Airfrance.jpg")

#donnée sous une liste d'octets
List_pixels = list(im.getdata())
#len(List_pixels)

#création de l'image cryptée
Cryptage =[]
j=0
for i in range(len(List_pixels)):
    Cryptage.append((List_pixels[i]+masque[j])%256)
    j = j+1 %len(masque)

imgcrypt=Image.new(im.mode,im.size)
imgcrypt.putdata(Crypatge)
imgcrypt.save("Ruisseaucrypte.jpg")