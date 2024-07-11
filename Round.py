class Round():
    def __init__(self, id):
        self.possible_positions = {0.:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[],14:[],15:[]}
        self.known_positions = {0.:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[],14:[],15:[]}
        self.time = 0
        self.id = id

    # Set the starting node of the round.    
    def set_starting_node(self, node):
        self.possible_positions[0].append(node)
        self.known_positions[0].append(node)
        node.set_hint(True)

    # This make the round advance to the next time.
    def advance(self, nodes):
        self.time += 1
        self.possible_positions[self.time] = nodes
        
        for node in nodes:
            node.set_possible(True)

    # Manages the hint, recalculating all the possible nodes for the current round
    def hint(self, hint_node, hint_time):
        time = self.time+1

        for i in range(1, time):
            for node in self.possible_positions[i]:
                node.set_possible(False)

        self.possible_positions[hint_time] = [hint_node]
        self.known_positions[hint_time] = [hint_node]

        for i in range(hint_time, time):
            new_possible_positions = []
            for node in self.possible_positions[i]:
                for child in node.neighbors:
                    new_possible_positions.append(child)
            self.possible_positions[i+1] = new_possible_positions

            for node in self.possible_positions[i]:
                node.set_possible(True)
        
        for i in range(0, time):
            node = self.known_positions[i][0]
            if node:
                node.set_possible(False)
                node.set_hint(True)

    # Returns the current positions where jack can be.
    def get_last_positions(self):
        return self.possible_positions[self.time]

    # Returns the current time of the round.
    def get_current_time(self):
        return self.time