import tkinter as tk
from PIL import Image
import numpy as np
from tkinter import *
import crypttextpython as ctp
import imagetest2 as imt
import cryptimage as dimc


## Variables



## Fonction initialisation

class Principale:
    def __init__(self, principale):
        self.principale = principale
        self.content =tk.Frame(principale)
        self.content.grid(column=0, row=0)


        self.Boutontext = tk.Button(self.content, text = 'Text', fg = "black", bg = "white",command= self.command1)
        self.Boutonimage = tk.Button(self.content, text = 'Image', fg = "black", bg = "white", command= self.command2)
        self.BoutonExit = tk.Button(self.content, text = 'Quit', fg = "black", bg = "white", command = principale.destroy)
        
        self.Boutontext.pack(expand = TRUE, fill = X, padx = 200, pady = 90)
        self.Boutonimage.pack(expand = TRUE, fill = X, padx = 200)
        self.BoutonExit.pack(expand = TRUE, padx = 200, pady = 90)

        self.Boutontext.configure(font=("Courier", 15, "bold"))
        self.Boutonimage.configure(font=("Courier", 15, "bold"))
        self.BoutonExit.configure(font=("Courier", 15, "bold"))
        
    def command1(self):
        self.principale.withdraw()
        toplevel = tk.Toplevel(self.principale)
        toplevel.geometry("800x800")
        
        
        Modelisation(toplevel, self.principale,'Text')

    def command2(self):
        self.principale.withdraw()
        toplevel = tk.Toplevel(self.principale)
        toplevel.geometry("800x800")
        Modelisation(toplevel, self.principale,'Image')

