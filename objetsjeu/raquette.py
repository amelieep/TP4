"""
    objectif : créer un jeu de casse brique
    date début : 06/10/2026
    auteur : Ameli.E, José.K
    to do : gerer le score et les vies.
            gerer la fin d'une partie (quand il n'y a plus de briques ou de vies).
            supprimer le temps de latence pour un appuie long sur une fleche.
            Ajouter deds images pour un rendu plus esthetique.
            Rendre le fichier cassebrique plus propre et respecteux des bonnes pratiques 
    
    
"""
import tkinter as tk
from objetsjeu.briques import GestionBriques

class Raquette:
    # Carctéristiques de la raquette
    def __init__(self,canvas):
        self.canvas=canvas

        self.canvas.update()
        self.raq=canvas.create_rectangle(310, 500, 440, 525,fill="blue")
        self.vitesse=20
        

    def gauche(self,event):
            # Déplace la raquette vers la gauche si elle n'est pas déjà au bord gauche du Canvas
            x1,y1,x2,y2=self.canvas.coords(self.raq)

            if x1>0:
                self.canvas.move(self.raq,-self.vitesse,0)


    def droite(self,event):
            # Déplace la raquette vers la droite si elle n'est pas déjà au bord droit du Canvas
            x1,y1,x2,y2=self.canvas.coords(self.raq)
            largeur=self.canvas.winfo_width()

            if x2<largeur:
                self.canvas.move(self.raq,self.vitesse,0)