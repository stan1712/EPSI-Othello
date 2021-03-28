# On importe la librairie  tkinter (interface)
from tkinter import *
import tkinter.font as font

# On import nos librairies gameWindow et game (gestion de jeu et d'interface)
import gameWindow, game

# On crée la fenêtre principale qui nous permettra de se déplacer entre les règles et la fenêtre de jeu.
def mainMenu():
	mainMenuWindow = Tk()

	mainMenuWindow.title("MENU PRINCIPAL") # On définie le titre de notre fenêtre.
	mainMenuWindow.geometry('400x300') # On définie la taille de notre fenêtre.
	mainMenuWindow.configure(bg='#02bd88') # On définie la couleur du background de notre fenêtre.

	buttonPlacement = Label(mainMenuWindow) # Nous créons une zone pour pouvoir placer nos boutons.
	buttonPlacement.configure(bg='#02bd88')
	buttonPlacement.pack()

	f = font.Font(weight='bold', size=15) # Cette ligne nous permet de mettre en gras et d'ajuster la taille de notre widget
	jugarButton = Button(buttonPlacement, text='Jouer',height=2, width=10, fg='black', bg='#009067', command=gameMenu) # Création d'un bouton qui une fois cliqué, appelera la fonction gameMenu().
	jugarButton['font'] = f
	jugarButton.pack(side=LEFT, padx=20, pady=(80,10)) # Placement du bouton jugarButton dans la zone de placement buttonPlacement.

	rulesButton = Button(buttonPlacement, text='Règles',height=2, width=10, fg='black', bg='#009067', command=showRules) # Création du bouton "Règles".
	rulesButton.pack(side=RIGHT, padx=20, pady=(80,10))
	rulesButton['font'] = f

	closeButton = Button(mainMenuWindow, text='Quitter', fg='red', bg='#009067', command=mainMenuWindow.destroy) # Création du bouton "Quitter".
	closeButton.pack(side=BOTTOM, fill=X, ipady=10, padx=10, pady=10) # Placement du boutton "Quitter" avec un padding de 10.

	# On crée un listener sur les clics et les entrées clavier sur la fenêtre.
	mainMenuWindow.mainloop()

# On crée la fenêtre qui nous permettra de lire les règles du jeu.
def showRules():
	rulesWindow = Tk() 

	rulesWindow.title("RÈGLES")
	rulesWindow.geometry('700x350')
	rulesWindow.configure(bg='#02bd88')

	ft = font.Font(size=8, weight='bold')

	title = Label(rulesWindow, text='Règles', bg='#02bd88')
	title['font'] = ft
	title.pack(pady=(15,0))

	rules = Label(rulesWindow, text='Le but du jeu est d\'avoir plus de pions de sa couleur que les autres joueurs à la fin de la partie.\n' # Création d'un paragraphe qui affiche les règles du jeu.
									'La partie se termine lorsque plus aucun des joueurs ne peut jouer.\n'
									'C\'est à dire, quand plus personne ne peux joué de coup légalement.\n'
									'Cela peut signifier que la grille est remplie.\n'
									'Un déplacement consiste à placer un jeton sur une case vide.\n'
									'Si vous ne pouvez pas capturer de pièces adverses, vous êtes forcés de passer votre tour.\n'
									'Si aucun des joueurs ne peut jouer, la partie est alors terminée.\n'
									'Le joueur ayant le plus de pièces remporte la partie.\n'
									'Vous pouvez capturer des lignes de jetons horizontales, verticales, et en diagonale.\n'
									'Vous pouvez également capturer plus d\'une ligne à la fois.\n',
									fg='white',
									bg='#02bd88')
	rules['font'] = ft
	rules.pack(pady=(10,10))
	
	closeButton = Button(rulesWindow, text='Quitter', fg='red', bg='#009067', command=rulesWindow.destroy)
	closeButton.pack(side=BOTTOM, fill=X, ipady=10, padx=10, pady=10)


	rulesWindow.mainloop()

# On crée la fenêtre que l'on utilisera pour afficher le jeu.
def gameMenu():
	print("Lancement du jeu")
	gridSize = 8

	game.initGame(gridSize)
	gameWindow.initDamier(gridSize) 

# Piste d'amélioration: Création d'une page qui demandera à l'utilisateur la taille du plateau de jeu.
def gridSize():
	gridSize = Tk()

	gridSize.title("TAILLE DU PLATEAU")
	gridSize.geometry('400x300')
	gridSize.configure(bg='#02bd88')


	f = font.Font(size=5)
	title = Label(gridSize, text='Veuillez indiquez la taille du plateau :', bg='#02bd88')
	title['font'] = f
	title.pack(pady=(20,0))

	getSize = Entry(gridSize)
	getSize.pack(pady=(10,0))	

	closeButton = Button(gridSize, text='Quitter', fg='red', bg='#009067', command=gridSize.destroy)
	closeButton.pack(side=BOTTOM, fill=X, ipady=10, padx=10, pady=10)

	jugarButton = Button(gridSize, text='Jouer', fg='black', bg='#009067', command=lambda:[gridSize.destroy(), gameMenu()])
	jugarButton.pack(side=BOTTOM, fill=X, ipady=10, padx=10, pady=10)
