import numpy as np
import random

from Player import Player


class UCBStrategy(Player):

    def __init__(self, bandit, name):
        super().__init__(bandit, name)

    def chooseArm(self, current_time) -> int:
        # Finds first occurence in list, else none
        arm = self.findUnplayedArm()

        if arm == None:
            arm = self.getBestArm(current_time)

        return arm

    def getBestArm(self, current_time):
        list = []

        for index, value in enumerate(self.estimated_values):
            list.append(value + np.sqrt(2 * np.log(current_time) / (1 + self.played_actions[index])))
        
        return list.index(max(list))

    def findUnplayedArm(self):
        return next((index for index, value in enumerate(self.played_actions) if value == 0), None)