class Modelisation:
    def __init__(self, toplevel, principale, mode_de_crypt):
        self.modedecrypt = mode_de_crypt
        self.toplevel = toplevel
        #self.toplevel.configure(bg = 'seagreen3')
        self.principale = principale

        

        self.label = tk.Label(self.toplevel, text = self.modedecrypt)
        self.label.configure(font=("Courier", 20, "bold"))
        self.label.pack()

  
        if self.modedecrypt == "Text":
            self.inputmsg = tk.Text(self.toplevel,
                                    height = 10,
                                    width = 90)
  
            self.inputmsg.pack(side = "top")

            self.message_non_crypt=str(self.inputmsg.get("0.0", tk.END))
            
            self.labelkey=tk.Label(self.toplevel, text = "clé:")
            self.labelkey.place(x = 20, y = 60)
            self.labelkey.pack()
        
        
            self.key = tk.Entry(self.toplevel, text = "clé:")
            self.key.place(x = 150, y = 20)
            self.key.pack()
            
            v = tk.IntVar()


            self.boutoncesar=tk.Radiobutton(self.toplevel, 
                           text="César",
                           padx = 1000, 
                           variable=v, 
                           value=1)
            self.boutoncesar.pack(anchor=tk.W)
            self.boutoncesar.configure(font=("Courier", 15, "bold"))

            self.boutonvigenere=tk.Radiobutton(self.toplevel, 
                           text="vigenère",
                           padx = 1000, 
                           variable=v, 
                           value=2)
            self.boutonvigenere.pack(anchor=tk.W)
            self.boutonvigenere.configure(font=("Courier", 15, "bold"))
            
        else:
            self.inputimg = tk.Text(self.toplevel,
                                    height = 10,
                                    width = 90)
  
            self.inputimg.pack(side = "top")

            self.image_non_crypt=str(self.inputimg.get("0.0", tk.END))
        #self.contenu = self.saisie.get ("0.0", tk.END)
        

        
        self.Boutoncrypt = tk.Button(self.toplevel, text = "coder", fg = "black", bg = "white", command = self.evaluatecrypt)
        self.Boutoncrypt.pack(side = "top")
        self.Boutoncrypt.configure(font=("Courier", 15, "bold"))
        self.Boutondecrypt = tk.Button(self.toplevel, text = "décoder", fg = "black", bg = "white", command = self.evaluatedecrypt)
        self.Boutondecrypt.pack(side = "top")
        self.Boutondecrypt.configure(font=("Courier", 15, "bold"))
        
        
        self.output = tk.Text(self.toplevel, height = 10,
              width = 90,
              bg = "light cyan")
        self.output.pack(expand = True, ipadx =  30, padx = 30, pady = 10)
        
        
        

        self.BoutonExit = tk.Button(self.toplevel, text = 'Exit', fg = "black", bg = "white", command = self.open_previous_window)
        self.BoutonExit.pack(expand = True, ipadx =  30, padx = 30, pady = 1)
        self.BoutonExit.configure(font=("Courier", 10, "bold"))
        
        
        

        #self.outputimg=tk.Text(self.toplevel, height = 10,
                                  #width = 90,
                                  #bg = "light cyan")
        #self.outputimg.pack()
        

        

     
    def evaluatedecrypt(self):
        '''self.labelmsg=tk.Label(self.toplevel)
        self.labelmsg.configure(text = str(self.inputmsg.get("0.0", tk.END)))
        self.labelmsg.place(x=300,y=400)'''
        if self.modedecrypt =="Text":
            self.message_decode=ctp.decodage(str(self.inputmsg.get("0.0", tk.END)),int(self.key.get()))
            self.output.insert(tk.END, self.message_decode)
        else:
            self.inputmodifie=str(self.inputimg.get("0.0", tk.END)).replace('\n', "")
            
            self.image_decode=dimc.final_crypt(self.inputmodifie)
            self.text_returned="Le nom du fichier est: "+self.image_decode[1]
            
            self.output.insert(tk.END, self.text_returned)
            
           
            
            
            #self.message_decode=ctp.decodage(str(self.inputmsg.get("0.0", tk.END)),int(self.key.get()))
            #self.output.insert(tk.END, self.message_decode)
            
    def evaluatecrypt(self):
        '''self.labelmsg=tk.Label(self.toplevel)
        self.labelmsg.configure(text = str(self.inputmsg.get("0.0", tk.END)))
        self.labelmsg.place(x=300,y=400)'''
        if self.modedecrypt =="Text":
            self.message_code=ctp.codage(str(self.inputmsg.get("0.0", tk.END)),int(self.key.get()))
            self.output.insert(tk.END, self.message_code)
        else:
            self.inputmodifie=str(self.inputimg.get("0.0", tk.END)).replace('\n', "")
            self.image_code=dimc.final_crypt(self.inputmodifie)
            self.text_returned="Le nom du fichier est: "+self.image_code[0]
            
            self.output.insert(tk.END,self.text_returned)
            #self.output.insert(tk.END, str(self.inputimg.get("0.0", tk.END)))
            #self.message_decode=ctp.decodage(str(self.inputmsg.get("0.0", tk.END)),int(self.key.get()))
            #self.output.insert(tk.END, self.message_decode)
            
     

        
        
    def close_windows(self):
        self.toplevel.destroy()
        self.principale.destroy()
    def open_previous_window(self):
        self.toplevel.destroy()
        #Principale(self)
        #self.mainloop()
        self.principale.deiconify()
        #comment afficher l'ancienne fenetre
        #creer une autre fonc destroy (la fonc  detruit tout )
    
   
    
        
## Création des fenêtres

def main():
    root = tk.Tk()
    root.title("CRypT")
    root.geometry("500x500")
    Principale(root)
    root.mainloop()
    

main()



"""
 # Create an object of tkinter ImageTk
        self.img = tk.PhotoImage(file="image.png")

# Create a Label Widget to display the text or Image
self.image_label = tk.Label(self.principale, image = self.img)
        self.image_label.pack()"""
        # Add image file
''' self.bg = tk.PhotoImage(file = "image.png")
  
# Show image using label
        self.label1bg = tk.Label(self.principale, image = self.bg)
        self.label1bg.place(x = 0, y = 0)'''
