import random
from ga_template import *
from string import digits
from string import punctuation
from string import ascii_uppercase
from string import ascii_lowercase

class HelloWorldGA(GeneticAlgorithm):
	POPULATION = 100
	TARGET = "Speedify 8.0.2"
	DOMAIN_SPACE = []

	def setup(self):
		print("Setting Up")
		upper_case_list = list(set(ascii_uppercase))
		lower_case_list = list(set(ascii_lowercase))
		punctuation_list = list(set(punctuation))
		digits_list = list(set(digits))

		self.DOMAIN_SPACE = upper_case_list + lower_case_list + punctuation_list + digits_list + [' ']

	def cleanup(self):
		print("Clean up")

	def generate_initial_population(self):
		target_len = len(self.TARGET)
		fitness_obj_list = []
		for i in range(0, self.POPULATION):
			random_str = random.sample(self.DOMAIN_SPACE, target_len)
			fitness_obj = FitnessObject(''.join(random_str))
			fitness_obj_list.append(fitness_obj)
		
		return fitness_obj_list

	def compute_fitness(self, fitness_obj_list):
		target_len = len(self.TARGET)
		for fitness_obj in fitness_obj_list:
			match = 0
			for i in range(0, target_len):
				if fitness_obj.obj[i] == self.TARGET[i]:
					match = match + 1
			fitness_obj.fitness = match / target_len

		return fitness_obj_list

	def select_fittest(self, fitness_obj_list):
		fitness_obj_list.sort(key=lambda x: x.fitness, reverse=True)
		return fitness_obj_list[0:5]

	def crossover_and_mutate(self, fitness_obj_list):
		fitness_len = len(fitness_obj_list)
		crossover_array = []
		for i in range(0 , fitness_len):
			for j in range(i + 1, fitness_len):
				chromosome1 = fitness_obj_list[i]
				chromosome2 = fitness_obj_list[j]

				for k in range(0, 5):
					mutate_chromo = self.create_new_chromosome(chromosome1, chromosome2)				
					crossover_array.append(mutate_chromo)
					mutate_chromo = self.create_new_chromosome(chromosome2, chromosome1)				
					crossover_array.append(mutate_chromo)

		return crossover_array

	def create_new_chromosome(self, chromosome1, chromosome2):
		crossover = self.calc_crossover_point(chromosome1, chromosome2)
		crossover_chromo = chromosome1.obj[0:crossover] + chromosome2.obj[crossover:]
		assert len(chromosome1.obj) == len(crossover_chromo)
		mutate_chromo = self.mutate(crossover_chromo, chromosome1, chromosome2)
		return mutate_chromo

	def calc_crossover_point(self, chromosome1, chromosome2):
		if chromosome1.fitness == 0 or chromosome2.fitness == 0:
			return 0.5

		crossover = chromosome1.fitness / (chromosome1.fitness + chromosome2.fitness)
		return int(crossover * len(chromosome1.obj))

	def mutate(self, crossover_chromo, chromosome1, chromosome2):
		max_fitness = max(chromosome1.fitness, chromosome2.fitness)

		mutate_val = 0
		if max_fitness < 0.2:
			mutate_val = 5
		elif max_fitness < 0.4:
			mutate_val = 4
		elif max_fitness < 0.6:
			mutate_val = 3
		elif max_fitness < 0.8:
			mutate_val = 2
		else:
			mutate_val = 1

		for i in range(0, mutate_val):
			idx = random.randint(0, len(crossover_chromo) - 1)
			crossover_chromo = self.replacer(crossover_chromo, random.choice(self.DOMAIN_SPACE), idx)
			assert len(crossover_chromo) == len(self.TARGET)
		return FitnessObject(crossover_chromo)

	def replacer(self, s, newstring, index, nofail=False):
		if not nofail and index not in range(len(s)):
			raise ValueError("index outside given string")

		if index < 0:
			return newstring + s
		if index > len(s): 
			return s + newstring

		return s[:index] + newstring + s[index + 1:]
	
	def max_fitness_value(self):
		return 1


helloWorldGA = HelloWorldGA()
helloWorldGA.process()