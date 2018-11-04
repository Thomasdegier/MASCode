import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
import seaborn as sns
from tabulate import tabulate

def swap_tuple(input_tuple):
    """Why swap: Because numpy gets row,col coordinates according to (y,x), so to use x,y, we need to swap that"""
    a, b = input_tuple
    return (b,a)

class Agent:
    def __init__(self, env, epsilon=0.2):
        self.curr_state = (0, 0)
        self.env = env
        self.epsilon = epsilon
        self.q_table = np.zeros((env.nr_rows, env.nr_columns, env.nr_actions))

    def run(self):
        pass

    def get_next_action(self, state):
        """ Returns the next index of the action according to the epsilon-greedy choice"""
        actions = self.q_table[swap_tuple(state)]
        random_actions = np.ones(len(actions), dtype=float) * self.epsilon / len(actions)
        best_action_index = np.argmax(actions)
        random_actions[best_action_index] += (1 - self.epsilon)
        
        return np.random.choice(np.arange(len(random_actions)), p=random_actions)

    def get_next_state(self, action):
        """ Return next theoretical state according to the environment."""
        return self.env.next_state(self.curr_state, action)

    def update_q_table(self, action, next_state, next_best_action):
        """ Updates the q table based on passed parameters of the TD walk."""
        pass

    def get_reward_for_state(self, state):
        """ Gets the reward for the state according to the environment."""
        return self.env.world[swap_tuple(state)]

    def terminated(self):
        """ Ask the environment whether the agent is terminated. """
        return self.env.check_termination(self.curr_state)

    def update_state(self, next_state):
        """ Set new state. """
        self.curr_state = next_state

    def q_table_max(self):
        """ Represent each state by the max of their actions. 
            Where axis=2 represents the third axis(actions) being maximized for each state.
        """
        return np.amax(self.q_table, axis=2)

    def q_table_min(self):
        """ Represent each state by the min of their actions. 
            Where axis=2 represents the third axis(actions) being minimized for each state.
        """
        return np.amin(self.q_table, axis=2)

    def q_table_avg(self):
        """ Represent each state by the avg of their actions. 
            Where axis=2 represents the third axis(actions) being averaged for each state.
        """
        return np.average(self.q_table, axis=2)

    def print_q_max(self):
        print(tabulate(self.q_table_max()))

    def print_q_min(self):
        print(tabulate(self.q_table_min()))

    # def print_q_directions(self):
    #     directions_table = np.argmax(self.q_table, axis=2)

    #     directions_table[directions_table == 0] = "D"
    #     directions_table[directions_table == 1] = "R"
    #     directions_table[directions_table == 2] = "U"
    #     directions_table[directions_table == 3] = "L"

    #     print(directions_table)