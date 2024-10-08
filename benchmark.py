import sys

from src.generation import random_graph

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 100

    graph_size = 60
    for _ in range(n):
        graph = random_graph(graph_size, graph_size * graph_size // 2)
        graph.has_cycle()
        graph.shortest_path(0)
