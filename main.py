import numpy as np
import json

class evlolutionary_algorithm:
    def __init__(self, city_population_per_block, problem_config, tower_place):
        self.city_population_per_block = city_population_per_block
        self.problem_config = problem_config
        self.tower_place = tower_place

    def evaluate(self):
        # get 2 parents from the population

    def selection(self):
        pass

    def crossover(self):
        pass

    def mutation(self):
        pass

    def run(self):
        pass


def main():
    # read the blocks_population into a matrix
    city_population_per_block = np.loadtxt('blocks_population.txt', delimiter=',', dtype=int)
    # read the problem_config to dictionary
    with open("problem_config.txt", "r") as f:
        problem_config = json.load(f)
    # read initial_population.txt containing (x,y) pairs to a list of 2d vectors
    with open('initial_population.txt', 'r') as f:
        data = [line.strip() for line in f]
        tower_place = [tuple(map(float, line.split(','))) for line in data]
    
    # create an instance of the evolutionary algorithm
    ea = evlolutionary_algorithm(city_population_per_block, problem_config, tower_place)
    
if __name__ == "__main__":
    main()