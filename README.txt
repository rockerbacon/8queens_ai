All the code presented was implemented for a college work at Universidade Federal Rural do Rio de Janeiro.
The objective was to implement an AI that could solve the 8 queens problem using hill climbing, simulated annealing and genetic algorithms.

Program call:
	python3 main.py <file containing initial state> HILL_CLIMBING <maximum number of sideway steps allowed>
		Recommended value for sideway steps: 3-5. The hill climbing algorithm will accept a solution that's as good as the one currently set as the best one using this value as the number of times it's allowed to do so.
	python3 main.py <file containing initial state> SIMULATED_ANNEALING <initial temperature> <cooling rate>
		Recommended values: <initial temperature> = 10-1000, <cooling rate> = 0.005-0.01
	python3 main.py GENETIC_ALGORITHM <population size> <reproduction rate> <mutation probability> <gamma k> <gamma theta>
		Recommended values: <population size> = 1000, <reproduction rate> = 0.5, <mutation probability> = 0.15, <gamma k> = 2, <gamma theta> = <population size>/(4 x <gamma k>)
		The values of k and theta determine who will be selected for reproduction and substitution. The recomended values will make so that, in general, the 25% best will reproduce and the 25% worst will be replaced (Average = k x theta). Smaller values of k increase the elitism, while smaller values get the distribution closer to a normal distribution

The file contains 8 integers where each represent the colum the queen in that line is
In case it's not possible to find a solution with the given initial state, the state is shuffled and the choses algorithm runs again using the shuffled state.