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

    # This make the round advance to the next time.
    def advance(self, nodes):
        self.time += 1
        self.possible_positions[self.time] = nodes

    # Returns the current positions where jack can be.
    def get_last_positions(self):

        return self.possible_positions[self.time]

    # Returns the current time of the round.
    def get_current_time(self):
        return self.time