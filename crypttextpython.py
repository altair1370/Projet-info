# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 17:16:15 2022

@author: zarhl
"""


""" 
    Décale de n place(s) dans la table ASCII
"""
def decal_lettre_c(lettre, n):
    return chr((ord(lettre) + n) % 255)


def decal_lettre_d(lettre, n):
    return chr((ord(lettre) - n) % 255)
        
""" 
    Crypte un texte 
"""        
def codage(text, n):
    texte_code = ""
    
    for i in range(0, len(text)):
        character = text[i]
        
        if character != " ":
            texte_code = texte_code + decal_lettre_c(character, n)
        else:
            texte_code = texte_code + " "
    
    return texte_code


""" 
    Décrypte un texte 
"""
def decodage(text, n):
    texte_decode = ""
    
    for i in range(0, len(text)):
        character = text[i]

        if character != " ":
            texte_decode = texte_decode + decal_lettre_d(character, n)
        else:
            texte_decode = texte_decode + " "
            
    return texte_decode

print(codage("hello world", 6))




