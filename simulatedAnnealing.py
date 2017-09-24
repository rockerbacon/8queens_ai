from board import State
from random import randrange, random
from math import exp, sqrt
import math

def simulateAnnealing (initialState, initialTemperature, coolingRate):

	initialState.evaluate()
	currentState = initialState

	bestState = currentState
	temperature = initialTemperature
	cool = 1-coolingRate
	while (temperature > 0.000001 and bestState.value != 0):
	
		#currentState.printSelf()	#debug
	
		#determinar estado aleatorio a partir de estado atual
		randI = randrange(0, 8)
		randJ = randrange(0, 8)
		#se estado escolhido eh estado atual gerar novo estado
		while randJ == currentState.queen[randI]:
			randI = randrange(0, 8)
			randJ = randrange(0, 8)
			
		nextState = currentState.copy()
		nextState.moveQueen(randI, randJ)
		nextState.evaluate()	
		
		deltaE = currentState.value-nextState.value
		chance = random()
		try:
			probability = exp(deltaE/temperature)
		except OverflowError:
			probability = float('inf')	
		
		#print (chance, probability, currentState.value, nextState.value, bestState.value) #debug
			
		if deltaE > 0:
			currentState = nextState
			if nextState.value < bestState.value:
				#print ('new best state')	#debug
				bestState = nextState
		elif chance < probability:
			#print('state accepted')	#debug
			currentState = nextState
			
		temperature = temperature*cool
		
	return bestState
