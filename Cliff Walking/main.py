from GridEnvironment import GridEnvironment
from CliffEnvironment import CliffEnvironment
from QLearnerAgent import QLearnerAgent

########################################################
# Cliff World
########################################################

# cliffWorld = CliffEnvironment(10, 4)
# QagentC = QLearnerAgent(cliffWorld, 10000, 0.2, (0, 3))
# QagentC.run()
########################################################
# Grid World
########################################################

gridWorld = GridEnvironment(8, 8)
QagentG = QLearnerAgent(gridWorld, 10000, 0.2, (0, 0))
QagentG.run()


# TODO: Q-learning gaat nog niet lekker, kennelijk gebeurt er nog iets geks. 