# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:53:57 2023

@author: laure
"""

#code avec la classe pour crypter et décrypter 

class Image():
    def __init__(self,masque,image):
        self.masque=masque
        self.image=image
    
    def cryptage(self,image,masque):#création de l'image cryptée
       
        Cryptage =[]
        j=0
        for i in range(len(self.image)):
            newp=(((self.image[i][0]+self.masque[j])%256),((self.image[i][1]+self.masque[j])%256),((self.image[i][2]+self.masque[j])%256))
            Cryptage.append(newp)
            j = (j+1)%len(self.masque)
        return Cryptage
    
    def decryptage(self,image,masque):# création de l'image décryptée
       
        Decryptage=[]
        k=0
        for i in range(len(self.image)):
            decrypt=(((self.image[i][0]-self.masque[k])%256),((self.image[i][1]-self.masque[k])%256),((self.image[i][2]-self.masque[k])%256))
            Decryptage.append(decrypt)
            k = (k+1)%len(self.masque)
        return Decryptage
    
    