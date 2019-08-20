class FitnessObject:
	def __init__(self, obj, fitness=0):
		self.obj = obj 
		self.fitness = fitness

class GeneticAlgorithm:
	def process(self):
		self.setup()
		fitness_obj_list = self.generate_initial_population()

		iterations = 0
		while True:
			fitness_obj_list = self.compute_fitness(fitness_obj_list)
			self.debug_fitness(iterations, fitness_obj_list)
			if self.should_terminate(fitness_obj_list) != None:
				break
			fitness_obj_list = self.select_fittest(fitness_obj_list)
			fitness_obj_list = self.crossover_and_mutate(fitness_obj_list)
			iterations = iterations + 1

		self.cleanup()

	# This is not an essential step, just finding a appropriate
	def setup(self):
		raise NotImplementedError

	def generate_initial_population(self):
		raise NotImplementedError

	def compute_fitness(self, fitness_obj_list):
		raise NotImplementedError

	def debug_fitness(self, iteration, fitness_obj_list):
		val = max(fitness_obj_list, key=lambda x: x.fitness)
		print("Iteration {0}, Maximum Fitness is: {1}, Population is {2}".format(iteration, val.fitness, val.obj))

	# Return None if doesn't exist yet
	def should_terminate(self, fitness_obj_list):
		val = max(fitness_obj_list, key=lambda x: x.fitness)
		if(val.fitness >= self.max_fitness_value()):
			print("Fitness is: {0}, Result is {1}".format(val.fitness, val.obj))
			return val 
		return None

	def max_fitness_value(self):
		raise NotImplementedError

	def select_fittest(self, fitness_obj_list):
		raise NotImplementedError

	def crossover_and_mutate(self, fitness_obj_list):
		raise NotImplementedError

	def cleanup(self):
		raise NotImplementedError