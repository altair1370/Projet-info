import tkinter as tk
import numpy as np
from tkinter import *
import crypttextpython as ctp


## Variables



## Fonction initialisation

class Principale:
    def __init__(self, principale):
        self.principale = principale
        self.content =tk.Frame(principale)
        self.content.grid(column=0, row=0)


        self.Boutoncode = tk.Button(self.content, text = 'Coder', fg = "black", bg = "white",command= self.command1)
        self.Boutondecode = tk.Button(self.content, text = 'Décoder', fg = "black", bg = "white", command= self.command2)
        self.BoutonExit = tk.Button(self.content, text = 'Quit', fg = "black", bg = "white", command = principale.destroy)
        
        self.Boutoncode.pack(expand = TRUE, fill = X, padx = 200, pady = 90)
        self.Boutondecode.pack(expand = TRUE, fill = X, padx = 200)
        self.BoutonExit.pack(expand = TRUE, padx = 200, pady = 90)

        self.Boutoncode.configure(font=("Courier", 15, "bold"))
        self.Boutondecode.configure(font=("Courier", 15, "bold"))
        self.BoutonExit.configure(font=("Courier", 15, "bold"))
        
    def command1(self):
        self.principale.withdraw()
        toplevel = tk.Toplevel(self.principale)
        toplevel.geometry("800x800")
        
        
        Modelisation(toplevel, self.principale,'Codage')

    def command2(self):
        self.principale.withdraw()
        toplevel = tk.Toplevel(self.principale)
        toplevel.geometry("800x800")
        Modelisation(toplevel, self.principale,'Décodage')

class Modelisation:
    def __init__(self, toplevel, principale, mode_de_crypt):
        self.modedecrypt = mode_de_crypt
        self.toplevel = toplevel
        #self.toplevel.configure(bg = 'seagreen3')
        self.principale = principale

        

        self.label = tk.Label(self.toplevel, text = self.modedecrypt)
        self.label.configure(font=("Courier", 20, "bold"))
        self.label.pack()

        self.inputmsg = tk.Text(self.toplevel,
                   height = 10,
                   width = 90)
  
        self.inputmsg.pack(side = "top")
        self.labelkey=tk.Label(self.toplevel, text = "clé:")
        self.labelkey.place(x = 20, y = 60)
        self.labelkey.pack()
        
        
        self.key = tk.Entry(self.toplevel, text = "clé:")
        self.key.place(x = 150, y = 20)
        self.key.pack()
        
  
        

        
        self.Boutoncrypt = tk.Button(self.toplevel, text = self.modedecrypt, fg = "black", bg = "white", command = self.evaluate)
        self.Boutoncrypt.pack(expand = True, ipadx =  30, padx = 30, pady = 10)
        self.Boutoncrypt.configure(font=("Courier", 10, "bold"))
  
        #self.contenu = self.saisie.get ("0.0", tk.END)
        self.output = tk.Text(self.toplevel, height = 10,
              width = 90,
              bg = "light cyan")
        self.output.pack()
        self.message_non_crypt=str(self.inputmsg.get("0.0", tk.END))

        self.BoutonExit = tk.Button(self.toplevel, text = 'Exit', fg = "black", bg = "white", command = self.close_windows)
        self.BoutonExit.pack(expand = True, ipadx =  30, padx = 30, pady = 1)
        self.BoutonExit.configure(font=("Courier", 10, "bold"))
        
        

     
    def evaluate(self):
        '''self.labelmsg=tk.Label(self.toplevel)
        self.labelmsg.configure(text = str(self.inputmsg.get("0.0", tk.END)))
        self.labelmsg.place(x=300,y=400)'''
        if self.modedecrypt =="Codage":
            self.message_code=ctp.codage(str(self.inputmsg.get("0.0", tk.END)),int(self.key.get()))
            self.output.insert(tk.END, self.message_code)
        else:
            self.message_decode=ctp.decodage(str(self.inputmsg.get("0.0", tk.END)),int(self.key.get()))
            self.output.insert(tk.END, self.message_decode)
            
     

        
        
    def close_windows(self):
        self.toplevel.destroy()
        self.principale.destroy()
    def open_previous_window(self):
        self.toplevel.destroy()
        #comment afficher l'ancienne fenetre
    
   
    
        
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
