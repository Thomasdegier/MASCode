import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
import seaborn as sns

def swap_tuple(input_tuple):
    """Why swap: Because numpy gets row,col coordinates according to (y,x), so to use x,y, we need to swap that"""
    a, b = input_tuple
    return (b,a)

class Environment:

    def __init__(self, nr_columns, nr_rows, nr_actions=4, init_qa_values=0):
        self.world = np.zeros((nr_rows, nr_columns))
        self.nr_columns = nr_columns
        self.nr_rows = nr_rows
        self.nr_actions = nr_actions
        
    def set_world_rewards(self):
        """ Initialize rewards for reaching different states. """
        pass
    
    def is_out_of_bounds(self, state):
        """ Checks if state is out of bounds of the world. """
        try:
            next_state = self.world[swap_tuple(state)]
        except IndexError:
            return True

        if state[0] < 0 or state[1] < 0:
            return True

        return False
    
    def next_state(self, state, action):
        """ Return next-state tuple. """
        pass
    
    def check_termination(self, state):
        """ Check termination. """
        pass