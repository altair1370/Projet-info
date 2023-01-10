# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:55:21 2023

@author: laure
"""
import classcrypt
from PIL import Image
import random

 #création de la clé
def creationDuMasque():
    masque=[]
    for i in range(1000):
        masque.append(random.randint(0,255))
    return masque

# module main pour utiliser la classe de cryptage
def Crypt(im,List_pixels,masque):
    #cryptage
    imgcrp=classcrypt.Image.cryptage(List_pixels,masque)
    imgcrypt=Image.new(im.mode,im.size)
    imgcrypt.putdata(imgcrp)
    imgcrypt.show()

def Decrypt(im,imgcrp,masque):
    #décryptage
    decrp= classcrypt.Image.decryptage(imgcrp,masque)
    imgdecrypt=Image.new(im.mode,im.size)
    imgdecrypt.putdata(decrp)
    imgdecrypt.show()




def main():
    
    masque=creationDuMasque()#appel de la fonction

    im = Image.open("test.jpg")#ouverture image
    im.show()

    
    List_pixels = list(im.getdata())#donnée sous une liste d'octets
    #len(List_pixels)
    #cryptage
    imgcrp=classcrypt.Image.cryptage(List_pixels,masque)
    imgcrypt=Image.new(im.mode,im.size)
    imgcrypt.putdata(imgcrp)
    imgcrypt.show()
    #décryptage
    decrp= classcrypt.Image.decryptage(imgcrp,masque)
    imgdecrypt=Image.new(im.mode,im.size)
    imgdecrypt.putdata(decrp)
    imgdecrypt.show()

main()