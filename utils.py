import json
import random
import numpy as np

class City:
    def __init__(self, towers=[], is_new=True, is_child=False):
        self.tower_construction_cost = 0
        self.size = 20
        self.tower_maintenance_cost = 0
        self.towers = []
        self.total_tower_cost = 0
        self.fitness_score = 0
        self.user_satisfaction_levels = None
        self.total_satisfaction_score = 0
        self.user_satisfaction_scores = None
        self.is_new = True
        self.is_child = is_child
        self.blocks = self.init_blocks()
        self.read_blocks_population_from_file(r'blocks_population.txt')
        self.read_problem_config(r'problem_config.txt')
        if not is_child:
            self.initialize_towers()

    def init_blocks(self):
        array = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(Block())
            array.append(row)

        return np.array(array)

    def read_problem_config(self, path):
        with open(path) as file:
            json_data = json.loads(file.read())
        self.tower_construction_cost = json_data['tower_construction_cost']
        self.tower_maintenance_cost = json_data['tower_maintanance_cost']
        self.user_satisfaction_levels = json_data['user_satisfaction_levels']
        self.user_satisfaction_scores = json_data['user_satisfaction_scores']

    def read_blocks_population_from_file(self, path):
        i = 0
        with open(path, 'r') as file:
            for line in file:
                x = line.split(',')
                for j in range(len(self.blocks)):
                    self.blocks[i][j].position = np.array([i, j])
                    self.blocks[i][j].population = int(x[j])
                i += 1

    def initialize_towers(self):
        for i in range(np.random.randint(1, 400)):
            random_tower = Tower([random.uniform(0, 19), random.uniform(0, 19)], random.randint(1, 10000))
            self.towers.append(random_tower)

    # allocate towers and blocks randomly
    def random_allocation(self):
        for x in range(self.size):
            for y in range(self.size):
                # allocate towers to blocks
                self.blocks[x][y].connected_tower = self.towers[random.randint(0, len(self.towers) - 1)]
                # allocate blocks to towers
                self.blocks[x][y].connected_tower.connected_population += self.blocks[x][y].population

    # calculate the BandWidth of a single block
    def cal_BW_bx(self):
        for x in range(self.size):
            for y in range(self.size):
                # sigma which is used in cov
                sigma = np.array([[8, 0]
                                , [0, 8]])
                # inverse of sigma
                inv_sigma = np.linalg.inv(sigma)
                connected_tower = self.blocks[x][y].connected_tower
                # calculate the covariance of given tower
                cov = np.exp( -0.5 * np.dot(np.dot((self.blocks[x][y].position - connected_tower.position), inv_sigma), (self.blocks[x][y].position - connected_tower.position).T))
                # calculate the nominal BandWidth of a single block
                self.blocks[x][y].BWprime_bx = (self.blocks[x][y].population * connected_tower.BW_ty) / connected_tower.connected_population
                # calculate the exact BandWidth of a single block
                self.blocks[x][y].BW_bx = cov * self.blocks[x][y].BWprime_bx

    # calculate BandWidth for each user
    def cal_BW_ui(self):
        for i in range(self.size):
            for j in range(self.size):
                self.blocks[i][j].BW_ui = self.blocks[i][j].BW_bx / self.blocks[i][j].population

    # calculate the satisfaction of each user based on input file
    def cal_user_satisfaction(self):
        for i in range(self.size):
            for j in range(self.size):
                block = self.blocks[i][j]

                if block.BW_ui < self.user_satisfaction_levels[0]:
                    block.user_satisfaction_score = 0
                elif self.user_satisfaction_levels[0] <= block.BW_ui < self.user_satisfaction_levels[1]:
                    block.user_satisfaction_score = self.user_satisfaction_scores[0]
                elif self.user_satisfaction_levels[1] <= block.BW_ui < self.user_satisfaction_levels[2]:
                    self.blocks[i][j].user_satisfaction_score = self.user_satisfaction_scores[1]
                elif block.BW_ui >= self.user_satisfaction_levels[2]:
                    block.user_satisfaction_score = self.user_satisfaction_scores[2]

    # calculate the fitness of the curretn generation
    def fitness(self):
        if self.is_new:
            if self.is_child:
                for i in self.towers:
                    i.connected_population = 0
                self.is_child = False

            self.random_allocation()
            self.cal_BW_bx()
            self.cal_BW_ui()
            self.cal_user_satisfaction()

            # calculate fitness for each individual

            self.total_tower_cost = self.tower_construction_cost * len(self.towers)
            for i in range(len(self.towers)):
                self.total_tower_cost += self.towers[i].BW_ty * self.tower_maintenance_cost

            self.total_satisfaction_score = 0
            for i in range(self.size):
                for j in range(self.size):
                    self.total_satisfaction_score += self.blocks[i][j].user_satisfaction_score * self.blocks[i][j].population

            # the more ther satisfaction score, the more the fitness score
            # the less the tower cost, the more the fitness score
            self.fitness_score = self.total_satisfaction_score - self.total_tower_cost
            self.is_new = False
            
            

class Block:
    def __init__(self):
        self.position = []
        self.connected_tower = None
        self.population = 0
        self.BW_bx = 0
        self.BW_ui = 0
        self.BWprime_bx = 0
        self.user_satisfaction_score = 0


class Tower:
    def __init__(self, position, BW_ty):
        self.position = position
        self.BW_ty = BW_ty
        self.connected_population = 0