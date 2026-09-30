from collections import deque


class Graph:

  def __init__(self):
    self.graph = {}

  def add_edge(self, u, v):
    """Adds an undirected edge between vertices u and v."""
    if u not in self.graph:
      self.graph[u] = []
    if v not in self.graph:
      self.graph[v] = []
    self.graph[u].append(v)
    self.graph[v].append(u)

  def bfs(self, start_node):
    """Performs Breadth-First Search starting from a given node."""
    if start_node not in self.graph:
      return []

    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    traversal_order = []

    while queue:
      current_node = queue.popleft()
      traversal_order.append(current_node)

      for neighbor in self.graph.get(current_node, []):
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append(neighbor)

    return traversal_order


if __name__ == "__main__":
  g = Graph()

  print("--- Graph BFS Interactive Input ---")
  try:
    num_edges = int(input("Enter the number of edges: "))

    print("Enter each edge separated by a space (e.g., A B):")
    for i in range(num_edges):
      edge_input = input(f"Edge {i+1}: ").strip().split()
      if len(edge_input) == 2:
        u, v = edge_input
        g.add_edge(u, v)
      else:
        print("Invalid input. Please enter exactly two nodes separated by a space.")

    start_node = input("Enter the starting node for BFS: ").strip()

    print(f"\nBFS Traversal starting from node '{start_node}':")
    result = g.bfs(start_node)

    if result:
      print(" -> ".join(result))
    else:
      print("The start node is not present in the graph.")

  except ValueError:
    print("Please enter a valid integer for the number of edges.")
