from tkinter import *
import tkinter.font as font

import gameWindow, game

def mainMenu():
	# On crée la fenêtre que l'on utilisera pour afficher le jeu.
	mainMenuWindow = Tk()

	mainMenuWindow.title("MENU PRINCIPAL")
	mainMenuWindow.geometry('400x300')
	mainMenuWindow.configure(bg='#02bd88')

	buttonPlacement = Label(mainMenuWindow)
	buttonPlacement.configure(bg='#02bd88')
	buttonPlacement.pack()

	f = font.Font(weight='bold', size=15)
	jugarButton = Button(buttonPlacement, text='Jouer',height=2, width=10, fg='black', bg='#009067', command=gameMenu)
	jugarButton['font'] = f
	jugarButton.pack(side=LEFT, padx=20, pady=(80,10))

	rulesButton = Button(buttonPlacement, text='Règles',height=2, width=10, fg='black', bg='#009067', command=showRules)

	rulesButton.pack(side=RIGHT, padx=20, pady=(80,10))
	rulesButton['font'] = f
	closeButton = Button(mainMenuWindow, text='Quitter', fg='red', bg='#009067', command=mainMenuWindow.destroy)
	closeButton.pack(side=BOTTOM,fill=X, ipady=10, padx=10, pady=10)

	# On crée un listener sur les clics et les entrées clavier sur la fenêtre.
	mainMenuWindow.mainloop()

def showRules():
	rulesWindow = Tk()

	rulesWindow.title("RÈGLES")
	rulesWindow.geometry('700x350')
	rulesWindow.configure(bg='#02bd88')

	ft = font.Font(size=8, weight='bold')

	title = Label(rulesWindow, text='Règles', bg='#02bd88')
	title['font'] = ft
	title.pack(pady=(15,0))
	
	rules = Label(rulesWindow, text='Le but du jeu est d\'avoir plus de pions de sa couleur que les autres joueurs à la fin de la partie.\n'
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
	closeButton.pack(side=BOTTOM,fill=X, ipady=10, padx=10, pady=10)

	
	rulesWindow.mainloop()

def gameMenu():
	print("Lancement du jeu")
	gridSize = 8

	game.initGame(gridSize)
	gameWindow.initDamier(gridSize)