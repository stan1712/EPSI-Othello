def initGame(gridSize):
	global vy
	global activePlayer

	global rounds
	global onGame

	onGame = True
	rounds = -3

	vy = []
	
	activePlayer = "B"

	for i in range(gridSize):
		temp = []

		for e in range(gridSize):
			temp.append('')

		vy.append(temp)

	print(vy)

def stateGame():
	compteurB = 0
	compteurN = 0

	if(rounds > 4):
		for i in vy:
			for e in i:
				if(e == "B"):
					compteurB = compteurB + 1
				if(e == "N"):
					compteurN = compteurN + 1

		if(compteurB == 0):
			sayEndGame("N", compteurN)
		if(compteurN == 0):
			sayEndGame("B", compteurB)
		
def sayEndGame(whoWon, count):
	global onGame
	
	print("Fin de partie !")

	if(whoWon == "B"):
		winner = "Blancs"
	elif(whoWon == "N"):
		winner = "Noirs"
	
	print("Les " + winner + " ont gagnes avec " + str(count) + " pions !")

	onGame = False

def isGameOn():
	return onGame

def checkPosition(x, y):
	x = x - 1
	y = y - 1

	# dégager le 8 constant pour mettre gridSize
	if(x > 8): 
		return "ERROR X : (" + str(x) + ";" + str(y) + ")"
	if(y > 8): 
		return "ERROR Y : (" + str(x) + ";" + str(y) + ")"

	if(vy[x][y]):
		return vy[x][y]
	else:
		return False

def logSign(player, x, y):
	global rounds

	vy[x][y] = player

	stateGame()

	if(rounds > 0):
		print("---\nTour numero " + str(rounds) + " :")

	rounds = rounds + 1

def whosTurn():
	return activePlayer

def nextTurn():
	global activePlayer

	if(activePlayer == "B"):
		activePlayer = "N"
	elif(activePlayer == "N"):
		activePlayer = "B"

	return whosTurn()