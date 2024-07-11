from Round import *

class Game():
    def __init__(self, game_map):
        self.rounds = [Round(i) for i in range(1,5)]
        self.current_round = 1
        self.map = game_map

    # Return the Round object of the current round
    def get_current_round(self):
        return self.rounds[self.current_round]

    # Manage the hint if the policemen found it
    def hint(self, clue):
        round = self.get_current_round()

        hint_node, hint_time = clue
        hint_node = hint_node.get()
        hint_time = hint_time.get()

        node = self.map.get_node(hint_node)
        round.hint(node, hint_time)

    # Advance in the game, this happens after the police turn.
    def advance(self):        
        round = self.get_current_round()
        current_possible_nodes = round.get_last_positions()

        next_possible_nodes = []

        for node in current_possible_nodes:
            for child in node.neighbors:
                next_possible_nodes.append(child)

        round.advance(next_possible_nodes)
