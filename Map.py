import json
from Node import *
from PIL import ImageTk
from tkinter import NW

class Map():
    def __init__(self, canvas):
        self.nodes = {}
        self.canvas = canvas

        self.init_graph('map.json')

        self.draw()

        super().__init__()
        self.update()
    
    # Init the graph data structure.
    def init_graph(self, jsonfile):
        # Read the nodes from JSON and store them as object in array nodes.
        f = open(f'assets/{jsonfile}')
        data = json.load(f)

        # Build the simple nodes dictionary.
        for node in data['nodes']:
            v = node['value']
            neigh = node['neighbors']
            x,y = node['position']
            self.nodes[v] = Node(v, neigh, x, y)

        # Substitute the effective Node object in the array neighbors of all nodes of the graph.
        for node in self.nodes.values():
            neigh = []
            for n in node.neighbors:
                neigh.append(self.nodes[n])
            node.neighbors = neigh
            
        f.close()

    # Draw the initial state of the graph, saving the handles to canvas item to not redraw them.
    def draw(self):
        for node in self.nodes.values():
            node.draw(self.canvas)    

    # Get the Node object from an ID
    def get_node(self, id):
        return self.nodes[id]

    # Update the map redrawing the nodes.
    def update(self):
        for node in self.nodes.values():
            node.update(self.canvas)
