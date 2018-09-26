import random
import copy

INIT_PAYOFF = 0

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
TIT_FOR_TWO_TATS = "tftt"
N_GAMES_STRAT = "n_games"
JEALOUS_MAN = "jealous_man"
DEFECT_STR = "defect_str"
COOP_STR = "coop_str"
RANDOM = "rand"
ANTI_TIT_FOR_TAT = "anti_tft"
WIN_STAY_LOSE_SWITCH = "win_stay_lose_switch"


def first_round(round_nr):
    return round_nr == 0

class Agent:
    def __init__(self, name: str, experiment, strategy: str, stochastic: bool = False, p_error: float = 0) -> None:
        self.name: str = name
        self.stochastic = stochastic
        self.experiment = experiment
        self.p_error = p_error
        self.strategy: str = strategy
        self.last_move: int = 0
        self.history: list = []
        self.public_history: list = []
        self.payoff_history: list = [INIT_PAYOFF]
        self.payoff: int = INIT_PAYOFF

    def play(self, opponent, round_nr: int):
        self.play_strategy(opponent, round_nr)

    def update_payoff(self, payoff: int) -> None:
        self.payoff += payoff
        self.payoff_history.append(self.payoff)

    def update_history(self):
        self.last_move = self.history[-1]
        self.public_history = copy.deepcopy(self.history)

    def play_strategy(self, opponent, round_nr: int):
        if self.strategy == TIT_FOR_TAT:
            self.play_tft(opponent, round_nr)
        elif self.strategy == RANDOM:
            self.play_rand(opponent, round_nr)
        elif self.strategy == ANTI_TIT_FOR_TAT:
            self.play_anti_tft(opponent, round_nr)
        # elif self.strategy == JEALOUS_MAN:
        #     self.play_jealous_man(opponent, round_nr)
        elif self.strategy == WIN_STAY_LOSE_SWITCH:
            self.play_win_stay_lose_switch(opponent, round_nr)
        elif self.strategy == TIT_FOR_TWO_TATS:
            self.play_tftt(opponent, round_nr)
        elif self.strategy == DEFECT_STR:
            self.play_defect(opponent, round_nr)
        elif self.strategy == COOP_STR:
            self.play_coop(opponent, round_nr)

    def play_rand(self, opponent, round_nr: int):
        prob: float = random.uniform(0, 1)
        play: int = DEFECT

        if prob > 0.5:
            play = COOPERATE

        self.make_decision(play)

    def play_tft(self, opponent, round_nr: int):
        play = COOPERATE

        if not first_round(round_nr):
            play = self.check_opponents_last_action(opponent)

        self.make_decision(play)

    def play_defect(self, opponent, round_nr):
        self.make_decision(DEFECT)

    def play_coop(self, opponent, round_nr):
        self.make_decision(COOPERATE)

    def play_tftt(self, opponent, round_nr: int):
        play = COOPERATE

        if len(opponent.public_history) > 1:
            play = self.tftt_check_opponents_last_two_actions(opponent)

        self.make_decision(play)

    def tftt_check_opponents_last_two_actions(self, opponent: 'Agent'):
        if COOPERATE in opponent.public_history[-2:]:
            return COOPERATE

        return DEFECT

    def play_anti_tft(self, opponent, round_nr):
        play = 0

        # Play it safe if both were PP last turn, else play defect
        if not first_round(round_nr) and self.last_move == DEFECT and self.check_opponents_last_action(opponent) == DEFECT:
            play = COOPERATE
        else:
            play = DEFECT

        self.make_decision(play)

    def play_n_games_strat(self, opponent, round_nr: int):
        total_nr_games = self.experiment.nr_games
        play: int = COOPERATE

        if round_nr + 1 == total_nr_games:
            play = DEFECT

        self.make_decision(play)

    def play_win_stay_lose_switch(self, opponent, round_nr):
        rand_prob: float = DEFECT if random.uniform(0, 1) > 0.5 else COOPERATE
        play: int = rand_prob

        if not first_round(round_nr):
            # Play if last move resulted in increase in payoff, else switch strategy
            play = self.last_move if self.payoff_history[-1] - \
                self.payoff_history[-2] > 0 else -1 * self.last_move

        self.make_decision(play)

    def make_decision(self, play):
        if not self.stochastic:
            self.history.append(play)

        if self.stochastic:
            prob = random.uniform(0, 1)
            play = play if prob > self.p_error else -1 * play

    def check_opponents_last_action(self, opponent):
        noise_prob = random.uniform(0, 1)

        # If we can't determine the opponent's last move due to noise
        if self.experiment.p_noisy > 0 and self.experiment.p_noisy > noise_prob:
            guess_prob = random.uniform(0, 1)
            return DEFECT if guess_prob > 0.5 else COOPERATE

        return opponent.last_move

    def has_played(self):
        return len(self.history) > 0


class IteratedPD:
    def __init__(self, nr_games: int, p_noisy: float = 0, strategy_A=TIT_FOR_TAT, strategy_B=WIN_STAY_LOSE_SWITCH)-> None:
        self.nr_games = nr_games
        self.agent_A: Agent = Agent("Alice", self, strategy_A)
        self.agent_B: Agent = Agent("Bob", self, strategy_B)
        self.history: list = []
        self.p_noisy = p_noisy

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

    def printResults(self):
        agents = [self.agent_A, self.agent_B]

        for agent in agents:
            print("Agent {} uses strategy: {}".format(
                agent.name, agent.strategy))
            print("Agent {} has scored: {}".format(agent.name, agent.history))
            print("Agent {}'s payoff: {}".format(
                agent.name, agent.payoff_history))
            print("\n")

    def getWinner(self):
        if self.agent_A.payoff > self.agent_A.payoff:
            return self.agent_A.strategy
        else:
            return self.agent_B.strategy

    def run(self):
        for round_nr in range(self.nr_games):
            self.agent_A.play(self.agent_B, round_nr)
            self.agent_B.play(self.agent_A, round_nr)
            self.update_last_moves()
            self.update_payoffs()

        self.printResults()
        print("Winner is: {}".format(self.getWinner()))
        return self.getWinner()

winner = []
for i in range(1, 100):
    game = IteratedPD(20, p_noisy=1, strategy_A=TIT_FOR_TAT, strategy_B=ANTI_TIT_FOR_TAT)
    winner.append(game.run())

print(winner)
