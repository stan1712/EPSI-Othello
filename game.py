def initGame(gridSize):
	global vy

	vy = []

	for i in range(gridSize):
		temp = []

		for e in range(gridSize):
			temp.append('')

		vy.append(temp)

	print(vy)
