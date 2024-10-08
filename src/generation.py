import random

from src.graph import Graph


def random_graph(n_nodes: int, n_edges: int) -> Graph:
    """Generate a random graph of `n_nodes` with a certain percentage of ."""
    assert n_edges <= n_nodes * n_nodes

    graph = Graph()

    all_edges = [(i, j) for i in range(n_nodes) for j in range(n_nodes)]
    random_edges = random.sample(all_edges, n_edges)

    for u, v in random_edges:
        graph.add_edge(u, v)

    return graph
