import numpy as np
import random

from Player import Player

class OptimisticGreedy(Player):

    def __init__(self, bandit, name, initial_r_value = 0.9999999999999):
        super().__init__(bandit, name)
        self.estimated_values = [initial_r_value for i in range(self.getNrArms())]

    def chooseArm(self, current_time) -> int:
        return np.argmax(self.estimated_values)