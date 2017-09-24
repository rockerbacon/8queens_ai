from board import State

def hillClimb (initialState, sidewayMovesLimit):

	sidewayLimit = sidewayMovesLimit

	initialState.evaluate()
	currentState = initialState

	bestState = currentState
	while (True):
	
		#currentState.printSelf()	#debug
	
		#encontrar melhor estado a partir de estado atual
		for i in range(len(initialState.queen)):
			for j in range(8):
				if j != currentState.queen[i]:
			
					#determinar estado a partir do estado atual
					neighbour = currentState.copy()
					neighbour.moveQueen(i, j)
					neighbour.evaluate()
				
					if neighbour.value <= bestState.value:
						bestState = neighbour				
										
		if bestState is currentState or bestState.value > currentState.value or (bestState.value == currentState.value and sidewayLimit <= 0):
			return currentState
		else:
			currentState = bestState
			if bestState.value == currentState.value:
				sidewayLimit -= 1
