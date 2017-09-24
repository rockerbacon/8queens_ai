from random import randrange

class State:
	def __init__(self):
		self.queen = [0 for i in range(8)]
		self.value = 0
		
	def randomize(self):
		self.queen = [randrange(8) for i in range(8)]
		return self
		
	def readFromFile(self, f):
		fline = f.read().split(' ')
		self.queen = [int(fline[i]) for i in range(8)];
		
	def moveQueen (self, line, colum):
		self.queen[line] = colum
		
	def copy(self):
		copy = State()
		copy.queen = [x for x in self.queen]
		copy.value = self.value
		return copy
		
	def evaluate(self):
		self.value = 0
		stop = len(self.queen)
	
		for i in range(stop):
			for j in range(i+1, stop):
				if self.queen[i] == self.queen[j]:
					self.value += 1
				elif abs(i-j) == abs(self.queen[i]-self.queen[j]):
					self.value += 1
					
	def printSelf(self):
		queenChar = 'w'
		emptyChar = '0'
		
		for i in range(len(self.queen)):
			for j in range(8):
				if j == self.queen[i]:
					print ("\033[32m", queenChar, end=' ')
				else:
					print ("\033[90m", emptyChar, end=' ')
			print(end='\n')
		
		print('\033[1;37mAttacking pairs =', self.value, end='\n')		
