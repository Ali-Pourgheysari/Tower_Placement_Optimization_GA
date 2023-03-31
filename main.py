import numpy as np
import json

def main():
    # read the blocks_population into a matrix
    city_population_per_block = np.loadtxt('blocks_population.txt', delimiter=',', dtype=int)
    # read the problem_config to dictionary
    problem_config = dict()
    with open("problem_config.txt", "r") as f:
        problem_config = json.load(f)
    
    
    
if __name__ == "__main__":
    main()