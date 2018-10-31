import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
import seaborn as sns

class Environment:

    def __init__(self, nr_columns, nr_rows, nr_actions=4, init_qa_values=0):
        self.world = np.zeros((nr_rows, nr_columns))
        self.nr_columns = nr_columns
        self.nr_rows = nr_rows
        self.nr_actions = nr_actions
        
    def set_world_rewards(self):
        pass
    
    def is_out_of_bounds(self, state):
        if state[0] < 0 or state[0] > self.nr_columns - 1:
            return True
        
        if state[1] < 0 or state[1] > self.nr_rows -1:
            return True
        
        return False
    
    def next_state(self, state, action):
        pass
    
    def check_termination(self, state):
        pass