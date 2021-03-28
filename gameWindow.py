# On importe les librairies Math et tkinter (interface et fonctions mathématiques)
from tkinter import *
import math as Math

# On import nos librairies game et windows (gestion de jeu et d'interface)
import game, windows

cell_size = 50

# Fonction qui vérifie et place (ou rejete) un pion
def addSign(canvas, type, x0, y0):
	# Si le jeu est en cours (True ou False)
	if(game.isGameOn()):
		# Si le mouvement est dans la taille de la grille et pas pris par un autre pion
		if(game.checkPosition(x0, y0) == False):
			# Si le mouvement est valide
			if(game.isMoveValid(type, x0, y0)):
				x0 = (x0 - 1)
				y0 = (y0 - 1)

				whiteFill = "WHITE"
				blackFill = "BLACK"

				width = "2"
				
				# On dessin un rond pour le joueur blanc ou noir
				if(type == "N"):
					canvas.create_oval(x0 * cell_size + 5, y0 * cell_size + 5, (x0 + 1) * cell_size - 5, (y0 + 1) * cell_size - 5, outline=blackFill, fill=blackFill, width=width)
				elif (type == "B"): {
					canvas.create_oval(x0 * cell_size + 5, y0 * cell_size + 5, (x0 + 1) * cell_size - 5, (y0 + 1) * cell_size - 5, outline=whiteFill, fill=whiteFill, width=width)
				}

				game.logSign(type, x0, y0)

				# On affiche le bon placement du pion
				print("Pion " + game.whosTurn() + " place en (" + str(x0) + ";" + str(y0) + ")")
			else:
				# On demande au joueur de rejouer son coup
				print("---\nCoup non valide, merci de rejouer")

		# Si les coordonnées sont déjà prises par un pion, on affiche par qui et le joueur devra rejouer son coup
		elif(game.checkPosition(x0, y0) == "B"):
			print("---\nCoup non valide : Deja pion blanc en (" + str(x0) + ";" + str(y0) + ")")
		elif(game.checkPosition(x0, y0) == "N"):
			print("---\nCoup non valide : Deja pion noir en (" + str(x0) + ";" + str(y0) + ")")
		else:
			print("Placement invalide")

# On initie/construit le damier dans notre interface de jeu
def initDamier(board_size):
	canvas_size = cell_size * board_size
	
	colors = ["#009067", "#02bd88"]
	
	gameWindow = Tk()
	gameWindow.title("Othello")
	gameWindow.configure(bg='grey')
	
	canvas = Canvas(gameWindow, width=canvas_size, height=canvas_size)

	# On définit et execute la fonction de placement d'un pion, lorsqu'un clic gauche est émis
	def coordinates(event):
		addSign(canvas, game.whosTurn(), Math.floor(event.x / cell_size) + 1, Math.floor(event.y / cell_size) + 1)

	canvas.bind("<Button-1>", coordinates)

	canvas.pack()
	
	for x in range(board_size):
		for y in range(board_size):
			color = colors[(x + y) % 2]
			canvas.create_rectangle(
				y * cell_size,
				x * cell_size,
				y * cell_size + cell_size,
				x * cell_size + cell_size,
				fill=color, outline=color
			)
	
	# On ajoute des boutons de navigation pour quitter et accéder aux règles
	closeButton = Button(gameWindow, text='Quitter', fg='red', bg='#009067', command=gameWindow.destroy)	
	closeButton.pack(side=BOTTOM, fill=X, ipady=10, padx=10, pady=10)

	rulesButton = Button(gameWindow, text='Règles', fg='red', bg='#009067', command=windows.showRules)
	rulesButton.pack(side=BOTTOM, fill=X, ipady=10, padx=10, pady=10)

	# On joue les 4 premiers tours pour poser les pions centraux
	addSign(canvas, game.whosTurn(), 4, 4)
	addSign(canvas, game.whosTurn(), 4, 5)
	addSign(canvas, game.whosTurn(), 5, 5)
	addSign(canvas, game.whosTurn(), 5, 4)

	gameWindow.mainloop()