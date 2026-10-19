
from tkinter import Tk, Label, Button, Canvas,Toplevel,PhotoImage
from objetsjeu.briques import GestionBriques
from objetsjeu.balle import GestionBalle
from objetsjeu.raquette import Raquette


# creation de la fenetre d'acceuil du jeu : menu
menu=Tk()
menu.title('jeu de casse brique')
menu.geometry('800x600+400+100')
menu['bg'] = 'pink'
        
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

     # Ajout d'une image de fond #
     image_fond = PhotoImage(file="Wallpaper_casse_brique.png")
     canevas.image_fond = image_fond 
     canevas.create_image(0, 0, image=canevas.image_fond, anchor="nw")

    
    canevas.focus_set() #indispensable pour relier les touches du clavier au code
    
    #appelle la classe gestionBriques dans le fichier objetsjeu.briques pour les afficher au début de la partie
    briques = GestionBriques(canevas, nb_lignes=5, nb_colonnes=10, couleur="salmon")

    
    
    # bouton pour quitter la partie, zone de texte du score et de la vie  
    quit = Button(jeu, text = 'QUITTER', command = jeu.destroy)
    quit.pack(side='right', padx = 23, pady = 10)
    
    points = Label(jeu, text = 'score: ', font =('Helvetica',15,'bold'))
    points.pack(side = 'left', padx=23, pady=5)
    
    vie = Label(jeu, text = 'vies: ', font =('Helvetica',15,'bold'))
    vie.pack(side = 'left', pady=5) 
    
    #appelle de la classe Raquette dans le fichier objetjeu.raquette pour afficher la raquette et ses actions
    raquette = Raquette(canevas)
    #appelle de la classee gestionballe dans le fichier objetsjeu.balle pour afficher la balle au début de la partie et ses actions.
    balle = GestionBalle(canevas, briques=briques, raq=raquette,score=0, rayon=15)
    
 
    # Liaison des touches aux méthodes de la raquette
    canevas.bind('<Left>',raquette.gauche)
    canevas.bind('<Right>',raquette.droite)



# contenu du menu : titre, bouton quitter(ferme toutes les fenetres), bouton lancer une partie
labelcb = Label(menu, text = "MENU PRINCIPAL", font = ("Helvetica", 20, "bold"), bg="pink")
labelcb.pack(pady=20)

boutonquitter = Button (menu, text = 'QUITTER', font = ("Helvetica",15), fg = 'red', bg = 'pink', command = menu.destroy)
boutonquitter.pack(side='bottom', padx= 10, pady = 10)

boutonpartie = Button(menu, text = 'Lancer partie',  font = ("Helvetica",15), bg = 'pink', relief = 'flat',command=lancerpartie)
boutonpartie.pack(pady =150)

menu.mainloop()
