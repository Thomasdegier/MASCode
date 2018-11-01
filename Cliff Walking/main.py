from GridEnvironment import GridEnvironment
from CliffEnvironment import CliffEnvironment
from QLearnerAgent import QLearnerAgent
from SAgent import SAgent
from plotter import GridPlotter

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

GridPlotter().plotHeatmap(grid)
GridPlotter().plotHeatmap(cliffWorld.world)
