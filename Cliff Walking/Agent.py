import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
import seaborn as sns

class Agent:
    def __init__(self, env, epsilon=0.2, init_position=(0,0)):
        self.init_position = init_position
        self.curr_state = init_position
        self.env = env
        self.epsilon = epsilon
        self.q_table = np.zeros((env.nr_columns, env.nr_rows + 1, env.nr_actions))
        
    def run(self):
        pass
    
    def get_next_action(self):
        """Returns the next index of the action according to the epsilon-greedy choice"""
        actions = self.q_table[self.curr_state]
        
        # If we choose randomly
        if np.random.random() < self.epsilon:
            return np.random.choice(4)
        
        return np.argmax(actions)
    
    def get_next_state(self, action):
        """Return next theoretical state according to the environment."""
        return self.env.next_state(self.curr_state, action)
    
    def update_q_table(self, action, next_state, next_best_action):
        pass
    
    def get_reward_for_state(self, state):
        return self.env.world.transpose()[state]
    
    def terminated(self):
        return self.env.check_termination(self.curr_state)
    
    def update_state(self, next_state):
        self.curr_state = next_state