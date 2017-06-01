"""
Problem:
Given a drawer containing red socks and black socks:
	What is the minimum number of socks such that the probablity of drawing two
	red socks is 50%?
	What if the number of black socks is even?
"""

"""
Solution explaination:
Probability of drawing two red socks is the probability of drawing one multiplied by the 
probability of drawing another after that one has been removed.
"""
from functools import reduce 

class Histogram:
	def __init__(self, dict):
		self.dict = dict.copy()

	def probability(self, value):
		return self.dict[value]/sum(self.dict.values())

	def set(self, value, freq):
		self.dict[value] = freq

	def freq(self, value):
		return self.dict[value]

class PMF:
	def __init__(self, dict):
		self.dict = dict.copy()
		self.normalize()

	def normalize(self):
		sum = sum(self.dict.values())
		for k, v in self.dict:
			dict[k] = v/sum

	def probability(self, value):
		return self.dict[value]

def draw_probability(hist, list_of_values):
	probs = []
	list_of_values = list_of_values.copy()
	while len(list_of_values) > 0:
		value = list_of_values.pop()
		probs.append(hist.probability(value))
		hist.set(value, hist.freq(value) - 1)
	return reduce((lambda x,y: x*y), probs)
		
def find_draw_probability(constraint = lambda x: True):
	dict = {'red': 1, 'black': 1}
	target_prob = 0.5
	target_draw = ['red', 'red']
	while True:
		prob = draw_probability(Histogram(dict), target_draw)
		if prob < target_prob:
			dict['red'] = dict['red'] + 1
		elif prob > target_prob:
			dict['black'] = dict['black'] + 1
		elif constraint(dict):
			return dict
		else:
			dict['red'] = dict['red'] + 1

print(find_draw_probability())

print(find_draw_probability(lambda x: x['black'] % 2 == 0))

print(draw_probability(Histogram({'red':3,'black':1}), ['red','red']))

print(draw_probability(Histogram({'red':10,'black':4}), ['red', 'red']))
