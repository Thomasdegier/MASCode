from itertools import *
import pandas as pd
import numpy as np
import matplotlib as plot
import sklearn as sk
import importlib
import random

class Bandit:

    def __init__(self, nr_arms: int):
        self.arms: list = [np.random.random() for i in range(nr_arms)]

    def run(self):
        print(self.arms)

    def getBestArm(self):
        return max(self.arms)
    
    def playArm(self, arm_index) -> int:
        """Plays arm, and returns some reward."""
        prob_success = random.random()
        reward = 0

        if prob_success < self.arms[arm_index]:
            reward = 1
        
        return reward