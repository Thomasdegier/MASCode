import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
import seaborn as sns

from Environment import Environment
from operator import add

REWARD_NONTERMINAL = -1

REWARD_TREASURE = 10
COORDINATES_TREASURE = (4, 5)

COORDINATES_WALL = [(2,1), (3,1), (4,1), (5,1), (5,2), (5,3), (5,4), (1, 6), (2,6), (3,6)]

COORDINATES_SNAKEPIT = (4,5)
REWARD_SNAKEPIT = -20

REWARD_CLIFF = -100

# Down, right, top, left
ACTION_DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class GridEnvironment(Environment):
    """
        Environment, where position coordinates correspond to (x, y).
        [(0,0), (1,0), (2,0), (3,0)]
        [(0,1), (1,1), (2,1), (3,1)]
        [(0,2), (1,2), (2,2), (3,2)]
        [(0,3), (1,3), (2,3), (3,3)]
    """
    def __init__(self, nr_columns, nr_rows, nr_actions=4, init_qa_values=0):
        super().__init__(nr_columns, nr_rows)
        self.init_world_rewards()

    def init_world_rewards(self):
        """ Initialize rewards for reaching different states. """
        self.world[:, :] = REWARD_NONTERMINAL
        self.world[self.nr_rows - 1:, 1:self.nr_columns - 1] = REWARD_CLIFF
        self.world[self.nr_rows - 1, self.nr_columns - 1] = REWARD_TERMINAL

    def next_state(self, state, action_index):
        """ Returns next-state tuple.
            If: state walks to edge, return same state. 
            Else: add action to tuple and return new state
        """
        action = ACTION_DIRECTIONS[action_index]
        next_state = tuple(map(add, state, action))

        if self.is_out_of_bounds(next_state):
            next_state = state

        return next_state

    def check_termination(self, state):
        """ Checks if state is in cliff or in terminal zone. """
        return state[1] == self.nr_rows - 1 and state[0] > 0
