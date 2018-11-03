from GridEnvironment import GridEnvironment
from CliffEnvironment import CliffEnvironment
from QLearnerAgent import QLearnerAgent
from SAgent import SAgent
from plotter import GridPlotter
import numpy as np

########################################################
# Cliff World
########################################################

cliffWorld = CliffEnvironment(10, 4)
QagentC = QLearnerAgent(cliffWorld, 10000, 0.2, (0, 3)) #Q Learning
slAgentC = SAgent(cliffWorld, 10000, 0.2, (0, 3)) # SARSA

# QagentC.run() for Qlearning
# slAgentC.run() for SARSA
########################################################
# Grid World
########################################################

gridWorld = GridEnvironment(8, 8)
QagentG = QLearnerAgent(gridWorld, 10000, 0.2, (0, 0))
slAgentG = SAgent(gridWorld, 10000, 0.2, (0,0))

# QagentG.run() for Qlearning
# slAgentCGrun() for SARSA


########################################################
# PLOTTING
########################################################

grid = gridWorld.world
cliff = cliffWorld.world

# dummy waardes
fake_q_grid = [[[x*(i+1/2.5) for i in range(4)] for x in y] for y in grid ]
fake_q_cliff = [[[x*(i+1/2.5) for i in range(4)] for x in y] for y in cliff ]

GridPlotter().plotHeatmap_V(grid)
GridPlotter().plotHeatmap_V(cliff)

# !! verwacht een 3d array van (y,x,acties)
GridPlotter().plotHeatmap_Q(fake_q_grid)
GridPlotter().plotHeatmap_Q(fake_q_cliff)
