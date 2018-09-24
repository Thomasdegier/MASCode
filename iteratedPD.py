import random

INIT_PAYOFF = 1000

# PAYOFF constants: where 2R > T + S
PAYOFF_REWARD_VALUE = 400
PAYOFF_SUCKER_VALUE = - 500
PAYOFF_TEMPTATION_VALUE = 600
PAYOFF_PUNISHMENT_VALUE = - 300

# ACTIONS
COOPERATE = 1
DEFECT = -1

# STRATEGIES
TIT_FOR_TAT = "tft"
ANTI_TIT_FOR_TAT = "anti_tft"
RANDOM = "rand"

def first_round(round_nr):
    return round_nr == 0

class Agent:

    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.last_move = None
        self.history = []
        self.payoff_history = [INIT_PAYOFF]
        self.payoff = INIT_PAYOFF

    def play(self, opponent, round_nr):
        self.play_strategy(opponent, round_nr)
        return

    def update_payoff(self, payoff):
        self.payoff += payoff
        self.payoff_history.append(self.payoff)
    
    def update_history(self):
        self.last_move = self.history[-1]

    def play_strategy(self, opponent, round_nr):
        if self.strategy == TIT_FOR_TAT:
            self.play_tft(opponent, round_nr)
        elif self.strategy == RANDOM:
            self.play_rand(opponent, round_nr)
        elif self.strategy == ANTI_TIT_FOR_TAT:
            self.play_anti_tft(opponent, round_nr)

    def play_rand(self, opponent, round_nr):
        prob = random.uniform(0, 1)
        play = DEFECT

        if prob > 0.5:
            play = COOPERATE

        self.history.append(play)

    def play_tft(self, opponent, round_nr):
        play = COOPERATE

        if not first_round(round_nr):
            play = opponent.last_move

        self.history.append(play)

    def play_anti_tft(self, opponent, round_nr):
        play = 0

        if not first_round(round_nr) and opponent.last_move == DEFECT:
            play = COOPERATE
        else:
            play = DEFECT

        self.history.append(play)
    
    def has_played(self):
        return len(self.history) > 0

class IteratedPD:
    def __init__(self, nr_games):
        self.nr_games = nr_games
        self.agent_A = Agent("Alice", TIT_FOR_TAT)
        self.agent_B = Agent("Bob", ANTI_TIT_FOR_TAT)
        self.history = []

    def update_last_moves(self):
        self.agent_A.update_history()
        self.agent_B.update_history()


    def update_payoffs(self):
        agent_A_move = self.agent_A.last_move
        agent_B_move = self.agent_B.last_move

        if agent_A_move == COOPERATE and agent_B_move == COOPERATE:
            self.agent_A.update_payoff(PAYOFF_REWARD_VALUE)
            self.agent_B.update_payoff(PAYOFF_REWARD_VALUE)
        elif agent_A_move == COOPERATE and agent_B_move == DEFECT:
            self.agent_A.update_payoff(PAYOFF_SUCKER_VALUE)
            self.agent_B.update_payoff(PAYOFF_TEMPTATION_VALUE)
        elif agent_A_move == DEFECT and agent_B_move == COOPERATE:
            self.agent_A.update_payoff(PAYOFF_TEMPTATION_VALUE)
            self.agent_B.update_payoff(PAYOFF_SUCKER_VALUE)
        else:
            self.agent_A.update_payoff(PAYOFF_PUNISHMENT_VALUE)
            self.agent_B.update_payoff(PAYOFF_PUNISHMENT_VALUE)

    def run(self):
        for round_nr in range(self.nr_games):
            self.agent_A.play(self.agent_B, round_nr)
            self.agent_B.play(self.agent_A, round_nr)
            self.update_last_moves()
            self.update_payoffs()
        
        print("Agent A has scored:", self.agent_A.history)
        print("Agent A's payoff:", self.agent_A.payoff_history)
        print("Agent B has scored:", self.agent_B.history)
        print("Agent B's payoff:", self.agent_B.payoff_history)
    
game = IteratedPD(3)
game.run()
print(game)