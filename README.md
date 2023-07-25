# Genetic Algorithm for Tower Placement Optimization
This repository contains Python code that implements a genetic algorithm to optimize the placement of communication towers in a city. The goal of this optimization is to maximize user satisfaction while minimizing the total cost of tower construction and maintenance.

## Requirements
To run the code, you will need the following libraries:

* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)

## Usage
1. Clone this repository to your local machine.
2. Make sure you have the required libraries installed using:
```bash
pip install numpy matplotlib
```
3. Run the code in the `main.ipynb` notebook.

## Description
`main.ipynb`
This script contains the main code for the genetic algorithm. It defines the following functions:

1. `crossover(parent1, parent2)`: Performs crossover between two parent cities to create two child cities.

2. `mutation(child)`: Introduces random mutations to a child city.

3. `selection(population, limit=50)`: Selects the best cities from the population based on their fitness scores.

4. `genetic_algorithm(max_generation=200, population=50, mutation_rate=0.1, crossover_rate=0.9)`: Implements the genetic algorithm to optimize tower placement.

5. `output(generation, j)`: Writes the results of each generation to a text file.

The script runs the genetic algorithm with different sets of parameters and saves the results to text files. It also generates fitness plots for each set of parameters.

`utils.py`
This script contains utility classes and functions required for tower placement optimization. It defines the following classes:

1. `City`: Represents a city with towers and blocks. It calculates fitness scores, user satisfaction, and bandwidth for each block and tower.

2. `Block`: Represents a block in the city with its position, connected tower, population, and bandwidth.

3. `Tower`: Represents a communication tower with its position and bandwidth capacity.

## Data Input
The genetic algorithm requires two input files:

1. `blocks_population.txt`: Contains the population data for each block in the city.

2. `problem_config.txt`: Contains configuration data for the problem, including tower construction cost, maintenance cost, user satisfaction levels, and corresponding satisfaction scores.

Make sure to provide the appropriate data in these files before running the algorithm.

## Output
The output of the genetic algorithm is saved in text files named `generationX.txt`, where X represents the generation number. Each output file contains the following information for each generation:

* The number of towers in the city.
* Tower positions and their bandwidth capacity.
* The assignment of blocks to towers and their respective positions.
Additionally, the script generates fitness plots showing the fitness score for each generation with different sets of parameters.

## Disclaimer
The genetic algorithm implemented in this code is meant for educational and illustrative purposes. It may not be optimized for large-scale real-world applications. The input data and parameters used for optimization should be adjusted according to specific use cases and problem requirements.

Read the complete documentation [here](Documentation.pdf)

Please note that the provided code may have room for improvements and optimization. Feel free to modify and adapt it to suit your needs.

Happy optimizing!
