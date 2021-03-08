from tkinter import *

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

"""
def addSign(canvas, type, x0, y0, x1, y1):
	if(type == "croix"):
		canvas.createLine
	else {

	}
"""

def initDamier(board_size):
	canvas_size = cell_size * board_size
	
	colors = ["grey", "white"]
	
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

	canvas.create_line(3 * cell_size, 3 * cell_size, 4 * cell_size, 4 * cell_size, fill="red", width="2")

	gameWindow.mainloop()