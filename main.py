from board import State
from hillClimbing import hillClimb
from simulatedAnnealing import simulateAnnealing
from geneticAlgorithm import geneticAlgorithm
import sys

# Program call:
# 	python3 main.py <file containing initial state> HILL_CLIMBING <maximum number of sideway steps allowed>
#		Recommended value for sideway steps: 3-5. The hill climbing algorithm will accept a solution that's as good as the one currently set as the best one using this value as the number of times it's allowed to do so.
#	python3 main.py <file containing initial state> SIMULATED_ANNEALING <initial temperature> <cooling rate>
# 		Recommended values: <initial temperature> = 10-1000, <cooling rate> = 0.005-0.01
#	python3 main.py GENETIC_ALGORITHM <population size> <reproduction rate> <mutation probability> <gamma k> <gamma theta>
#		Recommended values: <population size> = 1000, <reproduction rate> = 0.5, <mutation probability> = 0.15, <gamma k> = 2, <gamma theta> = <population size>/(4 x <gamma k>)
#		The values of k and theta determine who will be selected for reproduction and substitution. The recomended values will make so that, in general, the 25% best will reproduce and the 25% worst will be replaced (Average = k x theta). Smaller values of k increase the elitism, while smaller values get the distribution closer to a normal distribution
#
#
# The file contains 8 integers where each represent the colum the queen in that line is
#
# In case it's not possible to find a solution with the given initial state, the state is shuffled and the choses algorithm runs again using the shuffled state.
	
solution = State()
tries = 0
	
if sys.argv[2] == 'HILL_CLIMBING':
	solution.readFromFile( open(sys.argv[1], 'r') )
	solution.evaluate()
	sidewayLimit = int(sys.argv[3])
	
	while solution.value > 0:
		tries += 1
		solution = hillClimb(solution, sidewayLimit)
		
		if solution.value > 0:
			solution.randomize()
			solution.evaluate()
		
elif sys.argv[2] == 'SIMULATED_ANNEALING':
	solution.readFromFile( open(sys.argv[1], 'r') )
	solution.evaluate()
	temperature = float(sys.argv[3])
	coolingRate = float(sys.argv[4])
	
	while solution.value > 0:
		tries += 1
		solution = simulateAnnealing(solution, temperature, coolingRate)
		
		if solution.value > 0:
			solution.randomize()
			solution.evaluate()
			
elif sys.argv[1] == 'GENETIC_ALGORITHM':
	populationSize = int(sys.argv[2])
	reproductionRate = float(sys.argv[3])
	mutationProbability = float(sys.argv[4])
	gammaK = float(sys.argv[5])
	gammaTheta = float(sys.argv[6])
	
	solution.value = 1
	while solution.value > 0:
		tries += 1
		solution = geneticAlgorithm(populationSize, reproductionRate, mutationProbability, gammaK, gammaTheta, 1)
			
solution.printSelf()
print('Solution found after', tries, 'tries')
