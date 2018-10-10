import numpy as np
import random

from Player import Player


class EpsilonGreedyStrategy(Player):

    def __init__(self, bandit, name, epsilon=0.5):
        super().__init__(bandit, name)
        self.epsilon = epsilon

    def chooseArm(self, current_time) -> int:
        arm = 0

        # If we random explore
        if random.random() < self.epsilon:
            return random.randint(0, self.getNrArms() - 1)
        
        return np.argmax(self.estimated_values)