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
im = Image.open("test.jpg")
im.show()

#donnée sous une liste d'octets
List_pixels = list(im.getdata())
len(List_pixels)

#print(len(List_pixels))

def cryptage(image,masque):#création de l'image cryptée
    Cryptage =[]
    j=0
    for i in range(len(image)):
        newp=(((image[i][0]+masque[j])%256),((image[i][1]+masque[j])%256),((image[i][2]+masque[j])%256))
        Cryptage.append(newp)
        j = (j+1)%len(masque)
    return Cryptage
imgcrp=cryptage(List_pixels,masque)
imgcrypt=Image.new(im.mode,im.size)
imgcrypt.putdata(imgcrp)
imgcrypt.show()
#imgcrypt.save("Airfrancecrypte.jpg")

def decryptage(image,masque):# création de l'image décryptée
    Decryptage=[]
    k=0
    for i in range(len(image)):
        decrypt=(((image[i][0]-masque[k])%256),((image[i][1]-masque[k])%256),((image[i][2]-masque[k])%256))
        Decryptage.append(decrypt)
        k = (k+1)%len(masque)
    return Decryptage
decrp= decryptage(imgcrp,masque)
imgdecrypt=Image.new(im.mode,im.size)
imgdecrypt.putdata(decrp)
imgdecrypt.show()