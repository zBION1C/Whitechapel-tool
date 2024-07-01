from Round import *

class Game():
    def __init__(self, game_map):
        self.rounds = [Round(i) for i in range(1,5)]
        self.current_round = 1
        self.map = game_map

    # Return the Round object of the current round
    def get_current_round(self):
        return self.rounds[self.current_round]

    # Advance in the game, this happens after the police turn. After the police asked, if they discovered a hint, 
    # the map has to be updated accordingly.
    def advance(self, clue):
        round = self.get_current_round()

        hint_node, hint_time = clue

        if hint_node != 0: # The clue was found, we have to recalculate all of the possible nodes starting from the new hint and time.
            if time == round.get_current_time():
                current_possible_nodes = [hint_node]
            else:
                recalculate_from(hint_node, hint_time)
                return
        else: # No hint was given, calculate the possible nodes as all the adjacent of the possible nodes of the current step.
            current_possible_nodes = round.get_last_positions()
            next_possible_nodes = []
        
        for node in current_possible_nodes:
            for child in node.neighbors:
                next_possible_nodes.append(child)
                child.set_possible(True)
                
        round.advance(next_possible_nodes)




    # Advance to the next round.
    def next_round(self):
        self.current_round += 1
        round = self.get_current_round()
        current_possibilities = round.get_possible_steps(round.get_current_time())
        np = self.add_possible_steps(current_possibilities, round.time)
        print(round.possible_steps)
        round.add_time()
        self.map.highlight_nodes(np)