from Bandit import Bandit
import numpy as np

class Player:

    def __init__(self, bandit, name="Player A",):
        self.name: str = name
        self.bandit: Bandit = bandit
        self.reward: int = 0
        self.reward_history: list = []
        self.action_history: list = []
        self.estimated_values: list = []
        self.played_actions = np.zeros(self.getNrArms(), dtype=np.int)
        self.estimated_values = np.zeros(self.getNrArms(), dtype=np.float)
        self.cum_regret = 0
        self.cum_regret_history = []

    def chooseArm(self):
        pass

    def playArm(self, current_time):
        playing_arm = self.chooseArm(current_time)
        reward = self.bandit.playArm(playing_arm)
        self.updateRegret(playing_arm)
        self.updateEstimatedValues(playing_arm, reward)

    def updateRegret(self, arm):
        self.cum_regret += self.bandit.getBestArm() - self.bandit.arms[arm]
        self.cum_regret_history.append(self.cum_regret)
    
    def getNrArms(self) -> int:
        return len(self.bandit.arms)

    def updateEstimatedValues(self, played_action: int, reward: int):
        nr_played_actions = self.played_actions[played_action]

        self.estimated_values[played_action] += (1 / (nr_played_actions + 1)) * (
            reward - self.estimated_values[played_action])

        self.played_actions[played_action] += 1
        self.reward_history.append(reward)
        self.action_history.append(played_action)
        self.reward += reward
