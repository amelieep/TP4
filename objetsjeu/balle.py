
import math,random
from objetsjeu.briques import GestionBriques
from objetsjeu.raquette import Raquette

class GestionBalle:
    def __init__(self, canvas, briques, raq, score=0, rayon=15):
        self.canvas = canvas
        self.rayon = rayon
        self.briques = briques
        self.score = score
        self.raq = raq
        
        self.canvas.update()  # Force la mise a jour des dimensions
        self.largeur_canvas = self.canvas.winfo_width()
        self.hauteur_canvas = self.canvas.winfo_height()
        
        #coordonnées de départ du centre de la balle 
        self.posx = (self.largeur_canvas/2)
        self.posy = (self.hauteur_canvas*0.75)
        #création de la balle 
        self.balle = canvas.create_oval(self.posx-self.rayon, self.posy-self.rayon, self.posx+self.rayon, self.posy+self.rayon, width = 1, outline = 'pink', fill= 'pink')
        
        # caractéristiques initiales aléatoires vitesse et angle de lancement de la balle
        # random.uniform prend un nombre entre les deux arguments : renvoie un nombre de pixels par frames
        self.vitesse = 8 
        self.angle = random.uniform(1,math.pi/4)
        
        # direction ("rayon incident")
        self.DX = self.vitesse*math.cos(self.angle)
        self.DY = self.vitesse*math.sin(self.angle)
        
        self.deplacement()
        
    def deplacement(self) :    # respecte la loi de descarte  "angle réfléction"= -"angle incidence"
        
        if not self.canvas.winfo_exists():
            return
            
        #rebond a droite
        if self.posx + self.rayon + self.DX > self.largeur_canvas :
            self.posx = 2*(self.largeur_canvas-self.rayon)-self.posx
            self.DX = -self.DX
                
        # rebond a gauche
        if self.posx-self.rayon+self.DX < 0:
            self.posx = 2*self.rayon-self.posx
            self.DX = -self.DX
        # rebond en haut
        if self.posy+self.rayon+self.DY > self.hauteur_canvas:
            self.posy = 2*(self.hauteur_canvas-self.rayon)-self.posy
            self.DY = -self.DY
        # rebond en bas
        if self.posy-self.rayon+self.DY < 0:
            self.posy = 2*self.rayon-self.posy
            self.DY = -self.DY

        self.posx = self.posx+self.DX
        self.posy = self.posy+self.DY
        
        self.interactionbriques()
        # affichage
        self.canvas.coords(self.balle,self.posx-self.rayon,self.posy-self.rayon,self.posx+self.rayon,self.posy+self.rayon)
        # mise à jour toutes les 50 ms
        self.canvas.after(20, self.deplacement)
     
    #fonction gerant les rebond sur les briques et la disparition de celles-ci  
    
     
    def interactionbriques(self) :
        
        objetstouchés = self.canvas.find_overlapping(self.posx-self.rayon, self.posy-self.rayon, self.posx+self.rayon,self.posy+self.rayon)  # Permet de creer un tuple avec les ID de tous les objets touchés par la balle sur le canva. cette fonction prend en argument les coordonnées du carré contenant la balle
        
        for objet in objetstouchés :
            if objet in self.briques.briques :  #recupère briques du self.briques = briques
                self.canvas.delete(objet)  #suppression de la brique du canva (visuel)
                self.briques.briques.remove(objet)  #suppression de l'ID (briques.briques) touché dans la liste. Evite de gerer une collision inexistante
                self.score += 10 #ajout de 10 points au score
                self.DY = -self.DY #changement de direction
            #on utilise la meme logique pour le rebond sur la raquette 
            if objet == self.raq.raq :  
                self.DY = -self.DY