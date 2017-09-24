from board import State
from time import time
from random import gammavariate, gauss, random, randrange

def mean (l):
	total = 0
	for i in l:
		total += i.value
	return total/len(l)	

# gera novos estados
def reproducePopulation (population, numberOfReproductions, mutationProbability, gammaK, gammaTheta):
	populationSize = len(population)
	
	while numberOfReproductions > 0:
		# escolher pais utilizando distribuicao gamma
		fatherIndex = int(gammavariate(gammaK, gammaTheta)) % populationSize
		motherIndex = fatherIndex
		while motherIndex == fatherIndex:
			motherIndex = int(gammavariate(gammaK, gammaTheta)) % populationSize
		father = population[fatherIndex]
		mother = population[fatherIndex]
		
		# determinar qual o pai mais forte
		if father.value < mother.value:
			stronger = father
			weaker = mother
		else:
			stronger = mother
			weaker = father
			
		# quanto mais forte o pai mais cromossomos passa, pais fracos (valor > 8) passam em media metade dos cromossomos
		separationRandomization = gammavariate( stronger.value % 8 + 1 , 1/2 )
		separationIndex = int(round(separationRandomization)) % 4 + 1
		
		# chance de swap de maneira que ambos extremos dos cromossomos do mais forte possam ser passados
		if random() < 0.5:
			stronger, weaker = weaker, stronger
			separationIndex = 8 - separationIndex
			
		# gera filho	
		child = State()
		i = 0
		while i < separationIndex:
			child.queen[i] = stronger.queen[i]
			i += 1
		while i < 8:
			child.queen[i] = weaker.queen[i]
			i += 1
		# mutacao
		if random() < mutationProbability:
			child.queen[randrange(8)] = randrange(8)
				
		child.evaluate()	
			
		# filho eh inserido na populacao no lugar de alguem escolhido de acordo com uma distribuicao gamma
		replaceIndex = populationSize - int(gammavariate(gammaK, gammaTheta)) % populationSize - 1
		#print(populationSize, replaceIndex)	#debug
		population.pop(replaceIndex)
		population.insert(0, child)
			
		numberOfReproductions -= 1	
			

def geneticAlgorithm (populationSize, reproductionRate, mutationProbability, gammaK, gammaTheta, timeLimitInSeconds):

	initialTime = time()
	
	population = [State().randomize() for i in range(populationSize)]
	populationReproductions = int(populationSize*reproductionRate)

	for state in population:
		state.evaluate()
	population.sort(key=lambda state: state.value)
	bestState = population[0]
	print('Best =', bestState.value, end='\n')
	print('Mean =', mean(population), end='\n')
	
	while population[0].value > 0 and time()-initialTime < timeLimitInSeconds:

		reproducePopulation(population, populationReproductions, mutationProbability, gammaK, gammaTheta)
		
		population.sort(key=lambda state: state.value)
		if population[0].value < bestState.value:
			bestState = population[0]
			
		print('\033[2ABest =', bestState.value, '\nMean =', mean(population), end='\n')	
			
	return bestState		
			

