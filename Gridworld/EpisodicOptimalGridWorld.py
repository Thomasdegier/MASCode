import numpy as np
from operator import add

LOCATION_A = (1, 0)
LOCATION_B = (3, 0)
LOCATION_A_PRIME = (1, 4)
LOCATION_B_PRIME = (3, 2)

INIT_POLICY_P = 0.25
GAMMA = 1

TRANS_A_REWARD = 10
TRANS_B_REWARD = 5
OUT_OF_BOUNDS_REWARD = -1
STANDARD_REWARD = 0
NR_ACTIONS = 4

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
UP, RIGHT, DOWN, LEFT = DIRECTIONS


class EpisodictOptimalGridWorld:
    def __init__(self, dim_x=5, dim_y=5):
        self.grid = np.zeros((dim_x, dim_y))
        self.policies = np.full((dim_x, dim_y, NR_ACTIONS), INIT_POLICY_P)
        self.max_x = dim_x - 1
        self.max_y = dim_y - 1

    def isOutOfBounds(self, state_tuple) -> bool:
        if state_tuple[0] < 0 or state_tuple[0] > self.max_x:
            return True

        if state_tuple[1] < 0 or state_tuple[1] > self.max_y:
            return True

        return False

    def improvePolicy(self):
        policy_stable = True
        
        for row_index, row in enumerate(self.grid):
            for col_index, column in enumerate(row):
                state_tuple = (col_index, row_index)
                actions = self.getActionValuesForState(state_tuple)
                chosen_action = np.argmax(self.policies[state_tuple])
                best_action = np.argmax(actions)

                if chosen_action != best_action:
                    policy_stable = False

                self.setOptimalPolicy(state_tuple, best_action)

        if policy_stable:
            return

        self.evaluatePolicy(1)

    def setOptimalPolicy(self, state_tuple, best_action):
        self.policies[state_tuple] = [0 for i in self.policies[state_tuple]]
        self.policies[state_tuple][best_action] = 1

    def getActionValuesForState(self, state_tuple):
        qa_values = []

        for index, action in enumerate(DIRECTIONS):
            next_state_tuple = self.getNextState(state_tuple, action)
            expected_reward = self.getExpectedReward(
                state_tuple, next_state_tuple)
            qa_values.append(expected_reward + (
                GAMMA * self.getValueForNextState(state_tuple, next_state_tuple)))

        return qa_values
    
    def getValueForState(self, state_tuple):
        initial_value = 0
        possible_actions = self.getActionValuesForState(state_tuple)
        
        for index, action in enumerate(possible_actions):
            initial_value += self.getPolicy(state_tuple, index) * action

        self.grid.transpose()[state_tuple] = max(possible_actions)

    def getPolicy(self, state_tuple, action_index):
        x, y = state_tuple
        return self.policies[y, x, action_index]

    def getValueForNextState(self, current_state_tuple, next_state_tuple):
        if self.isOutOfBounds(next_state_tuple):
            return self.grid.transpose()[current_state_tuple]

        return self.grid.transpose()[next_state_tuple]

    def getNextState(self, state_tuple: tuple, action: tuple):
        if state_tuple == LOCATION_A:
            return LOCATION_A

        if state_tuple == LOCATION_B:
            return LOCATION_B

        return tuple(map(add, action, state_tuple))

    def getExpectedReward(self, current_state_tuples: tuple, next_state_tuple: tuple):
        if current_state_tuples == LOCATION_A or current_state_tuples == LOCATION_B:
            return 0

        if next_state_tuple == LOCATION_A:
            return TRANS_A_REWARD

        if next_state_tuple == LOCATION_B:
            return TRANS_B_REWARD

        if self.isOutOfBounds(next_state_tuple):
            return OUT_OF_BOUNDS_REWARD

        return STANDARD_REWARD

    def traverseGrid(self):
        for row_index, row in enumerate(self.grid):
            for col_index, column in enumerate(row):
                coordinates = (col_index, row_index)
                self.getValueForState(coordinates)

    def evaluatePolicy(self, max_k):
        for i in range(max_k):
            self.traverseGrid()

    def run(self):
        self.evaluatePolicy(100)
            # self.improvePolicy()

        print(self.grid)

gw = EpisodictOptimalGridWorld()
gw.run()