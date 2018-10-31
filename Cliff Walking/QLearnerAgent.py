import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
import seaborn as sns

from Agent import Agent

ALPHA = 0.1
GAMMA = 1

class QLearnerAgent(Agent):
    def __init__(self, env, nr_episodes, epsilon=0.2 , init_position=(0,0)):
        super().__init__(env, epsilon, init_position)
        self.nr_episodes = nr_episodes
        
    def run(self):
        for i in range(self.nr_episodes):
            self.curr_state = self.init_position
            
            while not self.terminated():
                action_index = self.get_next_action()
                next_state = self.get_next_state(action_index)
                next_state_best_action_index = np.argmax(self.q_table[next_state])

                self.update_q_table(action_index, next_state, next_state_best_action_index)
                self.update_state(next_state)
                
    def update_q_table(self, action_index, next_state, next_best_action_index):
        curr_q = self.q_table[self.curr_state][action_index]
        update = (self.get_reward_for_state(next_state) + GAMMA * self.q_table[next_state][next_best_action_index] - curr_q)
        self.q_table[self.curr_state][action_index] = curr_q + ALPHA * update