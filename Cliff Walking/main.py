from CliffEnvironment import CliffEnvironment
from QLearnerAgent import QLearnerAgent

NR_COLUMNS = 5

# Including the cliff
NR_ROWS = 4

cliffWorld = CliffEnvironment(NR_COLUMNS, NR_ROWS)
agent = QLearnerAgent(cliffWorld, 100, 0.2, (0, NR_ROWS - 1))

agent.run()