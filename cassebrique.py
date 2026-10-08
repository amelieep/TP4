"""
    objectif : créer un jeu de casse brique
    date début : 06/10/2026
    auteur : Ameli.E, José.K
    to do : les classes pour les differents objets : briques, balle,raquette. Les conditions de jeu : deplacement, ecran....
    
"""

from tkinter import Tk, Label, Button, Canvas,Entry,Toplevel


class GestionBriques:
    def __init__(self, canvas, nb_lignes=5, nb_colonnes=10, marge=30, espace=10, hauteur_brique=25, couleur="royalblue"):
        self.canvas = canvas
        self.briques = []  # Liste contenant les IDs Tkinter des briques creees
        
        # Recuperation des dimensions du canvas
        self.canvas.update()  # Force la mise a jour des dimensions
        largeur_canvas = self.canvas.winfo_width()
        
        # Calcul de la largeur de chaque brique pour remplir uniformément le haut
        largeur_utile = largeur_canvas - (2 * marge) - ((nb_colonnes - 1) * espace)
        largeur_brique = largeur_utile / nb_colonnes

        # Creation des briques en grille
        for ligne in range(nb_lignes):
            for col in range(nb_colonnes):
                x1 = marge + col * (largeur_brique + espace)
                y1 = 10 + ligne * (hauteur_brique + espace)
                x2 = x1 + largeur_brique
                y2 = y1 + hauteur_brique
                
                # Dessin du rectangle sur le canvas deja cree
                brique_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="black")
                self.briques.append(brique_id)
                
                
#fonction permettant de lancer une partie : ouvrir un nouvelle fentre fille (dépend de la fentre principale que l'on creer apres) qui contient le canva
def lancerpartie():
    jeu = Toplevel(menu)
    jeu.title('nouvelle partie')
    jeu.geometry('800x600+400+100')
    
    #caracteristiques du canva
    largeur = 750
    hauteur = 550
    canevas = Canvas(jeu, width=largeur, height=hauteur, bg = 'white' )
    canevas.pack(padx=5, pady=5)
    
    briques = GestionBriques(canevas, nb_lignes=5, nb_colonnes=10, couleur="salmon")

    # bouton pour quitter la partie, zone de texte du score et de la vie  
    quit = Button(jeu, text = 'QUITTER', command = jeu.destroy)
    quit.pack(side='right', padx = 23, pady = 10)
    
    score = Label(jeu, text = 'score: ', font =('Helvetica',15,'bold'))
    score.pack(side = 'left', padx=23, pady=5)
    
    vie = Label(jeu, text = 'vies: ', font =('Helvetica',15,'bold'))
    vie.pack(side = 'left', pady=5)

# creation de la fenetre d'acceuil du jeu
menu=Tk()
menu.title('jeu de casse brique')
menu.geometry('800x600+400+100')
menu['bg'] = 'pink'



# contenu du menu : titre, bouton quitter(ferme toutes les fenetres), bouton lancer une partie
labelcb = Label(menu, text = "MENU PRINCIPAL", font = ("Helvetica", 20, "bold"), bg="pink")
labelcb.pack(pady=20)

boutonquitter = Button (menu, text = 'QUITTER', font = ("Helvetica",15), fg = 'red', bg = 'pink', command = menu.destroy)
boutonquitter.pack(side='bottom', padx= 10, pady = 10)

boutonpartie = Button(menu, text = 'Lancer partie',  font = ("Helvetica",15), bg = 'pink', relief = 'flat',command=lancerpartie)
boutonpartie.pack(pady =150)

menu.mainloop()



