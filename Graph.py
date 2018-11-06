class Edge:
    def __init__(self, title):
        self.title = title
        self.visited = False

    def set_visited(self):
        self.visited = True

    def set_not_visited(self):
        self.visited = False

    def is_visited(self):
        return self.visited


class Graph:
    def __init__(self):
        self.edgeToNode = {}
        self.nodeToEdge = {}

    def node_to_edge_dictionary(self, actor, movie):
        if actor.name not in self.nodeToEdge.keys():
            self.nodeToEdge[actor.name] = []
        self.nodeToEdge[actor.name].append(movie)
