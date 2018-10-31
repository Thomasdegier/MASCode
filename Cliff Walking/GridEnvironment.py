import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
import seaborn as sns

from Environment import Environment
from operator import add

REWARD_NONTERMINAL = -1

REWARD_TREASURE = 10
COORDINATES_TREASURE = (7, 7)

COORDINATES_WALL = [(2, 1), (3, 1), (4, 1), (5, 1), (5, 2),
                    (5, 3), (5, 4), (1, 6), (2, 6), (3, 6)]

COORDINATES_SNAKEPIT = (4, 5)
REWARD_SNAKEPIT = -20

# Down, right, top, left
ACTION_DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def swap_tuple(input_tuple):
    """Why swap: Because numpy gets row,col coordinates according to (y,x), so to use x,y, we need to swap that"""
    a, b = input_tuple
    return (b, a)


class GridEnvironment(Environment):
    """
        Environment, where position coordinates correspond to (x, y).
        [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0)]
        [(0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]
        [(0,2), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2)]
        [(0,3), (1,3), (2,3), (3,3), (4,3), (5,3), (6,3), (7,3)]
        [(0,4), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), (7,4)]
        [(0,5), (1,5), (2,5), (3,5), (4,5), (5,5), (6,5), (7,5)]
        [(0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]
        [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7)]
    """

    def __init__(self, nr_columns, nr_rows, nr_actions=4, init_qa_values=0):
        super().__init__(nr_columns, nr_rows)
        self.init_world_rewards()

    def init_world_rewards(self):
        """ Initialize rewards for reaching different states. """
        self.world[:, :] = REWARD_NONTERMINAL
        self.world[swap_tuple(COORDINATES_TREASURE)] = REWARD_TREASURE
        self.world[swap_tuple(COORDINATES_SNAKEPIT)] = REWARD_SNAKEPIT

    def next_state(self, state, action_index):
        """ Returns next-state tuple.
            If: state walks to edge, return same state. 
            Else: add action to tuple and return new state
        """
        action = ACTION_DIRECTIONS[action_index]
        next_state = tuple(map(add, state, action))

        if next_state in COORDINATES_WALL:
            return state

        if self.is_out_of_bounds(next_state):
            return state

        return next_state

    def check_termination(self, state):
        """ Checks if state is in cliff or in terminal zone. """
        return state == COORDINATES_SNAKEPIT or state == COORDINATES_TREASURE