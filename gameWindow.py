from tkinter import *
import math as Math
import game, windows

cell_size = 50

def addSign(canvas, type, x0, y0):
	if(game.isGameOn()):
		if(game.checkPosition(x0, y0) == False):
			if(game.isMoveValid(type, x0, y0)):
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

				print("Pion " + game.whosTurn() + " place en (" + str(x0) + ";" + str(y0) + ")")
				
				game.nextTurn()
			else:
				print("---\nCoup non valide, merci de rejouer")

		elif(game.checkPosition(x0, y0) == "B"):
			print("---\nCoup non valide : Deja pion blanc en (" + str(x0) + ";" + str(y0) + ")")
		elif(game.checkPosition(x0, y0) == "N"):
			print("---\nCoup non valide : Deja pion noir en (" + str(x0) + ";" + str(y0) + ")")
		else:
			print("Placement invalide")

def initDamier(board_size):
	canvas_size = cell_size * board_size
	
	#colors = ["#2D1E2F", "#3A3657"]
	colors = ["#009067", "#02bd88"]
	
	gameWindow = Tk()
	gameWindow.title("Othello")
	gameWindow.configure(bg='grey')
	
	canvas = Canvas(gameWindow, width=canvas_size, height=canvas_size)

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
	

	closeButton = Button(gameWindow, text='Quitter', fg='red', bg='#009067', command=gameWindow.destroy)	
	closeButton.pack(side=BOTTOM, fill=X, ipady=10, padx=10, pady=10)

	rulesButton = Button(gameWindow, text='Règles', fg='red', bg='#009067', command=windows.showRules)
	rulesButton.pack(side=BOTTOM, fill=X, ipady=10, padx=10, pady=10)

	addSign(canvas, game.whosTurn(), 4, 4)

	addSign(canvas, game.whosTurn(), 4, 5)

	addSign(canvas, game.whosTurn(), 5, 5)

	addSign(canvas, game.whosTurn(), 5, 4)

	gameWindow.mainloop()