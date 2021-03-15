from tkinter import *
import game

cell_size = 50

def initWindow():
	# On crée la fenêtre que l'on utilisera pour afficher le jeu.
	gameWindow = Tk()

	# On crée nos éléments pour les incorporer à notre fenêtre.
	Text1 = Label(gameWindow, text='coucou', fg='red')
	Text1.pack()

	closeButton = Button(gameWindow, text='iodjsf', command=gameWindow.destroy)
	closeButton.pack()

	# On crée un listener sur les clics et les entrées clavier sur la fenêtre.
	gameWindow.mainloop()

def addSign(canvas, type, x0, y0):
	if(game.checkPosition(x0, y0) == False):
		x0 = (x0 - 1)
		y0 = (y0 - 1)

		whiteFill = "WHITE"
		blackFill = "BLACK"

		width = "2"
		
		if(type == "N"):
			"canvas.create_line(x0 * cell_size + 10, y0 * cell_size + 10, (x0 + 1) * cell_size - 10, (y0 + 1) * cell_size - 10, fill=fill, width=width)"
			"canvas.create_line((x0 + 1) * cell_size - 10, y0 * cell_size + 10, ((x0 + 1) - 1) * cell_size + 10, (y0 + 1) * cell_size - 10, fill=fill, width=width)"
			
			canvas.create_oval(x0 * cell_size + 5, y0 * cell_size + 5, (x0 + 1) * cell_size - 5, (y0 + 1) * cell_size - 5, outline=blackFill, fill=blackFill, width=width)
		elif (type == "B"): {
			canvas.create_oval(x0 * cell_size + 5, y0 * cell_size + 5, (x0 + 1) * cell_size - 5, (y0 + 1) * cell_size - 5, outline=whiteFill, fill=whiteFill, width=width)
		}

		game.logSign(type, x0, y0)

		print("Pion place en (" + str(x0) + ";" + str(y0) + ")")
	elif(game.checkPosition(x0, y0) == "B"):
		print("Deja blancs en (" + str(x0) + ";" + str(y0) + ")")
	elif(game.checkPosition(x0, y0) == "N"):
		print("Deja noirs en (" + str(x0) + ";" + str(y0) + ")")
	else:
		print("Placement invalide")

def initDamier(board_size):
	canvas_size = cell_size * board_size
	
	#colors = ["#2D1E2F", "#3A3657"]
	colors = ["#009067", "#02bd88"]
	
	gameWindow = Tk()
	gameWindow.title("Othello")
	
	canvas = Canvas(gameWindow, width=canvas_size, height=canvas_size)
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
	
	closeButton = Button(gameWindow, text='Quitter', command=gameWindow.destroy)
	closeButton.pack()

	addSign(canvas, "B", 4, 4)
	addSign(canvas, "B", 5, 5)

	addSign(canvas, "N", 4, 5)
	addSign(canvas, "N", 5, 4)

	gameWindow.mainloop()