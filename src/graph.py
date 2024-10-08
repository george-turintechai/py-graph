"""Simple graph class with DFS to detect cycles, implemented by ChatGPT."""

from typing import Dict, List, Set


class Graph:
    def __init__(self):
        self.graph: Dict[int, List[int]] = {}

    def add_edge(self, u: int, v: int):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def has_cycle(self):
        visited = set()
        for node in self.graph:
            if self.dfs(node, visited, set()):
                return True
        return False

    def shortest_path(self, start: int):
        distances = {node: float("inf") for node in self.graph}
        distances[start] = 0
        visited = set()
        while len(visited) < len(self.graph):
            min_distance = float("inf")
            min_node = None
            for node in self.graph:
                if node not in visited and distances[node] < min_distance:
                    min_distance = distances[node]
                    min_node = node

            assert min_node is not None

            visited.add(min_node)

            for neighbor in self.graph[min_node]:
                distance = distances[min_node] + 1
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        return distances

    def dfs(self, node: int, visited: Set[int], recursion_stack: Set[int]):
        visited.add(node)
        recursion_stack.add(node)
        if node in self.graph:
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    if self.dfs(neighbor, visited, recursion_stack):
                        return True
                elif neighbor in recursion_stack:
                    return True

        recursion_stack.remove(node)
        return False
