class Node():
    def __init__(self, id, neighbors, x, y):
        self.canvas_element = None
        self.neighbors = neighbors
        self.possible = False
        self.hint = False
        self.radius = 12
        self.id = id
        self.x = x
        self.y = y

    # Draw the node in the canvas
    def draw(self, canvas):
        self.canvas_element = canvas.create_oval(self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius, fill='white', width=2)
        canvas.create_text(self.x, self.y, text=self.id)

    # Update the node 
    def update(self, canvas):
        if self.possible:
            canvas.itemconfig(self.canvas_element, fill='white', width=2)
        elif self.hint: 
            canvas.itemconfig(self.canvas_element, fill='lightgreen', width=2)
        else: 
            canvas.itemconfig(self.canvas_element, fill='grey', width=2)

    # Set the possible variable, if True the node is a possible node where jack could be.
    def set_possible(self, b):
        self.possible = b
    
    # Set the hint variable, if True the node is an hint, so jack has stepped on it.
    def set_hint(self, b):
        self.hint = b

    # Reset the node to the default state.
    def reset(self):
        self.possible = False
        self.hint = False
    
    