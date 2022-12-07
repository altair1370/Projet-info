"dictionnaire = {"é" : "e", "ê" : "e", "è" : "e", "î" : "i", "ï" : "i", "ö" : "o", "ô"
: "o", "à" : "a", "â" : "a", "ù" : "u", "ç" : "c", "æ" : "ae", "œ" : "oe"}

def multi_replace(texte, dico):
    for clef in dico:
        texte = texte.replace(clef, dico[clef])
        texte= texte.replace(" ","")
    return texte

def liste(texte):
    x=list(texte)
    return x

def lettre(x):
    for c in x:
        carac= ord(c.upper())
    return carac>64 and carac<91
    
