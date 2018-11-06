class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False

    def set_visited(self):
        self.visited = True

    def set_not_visited(self):
        self.visited = False
        
    def is_visited(self):
        return self.visited
