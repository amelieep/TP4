# JEU DE CASSE BRIQUE

Voici un jeu de casse brique développé en python (programmation orientée objet) avec la bibliotheque graphique Tkinter.

[repertoir git](https://github.com/amelieep/TP4.git)

## Règles du jeu :

    - OBJECTIF : faire rebondir la balle sur une raquette afin qu'elle detruise toutes les briques. Attentiona ne pas la laisser tomber en bas de l'écran
    - VIE ET SCORE : vous démarez la partie avec 4 vies que vous pouvez perdre en laissant tomber la balle. Chaque brique détruite rapporte 10 points
    - COMMANDES : sur votre clavier, utiliser la fleche droite pour déplacer la raquette à droite et la flèche gauche pour la deplacer à gauche. 

## structure du projet :

En ouvrant le dossier TP4, vous trouverez un fichier "main" afin de lancer le jeu et contenant certaines informations notament ce qu'il reste a faire. 
Un fichier principal "cassebrique" gère le menu principal et le lancement d'une partie. 
Le dossier "objetsjeu" contient les différents objets du jeu : 
        "briques" -> gère la grille de briques et la liste de briques resatantes.
        "balle"   -> gère la création de la balle, ses mouvement, les rebonds et les interactions avec les autres objets.
        "raquette"-> gère la création de la raquette, ses déplacempents.





