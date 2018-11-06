""""
Graph search implemented to find mutual movie actors.
This project will help us to understand how graph search works. Movie is an edge and actor is node
@author: Segni Habulu
"""


from Graph import Graph, Edge
from Queue import Queue as Queue
from Node import Node
import time


# we will use the following list to reset later

visited_movie = []
visited_actor = []


def load_graph(graph, file_path):
    file = open(file_path, mode="r", encoding="utf-8")
    for line in file.readlines():
        line = line.strip().split('/')
        movie, casts = Edge(line[0]), line[1:]

        # using list comprehension we add to our list and dictionary
        node_list = [Node(cast) for cast in casts]
        [graph.node_to_edge_dictionary(node, movie) for node in node_list]

        if movie.title not in graph.edgeToNode.keys():
            graph.edgeToNode[movie.title] = node_list
            # we will store on dictionary {movie : [nodes]}
        file.readline().strip()
    file.close()
    
    return graph


def distance(graph, actor1, actor2):

    if visited_movie is not None:
        [node.set_not_visited() for node in visited_actor]
        [edge.set_not_visited() for edge in visited_movie]
        visited_movie.clear()
        visited_actor.clear()

    first_node = Node(actor1)
    current_que, next_que = Queue(), Queue()
    if actor1 == actor2:
        return print("The distance is ", 0)

    _distance = 1
    current_que.enqueue(first_node)
    while not current_que.is_empty():
        cast = current_que.deque()
        if cast.name in graph.nodeToEdge.keys():
            movies = graph.nodeToEdge[cast.name]

        try: 
            for movie in movies:
                if not movie.is_visited():
                    actors = graph.edgeToNode[movie.title]
                    for actor in actors:
                        if not actor.is_visited():
                            if actor.name == actor2:
                                return print("minimum distance between ", actor1, " and ", actor2, " is ", _distance)
                            actor.set_visited()
                            visited_actor.append(actor)
                            next_que.enqueue(actor)
                    movie.set_visited()
                    visited_movie.append(movie)
        except UnboundLocalError:
            return print(None)
        
        if current_que.is_empty():
            if not next_que.is_empty():
                current_que = next_que
                next_que = Queue()
                _distance += 1
            else:
                return print("No edge exists between nodes.")


def __test__():
    start = time.time()
    graph = Graph()
    graph = load_graph(graph, "cast.txt")
    distance(graph, "Knuppe, Kerry", "Doyle, Norman")
    stop = time.time()
    print(stop - start, "seconds")

    start = time.time()
    distance(graph, "Knuppe, Kerry", "Doyle, Norman")
    stop = time.time()
    print(stop - start, "seconds")


__test__()


