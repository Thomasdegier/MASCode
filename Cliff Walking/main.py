from GridEnvironment import GridEnvironment
from CliffEnvironment import CliffEnvironment
from QLearnerAgent import QLearnerAgent

########################################################
# Gridworld
########################################################

cliffWorld = CliffEnvironment(10, 4)
agentC = QLearnerAgent(cliffWorld, 100, 0.2, (0, 3))

########################################################
# ClifWorld
########################################################

gridWorld = GridEnvironment(8, 8)
agentG = QLearnerAgent(gridWorld, 100, 0.2, (0, 0))
gridWorld.world
print("Dog")