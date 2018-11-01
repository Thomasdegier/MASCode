from GridEnvironment import GridEnvironment
from CliffEnvironment import CliffEnvironment
from QLearnerAgent import QLearnerAgent
from plotter import GridPlotter

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



grid = gridWorld.world

GridPlotter().plotHeatmap(grid)
GridPlotter().plotHeatmap(cliffWorld.world)