from tkinter import *

import gameWindow, game

def mainMenu():
	# On crée la fenêtre que l'on utilisera pour afficher le jeu.
	mainMenuWindow = Tk()

	mainMenuWindow.title("MENU PRINCIPAL")

	jugarButton = Button(mainMenuWindow, text='Jouer', command=gameMenu)
	jugarButton.pack()

	rulesButton = Button(mainMenuWindow, text='Règles', command=showRules)
	rulesButton.pack()

	closeButton = Button(mainMenuWindow, text='Quitter', command=mainMenuWindow.destroy)
	closeButton.pack()

	# On crée un listener sur les clics et les entrées clavier sur la fenêtre.
	mainMenuWindow.mainloop()

def showRules():
	rulesWindow = Tk()

	rulesWindow.title("RÈGLES")

	closeButton = Button(rulesWindow, text='Quitter', command=rulesWindow.destroy)
	closeButton.pack()
	
	rulesWindow.mainloop()

def gameMenu():
	print("Lancement du jeu")
	gridSize = 12

	game.initGame(gridSize)
	gameWindow.initDamier(gridSize)