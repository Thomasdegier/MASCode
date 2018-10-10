import matplotlib.pyplot as plt

from Bandit import Bandit
from Player import Player
from EpsilonGreedyStrategy import EpsilonGreedyStrategy
from UCBStrategy import UCBStrategy
import random

bandit1 = Bandit(10)
playerA = UCBStrategy(bandit1, "A")

# From perspective of some player

def plotRegret(history):
    time = [i for i in range(3000)]
    plt.plot(history, time)

def run_simulation(max_time, player, bandit):
    curr_time = 0
    
    while(curr_time < max_time):
        player.playArm(curr_time)
        curr_time += 1
    
    print("Player estimates:{}".format(player.estimated_values))
    print("True bandit:{}".format(bandit.arms))
    print("Player's reward: {}".format(player.reward))
    plotRegret(player.cum_regret_history)

run_simulation(3000, playerA, bandit1)