def initGame(gridSize):
	global vy

	vy = []

	for i in range(gridSize):
		temp = []

		for e in range(gridSize):
			temp.append('')

		vy.append(temp)

	print(vy)

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
	vy[x][y] = player

	print(vy)
	