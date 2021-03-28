# Fonction d'initialisation du jeu
def initGame(gridSize):
	# On va définir des variables et constantes pour le déroulé du jeu
	global vy
	global activePlayer

	global rounds
	global onGame

	onGame = True
	rounds = -3
	
	activePlayer = "B"

	# On construit la grille
	vy = []

	for i in range(gridSize):
		temp = []

		for e in range(gridSize):
			temp.append('')

		vy.append(temp)

# Fonction de vérification du statut de la partie
def stateGame():
	compteurB = 0
	compteurN = 0

	if(rounds > 0):
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

# Fonction pour annoncer et terminer la partie
def sayEndGame(whoWon, count):
	global onGame
	
	print("-*-*-\nFin de partie !")

	# On définit qui est le gagnant...
	if(whoWon == "B"):
		winner = "Blancs"
	elif(whoWon == "N"):
		winner = "Noirs"
	
	# ... et on l'affiche
	print("Les " + winner + " ont gagnes avec " + str(count) + " pions !\n-*-*-")

	onGame = False

# Fonction de vérification de l'état de la partie (en cours ou terminée)
def isGameOn():
	return onGame

# Fonction qui permet de valider ou non un mouvement
def isMoveValid(player, x, y):
	x = x - 1
	y = y - 1

	# Selon les règles de l'Othello, le premier mouvement fonctionne différemment des autres, donc selon le nombre de tours actuels, les règles de mouvements ne s'appliquent pas pareil
	if(rounds == 1):
		if(vy[x + 1][y] == player): return True
		elif(vy[x][y + 1] == player): return True

		elif(vy[x - 1][y] == player): return True
		elif(vy[x][y - 1] == player): return True

		else: return False
	elif(rounds > 1):
		if(vy[x + 1][y] == whoIsNext()): return True
		elif(vy[x][y + 1] == whoIsNext()): return True

		elif(vy[x - 1][y] == whoIsNext()): return True
		elif(vy[x][y - 1] == whoIsNext()): return True
		
		elif(vy[x + 1][y + 1] == whoIsNext()): return True
		elif(vy[x - 1][y - 1] == whoIsNext()): return True

		else: return False
	else: return True

# Fonction qui permet de vérifier un mouvement
def checkPosition(x, y):
	x = x - 1
	y = y - 1

	# Si les coordonnées sont plus grandes que la taille de la grille, alors on annule le coup et on retourne une erreur
	if(x > 8): 
		return "ERROR X : (" + str(x) + ";" + str(y) + ")"
	if(y > 8): 
		return "ERROR Y : (" + str(x) + ";" + str(y) + ")"

	# Si un pion existe déjà aux coordonnées, on retourne le pion existant
	if(vy[x][y]):
		return vy[x][y]
	else:
		return False

# Piste d'amélioration: Fonction qui permet de retourner les pions si besoin
def checkCrossing(player, x, y):
	"""
	(x,y) : x, y
	S : player
	S2 : whoIsNext()
	"""
	counterTO = []

# Fonction qui permet de jouer un tour
def logSign(player, x, y):
	global rounds

	# On inscrit le pion du joueur dans notre tableau
	vy[x][y] = player

	stateGame()
	#checkCrossing(player, x, y)

	# On affiche le numéro de tour, puis on passe au tour suivant
	if(rounds > 0):
		print("---\nTour numero " + str(rounds) + " :")

	rounds = rounds + 1
				
	nextTurn()

# Fonction qui retourne le joueur actuel (B ou N)
def whosTurn():
	return activePlayer

# Fonction qui retourne le joueur suivant (B ou N)
def whoIsNext():
	if(activePlayer == "B"):
		return "N"
	elif(activePlayer == "N"):
		return "B"

# Fonction qui permets d'afficher le joueur suivant
def nextTurn():
	global activePlayer

	if(activePlayer == "B"):
		activePlayer = "N"
	elif(activePlayer == "N"):
		activePlayer = "B"

	print("C'est au tour de " + whosTurn() + " de jouer.")

	return whosTurn()