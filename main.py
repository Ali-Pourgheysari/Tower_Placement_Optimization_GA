import numpy as np
import json

def main():
    # read the blocks_population into a matrix
    city_population_per_block = np.loadtxt('blocks_population.txt', delimiter=',', dtype=int)
    # read the problem_config to dictionary
    problem_config = dict()
    with open("problem_config.txt", "r") as f:
        problem_config = json.load(f)
    # read initial_population.txt containing (x,y) pairs to a list of 2d vectors
    initial_population = list()
    with open('initial_population.txt', 'r') as f:
        data = [line.strip() for line in f]
        points = [tuple(map(float, line.split(','))) for line in data]
        n = 4
        

    
    
if __name__ == "__main__":
    main()