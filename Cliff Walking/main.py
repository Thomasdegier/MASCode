from GridEnvironment import GridEnvironment
from CliffEnvironment import CliffEnvironment
from QLearnerAgent import QLearnerAgent
from SAgent import SAgent
from plotter import GridPlotter
import numpy as np

########################################################
# Cliff World
########################################################
# cliffWorld = CliffEnvironment(10, 4)
# QagentC = QLearnerAgent(cliffWorld, 10000, 0.2) #Q Learning

# slAgentC = SAgent(cliffWorld, 10000, 0.2) # SARSA

# QagentC.run()
# slAgentC.run()
########################################################
# Grid World
########################################################

gridWorld = GridEnvironment(8, 8)
QagentG = QLearnerAgent(gridWorld, 10000, 0.2)
slAgentG = SAgent(gridWorld, 10000, 0.2)

QagentG.run()
# slAgentCGrun() for SARSA


########################################################
# PLOTTING
########################################################

grid = gridWorld.world
cliff = cliffWorld.world

# !! verwacht een 3d array van (y,x,acties)
GridPlotter().plotHeatmap_Q(QagentC.q_table)
# GridPlotter().plotHeatmap_Q(fake_q_cliff)
